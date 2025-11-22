"""
Data Loader Module
==================
Centralized data loading utilities for the Tampa Bay Anthropogenic Index project.

This module provides convenient functions to load all project datasets from
Parquet files, with automatic path resolution and error handling.

Usage in notebooks:
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path.cwd().parent / 'scripts'))
    from data_loader import load_marine_data, load_anthropogenic_data

    # Load data
    benthic_df = load_marine_data('benthic')
    nekton_df = load_marine_data('nekton')
    construction_df = load_anthropogenic_data('construction')
"""

import pandas as pd
from pathlib import Path
import warnings


class DataPaths:
    """Centralized path management for project data."""

    def __init__(self):
        # Get project root (assumes this script is in scripts/)
        self.project_root = Path(__file__).parent.parent
        self.data_dir = self.project_root / 'data'
        self.parquet_dir = self.data_dir / 'parquet'
        self.processed_dir = self.data_dir / 'processed'

        # Data file mappings
        self.files = {
            # Marine Ecosystem Data
            'benthic': 'bBioAdj_1.parquet',
            'nekton': 'Nekton.parquet',

            # Anthropogenic Data
            'construction': 'construction.parquet',
            'development_pct_change': 'percentchange_dev.parquet',
            'population': 'population_data.parquet',
            'demographics': 'dfdemographics.parquet',

            # Water Quality / Nitrogen Data
            'kjeldahl': 'kjeldahl.parquet',
            'nitrate': 'nitrate.parquet',
            'ammonia': 'ammonia.parquet',
            'nitrates_var': 'Nitrates_VAR_organics.parquet',
            'nitrogen_final': 'NIT_FINAL.parquet',
        }

    def get_path(self, dataset_key):
        """Get the full path for a dataset."""
        if dataset_key not in self.files:
            raise ValueError(
                f"Unknown dataset: '{dataset_key}'. "
                f"Available datasets: {list(self.files.keys())}"
            )
        return self.parquet_dir / self.files[dataset_key]


# Global instance
_paths = DataPaths()


def load_data(dataset_key, verbose=True):
    """
    Load a dataset by its key name.

    Args:
        dataset_key: Key name of the dataset (e.g., 'benthic', 'nekton', 'construction')
        verbose: Print loading information

    Returns:
        pd.DataFrame: Loaded dataset

    Raises:
        FileNotFoundError: If the parquet file doesn't exist
        ValueError: If dataset_key is not recognized

    Examples:
        >>> df = load_data('benthic')
        >>> df = load_data('construction', verbose=False)
    """
    filepath = _paths.get_path(dataset_key)

    if not filepath.exists():
        raise FileNotFoundError(
            f"Data file not found: {filepath}\n"
            f"Have you converted your CSV files to Parquet?\n"
            f"Run: python scripts/convert_csv_to_parquet.py"
        )

    if verbose:
        print(f"Loading {dataset_key} data from {filepath.name}...", end=" ")

    df = pd.read_parquet(filepath, engine='pyarrow')

    if verbose:
        print(f"✓ ({len(df):,} rows, {len(df.columns)} columns)")

    return df


# Convenience functions for specific datasets
def load_marine_data(dataset='benthic', verbose=True):
    """
    Load marine ecosystem data.

    Args:
        dataset: 'benthic' or 'nekton'
        verbose: Print loading information

    Returns:
        pd.DataFrame: Marine ecosystem data with indices
    """
    if dataset not in ['benthic', 'nekton']:
        raise ValueError(f"dataset must be 'benthic' or 'nekton', got: {dataset}")

    return load_data(dataset, verbose=verbose)


def load_anthropogenic_data(dataset='construction', verbose=True):
    """
    Load anthropogenic pressure data.

    Args:
        dataset: One of 'construction', 'development_pct_change', 'population', 'demographics'
        verbose: Print loading information

    Returns:
        pd.DataFrame: Anthropogenic data
    """
    valid_datasets = ['construction', 'development_pct_change', 'population', 'demographics']
    if dataset not in valid_datasets:
        raise ValueError(f"dataset must be one of {valid_datasets}, got: {dataset}")

    return load_data(dataset, verbose=verbose)


def load_nitrogen_data(dataset='nitrogen_final', verbose=True):
    """
    Load nitrogen/water quality data.

    Args:
        dataset: One of 'kjeldahl', 'nitrate', 'ammonia', 'nitrates_var', 'nitrogen_final'
        verbose: Print loading information

    Returns:
        pd.DataFrame: Nitrogen data
    """
    valid_datasets = ['kjeldahl', 'nitrate', 'ammonia', 'nitrates_var', 'nitrogen_final']
    if dataset not in valid_datasets:
        raise ValueError(f"dataset must be one of {valid_datasets}, got: {dataset}")

    return load_data(dataset, verbose=verbose)


def load_all_data(verbose=True):
    """
    Load all available datasets into a dictionary.

    Args:
        verbose: Print loading information

    Returns:
        dict: Dictionary with dataset keys and DataFrames
    """
    data = {}
    failed = []

    if verbose:
        print("Loading all datasets...")
        print("=" * 50)

    for key in _paths.files.keys():
        try:
            data[key] = load_data(key, verbose=verbose)
        except FileNotFoundError as e:
            if verbose:
                print(f"✗ {key}: File not found")
            failed.append(key)

    if verbose:
        print("=" * 50)
        print(f"Successfully loaded: {len(data)}/{len(_paths.files)} datasets")
        if failed:
            print(f"Missing datasets: {failed}")

    return data


def get_data_info():
    """
    Print information about available datasets and their status.
    """
    print("Tampa Bay Anthropogenic Index - Data Inventory")
    print("=" * 70)

    categories = {
        'Marine Ecosystem': ['benthic', 'nekton'],
        'Anthropogenic Pressure': ['construction', 'development_pct_change', 'population', 'demographics'],
        'Water Quality / Nitrogen': ['kjeldahl', 'nitrate', 'ammonia', 'nitrates_var', 'nitrogen_final']
    }

    for category, datasets in categories.items():
        print(f"\n{category}:")
        print("-" * 70)
        for dataset in datasets:
            filepath = _paths.get_path(dataset)
            status = "✓" if filepath.exists() else "✗"
            size_info = ""

            if filepath.exists():
                size_mb = filepath.stat().st_size / (1024 * 1024)
                try:
                    df = pd.read_parquet(filepath)
                    size_info = f"({len(df):,} rows, {len(df.columns)} cols, {size_mb:.2f} MB)"
                except:
                    size_info = f"({size_mb:.2f} MB)"

            print(f"  {status} {dataset:25} {filepath.name:30} {size_info}")

    print("\n" + "=" * 70)


# Example usage
if __name__ == '__main__':
    # Show data inventory
    get_data_info()

    # Try to load a dataset (example)
    try:
        print("\nExample: Loading benthic data...")
        df = load_data('benthic')
        print(f"Columns: {list(df.columns[:5])}...")
        print(df.head())
    except FileNotFoundError as e:
        print(f"Error: {e}")
