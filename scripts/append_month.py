"""Add one month of Analysis output to the 3 shared data files.

Usage, from the repo root:
    python -m scripts.append_month 202610 path/to/analysis/output

The folder must hold that month's 6 files, e.g. Rapid_kl_monthly_bpi_202610.csv.
Nothing is written unless all 6 files pass every check.
"""
import sys
from pathlib import Path
import pandas as pd
from scripts.shared_format import KEYS, SOURCES, to_shared

DATASET = Path(__file__).resolve().parent.parent / "dataset"


def main(yyyymm, folder):
    if len(yyyymm) != 6 or not yyyymm.isdigit():
        sys.exit(f"Month must look like 202610, got {yyyymm!r}")
    month = f"{yyyymm[:4]}-{yyyymm[4:]}"

    new_rows = {}
    for name, networks in SOURCES.items():
        existing = pd.read_csv(DATASET / f"{name}.csv", usecols=["month"])
        if month in set(existing["month"]):
            sys.exit(f"{name}.csv already has {month}. Nothing written.")

        parts = []
        for network, prefix in networks.items():
            path = Path(folder) / f"{prefix}_{yyyymm}.csv"
            if not path.exists():
                sys.exit(f"Missing {path}. Nothing written.")
            df = to_shared(name, network, pd.read_csv(path), path.name)
            other_months = set(df["month"]) - {month}
            if other_months:
                sys.exit(f"{path.name} also has rows for {sorted(other_months)}. Nothing written.")
            parts.append(df)

        df = pd.concat(parts, ignore_index=True)
        dupes = int(df.duplicated(subset=KEYS[name]).sum())
        if dupes:
            sys.exit(f"{name}: {dupes} duplicate rows in the new files. Nothing written.")
        new_rows[name] = df.sort_values(KEYS[name])

    # Every check passed: add the rows to the end of each file
    for name, df in new_rows.items():
        df.to_csv(DATASET / f"{name}.csv", mode="a", header=False, index=False, lineterminator="\n")
        print(f"{name}.csv: added {len(df):,} rows for {month}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
