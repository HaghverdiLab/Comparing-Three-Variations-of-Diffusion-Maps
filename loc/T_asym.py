import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.linalg import fractional_matrix_power
from sklearn.neighbors import NearestNeighbors

def T_asym(data1,nsig):
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

    d1_ = np.diag(w1.sum(axis=1))
    # asymmetric row-normalization
    dp = fractional_matrix_power(d1_,-1)
    t1 = np.matmul(dp,w1)

    # calculating the first eigenvector, phi0
    a = np.diag(d1_)
    b = np.sqrt(sum(np.power(a,2)))
    phi0 = np.divide(a,b)

    return t1, phi0
