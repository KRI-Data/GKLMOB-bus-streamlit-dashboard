from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent


def read_shared(name):
    """Read one shared data file: monthly_bpi, daily_bpi or stop_otp."""
    return pd.read_csv(DATA_DIR / f"{name}.csv")


def add_ratios(df):
    """Share of on-time / early / late trips in each row, rounded to 4 dp."""
    for ratio, count in [("ratio_on_time", "n_on_time"), ("ratio_early", "n_early"), ("ratio_late", "n_late")]:
        df[ratio] = (df[count] / df["n"]).round(4)
    return df


def only(df, network):
    """Rows for one network."""
    return df[df["network"] == network].reset_index(drop=True)
