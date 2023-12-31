# TimewarpVAE: Simultaneous Time-Warping and Representation Learning of Trajectories

This repository is the official implementation of [TimewarpVAE: Simultaneous Time-Warping and Representation Learning of Trajectories](). 

## Requirements and Setup
Install needed packages using something like
```
conda create --name timewarpvae --file conda_requirements.txt
conda activate timewarpvae
pip install -r pip_requirements.txt
```

Note that the pip_requirements.txt file was created by running `python -m pip list --format freeze > pip_requirements.txt` 
(and then removing the line about the locally-installed custom-dtw package from timewarp_lib).

In `timewarp_lib` directory, run the `./make.sh` command, or the `./make_nocuda.sh` if you do not have CUDA installed.

In this directory, run `make` to download and preprocess data


## Train and Evaluate Models 
For the experiments in our paper, we ran
train_fork_model.py  
train_fork_conv.py   
train_fork_notw_model.py  
train_model_notimewarpablation.py  
train_model.py                 
train_model_betavae.py    
train_model_no_tw.py               
train_model_timewarpvaedtw.py

created pca model on timing-augmented data using
train_pca_model.py
applied it using
`paper_calculations/PCA Model Applier.ipynb`

created and applied the Parametric DMP model using
'paper_calculations/dynamic_movement_primitive simple.ipynb'

