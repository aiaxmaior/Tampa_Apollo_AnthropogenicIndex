#!/usr/bin/env python3
"""
CSV to Parquet Converter
========================
Converts all CSV data files to Parquet format for efficient storage and faster loading.

Usage:
    python scripts/convert_csv_to_parquet.py

This script will:
1. Look for CSV files in data/raw_csv/
2. Convert them to Parquet format
3. Save to data/parquet/
4. Display compression statistics
"""

import pandas as pd
from pathlib import Path
import sys
import os

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Define data directories
RAW_CSV_DIR = project_root / 'data' / 'raw_csv'
PARQUET_DIR = project_root / 'data' / 'parquet'

# Expected data files based on notebook analysis
EXPECTED_FILES = {
    # Marine Ecosystem Data
    'bBioAdj_1.csv': 'Benthic biodiversity with TBBI scores',
    'Nekton.csv': 'Nekton/pelagic data with TBNI scores',

    # Anthropogenic Data
    'construction.csv': 'Property development and construction records',
    'percentchange_dev.csv': 'Development rate changes',
    'population_data.csv': 'Population growth data',
    'dfdemographics.csv': 'Demographic data',

    # Water Quality / Nitrogen Data
    'kjeldahl.csv': 'Organic nitrogen (Kjeldahl method)',
    'nitrate.csv': 'Nitrate concentrations',
    'ammonia.csv': 'Ammonia concentrations',
    'Nitrates_VAR_organics.csv': 'VAR analysis data',
    'NIT_FINAL.csv': 'Processed nitrogen data',
}


def get_file_size_mb(filepath):
    """Get file size in MB."""
    return os.path.getsize(filepath) / (1024 * 1024)


def convert_csv_to_parquet(csv_path, parquet_path, description=""):
    """
    Convert a single CSV file to Parquet format.

    Args:
        csv_path: Path to input CSV file
        parquet_path: Path to output Parquet file
        description: Description of the data file

    Returns:
        dict: Conversion statistics
    """
    try:
        print(f"\n{'='*70}")
        print(f"Converting: {csv_path.name}")
        if description:
            print(f"Description: {description}")

        # Read CSV
        print(f"  Reading CSV...", end=" ")
        df = pd.read_csv(csv_path)
        csv_size = get_file_size_mb(csv_path)
        print(f"✓ ({len(df):,} rows, {len(df.columns)} columns)")

        # Display data info
        print(f"  CSV size: {csv_size:.2f} MB")
        print(f"  Memory usage: {df.memory_usage(deep=True).sum() / (1024**2):.2f} MB")

        # Convert to Parquet
        print(f"  Writing Parquet...", end=" ")
        df.to_parquet(
            parquet_path,
            engine='pyarrow',
            compression='snappy',  # Good balance of speed and compression
            index=False
        )
        parquet_size = get_file_size_mb(parquet_path)
        print(f"✓")

        # Calculate compression ratio
        compression_ratio = (1 - parquet_size / csv_size) * 100
        size_reduction = csv_size - parquet_size

        print(f"  Parquet size: {parquet_size:.2f} MB")
        print(f"  Compression: {compression_ratio:.1f}% smaller ({size_reduction:.2f} MB saved)")

        return {
            'file': csv_path.name,
            'rows': len(df),
            'columns': len(df.columns),
            'csv_size_mb': csv_size,
            'parquet_size_mb': parquet_size,
            'compression_pct': compression_ratio,
            'success': True
        }

    except FileNotFoundError:
        print(f"  ✗ File not found: {csv_path}")
        return {'file': csv_path.name, 'success': False, 'error': 'File not found'}

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return {'file': csv_path.name, 'success': False, 'error': str(e)}


def convert_all_csvs():
    """Convert all CSV files in raw_csv directory to Parquet format."""

    print("="*70)
    print("CSV to Parquet Converter")
    print("="*70)
    print(f"\nSource directory: {RAW_CSV_DIR}")
    print(f"Target directory: {PARQUET_DIR}")

    # Create parquet directory if it doesn't exist
    PARQUET_DIR.mkdir(parents=True, exist_ok=True)

    # Check if raw_csv directory exists
    if not RAW_CSV_DIR.exists():
        print(f"\n✗ Error: Directory not found: {RAW_CSV_DIR}")
        print("\nPlease create the directory and place your CSV files there:")
        print(f"  mkdir -p {RAW_CSV_DIR}")
        return

    # Find all CSV files
    csv_files = list(RAW_CSV_DIR.glob('*.csv'))

    if not csv_files:
        print(f"\n✗ No CSV files found in {RAW_CSV_DIR}")
        print("\nExpected files:")
        for filename, desc in EXPECTED_FILES.items():
            print(f"  - {filename}: {desc}")
        print(f"\nPlease place your CSV files in: {RAW_CSV_DIR}")
        return

    print(f"\nFound {len(csv_files)} CSV file(s)")

    # Convert each file
    results = []
    for csv_file in sorted(csv_files):
        parquet_file = PARQUET_DIR / csv_file.with_suffix('.parquet').name
        description = EXPECTED_FILES.get(csv_file.name, "")
        result = convert_csv_to_parquet(csv_file, parquet_file, description)
        results.append(result)

    # Print summary
    print("\n" + "="*70)
    print("CONVERSION SUMMARY")
    print("="*70)

    successful = [r for r in results if r.get('success')]
    failed = [r for r in results if not r.get('success')]

    if successful:
        total_csv_size = sum(r['csv_size_mb'] for r in successful)
        total_parquet_size = sum(r['parquet_size_mb'] for r in successful)
        total_savings = total_csv_size - total_parquet_size
        overall_compression = (1 - total_parquet_size / total_csv_size) * 100

        print(f"\n✓ Successfully converted {len(successful)} file(s)")
        print(f"\nTotal CSV size:     {total_csv_size:.2f} MB")
        print(f"Total Parquet size: {total_parquet_size:.2f} MB")
        print(f"Total savings:      {total_savings:.2f} MB ({overall_compression:.1f}%)")

        print("\nConverted files:")
        for r in successful:
            print(f"  ✓ {r['file']}: {r['rows']:,} rows, {r['columns']} cols, "
                  f"{r['compression_pct']:.1f}% smaller")

    if failed:
        print(f"\n✗ Failed to convert {len(failed)} file(s):")
        for r in failed:
            print(f"  ✗ {r['file']}: {r.get('error', 'Unknown error')}")

    # Check for missing expected files
    converted_names = {r['file'] for r in results}
    missing_files = set(EXPECTED_FILES.keys()) - converted_names

    if missing_files:
        print(f"\n⚠ Missing expected files ({len(missing_files)}):")
        for filename in sorted(missing_files):
            print(f"  - {filename}: {EXPECTED_FILES[filename]}")
        print(f"\nPlace these files in: {RAW_CSV_DIR}")

    print("\n" + "="*70)
    print("Next steps:")
    print("  1. Review the converted files in data/parquet/")
    print("  2. Git add and commit the parquet files")
    print("  3. Use the data_loader.py module in your notebooks")
    print("="*70)


if __name__ == '__main__':
    convert_all_csvs()
