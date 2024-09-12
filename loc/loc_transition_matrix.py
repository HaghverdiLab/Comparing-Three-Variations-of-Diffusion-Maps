import loc.T_asym as T_asym
import loc.T_asym_D as T_asym_D
import loc.T_sym as T_sym
import loc.T_sym_D as T_sym_D
import loc.T_sym_CD as T_sym_CD
import loc.T_sym_CD_D as T_sym_CD_D

# used to calculate the locally scaled transition matrix and the first eigenvector

def loc_transition_matrix(data, k, sym=False, density=False, diag=False):
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
    return t, phi0