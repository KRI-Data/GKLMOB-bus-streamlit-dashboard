import streamlit as st
from config import RAPID_KL, MRT_FEEDER
from dataset.common import read_shared, add_ratios, only


@st.cache_data
def monthly():
    """One row per network, route and month."""
    df = add_ratios(read_shared("monthly_bpi"))
    df["rMAE"] = df["mae_ratio"].clip(upper=1)
    return df.rename(columns={"otp": "OTP"})


@st.cache_data
def months():
    return sorted(monthly()["month"].unique())


# --- Old function names, kept so the pages work unchanged. Delete in PR 2. ---
RATIO_COLS = ["month", "n", "n_on_time", "n_early", "n_late", "ratio_on_time", "ratio_early", "ratio_late"]


@st.cache_data
def ratio_rapid_kl():
    return only(monthly(), RAPID_KL)[["route_short_name", "route_long_name", *RATIO_COLS]]


@st.cache_data
def ratio_mrt_feeder():
    return only(monthly(), MRT_FEEDER)[["route_id", *RATIO_COLS]]


@st.cache_data
def bpi_rapid_kl():
    return only(monthly(), RAPID_KL)[["route_short_name", "route_long_name", "rMAE", "OTP", "month", "BPI"]]


@st.cache_data
def bpi_mrt_feeder():
    return only(monthly(), MRT_FEEDER)[["route_id", "rMAE", "OTP", "month", "BPI"]]


def unique_months():
    return months()
