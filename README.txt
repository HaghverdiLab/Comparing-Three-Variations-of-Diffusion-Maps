This report and computational experiments are written and carried out by Lilian Contius (lmarieac@gmail.com), based on parts from [Haghverdi et al, Nature Methods 2016].

may need to set up a virtual environment first:
    python3 -m venv path/to/venv
    source path/to/venv/bin/activate
install numpy, scipy, scikit-learn, matplotlib, pandas, jupyter

data:
- adrenal_medulla_subset_processed.csv used for real data
- toydata.csv used for simulated data
- toydata_increased_density.csv used for simulated data with 325 cells added close to cell 361

to run program:

locally scaled:

- loc_transition_matrix(data, k, sym=False, density=False, diag=False)
    - returns the transition matrix and zeroth eigenvector. 
    - need to load data before use 
    - need to specify k, the number of nearest neighbors considered when computing sigma
    - default is the preferred asymmetric version, without density normalization
    - to use other versions change set the relevant parameters to True
    - diag refers to compensation on the diagonal and is only relevant for symmetric versions 

- loc_diffusionmap(data, k, sym=False, density=False, diag=False, l = 4, DCa = 1, DCb = 2)
    - plots the diffusion map using the first two diffusion components
    - first parameters are the same as in loc_transition_matrix
    - l specifies the number of eigenvectors that are calculated
    - first two diffusion components, the second and third eigenvectors, are used for plots
    - to use other diffusion components change DCa and DCb, must be smaller than l

classic:

- T_classic(data1,sigma)
    - returns the transition matrix and zeroth eigenvector. 
    - need to load data before use 
    - need to specify sigma, used for all cells
    
- classic_diffusionmap(data, sigma, l = 4, DCa = 1, DCb = 2)
    - plots the diffusion map using the first two diffusion components
    - first parameters are the same as in loc_transition_matrix
    - l specifies the number of eigenvectors that are calculated
    - first two diffusion components, the second and third eigenvectors, are used for plots
    - to use other diffusion components change DCa and DCb, must be smaller than l
