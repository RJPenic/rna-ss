import torch
from torch.utils.data import Dataset
from lightning.pytorch import LightningDataModule
from torch.utils.data import DataLoader

from pathlib import Path
from tokenizer import RNATokenizer


class SecondaryStructureDataset(Dataset):
    def __init__(
        self,
        data_dir: Path
    ) -> None:
        super().__init__()

        self.tokenizer = RNATokenizer()
        self.data_dir = data_dir

    def __len__(self) -> int:
        # TODO: Return dataset size (number of structures)
        pass

    def __getitem__(self, idx: int) -> dict[str, object]:
        # TODO: Secondary structure file loading logic
        # Returns filename (without extension), tokenized sequence
        # and secondary structure (matrix representation) in a
        # dictionary (keys: "id", "tokens", "ss")
        pass


class SecondaryStructureDatamodule(LightningDataModule):
    def __init__(
        self,
        data_dir: Path,
        num_workers: int,
        pin_memory: bool,
    ) -> None:
        super().__init__()

        self.data_dir = data_dir
        self.num_workers = num_workers
        self.pin_memory = pin_memory

    def setup(self, stage: str) -> None:
        # TODO: Change the name of subdirs depending on your implementation
        if stage == "fit":
            self.train_dataset = SecondaryStructureDataset(
                self.data_dir / "train"
            )

        if stage in ("fit", "validate"):
            self.val_dataset = SecondaryStructureDataset(
                self.data_dir / "valid"
            )

        if stage == "test":
            self.test_dataset = SecondaryStructureDataset(
                self.data_dir / "test",
            )

    def train_dataloader(self) -> DataLoader:
        return DataLoader(
            self.train_dataset,
            batch_size=1,
            num_workers=self.num_workers,
            pin_memory=self.pin_memory,
            shuffle=True,
        )

    def val_dataloader(self) -> DataLoader:
        return DataLoader(
            self.val_dataset,
            batch_size=1,
            num_workers=self.num_workers,
            pin_memory=self.pin_memory,
        )

    def test_dataloader(self) -> DataLoader:
        return DataLoader(
            self.test_dataset,
            batch_size=1,
            num_workers=self.num_workers,
            pin_memory=self.pin_memory,
        )
