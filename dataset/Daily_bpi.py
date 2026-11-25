import streamlit as st
from config import RAPID_KL, MRT_FEEDER
from dataset.common import read_shared, only


@st.cache_data
def daily():
    """One row per network, route and day."""
    return read_shared("daily_bpi")


# --- Old function names, kept so the pages work unchanged. Delete in PR 2. ---
OLD_NAMES = {"route": "Route", "date": "Date"}


@st.cache_data
def daily_rapid_kl():
    return only(daily(), RAPID_KL)[["route", "date", "month", "BPI"]].rename(columns=OLD_NAMES)


@st.cache_data
def daily_mrt_feeder():
    return only(daily(), MRT_FEEDER)[["route", "date", "month", "BPI"]].rename(columns=OLD_NAMES)
