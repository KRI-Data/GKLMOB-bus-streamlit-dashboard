import base64
import pandas as pd
from pathlib import Path
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
import sys

# Import custom components
from sections.header.Header import render_header
from sections.network.network import render_network
from sections.route.route import render_route
from sections.about.about import render_about

# Import datasets
from dataset.BPI_dt import (
    ratio_rapid_kl, unique_months, ratio_mrt_feeder,
    bpi_mrt_feeder, bpi_rapid_kl
)
from dataset.Stop_dt import (
    list_route, stop_mrt_feeder, stop_rapid_kl
)
from dataset.Daily_bpi import (
    daily_mrt_feeder, daily_rapid_kl
)

# Import graphs
from graphs.Ternary_plots import (
    month_slider, get_ternary_rapid_kl, get_ternary_mrt_feeder
)
from graphs.Violin_plots import get_violin
from graphs.Stop_plots import (
    route_selector, get_stop, get_time_series
)

# Streamlit page setup 
st.set_page_config(
    page_title="Bus Dashboard",
    layout="wide",
    page_icon="pictures/KRI_Mini Logo2 Light.png"
)

# Initialize session state 
if "active_page" not in st.session_state:
    st.session_state.active_page = "Network"

# Render header 
selected = render_header()

# Update active page 
st.session_state.active_page = selected

# Cache heavy dataset
@st.cache_resource
def load_data():
    return {
        "bpi_rapid_kl": bpi_rapid_kl,
        "bpi_mrt_feeder": bpi_mrt_feeder,
        "daily_rapid_kl": daily_rapid_kl,
        "daily_mrt_feeder": daily_mrt_feeder
    }

data = load_data()

# page rendering
try:
    if st.session_state.active_page == "Network":
        render_network()
    elif st.session_state.active_page == "Routes":
        render_route()
    elif st.session_state.active_page == "About":
        render_about()
    else:
        st.warning("⚠️ Unknown page selected. Please choose from the menu.")
except Exception as e:
    st.error(f"⚠️ Error rendering page: {e}")
