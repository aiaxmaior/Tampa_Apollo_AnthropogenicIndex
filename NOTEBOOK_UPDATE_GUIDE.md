# Notebook Update Guide

This guide explains how to update your existing notebooks to use the new data loading system with Parquet files and relative paths.

## Changes Overview

1. **Remove hardcoded Windows paths** (`J:\Brainstation\...`)
2. **Use data_loader module** instead of direct CSV reading
3. **Use relative paths** for all file operations
4. **Load from Parquet** instead of CSV

---

## Step-by-Step Updates

### 1. Replace Path Setup (At the top of each notebook)

**OLD CODE (Remove this):**
```python
import os
os.chdir('J:\\Brainstation\\BS Git\\Capstone\\notebooks')
```

**NEW CODE (Replace with this):**
```python
# Setup paths (works on any OS, any machine)
import sys
from pathlib import Path

# Get the notebook directory
notebook_dir = Path.cwd()
project_root = notebook_dir.parent if notebook_dir.name == 'notebooks' else notebook_dir
scripts_dir = project_root / 'scripts'

# Add scripts to path for importing utilities
sys.path.insert(0, str(scripts_dir))

print(f"Project root: {project_root}")
print(f"Notebook dir: {notebook_dir}")
```

---

### 2. Replace Data Loading

**OLD CODE (CSV loading):**
```python
# Old way - loading CSV with hardcoded paths
df = pd.read_csv('bBioAdj_1.csv')
nekton_df = pd.read_csv('Nekton.csv')
construction_df = pd.read_csv('construction.csv')
```

**NEW CODE (Parquet with data_loader):**
```python
# Import the data loader
from data_loader import load_marine_data, load_data, load_nitrogen_data

# Load marine data
benthic_df = load_marine_data('benthic')
nekton_df = load_marine_data('nekton')

# Load anthropogenic data
construction_df = load_data('construction')
population_df = load_data('population')
dev_pct_change_df = load_data('development_pct_change')

# Load nitrogen/water quality data
kjeldahl_df = load_nitrogen_data('kjeldahl')
nitrate_df = load_nitrogen_data('nitrate')
ammonia_df = load_nitrogen_data('ammonia')
nitrogen_final_df = load_nitrogen_data('nitrogen_final')
```

**Alternative (for all datasets at once):**
```python
from data_loader import load_all_data

# Load everything into a dictionary
data = load_all_data()

# Access datasets
benthic_df = data['benthic']
nekton_df = data['nekton']
construction_df = data['construction']
```

---

### 3. Update Image/Output Paths

**OLD CODE:**
```python
# Saving figures with absolute paths
plt.savefig('J:\\Brainstation\\BS Git\\Capstone\\Visualizations\\my_plot.png')
```

**NEW CODE:**
```python
# Use relative paths
output_dir = project_root / 'Capstone_Visualizations'
output_dir.mkdir(exist_ok=True)  # Create if doesn't exist

plt.savefig(output_dir / 'my_plot.png', dpi=300, bbox_inches='tight')
```

---

### 4. Update Imports Section

**OLD CODE:**
```python
# Scattered imports or importing from scripts with absolute paths
sys.path.insert(0, 'J:\\Brainstation\\BS Git\\Capstone\\scripts')
from imports import *
```

**NEW CODE:**
```python
# Clear, organized imports at the top
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.vector_ar.var_model import VAR
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Import project utilities
from data_loader import load_marine_data, load_data, load_nitrogen_data
from stored_functions import check_stationarity, set_plotcolor
```

---

## Notebook-Specific Changes

### For: `EstuarineEcosystems_ProcEdaBLModel_FINAL.ipynb`

**Data loading updates:**
```python
# OLD
bBioAdj = pd.read_csv('bBioAdj_1.csv')

# NEW
bBioAdj = load_marine_data('benthic')
nekton = load_marine_data('nekton')
```

---

### For: `AnthropogenicPressure_ProcEdaBLModel_FINAL.ipynb`

**Data loading updates:**
```python
# OLD
construction = pd.read_csv('construction.csv')
pop_data = pd.read_csv('population_data.csv')
pct_change = pd.read_csv('percentchange_dev.csv')
kjeldahl = pd.read_csv('kjeldahl.csv')
nitrate = pd.read_csv('nitrate.csv')
ammonia = pd.read_csv('ammonia.csv')

# NEW
construction = load_data('construction')
pop_data = load_data('population')
pct_change = load_data('development_pct_change')
kjeldahl = load_nitrogen_data('kjeldahl')
nitrate = load_nitrogen_data('nitrate')
ammonia = load_nitrogen_data('ammonia')
```

