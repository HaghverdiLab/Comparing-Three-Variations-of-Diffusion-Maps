# used to plot rowsums to analyze the effect of density normalization on the symmetric version with compensation on the diagonal

import loc.row_sums.ROW_sym_CD_D as ROW_sym_CD_D
import loc.row_sums.ROW_sym_CD as ROW_sym_CD
import matplotlib.pyplot as plt

def plot_rowsums(data,k):
    w_sum_D, t_sum_D = ROW_sym_CD_D.ROW_sym_CD_D(data, k)
    w_sum, t_sum = ROW_sym_CD.ROW_sym_CD(data, k)

    fig, axs = plt.subplots(2, 2, figsize=(10,7))
    plt.subplots_adjust(wspace = 0.5, hspace = 0.7)
    axs[0,0].plot(t_sum_D)
    axs[0,0].set_title('Plot 1 \n Rowsums of transition matrix \n with density normalization')
    axs[0,0].set_xlabel('Row number')
    axs[0,0].set_ylabel('Row sum')
    axs[0,1].plot(t_sum)
    axs[0,1].set_title('Plot 2 \n Rowsums of transition matrix \n without density normalization')
    axs[0,1].set_xlabel('Row number')
    axs[0,1].set_ylabel('Row sum')
    axs[1,0].plot(w_sum_D)
    axs[1,0].set_title('Plot 3 \n Rowsums before row normalization \n with density normalization')
    axs[1,0].set_xlabel('Row number')
    axs[1,0].set_ylabel('Row sum')
    axs[1,1].plot(w_sum)
    axs[1,1].set_title('Plot 4 \n Rowsums before row normalization \n without density normalization')
    axs[1,1].set_xlabel('Row number')
    axs[1,1].set_ylabel('Row sum')
    plt.show()