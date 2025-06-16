class RNATokenizer:
    NUC2IDX = {
        "P": 0,  # Padding
        "A": 1,  # Adenine
        "C": 2,  # Cytosine
        "G": 3,  # Guanine
        "T": 4,  # Thymine (Uracil)
        "N": 5,  # Undefined nucleotide
    }

    def tokenize(self, seq: str) -> list[int]:
        # TODO: Implement RNA seq tokenization (e.g. "AGA" => [1, 3, 1])
        pass
