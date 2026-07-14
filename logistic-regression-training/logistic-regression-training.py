import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    X = np.asarray(X,dtype=float)
    Y = np.asarray(y,dtype=float)

    nsamples,nfeatures=X.shape

    w = np.zeros(nfeatures)
    b=0;

    for i in range(steps):

        z = X@w+b

        y_hat=_sigmoid(z)

        dw = (X.T@(y_hat-Y))/nsamples

        db = np.mean(y_hat-Y)

        w = w-lr*dw
        b = b-lr*db


    return w,b

    