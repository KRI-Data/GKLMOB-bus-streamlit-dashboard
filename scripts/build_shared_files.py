"""One-off: merge every Analysis CSV in dataset/ into the 3 shared files.

Run once from the repo root:  python -m scripts.build_shared_files
"""
from pathlib import Path
import pandas as pd
from config import RAPID_KL, MRT_FEEDER
from scripts.shared_format import KEYS, SOURCES, to_shared

DATASET = Path(__file__).resolve().parent.parent / "dataset"

# Apr–Nov 2025, from before the one-file-per-month format
LEGACY = {
    "monthly_bpi": {RAPID_KL: ["BPI_Rapid_KL_relative.csv", "BPI_Rapid_KL_new.csv"],
                    MRT_FEEDER: ["BPI_MRT_Feeder_relative.csv", "BPI_MRT_Feeder_new.csv"]},
    "daily_bpi": {RAPID_KL: ["Daily_BPI_Rapid_KL_relative.csv", "Daily_BPI_Rapid_KL_relative_new.csv"],
                  MRT_FEEDER: ["Daily_BPI_MRT_Feeder_relative.csv", "Daily_BPI_MRT_Feeder_relative_new.csv"]},
    "stop_otp": {RAPID_KL: ["Stop_OTP_Rapid_KL_relative.csv", "Stop_OTP_Rapid_KL_new.csv"],
                 MRT_FEEDER: ["Stop_OTP_MRT_Feeder_relative.csv", "Stop_OTP_MRT_Feeder_new.csv"]},
}

for name, networks in SOURCES.items():
    parts = []
    for network, prefix in networks.items():
        files = [DATASET / f for f in LEGACY[name][network]] + sorted(DATASET.glob(f"{prefix}_*.csv"))
        parts += [to_shared(name, network, pd.read_csv(f), f.name) for f in files]
    df = pd.concat(parts, ignore_index=True)

    # Daily_BPI_MRT_Feeder_relative_new.csv repeats Apr–Jun 2025 from _relative.csv: keep one copy
    dupes = df.duplicated(subset=KEYS[name], keep="last")
    df = df[~dupes].sort_values(["month", *KEYS[name]])

    df.to_csv(DATASET / f"{name}.csv", index=False, lineterminator="\n")
    print(f"{name}.csv: {len(df):,} rows, {df['month'].min()} to {df['month'].max()}, {int(dupes.sum()):,} duplicates dropped")
