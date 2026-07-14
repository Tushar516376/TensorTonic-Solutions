import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.array(A)
    rows,cols=A.shape
    
    B = np.zeros((cols,rows), dtype=A.dtype)

    for i in range(cols):
        for j in range(rows):
            B[i,j] = A[j,i]
    
    return B
