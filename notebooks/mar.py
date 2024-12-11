# %% [markdown]
# Arjun Joshi. Brainstation Capstone. <br>
# December, 2024    <br>
# Diploma Program: Data Science

# %% [markdown]
# ![header.png](attachment:3b73122e-2c0e-41e1-acb2-2b0ec75981d0.png)

# %% [markdown]
# ##### Run intro scripts

# %%
pwd

# %%
import os
os.chdir('J:\\Brainstation\\BS Git\\Tampa_Apollo_AnthropogenicIndex\\notebooks\\scripts')

# %%
# Load libraries
%run imports.py
%run DataDictionary.py
%run stored_functions.py

# %% [markdown]
# ### **Introduction : Context and Notebook Overview**

# %%


# %% [markdown]
# <html>
# <style>
# sup {
#     vertical-align: super;
#     font-size: smaller;
# }
# </style>
# <p>Capstone. Case Study: Application of Anthropogenic WSM 
# <h1> <center>DATA CLEANING, EDA & PRE-PROCESSING
# <sup><h3> NEKTON AND BENTHIC ENVIRONMENTS. </h3></sup><center></center></h1>
# </html>
# 

# %% [markdown]
# #### Indexes

# %% [markdown]
# ##### Data Dictionary

# %% [markdown]
# ##### Abbreviations

# %% [markdown]
# Types:<br>
# Measurements.
# - **SDI** :   Shannon Diversity Index
# - **WQI**:   Water Quality Index
# - **TBNI**:  Tampa Bay Nekton Index
# - **TBBI**:  Tampa Bay Benthic Index
# 
# Organization:
# - **TBEP**:  Tampa Bay Estuary Program
# - **FWC**:   Florida Fish and Wildlife Commission
# - **NOAA**:  National Oceanic and Atmospheric
# - **NMFS**:  National Marine Fisheries Service
# - **HC**:    Hillsborough County
# - **HCPA**:  Hillsborough COunty Property Appraiser
# 
# Locations:
# - **HB**: Hillsborough Bay
# - **MTB**: Middle Tampa Bay
# - **OTB**: Old Tampa Bay
# - **LTB**: Lower Tampa Bay
# Other:
# - **Nit**: Nitrates
# - **Phos**: Phosphate

# %% [markdown]
# ##### Data Dictionary

# %%
pwd

# %%
run scripts/datadictionary.py

# %%
dic_df

# %%


# %%


# %%


# %% [markdown]
# #### Overview
# 
# This notebook serves to preprocess the data for the marine environments. The 2 marine environments included in this preliminary study are part of the PELAGIC system and the BENTHIC system in all subsections of Tampa Bay (defined below). 
# 
# 
# DESCRIPTIONS.<br>
# * NEKTON. <br>
#     In the open ocean, Nekton describes organisms of all types (animals, plants, archea) that live in the pelagic system. The pelagic system is defined as the area between the surface and the sea floor. Granted  Nekton should be understood as the species of fish that move freely through the water and the bay, for example a fish that moves from reef to reef finding fish. This doesn't change the implications of this particulary study, we notate this as part of documentation and understanding of any user or reader of this code.
# 
# * BENTHIC. <br>
#     The Benthic system is defined as the sea floor - both on the surface of the sea floor and the sediments of the sea floor. The types of organisms found here are distinct from any other system and have little overlap in species.
# 

# %%
pwd

# %%
from chronos import ChronosPipeline

# %%
import torch

# %%
from chronos import ChronosPipeline

# %%
pip install chronos

# %%
import chronos

# %%
from chronos import ChronosPipeline

# %%
pip install git+https://github.com/amazon-science/chronos-forecasting.git

# %%