---

### For: `Final_A.P.Index_RNN_FINAL.ipynb`

**Data loading updates:**
```python
# OLD
nitrogen_final = pd.read_csv('NIT_FINAL.csv')
benthic = pd.read_csv('bBioAdj_1.csv')
nekton = pd.read_csv('Nekton.csv')

# NEW
nitrogen_final = load_nitrogen_data('nitrogen_final')
benthic = load_marine_data('benthic')
nekton = load_marine_data('nekton')
```

---

## Complete Example: First Cell of Each Notebook

Replace the first code cell in each notebook with this standardized setup:

```python
"""
Tampa Bay Anthropogenic Index
[Notebook Name]

Author: Arjun Joshi
Brainstation Data Science Diploma - December 2024
"""

# ============================================
# Environment Setup
# ============================================
import sys
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Setup paths (cross-platform compatible)
notebook_dir = Path.cwd()
project_root = notebook_dir.parent if notebook_dir.name == 'notebooks' else notebook_dir
scripts_dir = project_root / 'scripts'
viz_dir = project_root / 'Capstone_Visualizations'

# Add scripts to path
sys.path.insert(0, str(scripts_dir))

# Verify paths
print(f"✓ Project root: {project_root}")
print(f"✓ Scripts dir: {scripts_dir}")
print(f"✓ Notebook dir: {notebook_dir}")

# ============================================
# Imports
# ============================================
# Core libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Stats and ML
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.vector_ar.var_model import VAR

# Deep Learning (if needed)
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dense, Dropout

# Project utilities
from data_loader import load_marine_data, load_data, load_nitrogen_data
from stored_functions import check_stationarity, set_plotcolor

# Plotting style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("✓ All imports successful")

# ============================================
# Load Data
# ============================================
# [Add specific data loading for this notebook here]
```

---

## Testing Your Updates

After updating a notebook, verify it works:

1. **Restart kernel and clear outputs:**
   - In Jupyter: `Kernel > Restart & Clear Output`

2. **Run all cells:**
   - `Cell > Run All`

3. **Check for errors:**
   - Look for path-related errors
   - Verify data loads correctly
   - Check that all visualizations save properly

4. **Verify outputs:**
   - Check that figures are saved to correct directory
   - Ensure relative paths work on your system

---

## Common Issues and Solutions

### Issue: "Module not found: data_loader"
**Solution:**
```python
# Make sure scripts are in path
import sys
from pathlib import Path
scripts_dir = Path.cwd().parent / 'scripts'
sys.path.insert(0, str(scripts_dir))
```

### Issue: "File not found: [dataset].parquet"
**Solution:**
1. Check that CSV files are in `data/raw_csv/`
2. Run conversion: `python scripts/convert_csv_to_parquet.py`
3. Verify files exist in `data/parquet/`

### Issue: Plots not saving
**Solution:**
```python
# Create output directory if it doesn't exist
viz_dir = project_root / 'Capstone_Visualizations'
viz_dir.mkdir(exist_ok=True)
plt.savefig(viz_dir / 'plot.png')
```

---

## Checklist for Each Notebook

- [ ] Remove hardcoded Windows paths
- [ ] Add path setup cell at the top
- [ ] Replace `pd.read_csv()` with `load_data()` functions
- [ ] Update all file save paths to use relative paths
- [ ] Add scripts directory to Python path
- [ ] Test by restarting kernel and running all cells
- [ ] Verify all outputs are created correctly
- [ ] Commit changes to Git

---

## Benefits of These Changes

✓ **Portability** - Works on Windows, Mac, Linux
✓ **Reproducibility** - Anyone can clone and run
✓ **Efficiency** - Parquet loads 3-5x faster than CSV
✓ **Smaller files** - 40-70% size reduction
✓ **Type safety** - Parquet preserves data types
✓ **Cleaner code** - Centralized data loading logic
✓ **Version control** - Better Git diffs with Parquet

---

## Next Steps

After updating all notebooks:

1. Run the full analysis pipeline
2. Verify all outputs are generated
3. Update README if any workflow changes
4. Commit all changes to Git
5. Create a fresh clone and test reproducibility
