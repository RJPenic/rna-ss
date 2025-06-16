import argparse
import json
from pathlib import Path

from argparse import Namespace, ArgumentParser
from copy import deepcopy

from lightning_wrapper import ModelWrapper
from data import SecondaryStructureDatamodule

import lightning.pytorch as pl
from lightning.pytorch.loggers.wandb import WandbLogger
from lightning.pytorch.callbacks.model_checkpoint import ModelCheckpoint
from lightning.pytorch.strategies import DDPStrategy


def update_args_with_parser_default_vals(
    args: Namespace,
    *parsers: ArgumentParser
) -> Namespace:
    # I understand this isn't pretty but it gets the job done! :)
    args = deepcopy(args)
    args_dict = vars(args)

    for parser in parsers:
        defaults = {action.dest: action.default for action in parser._actions}

        for key in defaults:
            if key not in args_dict:
                args_dict[key] = defaults[key]

    return args


def is_multiple_devices(devices: str) -> bool:
    if devices.isdigit():
        num_devices = int(devices)
        return num_devices > 1

    if "," in devices:
        return len(devices.replace(" ", "").split(",")) > 1

    return False


def main(args):
    # Initialize random number generation
    if args.seed:
        pl.seed_everything(args.seed)

    # Create output directory if it doesn't exist
    if args.output_dir:
        Path(args.output_dir).mkdir(parents=True, exist_ok=True)

    # Load model configuration
    with open(args.config_file, "w") as f:
        config = json.load(f)

    # Create model and datamodule
    model = ModelWrapper(config)
    datamodule = SecondaryStructureDatamodule(
        data_dir=args.data_dir,
        num_workers=args.num_workers,
        pin_memory=args.pin_memory
    )

    # Callbacks
    callbacks = []

    if args.checkpoint_every_epoch:
        epoch_ckpt_callback = ModelCheckpoint(
            dirpath=args.output_dir,
            filename='train-rna-{epoch}-{step}',
            every_n_epochs=1,
            save_top_k=-1
        )
        callbacks.append(epoch_ckpt_callback)

    # Loggers
    loggers = []

    if args.wandb:
        wandb_logger = WandbLogger(
            name=args.wandb_experiment_name,
            save_dir=args.output_dir,
            project=args.wandb_project,
            entity=args.wandb_entity,
            offline=args.wandb_offline,
            save_code=True,
        )
        loggers.append(wandb_logger)

    # Multi-GPU strategy
    strategy = "auto"
    if is_multiple_devices(args.devices):
        strategy = DDPStrategy(find_unused_parameters=False)

    # Training
    trainer = pl.Trainer(
        default_root_dir=args.output_dir,
        accelerator=args.accelerator,
        devices=args.devices,
        max_epochs=args.max_epochs,
        callbacks=callbacks,
        logger=loggers,
        log_every_n_steps=args.log_every_n_steps,
        precision=args.precision,
        strategy=strategy,
    )

    # Fit/test
    if args.command == "fit":
        trainer.fit(
            model=model,
            datamodule=datamodule,
            ckpt_path=args.ckpt_path
        )
    elif args.command == "test":
        trainer.test(
            model=model,
            datamodule=datamodule,
            ckpt_path=args.ckpt_path
        )
    else:
        raise ValueError("Unrecognized command!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="RNA secondary structure prediction"
    )

    # - - Command-agnostic arguments - -
    parent_parser = argparse.ArgumentParser()

    parent_parser.add_argument(
        "data_dir", type=str,
        help="Directory containing training, validation and test data"
    )

    parent_parser.add_argument(
        "--seed", type=int, default=None,
        help="Random seed"
    )
    parent_parser.add_argument(
        "--output_dir", type=str, default=None,
        help="""
            Directory for all the output files (checkpoints, logs, temporary
            files, etc.)
        """
    )

    parent_parser.add_argument(
        "--ckpt_path", type=str, default=None,
        help="""
            Path of the checkpoint from which the training is resumed
            or that is used for evaluation/prediction
        """
    )

    # Data loading
    parent_parser.add_argument(
        "--num_workers", type=int, default=0,
        help="How many subprocesses to use for data loading"
    )
    parent_parser.add_argument(
        "--pin_memory", action="store_true", default=False,
        help="""
            If activated, the data loader will copy Tensors into
            device/CUDA pinned memory before returning them
        """
    )

    # Trainer
    parent_parser.add_argument(
        "--accelerator", type=str, default='auto',
        help="""
            Supports passing different accelerator types (“cpu”, “gpu”, “tpu”,
            “ipu”, “hpu”, “mps”, “auto”)
        """
    )
    parent_parser.add_argument(
        "--devices", type=str, default='auto',
        help="The devices to use"
    )
    parent_parser.add_argument(
        "--precision", type=str, default='32-true',
        help="""
            Double precision, full precision, 16bit mixed precision or
            bfloat16 mixed precision
        """
    )

    # - - Command specification - -
    subparsers = parser.add_subparsers(
        dest="command", title="Available commands", required=True
    )

    # - - Fit - -
    fit_parser = subparsers.add_parser(
        "fit",
        help="Train the model", parents=[parent_parser]
    )

    # Checkpointing
    fit_parser.add_argument(
        "--checkpoint_every_epoch", action="store_true", default=False,
        help="Whether to checkpoint at the end of every training epoch"
    )

    # Logging
    fit_parser.add_argument(
        "--wandb", action="store_true", default=False,
        help="Whether to log metrics to Weights & Biases"
    )
    fit_parser.add_argument(
        "--wandb_offline", action="store_true", default=False,
        help="Run logging offline"
    )
    fit_parser.add_argument(
        "--wandb_experiment_name", type=str, default=None,
        help="Name of the current experiment. Used for wandb logging"
    )
    fit_parser.add_argument(
        "--wandb_project", type=str, default=None,
        help="Name of the wandb project to which this run will belong"
    )
    fit_parser.add_argument(
        "--wandb_entity", type=str, default=None,
        help="Wandb username or team name to which runs are attributed"
    )
    fit_parser.add_argument(
        "--log_every_n_steps", type=int, default=50,
        help="How often to log within steps"
    )

    # Trainer
    fit_parser.add_argument(
        "--max_epochs", type=int, default=-1,
        help=" Stop training once this number of epochs is reached"
    )

    # - - Test - -
    test_parser = subparsers.add_parser(
        "test",
        help="Evaluate the model on the test set", parents=[parent_parser]
    )

    args = parser.parse_args()
    args = update_args_with_parser_default_vals(
        args, fit_parser, test_parser
    )

    main(args)
