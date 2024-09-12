import matplotlib.pyplot as plt
import time
import numpy as np

import loc.T_asym as T_asym
import loc.T_asym_D as T_asym_D
import loc.T_sym as T_sym
import loc.T_sym_D as T_sym_D
import loc.T_sym_CD as T_sym_CD
import loc.T_sym_CD_D as T_sym_CD_D

import eig_decompose_normalized

# used to plot the locally scaled diffusion map

def loc_diffusionmap(data, k, sym=False, density=False, diag=False, l = 4, DCa = 1, DCb = 2):
    if (DCa>=l) or (DCb >=l):
        print('diffusion components outside bounds, increase l to get higher diffusion components')
        return
    else:
        start = time.time()
        # get transition matrix 
        # asymmetric without density normalization
        if (sym == False):
            t, phi0 = T_asym.T_asym(data,k)
        # assymetric with density normalization
        if (sym == False) and (density == True):
            t, phi0 = T_asym_D.T_asym_D(data,k)
        # symmetric without density normalization, without compensation on diagonal
        if (sym == True):
            t, phi0 = T_sym.T_sym(data,k)
        # symmetric with density normalization, without compensation on diagonal  
        if (sym == True) and (density == True):
            t, phi0 = T_sym_D.T_sym_D(data,k)
        # symmetric without density normalization, with compensation on diagonal
        if (sym == True) and (diag == True):
            t, phi0 = T_sym_CD.T_sym_CD(data,k)
        # symmetric with density normalization with compensation on diagonal
        if (sym == True) and (density == True) and (diag == True):
            t, phi0 = T_sym_CD_D.T_sym_CD_D(data,k)
        
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
