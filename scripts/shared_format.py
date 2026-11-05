"""How the Analysis output files map onto the dashboard's 3 shared data files.

This is the only code that knows the Analysis file names and column names.
"""
from config import RAPID_KL, MRT_FEEDER

# Analysis file-name prefix for each shared file and network, e.g. Rapid_kl_monthly_bpi_202609.csv
SOURCES = {
    "monthly_bpi": {RAPID_KL: "Rapid_kl_monthly_bpi", MRT_FEEDER: "MRT_monthly_bpi"},
    "daily_bpi": {RAPID_KL: "Rapid_kl_daily_bpi", MRT_FEEDER: "MRT_daily_bpi"},
    "stop_otp": {RAPID_KL: "Rapid_kl_bus_stop_otp", MRT_FEEDER: "MRT_bus_stop_otp"},
}

# Columns of each shared file, in order
COLUMNS = {
    "monthly_bpi": ["network", "route_id", "route", "route_short_name", "route_long_name", "month",
                    "n", "n_on_time", "n_early", "n_late", "otp", "mae_ratio", "BPI"],
    "daily_bpi": ["network", "route_id", "route", "date", "month", "BPI"],
    "stop_otp": ["network", "route_id", "route", "stop_name", "month", "n_on_time", "n_early", "n_late"],
}

# Columns that identify one row; no two rows may share them
KEYS = {
    "monthly_bpi": ["network", "route_id", "month"],
    "daily_bpi": ["network", "route_id", "date"],
    "stop_otp": ["network", "route_id", "stop_name", "month"],
}

# Analysis column names that differ from the shared names
RENAME = {"I_hat": "BPI", "on time": "n_on_time", "early": "n_early", "late": "n_late"}
RAPID_NAMES = {"route_short_name", "route_long_name"}


def to_shared(name, network, df, source):
    """Convert one Analysis file (any number of months) to the shared format of `name`."""
    df = df.rename(columns=RENAME)

    needed = set(COLUMNS[name]) - {"network", "route"} - RAPID_NAMES
    if network == RAPID_KL:
        needed |= RAPID_NAMES  # used to build the route label
    missing = sorted(needed - set(df.columns))
    if missing:
        raise ValueError(f"{source} is missing columns {missing}")

    df["network"] = network
    if network == RAPID_KL:
        df["route"] = df["route_short_name"] + " (" + df["route_long_name"] + ")"
    else:
        df["route"] = df["route_id"]
    return df.reindex(columns=COLUMNS[name])  # MRT files have no route names: left blank
