import streamlit as st
from config import RAPID_KL, MRT_FEEDER
from dataset.common import read_shared, add_ratios, only


@st.cache_data
def stops():
    """One row per network, route, stop and month."""
    df = read_shared("stop_otp")
    df["n"] = df["n_on_time"] + df["n_early"] + df["n_late"]
    return add_ratios(df)


@st.cache_data
def routes():
    """Routes running in the latest month, for the route picker."""
    df = stops()
    return sorted(df.loc[df["month"] == df["month"].max(), "route"].unique())


# --- Old function names, kept so the pages work unchanged. Delete in PR 2. ---
OLD_NAMES = {"route": "route_id", "n_on_time": "on time", "n_early": "early", "n_late": "late", "n": "total"}
OLD_COLS = ["route_id", "stop_name", "month", "on time", "early", "late",
            "total", "ratio_on_time", "ratio_early", "ratio_late"]


def _old_format(df):
    return df.drop(columns="route_id").rename(columns=OLD_NAMES)[OLD_COLS]


@st.cache_data
def stop_rapid_kl():
    return _old_format(only(stops(), RAPID_KL))


@st.cache_data
def stop_mrt_feeder():
    return _old_format(only(stops(), MRT_FEEDER))


def list_route():
    return routes()
