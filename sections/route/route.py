import sys
import streamlit as st
import plotly.express as px
import pandas as pd
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from graphs.Ternary_plots import month_slider
from graphs.Stop_plots import route_selector, get_stop, get_time_series
from dataset.BPI_dt import unique_months
from dataset.Stop_dt import list_route, stop_mrt_feeder, stop_rapid_kl
from dataset.Daily_bpi import daily_mrt_feeder, daily_rapid_kl

def render_route():
    # --- Month selection container ---
    with st.container(border=True):
        selected_month_raw, selected_month_dt = month_slider(
            unique_months(),
            label="Select Month:",
            key="month_slider_otp_1",
        )

    # --- Route selection container ---
    with st.container(border=False):
        

        with st.container(border=True):
            selected_routes = route_selector(label="Select Route(s):")

            if not selected_routes:
                st.info("No routes selected yet.")
        
    df = stop_rapid_kl()
    df1 = stop_mrt_feeder()
    combined_df = pd.DataFrame() 

    if "month" in df1.columns and "month" in df.columns:
        df_filtered = df[df["month"] == selected_month_raw]
        df1_filtered = df1[df1["month"] == selected_month_raw]

        if selected_routes:
            df_filtered =  df_filtered[df_filtered["route_id"].isin(selected_routes)]
            df1_filtered =  df1_filtered[df1_filtered["route_id"].isin(selected_routes)]

            combined_df = pd.concat([df_filtered, df1_filtered], ignore_index=True)

    with st.container(border=True):

        if not combined_df.empty and "route_id" in combined_df.columns:
            st.markdown("""<h3 style="font-weight: 600; font-family: 'Crimson Pro', serif; font-size: 2.25rem; line-height: 1.15; text-align: center">Bus Stop On-Time Performance Breakdown</h3>""", unsafe_allow_html=True)
            st.plotly_chart(get_stop(combined_df), use_container_width=True, key="stop_ternary")
            st.caption("Note: Click a route in the legend once to toggle it on or off. Double-click a route to isolate it or show all routes")

            if selected_routes:

                for i in range(0, len(selected_routes), 2):

                    # Get the current pair of routes
                    pair = selected_routes[i:i+2]

                    # Create two columns
                    col1, col2 = st.columns(2)

                    # First route in col1
                    route = pair[0]

                    with col1:
                        st.markdown(f"""
                            <h3 style="
                            font-family: 'Crimson Pro', serif;
                            font-weight: 500;
                            font-size: 1.25rem;
                            line-height: 1.6;
                            color: white;
                            margin-top: 0;
                            ">
                                Route {route}
                            </h3>
                            """,
                            unsafe_allow_html=True
                        )

                        route_df = combined_df[combined_df["route_id"] == route]

                        route_df_display = route_df[['stop_name', 'ratio_on_time', 'ratio_early', 'ratio_late']].rename(
                            columns={'stop_name': 'Stop Name', 'ratio_on_time': 'On-Time', 'ratio_early': 'Early', 'ratio_late':'Late'}
                        )

                        route_df_display = route_df_display.sort_values(by='On-Time', ascending=True)
                        route_df_display.reset_index(drop=True, inplace=True)
                        route_df_display.index = range(1, 1 + len(route_df_display))

                        # Conditional coloring
                        styled_df = route_df_display.style.map(
                            lambda val: 'color: green; font-weight: bold' if val > 0.7 else 'color: red; font-weight: bold',
                            subset=['On-Time']
                        )

                        st.dataframe(styled_df, use_container_width=True)

                    # Second route in col2 (if exists)
                    if len(pair) > 1:

                        route = pair[1]

                        with col2:

                            st.markdown(f"""
                            <h3 style="
                            font-family: 'Crimson Pro', serif;
                            font-weight: 500;
                            font-size: 1.25rem;
                            line-height: 1.6;
                            color: white;
                            margin-top: 0;
                            ">
                                Route {route}
                            </h3>
                            """,
                            unsafe_allow_html=True
                        )
                            route_df = combined_df[combined_df["route_id"] == route]

                            route_df_display = route_df[['stop_name', 'ratio_on_time', 'ratio_early', 'ratio_late']].rename(
                                columns={'stop_name': 'Stop Name', 'ratio_on_time': 'On-Time', 'ratio_early': 'Early', 'ratio_late':'Late'}
                            )
                            route_df_display[['On-Time', 'Late', 'Early']] = route_df_display[['On-Time', 'Late', 'Early']].round(4)
                            route_df_display = route_df_display.sort_values(by='On-Time', ascending=True)
                            route_df_display.reset_index(drop=True, inplace=True)
                            route_df_display.index = range(1, 1 + len(route_df_display))

                            styled_df = route_df_display.style.map(
                                lambda val: 'color: green; font-weight: bold' if val > 0.7 else 'color: red; font-weight: bold',
                                subset=['On-Time']
                            )
                            st.dataframe(styled_df, use_container_width=True)
    
    with st.container(border=True):
        
        daily = daily_rapid_kl()
        daily1 = daily_mrt_feeder()

        daily_combined = pd.DataFrame() 

        if "month" in daily.columns and "month" in daily1.columns:
            daily_filtered = daily[daily["month"] == selected_month_raw]
            daily1_filtered = daily1[daily1["month"] == selected_month_raw]

            if selected_routes:
                daily_filtered  =  daily_filtered[daily_filtered ["Route"].isin(selected_routes)]
                daily1_filtered =  daily1_filtered[daily1_filtered["Route"].isin(selected_routes)]

                daily_combined = pd.concat([daily_filtered, daily1_filtered], ignore_index=True)

        if not daily_combined.empty and "Route" in daily_combined.columns:

            st.markdown("""<h3 style="font-weight: 600; font-family: 'Crimson Pro', serif; font-size: 2.25rem; line-height: 1.15; text-align: center">BPI Time Series</h3>""", unsafe_allow_html=True)
            st.plotly_chart(get_time_series(daily_combined), use_container_width=True, key="daily_bpi")
            st.caption("Note: The observation period are differ for both MRT and Rapid KL due to ocassional General Transit Feed Specifications (GTFS) interuption.")

            pivot_df = daily_combined.pivot_table(
                index='Date',
                columns='Route',
                values='BPI'
            ).reset_index()

            route_columns = pivot_df.columns.drop('Date')

            styled_pivot_df = pivot_df.style.applymap(
                lambda val: 'color: green; font-weight: bold' if val > 0.7 else 'color: red; font-weight: bold',
                subset=route_columns
                )

            st.dataframe(styled_pivot_df)