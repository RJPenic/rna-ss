import numpy as np
from pathlib import Path


def parse_ct_file(ct_file: Path) -> tuple[str, np.ndarray]:
    # TODO: CT file parsing, returns sequence (string) and
    # secondary structure in matrix form (np.ndarray)
    pass


def save_to_ct(sec_struct: np.ndarray, seq: str, ct_file: Path) -> None:
    # TODO: Save secondary structure (matrix representation) into the CT file
    pass


def prob_mat_to_sec_struct(
    probs: np.ndarray,
    seq: str,
    threshold: float = 0.5,
    allow_nc_pairs: bool = False,
    allow_sharp_loops: bool = False
) -> np.ndarray:
    # TODO: Convert matrix of base pairing probabilities into
    # a proper secondary structure (Greedy approach)
    pass
