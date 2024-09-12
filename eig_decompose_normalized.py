import numpy as np
from scipy.sparse.linalg import eigs

# calculates the first l eigenvalues and -vectors of a transition matrix

def eig_decompose_normalized(T,l):
   # finds l eigenvalues of highest magnitude
   lambda_, phi = eigs(T,l,which = 'LM')
   
   # sort eigenvalues in descending order
   ind = np.flip(np.argsort(lambda_,axis=0),axis=0)
   lambda_ = np.take_along_axis(lambda_,ind,axis=0)
   phi = phi[:,ind]
   
   return phi, lambda_