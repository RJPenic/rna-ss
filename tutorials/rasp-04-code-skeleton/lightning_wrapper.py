import torch
import pytorch_lightning as pl


class ModelWrapper(pl.LightningModule):
    def __init__(
        self,
        config: dict
    ) -> None:
        super().__init__()
        self.save_hyperparameters()

        self.config = config

        # TODO: Initialize model and loss modules
        self.model = None
        self.loss = None

    def forward(self, tokens: torch.Tensor) -> torch.Tensor:
        logits = self.model(tokens)
        return logits

    def _common_step(
        self,
        batch: tuple[torch.Tensor, torch.Tensor],
        batch_idx: int,
        log_prefix: str,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        # TODO: Shared training/evaluation logic
        # (e.g. forward pass, loss calculation),
        # return loss and SS prediction logits
        pass

    def training_step(
        self,
        batch: dict[str, object],
        batch_idx: int
    ) -> torch.Tensor:
        loss, _ = self._common_step(batch, batch_idx, log_prefix="train")
        return loss

    def validation_step(
        self,
        batch: dict[str, object],
        batch_idx: int,
    ) -> None:
        self._eval_step(batch, batch_idx, log_prefix="val")

    def test_step(
        self,
        batch: dict[str, object],
        batch_idx: int,
    ) -> None:
        self._eval_step(batch, batch_idx, log_prefix="test")

    def _eval_step(
        self,
        batch: dict[str, object],
        batch_idx: int,
        log_prefix: str,
    ) -> None:
        _, logits = self._common_step(batch, batch_idx, log_prefix=log_prefix)

        # TODO: Convert base pairing probabilities into SS
        # TODO: Log metrics (Recall, F1, etc.)
        # TODO: If testing, save secondary structures in the output directory
        pass

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=self.config["lr"])
        return optimizer
