import sys
from pathlib import Path
import base64
import streamlit as st
from streamlit_option_menu import option_menu

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parents[2]))

st.markdown("""
<style>

    /* --- Base (mobile-first) --- */
    .nav-link {
        font-size: 10px !important;
    }
    .nav-link > i {
        font-size: 9px !important;
    }

    /* --- Large screens (desktops) --- */
    @media (min-width: 1200px) {
        .nav-link {
            font-size: 18px !important;
        }
        .nav-link > i {
            font-size: 14px !important;
        }
    }

</style>
""", unsafe_allow_html=True)


from dataset.BPI_dt import (
    ratio_rapid_kl,
    unique_months,
    ratio_mrt_feeder,
    bpi_mrt_feeder,
    bpi_rapid_kl,
)
from graphs.Ternary_plots import month_slider, get_ternary_rapid_kl, get_ternary_mrt_feeder
from graphs.Violin_plots import get_violin
from sections.network.network import render_network

# Header function 
def render_header():
    # Load logo as base64
    logo_path = Path("pictures/KRI_Main Logo Light.png")
    with open(logo_path, "rb") as f:
        img_base64 = base64.b64encode(f.read()).decode()

    # Header container with logo + menu
    with st.container():
        col1, col2 = st.columns([1, 5])

        # Logo
        with col1:
            st.markdown(
                f"""
                <div style="text-align: left;">
                    <a href="https://www.krinstitute.org/">
                        <img src="data:image/png;base64,{img_base64}" width="100" >
                    </a>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Horizontal navigation menu
        with col2:

            st.markdown(
                """
                <style>
                    div[data-testid="stContainer"] {
                        background-color: transparent !important;
                    }
                </style>
                """,
                unsafe_allow_html=True
                )
            
            with st.container(border=True):
                selected = option_menu(
                    menu_title=None,
                    options=["Network", "Routes", "About"],
                    icons=["house", "map", "info-circle"],
                    menu_icon="cast",
                    default_index=0,
                    orientation="horizontal",
                    styles={
                        "container": {"padding": "0 0", "background-color": "transparent"},
                        "icon": {"color": "white"},
                        "options": {},
                        "nav-link": {
                            "text-align": "center",
                            "margin": "0px 0px",
                            "color": "rgba(255,255,255,0.7)",
                            "background-color": "transparent",
                        },
                        "nav-link-selected": {
                            "color": "white",
                            "background-color": "#615fff",
                        },
                        "nav-link:hover": {
                            "color": "white",
                            "background-color": "transparent",
                        },

                    }
                )

        # Spacing below header
        st.markdown("<br>", unsafe_allow_html=True)

    return selected
