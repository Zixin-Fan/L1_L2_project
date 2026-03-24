import numpy as np
import matplotlib.pyplot as plt

def generate_sparse_linear_data(n=1000,d=50,s=5,sigma=1.0,signal=2.0,random_seeds=100):
    # initialize random generator
    rng=np.random.default_rng(random_seeds)
    # generate feature matrix X ~ N(0, I)
    X=rng.normal(0,1,size=(n,d))
    # initialize sparse coefficient vector
    w_true=np.zeros(d)
    # randomly select nonzero positions
    non0=rng.choice(d,size=s,replace=False)
    # assign values (+/- signal) to nonzero coefficients
    signs=rng.choice([-1,1],size=s)
    w_true[non0]=signal*signs
    # generate Gaussian noise
    epsilon=rng.normal(0,sigma,size=n)
    # generate response
    y=X@w_true+epsilon
    # X: feature matrix (n x d)
    # y: response vector (n,)
    # w_true: true coefficient vector (d,)
    # non0: indices of nonzero coefficients
    return X,y,w_true,non0