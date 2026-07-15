import numpy as np

def dropout(x, p=0.5, rng=None):
    X = np.asarray(x, dtype=float)

    if rng is None:
        pattern = (np.random.random(X.shape) >= p).astype(int)
    else:
        pattern = (rng.random(X.shape) >= p).astype(int)

    output = X * pattern/(1-p)

    pattern = pattern/(1-p)

    return output, pattern