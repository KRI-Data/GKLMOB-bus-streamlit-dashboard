import sys
import streamlit as st
import plotly.express as px
from pathlib import Path
from datetime import datetime
import pandas as pd

# Add parent directory to sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from dataset.BPI_dt import bpi_rapid_kl, bpi_mrt_feeder

@st.cache_data
def get_violin(df_rapid, df_mrt):
    # Add mode column
    df_rapid = df_rapid.copy()
    df_mrt = df_mrt.copy()
    df_rapid['Network'] = 'Rapid KL Bus'
    df_mrt['Network'] = 'MRT Feeder'

    # Ensure month is datetime
    for df in [df_rapid, df_mrt]:
        df['month_dt'] = pd.to_datetime(df['month'], format="%Y-%m")
        df['month_label'] = df['month_dt'].dt.strftime('%B %Y')

    # Combine the two DataFrames
    df_combined = pd.concat([df_rapid, df_mrt], ignore_index=True)

    # Create violin plot
    fig = px.violin(
        df_combined,
        y='BPI',
        x='month_label',
        color='Network',
        box=True,
        points='all',
        hover_data=df_combined.columns
    )

    # Custom scatter point colors per mode
    scatter_colors = {'Rapid KL Bus': '#8FAAE5', 'MRT Feeder': '#FF671B'}

    for i, network in enumerate(df_combined['Network'].unique()):
        fig.update_traces(
            selector=dict(name=network),
            marker=dict(color=scatter_colors[network], size=6)
        )

    df_combined["hover_text"] = (
        "<b>Route " + df_combined["route_short_name"].astype(str) + "  " + df_combined["route_long_name"] + "</b>" +
        "<br><b>Network:</b> " + df_combined["Network"] +
        "<br><b>Month:</b> " + df_combined["month_label"] +
        "<br><b>BPI:</b> " + (df_combined["BPI"]).round(4).astype(str)
    )

    # Update scatter point hover
    fig.update_traces(
        selector=dict(type='violin'),
        points='all',  # show scatter points
        marker=dict(size=6),
        hovertemplate="%{customdata}<extra></extra>",  # show full HTML from customdata
        customdata=df_combined["hover_text"],
        hoverlabel=dict(
            bgcolor='rgba(255,255,255,0.95)',  # bright white background
            bordercolor='rgba(200,200,200,0.8)',  # subtle border
            font= dict(size= 13, color='black')
        )
    )


    fig.update_layout(
        width=900,
        height=350,
        xaxis_title="Month",
        yaxis_title="Bus Performance Index (BPI)",
        template="plotly_white",
        paper_bgcolor='#1c293d',
        plot_bgcolor= '#1c293d',
    )

    fig.update_yaxes(     
        ticks='outside',
        ticklen=6,
        tickcolor='white',
        tickwidth=2,
        showline=True,
        linecolor='white',
        title_font=dict(color='white'),
        tickfont=dict(color='white'),
        range=[0, 1]
    )
    fig.update_layout(
        legend=dict(
            font=dict(
                size=13,        
                color="white"   # optional
            ),
            bgcolor='#1c293d'
        )
    )

    return fig
