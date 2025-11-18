import sys
import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path
from datetime import datetime

# Add parent directory to sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from dataset.Stop_dt import list_route, stop_mrt_feeder
from dataset.Daily_bpi import daily_mrt_feeder, daily_rapid_kl

def route_selector(label="Select route(s):", key=None, max_choices=6):
    """
    Creates a Streamlit multiselect widget for selecting one or more routes.
    """
    routes = list_route()  # Load available routes

    # Multiselect widget
    selected_routes = st.multiselect(
        label,
        routes,
        default=['851 (Hab Pasar Seni ~ Kompleks Mahkamah Jalan Duta)', 'AJ03 (Stesen LRT Cempaka ~ Bukit Teratai)',  'T789 (Stesen LRT Universiti ~ Universiti Malaya via Pantai Hillpark)'],
        key=key,
    )

    if len(selected_routes) > max_choices:
        st.warning(f"You can select up to {max_choices} routes only. Extra selections will be ignored.")
        selected_routes = selected_routes[:max_choices]

    return selected_routes

@st.cache_data
def get_stop(df):
    """Generates a ternary scatter chart grouped by route, each with its own color and average star."""
    
    # Create figure
    fig = go.Figure()

    # Group by route
    for route_id, group in df.groupby("route_id"):
        # Compute route average
        total_early = group["early"].sum()
        total_on_time = group["on time"].sum()
        total_late = group["late"].sum()
        total_all = total_early + total_on_time + total_late

        avg_ratios = {
            "ratio_early": total_early / total_all,
            "ratio_on_time": total_on_time / total_all,
            "ratio_late": total_late / total_all
        }

        avg_hover_text = (
            f"<b>Route {route_id} Average</b>"
            f"<br><b>Early:</b>&nbsp;&nbsp;{avg_ratios['ratio_early']*100:.1f}%"
            f"<br><b>On-Time:</b>&nbsp;&nbsp;{avg_ratios['ratio_on_time']*100:.1f}%"
            f"<br><b>Late:</b>&nbsp;&nbsp;{avg_ratios['ratio_late']*100:.1f}%"
        )

        # Add route stops (main points)
        fig.add_scatterternary(
            a=group["ratio_late"],
            b=group["ratio_early"],
            c=group["ratio_on_time"],
            mode='markers',
            name=f"Route {route_id}",
            customdata=(
                "<b>Stop: " + group["stop_name"].astype(str) + "</b>"
                + "<br><b>Early:</b>&nbsp;&nbsp;" + (group["ratio_early"] * 100).round(1).astype(str) + "%"
                + "<br><b>On-Time:</b>&nbsp;&nbsp;" + (group["ratio_on_time"] * 100).round(1).astype(str) + "%"
                + "<br><b>Late:</b>&nbsp;&nbsp;" + (group["ratio_late"] * 100).round(1).astype(str) + "%"
            ),
            hovertemplate="%{customdata}<extra></extra>",
            marker=dict(size=7, line=dict(width=1, color="white")),
            legendgroup=f"route_{route_id}",
            showlegend=True
        )

        # Add route average (star)
        fig.add_scatterternary(
            a=[avg_ratios["ratio_late"]],
            b=[avg_ratios["ratio_early"]],
            c=[avg_ratios["ratio_on_time"]],
            mode='markers',
            marker=dict(symbol='star', size=14, line=dict(width=1.5, color='white')),
            hoverinfo='text',
            hovertext=[avg_hover_text],
            name=f"Route {route_id} Average",
            legendgroup=f"route_{route_id}",
            showlegend=False  # keep it hidden from legend, but toggled with group
        )

    # --- Styling ---
    fig.update_ternaries(
        aaxis=dict(tickvals=[0.2, 0.4, 0.6, 0.8, 1.0]),
        baxis=dict(tickvals=[0.2, 0.4, 0.6, 0.8, 1.0]),
        caxis=dict(tickvals=[0.2, 0.4, 0.6, 0.8, 1.0])
    )
    fig.update_layout(
        width=250,
        height=400,
        paper_bgcolor='#1c293d',
        plot_bgcolor='#1c293d',
        ternary=dict(
            bgcolor='#1c293d',
            aaxis=dict(title=dict(text='Late', font=dict(color='white')), tickcolor='white'),
            baxis=dict(title=dict(text='Early', font=dict(color='white')), tickcolor='white'),
            caxis=dict(title=dict(text='On Time', font=dict(color='white')), tickcolor='white')
        ),
        font=dict(color='white'),
        margin=dict(l=40, r=40, t=40, b=40),
        legend=dict(
            bgcolor='#1c293d',            
            x=0,                        
            y=-0.3,                     
            xanchor='left',
            yanchor='top'
        ),
        hoverlabel=dict(
            bgcolor='rgba(255,255,255,0.85)',  # white with ~85% opacity
            bordercolor='white',
            font=dict(color='black')
        )
    )

    # --- Optional: start with only the first route visible ---
    for trace in fig.data:
        trace.visible = 'legendonly'

    return fig

def get_time_series(df):
    """
    Plots a time series of BPI for all routes in the dataframe.
    
    Parameters:
    df : pd.DataFrame
        Must contain columns ['route_id', 'date', 'BPI']
    """
    # Ensure 'date' is datetime
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    df = df.rename(columns={'route_id':'Route'})
    
    # Create Plotly line chart
    fig = px.line(
        df,
        x='Date',
        y='BPI',
        color='Route',
        labels={'BPI':'Bus Performance Index (BPI)', 'date':'Date'}
    )

    fig.update_traces(
        hovertemplate='<b>%{customdata[0]}</b><br>Date: %{x}<br>BPI: %{y:.2f}<extra></extra>',
        customdata=df[['Route']]  # Use customdata for bold Route
    )

    fig.update_layout(
        legend=dict(
            bgcolor='#1c293d',            
            x=0,                         # position: x-axis (0=left)
            y=-0.3,                      # position: y-axis (below plot)
            xanchor='left',
            yanchor='top'
            ),
            hoverlabel=dict(
                bgcolor='rgba(255,255,255,0.95)',  # bright white background
                bordercolor='rgba(200,200,200,0.8)',  # subtle border
                font= dict(color='black')
            )
        )
    
    for trace in fig.data:
        trace.visible = 'legendonly'
    
    # Render in Streamlit
    return fig