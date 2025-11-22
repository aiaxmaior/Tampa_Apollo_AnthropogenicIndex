# Tampa Bay Anthropogenic Index - Setup Guide

Quick setup guide to get this project running on your machine.

## Prerequisites

- Python 3.8 - 3.10 (recommended)
- Git
- pip or conda

## Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd Tampa_Apollo_AnthropogenicIndex
```

### 2. Create Virtual Environment

**Using conda (recommended):**
```bash
conda create -n tampa_bay python=3.9
conda activate tampa_bay
```

**Using venv:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages:
- pandas, numpy (data manipulation)
- matplotlib, seaborn, plotly (visualization)
- scikit-learn (machine learning)
- statsmodels (time series analysis)
- tensorflow (deep learning - LSTM models)
- pyarrow (Parquet file support)

### 4. Prepare Data Files

#### Option A: You Have the Original CSV Files

1. Place all CSV files in the `data/raw_csv/` directory:
   ```bash
   # Example: copy from your original location
   cp /path/to/your/csv/files/*.csv data/raw_csv/
   ```

2. Convert CSVs to Parquet format:
   ```bash
   python scripts/convert_csv_to_parquet.py
   ```

   This will:
   - Read all CSV files from `data/raw_csv/`
   - Convert them to efficient Parquet format
   - Save to `data/parquet/`
   - Show compression statistics (typically 40-70% smaller)

3. Verify conversion:
   ```bash
   python scripts/data_loader.py
   ```

#### Option B: Data Already Converted (Parquet files in repo)

If Parquet files are already in `data/parquet/`, you can skip the conversion step.

**Verify data is available:**
```bash
python scripts/data_loader.py
```

### 5. Launch Jupyter

```bash
jupyter notebook
```

Or if using JupyterLab:
```bash
jupyter lab
```

### 6. Run the Notebooks

Navigate to the `notebooks/` directory and run in this order:

1. **EstuarineEcosystems_ProcEdaBLModel_FINAL.ipynb** - Marine ecosystem EDA
2. **AnthropogenicPressure_ProcEdaBLModel_FINAL.ipynb** - Anthropogenic factors analysis
3. **Final_A.P.Index_RNN_FINAL.ipynb** - LSTM modeling and API formation

---

## Project Structure

```
Tampa_Apollo_AnthropogenicIndex/
├── README.md                          # Project overview and documentation
├── SETUP.md                          # This file - setup instructions
├── NOTEBOOK_UPDATE_GUIDE.md          # Guide for updating notebooks
├── requirements.txt                  # Python dependencies
├── .gitignore                        # Git exclusions
│
├── data/                             # Data directory
│   ├── README.md                     # Data documentation
│   ├── raw_csv/                      # Original CSV files (not in Git)
│   ├── parquet/                      # Converted Parquet files (in Git)
│   └── processed/                    # Intermediate/processed data
│
├── scripts/                          # Utility scripts
│   ├── convert_csv_to_parquet.py    # CSV to Parquet converter
│   └── data_loader.py               # Centralized data loading
│
├── notebooks/                        # Jupyter notebooks
│   ├── EstuarineEcosystems_ProcEdaBLModel_FINAL.ipynb
│   ├── AnthropogenicPressure_ProcEdaBLModel_FINAL.ipynb
│   ├── Final_A.P.Index_RNN_FINAL.ipynb
│   ├── scripts/                      # Notebook utilities
│   │   ├── imports.py
│   │   ├── stored_functions.py
│   │   └── DataDictionary.py
│   └── images/                       # Notebook images
│
├── Capstone_Visualizations/          # Output visualizations
├── Presentations/                    # Project presentations
├── img/                              # Documentation images
└── ArchivedMaterials/                # Historical work
```

---

## Required Data Files

The project requires the following CSV files in `data/raw_csv/`:

### Marine Ecosystem Data
- `bBioAdj_1.csv` - Benthic biodiversity with TBBI scores
- `Nekton.csv` - Nekton/pelagic data with TBNI scores

### Anthropogenic Data
- `construction.csv` - Property development records
- `percentchange_dev.csv` - Development rate changes
- `population_data.csv` - Population growth data
- `dfdemographics.csv` - Demographic data

### Water Quality Data
- `kjeldahl.csv` - Organic nitrogen
- `nitrate.csv` - Nitrate concentrations
- `ammonia.csv` - Ammonia concentrations
- `Nitrates_VAR_organics.csv` - VAR analysis data
- `NIT_FINAL.csv` - Processed nitrogen data

See `data/README.md` for more details on data sources.

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'xyz'"
**Solution:** Install requirements
```bash
pip install -r requirements.txt
```

### "FileNotFoundError: Data file not found"
**Solution:**
1. Check CSV files are in `data/raw_csv/`
2. Run conversion: `python scripts/convert_csv_to_parquet.py`
3. Verify with: `python scripts/data_loader.py`

### "No CSV files found in data/raw_csv/"
**Solution:** Place your CSV files in the `data/raw_csv/` directory

### Jupyter kernel not found
**Solution:** Install kernel for your environment
```bash
python -m ipykernel install --user --name tampa_bay --display-name "Python (Tampa Bay)"
```

### TensorFlow installation issues (M1/M2 Mac)
**Solution:** Use conda for TensorFlow on Apple Silicon
```bash
conda install -c apple tensorflow-deps
pip install tensorflow-macos tensorflow-metal
```

### Import errors in notebooks
**Solution:** Ensure the first cell includes path setup:
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd().parent / 'scripts'))
```

---

## Data Sources

### Tampa Bay Estuary Program (TBEP)
- Website: https://www.tbep.org/
- Marine ecosystem and water quality data

### U.S. Census Bureau
- Website: https://www.census.gov/
- Population and demographic data

### Hillsborough County Property Appraiser
- Website: https://www.hcpafl.org/
- Property development data

### Florida DEP
- Website: https://floridadep.gov/
- Water quality monitoring data

---

## Running Specific Analyses

### Vector Autoregression (VAR) Analysis
Found in: `AnthropogenicPressure_ProcEdaBLModel_FINAL.ipynb`
- Analyzes relationships between nitrogen compounds over time
- Establishes seasonality patterns
- Uses 4-week lag periods

### LSTM Neural Network
Found in: `Final_A.P.Index_RNN_FINAL.ipynb`
- Predicts TBNI (Tampa Bay Nekton Index) using API
- Two-layer LSTM architecture
- MSE < 3.5%

### Anthropogenic Pressure Index (API)
Calculated as weighted sum of standardized values:
- Nitrogen compounds (inorganic)
- Population growth
- Development rates

---

## Development

### Running Tests (if implemented)
```bash
pytest tests/
```

### Code Formatting (if using black)
```bash
black notebooks/scripts/
```

### Generating Frozen Requirements
```bash
pip freeze > requirements_frozen.txt
```

---

## Contributing

If you're continuing development:

1. Create a new branch for your work
2. Update notebooks using `NOTEBOOK_UPDATE_GUIDE.md`
3. Test thoroughly (restart kernel, run all)
4. Document any new data sources or methods
5. Update README if workflow changes

---

## Getting Help

**Documentation:**
- `README.md` - Project overview and research background
- `data/README.md` - Data documentation and sources
- `NOTEBOOK_UPDATE_GUIDE.md` - Updating notebooks

**Issues:**
- Check existing data files with: `python scripts/data_loader.py`
- Verify environment: `pip list`
- Check Python version: `python --version`

**Research References:**
See the References section in `README.md` for academic literature and methodology.

---

## Next Steps After Setup

1. **Verify everything works:**
   - Run `python scripts/data_loader.py` to check data
   - Open and run the first few cells of each notebook
   - Check that visualizations are generated

2. **Complete unfinished execution:**
   - `EstuarineEcosystems` notebook needs full execution (currently 13%)
   - `RNN_FINAL` notebook needs completion (currently 74%)

3. **Review outputs:**
   - Check `Capstone_Visualizations/` for generated plots
   - Verify model results match expectations

4. **Next phase development:**
   - Refine API weight values
   - Add geospatial analysis
   - Implement real-time data integration

---

## License

[Add your license here]

## Contact

**Author:** Arjun Joshi
**Program:** Brainstation Data Science Diploma
**Date:** December 2024
