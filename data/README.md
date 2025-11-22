# Data Directory

This directory contains all datasets used in the Tampa Bay Anthropogenic Index project.

## Directory Structure

```
data/
├── raw_csv/        # Place your original CSV files here (not committed to Git)
├── parquet/        # Converted Parquet files (committed to Git)
└── processed/      # Processed/intermediate datasets
```

## Required Data Files

### Marine Ecosystem Data
- **bBioAdj_1.csv** - Benthic biodiversity with TBBI scores
- **Nekton.csv** - Nekton/pelagic data with TBNI scores

### Anthropogenic Pressure Data
- **construction.csv** - Property development and construction records
- **percentchange_dev.csv** - Development rate changes over time
- **population_data.csv** - Population growth data
- **dfdemographics.csv** - Demographic data

### Water Quality / Nitrogen Data
- **kjeldahl.csv** - Organic nitrogen (Kjeldahl method)
- **nitrate.csv** - Nitrate concentrations
- **ammonia.csv** - Ammonia concentrations
- **Nitrates_VAR_organics.csv** - Vector Autoregression analysis data
- **NIT_FINAL.csv** - Processed nitrogen data

## Setup Instructions

### Step 1: Place CSV Files

Place all your original CSV files in the `raw_csv/` directory:

```bash
# From your original data location, copy files to raw_csv/
cp /path/to/your/csv/files/*.csv data/raw_csv/
```

### Step 2: Convert to Parquet

Run the conversion script to convert all CSV files to Parquet format:

```bash
python scripts/convert_csv_to_parquet.py
```

This will:
- Read all CSV files from `data/raw_csv/`
- Convert them to Parquet format (compressed, efficient)
- Save them to `data/parquet/`
- Show compression statistics

**Benefits of Parquet:**
- 40-70% smaller file size than CSV
- Faster loading times
- Better for Git (compressed, binary diff)
- Preserves data types

### Step 3: Verify Data

Check that all files were converted successfully:

```bash
python scripts/data_loader.py
```

This will show you the status of all expected datasets.

## Using Data in Notebooks

Use the `data_loader` module for consistent data loading:

```python
import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path.cwd().parent / 'scripts'))
from data_loader import load_data, load_marine_data, load_nitrogen_data

# Load specific datasets
benthic_df = load_marine_data('benthic')
nekton_df = load_marine_data('nekton')
construction_df = load_data('construction')
nitrogen_df = load_nitrogen_data('nitrogen_final')

# Load all datasets
from data_loader import load_all_data
all_data = load_all_data()
```

## Data Sources

### Tampa Bay Estuary Program (TBEP)
- **Website**: https://www.tbep.org/
- **Data Portal**: https://www.tbep.org/data-and-reports/
- Marine ecosystem data (benthic, nekton sampling)
- Water quality monitoring data
- TBBI and TBNI index scores

### U.S. Census Bureau
- **Website**: https://www.census.gov/
- Population data by county and census tract
- Demographic data

### Hillsborough County Property Appraiser
- **Website**: https://www.hcpafl.org/
- Property development records
- Building permits
- Construction data

### Florida Department of Environmental Protection (FDEP)
- **Website**: https://floridadep.gov/
- Water quality data
- Nitrogen compound measurements (nitrate, ammonia, Kjeldahl)

## Notes

- **CSV files are NOT committed to Git** - They're excluded via `.gitignore`
- **Parquet files ARE committed to Git** - They're optimized and compressed
- Keep original CSV files in `raw_csv/` as a local backup
- Never modify files in `parquet/` directly - regenerate from CSVs if needed

## File Size Expectations

Typical file sizes after conversion:

| File | CSV Size | Parquet Size | Compression |
|------|----------|--------------|-------------|
| bBioAdj_1 | ~50 MB | ~15 MB | ~70% |
| Nekton | ~80 MB | ~25 MB | ~68% |
| construction | ~20 MB | ~6 MB | ~70% |
| nitrogen data | ~5-10 MB | ~2-3 MB | ~60% |

*Actual sizes depend on your specific datasets*

## Troubleshooting

### "File not found" error
1. Check that CSV files are in `data/raw_csv/`
2. Run conversion script: `python scripts/convert_csv_to_parquet.py`
3. Verify parquet files exist in `data/parquet/`

### "No CSV files found"
- Make sure your CSV files are in `data/raw_csv/`, not in `data/` root
- Check file names match expected names (see Required Data Files above)

### Import errors
- Make sure you've added the scripts directory to your Python path
- Install required packages: `pip install -r requirements.txt`
