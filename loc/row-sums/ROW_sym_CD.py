# used to analyze the effect of density normalization on the symmetric version with compensation on the diagonal
# returns rowsums before and after row-normalization (without density normalization)

import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.linalg import fractional_matrix_power
from sklearn.neighbors import NearestNeighbors

def ROW_sym_CD(data1,nsig):
    d2 = np.power(pdist(data1),2)
    d2 = squareform(d2)

    # finding the distance to the k nearest neighbors
    knn = NearestNeighbors(n_neighbors=nsig+1)
    knn.fit(data1)
    distances, indices = knn.kneighbors(data1)
    distances = np.array(distances)

    # calculating local sigma, based on distance to kth neighbor
    sigma = distances[:,nsig-1]/2
  
    sigmaT = sigma.reshape((-1,1))
    s = sigma*sigmaT

    sigmasquared = np.power(sigma,2)
    sigmasquaredT = sigmasquared.reshape((-1,1))
    s2 = np.add(sigmasquared, sigmasquaredT)

    # calculating kernel using local sigma, gives W matrix
    w1 = np.sqrt(2*s/s2)*np.exp(-d2/s2)
    w_sum = w1.sum(axis=1)

    d1_ = np.diag(w1.sum(axis=1))
    # symmetric row-normalization
    dp = fractional_matrix_power(d1_,-0.5)
    t1 = np.matmul(dp,w1)
    t1 = np.matmul(t1,dp)
    t_sum = t1.sum(axis=1)
    
    return w_sum, t_sum
    