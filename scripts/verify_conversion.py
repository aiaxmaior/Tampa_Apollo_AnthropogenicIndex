#!/usr/bin/env python3
"""
Parquet Conversion Verifier
===========================
Checks metadata (row counts, column counts, file sizes) to ensure
data integrity between original CSVs and converted Parquet files.
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

def get_file_size_mb(filepath):
    """Get file size in MB."""
    if not filepath.exists():
        return 0.0
    return os.path.getsize(filepath) / (1024 * 1024)

def read_csv_robust(filepath):
    """
    Attempts to read a CSV with multiple encodings and type safeguards.
    Returns DataFrame or None if failed.
    """
    encodings = ['utf-8', 'latin1', 'cp1252', 'ISO-8859-1']
    
    for encoding in encodings:
        try:
            # Read with low_memory=False to prevent mixed-type warnings/crashes
            # dtype=str forces everything to string to match Parquet sanitization
            df = pd.read_csv(filepath, encoding=encoding, low_memory=False, dtype=str)
            return df
        except UnicodeDecodeError:
            continue
        except Exception:
            continue
    return None

def verify_conversion():
    print(f"{'File':<30} | {'Rows':<10} | {'Cols':<5} | {'CSV MB':<8} | {'Parquet MB':<10} | {'Status':<10}")
    print("-" * 90)

    parquet_files = list(PARQUET_DIR.glob('*.parquet'))
    
    if not parquet_files:
        print("No Parquet files found to verify.")
        return

    for pq_file in sorted(parquet_files):
        csv_file = RAW_CSV_DIR / pq_file.with_suffix('.csv').name
        
        # 1. Check if source CSV exists
        if not csv_file.exists():
            print(f"{pq_file.name:<30} | {'MISSING CSV':<50}")
            continue

        # 2. Read Parquet
        try:
            df_pq = pd.read_parquet(pq_file)
        except Exception as e:
            print(f"{pq_file.name:<30} | {'PARQUET READ ERROR':<50}")
            continue

        # 3. Read CSV (Robustly)
        df_csv = read_csv_robust(csv_file)
        
        if df_csv is None:
            print(f"{csv_file.name:<30} | {'CSV READ ERROR':<50}")
            continue

        # 4. Compare
        rows_match = len(df_csv) == len(df_pq)
        cols_match = len(df_csv.columns) == len(df_pq.columns)
        
        csv_size = get_file_size_mb(csv_file)
        pq_size = get_file_size_mb(pq_file)
        
        status = "✅ PASS" if (rows_match and cols_match) else "❌ FAIL"
        
        # Logic to flag mismatches specifically
        if not rows_match:
            status = f"❌ ROWS ({len(df_csv)} vs {len(df_pq)})"
        elif not cols_match:
            status = f"❌ COLS ({len(df_csv.columns)} vs {len(df_pq.columns)})"

        print(f"{pq_file.name:<30} | {len(df_pq):<10,} | {len(df_pq.columns):<5} | {csv_size:<8.2f} | {pq_size:<10.2f} | {status}")

if __name__ == "__main__":
    print("Verifying Parquet Integrity...")
    print(f"Source: {RAW_CSV_DIR}")
    print(f"Target: {PARQUET_DIR}\n")
    verify_conversion()