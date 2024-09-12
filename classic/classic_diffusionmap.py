import matplotlib.pyplot as plt
import time
import numpy as np

import classic.T_classic as T_classic

import eig_decompose_normalized

# used to plot the classic diffusion map with fixed sigma
# density normalization is included since sigma is not locally scaled

def classic_diffusionmap(data, sigma, l = 4, DCa = 1, DCb = 2):
    if (DCa>=l) or (DCb >=l):
        print('diffusion components outside bounds, increase l to get higher diffusion components')
        return
    else:
        start = time.time()
        # get transition matrix 
        t, phi0 = T_classic.T_classic(data,sigma)
        
        # get diffusion components
        phi, lambda_ = eig_decompose_normalized.eig_decompose_normalized(t,l)
        
        # plot diffusion map using first two diffusion components
        plt.scatter(np.real(phi[:,DCa]),np.real(phi[:,DCb]), s=3)
        plt.xlabel('DC' + str(DCa))
        plt.ylabel('DC' + str(DCb))
        end = time.time()
        runtime = end - start
        print("Runtime: ")
        print(runtime)
        plt.show()
        return
