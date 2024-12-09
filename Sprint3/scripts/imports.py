#### Load Libraries ####

# System
import os
import glob as glob

# Standard Imports
import pandas as pd
import numpy as np

import numpy as np
import pandas as pd
import glob as glob
import os as os
import statsmodels.api as sm 
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Visuals
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import seaborn as sns


### Statistics Packages ###

# Operations
from sklearn.model_selection import train_test_split

#Time Series Analysis
import statsmodels.tsa as tsa
from statsmodels.graphics.tsaplots import month_plot
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose

#VIF
from statsmodels.stats.outliers_influence import variance_inflation_factor #VIF

#Scalers
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

#Regression
from sklearn.linear_model import Lasso, Ridge
from sklearn.linear_model import LinearRegression

#NN
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense


