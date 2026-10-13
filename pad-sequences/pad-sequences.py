import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if len(seqs) == 0 :
        return np.empty((0, 0), dtype=int)
    
    if max_len is None :
        seq_lengths = [len(x) for x in seqs]
        max_len = max(seq_lengths)

    padded_seq = [(seq + ([pad_value] * (max_len - len(seq)))) if max_len >= len(seq) else seq[:max_len] for seq in seqs]
    ans = np.array(padded_seq, dtype=int)
    return ans