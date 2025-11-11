import sys
import streamlit as st
import plotly.express as px
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from dataset.BPI_dt import ratio_rapid_kl, unique_months, ratio_mrt_feeder, bpi_mrt_feeder, bpi_rapid_kl
from graphs.Ternary_plots import month_slider, get_ternary_rapid_kl, get_ternary_mrt_feeder
from graphs.Violin_plots import get_violin

def render_network():

    with st.container(border=True):

         selected_month_raw, selected_month_dt = month_slider(
            unique_months(), 
            label="Select Month:",
            key="month_slider_otp_1"
        )

    # --- Big container for entire OTP section ---
    with st.container(border=True):
        st.markdown("""
        <h3 style="font-weight: 600; font-family: 'Crimson Pro', serif; font-size: 2.25rem; line-height: 1.15; text-align: center"> On-Time Performance (OTP) </h3>
        """, unsafe_allow_html=True)
        st.caption("Note: A bus is considered on-time if it arrived not earlier than 1 minute and not later than 5 minutes.")

        # --- Load and filter data ---
        df = ratio_rapid_kl()
        df1 = ratio_mrt_feeder()
        bpi = bpi_rapid_kl()
        bpi1 = bpi_mrt_feeder()
        if "month" in df.columns and "month" in df1.columns:
            df_filtered = df[df["month"] == selected_month_raw]
            df1_filtered = df1[df1["month"] == selected_month_raw]
            bpi_filtered =bpi[bpi["month"] == selected_month_raw]
            bpi1_filtered = bpi1[bpi1["month"] == selected_month_raw]

        # --- Compute network-wide OTP ---
        total_early_rapid_kl = df_filtered["n_early"].sum()
        total_on_time_rapid_kl = df_filtered["n_on_time"].sum()
        total_late_rapid_kl = df_filtered["n_late"].sum()
        total_all_rapid_kl = total_early_rapid_kl + total_on_time_rapid_kl + total_late_rapid_kl
        otp_rapid_kl = total_on_time_rapid_kl / total_all_rapid_kl

        total_early_mrt_feeder = df1_filtered["n_early"].sum()
        total_on_time_mrt_feeder = df1_filtered["n_on_time"].sum()
        total_late_mrt_feeder = df1_filtered["n_late"].sum()
        total_all_mrt_feeder = total_early_mrt_feeder + total_on_time_mrt_feeder + total_late_mrt_feeder
        otp_mrt_feeder = total_on_time_mrt_feeder / total_all_mrt_feeder
        
        avg_data = [f"{otp_rapid_kl:.2%}", f"{otp_mrt_feeder:.2%}"]

        # --- Graph cards ---
        col1, col2 = st.columns(2)

        with col1:
            with st.container(border=True):
                st.markdown("""<h3 style="font-weight: 600; font-family: 'Crimson Pro', serif; font-size: 1.5rem; line-height: 1.3; text-align: center;">Rapid KL Bus</h3>""", unsafe_allow_html=True)
                st.plotly_chart(get_ternary_rapid_kl(df_filtered), use_container_width=True, key="rapid_kl_ternary")

        with col2:
            with st.container(border=True):
                st.markdown("""<h3 style="font-weight: 600; font-family: 'Crimson Pro', serif; font-size: 1.5rem; line-height: 1.3; text-align: center;">MRT Feeder</h3>""", unsafe_allow_html=True)
                st.plotly_chart(get_ternary_mrt_feeder(df1_filtered), use_container_width=True, key="mrt_feeder_ternary")

    with st.container(border=True):

        # --- Average OTP cards ---
        st.markdown("""
        <h3 style="font-weight: 600; font-family: 'Crimson Pro', serif; font-size: 2.25rem; line-height: 1.15; text-align: center">Average OTP Performance</h3>""", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)

        with col1:
            with st.container(border=True):
                st.markdown("""<h3 style="font-weight: 600; font-family: 'Crimson Pro', serif; font-size: 1.5rem; line-height: 1.3; text-align: center;">Rapid KL Bus</h3>""", unsafe_allow_html=True)
                value_num1 = float(avg_data[0].strip('%'))
                color1 = "red" if value_num1 <= 70 else "green"
                
                # Nested container specifically for the numeric value
                with st.container(border=True):
                    st.markdown(
                        f"""<div style="
                            font-size: 32px;
                            font-weight: bold;
                            text-align: center;
                            color: {color1};
                            margin: 10px;
                        ">
                            {avg_data[0]}
                        </div>""",
                        unsafe_allow_html=True
                    )

        with col2:
            with st.container(border=True):
                st.markdown("""<h3 style="font-weight: 600; font-family: 'Crimson Pro', serif; font-size: 1.5rem; line-height: 1.3; text-align: center;">MRT Feeder</h3>""", unsafe_allow_html=True)
                value_num2 = float(avg_data[1].strip('%')) if '%' in avg_data[1] else 100
                color2 = "red" if value_num2 <= 70 else "green"
                # Nested container specifically for the numeric value

                with st.container(border=True):
                    st.markdown(
                        f"""<div style="
                            font-size: 32px;
                            font-weight: bold;
                            text-align: center;
                            color: {color2};
                            margin: 10px;
                        ">
                            {avg_data[1]}
                        </div>""",
                        unsafe_allow_html=True
                    )

    with st.container(border=True):

        st.markdown("""
        <h3 style="font-weight: 600; font-family: 'Crimson Pro', serif; font-size: 2.25rem; line-height: 1.15; text-align: center">Bus Performance Index (BPI)</h3>""", unsafe_allow_html=True)
        st.caption("Note: BPI measured both on-time arrivals and the severity of deviation from schedule when a bus is not punctual.")
        
        with st.container(border=True):

            st.plotly_chart(get_violin(bpi_filtered, bpi1_filtered), use_container_width=True, key="violin plot")

       
    
    with st.container(border=True):

        st.markdown("""
        <h3 style="font-weight: 600; font-family: 'Crimson Pro', serif; font-size: 2.25rem; line-height: 1.15; text-align: center">Best Performing Routes</h3>""", unsafe_allow_html=True)
        st.caption("Note: BPI close to 1 implies that most of the bus arrive on-time and the deviation from schedule is minimum if it's not on-time.")
        
        col1, col2 = st.columns(2)

        with col1:

            with st.container(border=True):

                st.markdown("""<h3 style="font-weight: 600; font-family: 'Crimson Pro', serif; font-size: 1.5rem; line-height: 1.3; text-align: center;">Rapid KL Bus</h3>""", unsafe_allow_html=True)

                # Combine short and long names
                bpi_filtered_display = bpi_filtered.copy()
                bpi_filtered_display['Route'] = bpi_filtered_display['route_short_name'] + " (" + bpi_filtered_display['route_long_name'] + ")"

                # Keep only the combined column and BPI
                bpi_filtered_display = bpi_filtered_display[['Route', 'BPI','OTP','Deviation from schedule']]

                # Sort by BPI descending
                bpi_filtered_sorted = bpi_filtered_display.sort_values(by='BPI', ascending=False)

                # Reset index and set it to start from 1
                bpi_filtered_sorted.reset_index(drop=True, inplace=True)
                bpi_filtered_sorted.index = range(1, 1 + len(bpi_filtered_sorted))

                # Function to color BPI values
                def color_bpi(val):
                    if val > 0.7:
                        color = 'green'
                    else:
                        color = 'red'
                        
                    return f'color: {color}; font-weight: bold'
                
                def color_otp(val):
                    if val > 0.7:
                        color = 'green'
                    else:
                        color = 'red'
                        
                    return f'color: {color}; font-weight: bold'
                
                def color_mae(val):
                    if val <= 0.5:
                        color = 'green'
                    else:
                        color = 'red'
                        
                    return f'color: {color}; font-weight: bold'

                # Apply styling only to BPI column
                styled_df = (
                    bpi_filtered_sorted.style
                        .map(color_bpi, subset=['BPI'])
                        .map(color_otp, subset=['OTP'])
                        .map(color_mae, subset=['Deviation from schedule'])
                )
  
                st.dataframe(styled_df)


        with col2:

            with st.container(border=True):
                st.markdown("""<h3 style="font-weight: 600; font-family: 'Crimson Pro', serif; font-size: 1.5rem; line-height: 1.3; text-align: center;">MRT Feeder</h3>""", unsafe_allow_html=True)

                bpi1_filtered_display = bpi1_filtered[['route_id', 'BPI','OTP', 'Deviation from schedule']].rename(columns={'route_id': 'Route'})

    
                # Sort by BPI descending
                bpi1_filtered_sorted = bpi1_filtered_display.sort_values(by='BPI', ascending=False)

                # Reset index and set it to start from 1
                bpi1_filtered_sorted.reset_index(drop=True, inplace=True)
                bpi1_filtered_sorted.index = range(1, 1 + len(bpi1_filtered_sorted))

                # Function to color BPI values
                def color_otp(val):
                    if val > 0.7:
                        color = 'green'
                    else:
                        color = 'red'
                        
                    return f'color: {color}; font-weight: bold'
                
                def color_mae(val):
                    if val <= 0.5:
                        color = 'green'
                    else:
                        color = 'red'
                        
                    return f'color: {color}; font-weight: bold'

                # Apply styling only to BPI column
                styled_df = (
                    bpi1_filtered_sorted.style
                        .map(color_bpi, subset=['BPI'])
                        .map(color_otp, subset=['OTP'])
                        .map(color_mae, subset=['Deviation from schedule'])
                )
  
                st.dataframe(styled_df)

    with st.container(border=True):

        st.markdown("""<h3 style="font-weight: 600; font-family: 'Crimson Pro', serif; font-size: 2.25rem; line-height: 1.15; text-align: center">Least Performing Routes</h3>""", unsafe_allow_html=True)
        st.caption("Note: BPI close to 0 implies that either most of the bus doesn't arrive on-time or the deviation from schedule is more than the schedule itself if it's not on-time.")

        col1, col2 = st.columns(2)

        with col1:

            with st.container(border=True):

                st.markdown("""<h3 style="font-weight: 600; font-family: 'Crimson Pro', serif; font-size: 1.5rem; line-height: 1.3; text-align: center;">Rapid KL Bus</h3>""", unsafe_allow_html=True)

                # Combine short and long names
                bpi_filtered_display = bpi_filtered.copy()
                bpi_filtered_display['Route'] = bpi_filtered_display['route_short_name'] + " (" + bpi_filtered_display['route_long_name'] + ")"

                # Keep only the combined column and BPI
                bpi_filtered_display = bpi_filtered_display[['Route', 'BPI', 'OTP', 'Deviation from schedule']]

                # Sort by BPI ascending
                bpi_filtered_sorted = bpi_filtered_display.sort_values(by='BPI', ascending=True)

                # Reset index and set it to start from 1
                bpi_filtered_sorted.reset_index(drop=True, inplace=True)
                bpi_filtered_sorted.index = range(1, 1 + len(bpi_filtered_sorted))

                # Function to color BPI values
                def color_otp(val):
                    if val > 0.7:
                        color = 'green'
                    else:
                        color = 'red'
                        
                    return f'color: {color}; font-weight: bold'
                
                def color_mae(val):
                    if val <= 0.5:
                        color = 'green'
                    else:
                        color = 'red'
                        
                    return f'color: {color}; font-weight: bold'

                # Apply styling only to BPI column
                styled_df = (
                    bpi_filtered_sorted.style
                        .map(color_bpi, subset=['BPI'])
                        .map(color_otp, subset=['OTP'])
                        .map(color_mae, subset=['Deviation from schedule'])
                )
  
                st.dataframe(styled_df)


        with col2:

            with st.container(border=True):
                st.markdown("""<h3 style="font-weight: 600; font-family: 'Crimson Pro', serif; font-size: 1.5rem; line-height: 1.3; text-align: center;">MRT Feeder</h3>""", unsafe_allow_html=True)

                bpi1_filtered_display = bpi1_filtered[['route_id', 'BPI', 'OTP', 'Deviation from schedule']].rename(columns={'route_id': 'Route'})

    
                # Sort by BPI ascending
                bpi1_filtered_sorted = bpi1_filtered_display.sort_values(by='BPI', ascending=True)

                # Reset index and set it to start from 1
                bpi1_filtered_sorted.reset_index(drop=True, inplace=True)
                bpi1_filtered_sorted.index = range(1, 1 + len(bpi1_filtered_sorted))

                # Function to color BPI values
                def color_otp(val):
                    if val > 0.7:
                        color = 'green'
                    else:
                        color = 'red'
                        
                    return f'color: {color}; font-weight: bold'
                
                def color_mae(val):
                    if val <= 0.5:
                        color = 'green'
                    else:
                        color = 'red'
                        
                    return f'color: {color}; font-weight: bold'

                # Apply styling only to BPI column
                styled_df = (
                    bpi1_filtered_sorted.style
                        .map(color_bpi, subset=['BPI'])
                        .map(color_otp, subset=['OTP'])
                        .map(color_mae, subset=['Deviation from schedule'])
                )
  
                st.dataframe(styled_df)

