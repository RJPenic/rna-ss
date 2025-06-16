import torch
from torch import nn


class SecondaryStructurePredictor(nn.Module):
    def __init__(
        self,
        embed_dim: int,
        num_blocks: int,
        conv_dim: int,
        kernel_size: int,
    ):
        super().__init__()

        # TODO: Initialize model components
        pass

    def forward(self, tokens: torch.Tensor) -> torch.Tensor:
        # TODO: Model forward pass
        # Output: Base pairing logits matrix
        pass
