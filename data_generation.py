import numpy as np
import matplotlib.pyplot as plt

# ==================================================
# dataset 1: An independent Gaussian design
# ==================================================

def generate_sparse_linear_data(n=1000,d=50,s=5,sigma=1.0,signal=2.0,random_seeds=100):
    if s>d:
        raise ValueError("s must be less than or equal to d")
    if n<=0 or d<=0:
        raise ValueError("n and d must be positive")
    if sigma<0:
        raise ValueError("sigma must be nonnegative")
    # initialize random generator
    rng=np.random.default_rng(random_seeds)
    # generate feature matrix X ~ N(0, I)
    X=rng.normal(0,1,size=(n,d))
    # initialize sparse coefficient vector
    w_true=np.zeros(d)
    # randomly select nonzero positions
    support=rng.choice(d,size=s,replace=False)
    # assign values (+/- signal) to nonzero coefficients
    signs=rng.choice([-1,1],size=s)
    w_true[support]=signal*signs
    # generate Gaussian noise
    epsilon=rng.normal(0,sigma,size=n)
    # generate response
    y=X@w_true+epsilon
    # X: feature matrix (nxd)
    # y: response vector (n,)
    # w_true: true coefficient vector (d,)
    # support: indices of nonzero coefficients
    return X,y,w_true,support

# ==================================================
# dataset 2: A correlated Gaussian design
# ==================================================

def generate_toeplitz_covariance(d=50,rho=0.5):
    if not (-1<rho<1):
        raise ValueError("rho must be between -1 and 1")
    # create index array [0,1,2,...,d-1]
    indices=np.arange(d)
    # compute pairwise distance |i-j| for all pairs
    # subtract.outer gives a matrix where entry (i,j) = i - j
    # then take absolute value to get |i-j|
    # finally apply rho^|i-j| to build covariance
    Sigma=rho**np.abs(np.subtract.outer(indices,indices))
    # Sigma: covariance matrix (d x d)
    # diagonal = 1 (since rho^0 = 1)
    # off-diagonal decays as distance increases
    return Sigma

def generate_correlated_sparse_linear_data(n=1000,d=50,s=5,sigma=1.0,signal=2.0,rho=0.5,random_seeds=100):
    if s>d:
        raise ValueError("s must be less than or equal to d")
    if n<=0 or d<=0:
        raise ValueError("n and d must be positive")
    if sigma<0:
        raise ValueError("sigma must be nonnegative")
    rng=np.random.default_rng(random_seeds)
    Sigma=generate_toeplitz_covariance(d=d,rho=rho)
    # generate X ~ N(0, Sigma)
    # each row of X is a d-dimensional vector with correlation defined by Sigma
    # this is different from independent case (where covariance = I)
    X=rng.multivariate_normal(
        mean=np.zeros(d),
        cov=Sigma,
        size=n
    )
    w_true=np.zeros(d)
    support=rng.choice(d,size=s,replace=False)
    signs=rng.choice([-1,1],size=s)
    w_true[support]=signal*signs
    epsilon=rng.normal(0,sigma,size=n)
    y=X@w_true+epsilon
    # X: feature matrix (nxd)
    # y: response vector (n,)
    # w_true: true coefficient vector (d,)
    # support: indices of nonzero coefficients
     # Sigma: covariance matrix
    return X,y,w_true,support,Sigma

# ==================================================
# dataset 3: high-dimensional sparse design (d > n)
# use the same generation function, but set d > n
# ==================================================