import sys
import streamlit as st
import plotly.express as px
from pathlib import Path
from datetime import datetime

# Add parent directory to sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

# --- Reusable slider function ---
def month_slider(unique_months_list, label="Select Month:", key=None):
    """
    Creates a Streamlit slider for selecting a month.
    """
    # Sort and convert to datetime objects
    raw_months = sorted(unique_months_list)
    month_datetimes = [datetime.strptime(m, "%Y-%m") for m in raw_months]

    # Slider
    selected_month_dt = st.slider(
        label,
        min_value=month_datetimes[0],
        max_value=month_datetimes[-1],
        value=month_datetimes[0],
        format="YYYY/MM",
        key=key,
    )

    selected_month_raw = selected_month_dt.strftime("%Y-%m")

    return selected_month_raw, selected_month_dt


# --- Cached data and chart generator ---
@st.cache_data
def get_ternary_rapid_kl(df):
    """Generates a ternary scatter chart from a given dataframe."""
    df["hover_text"] = (
        "<b>Route " + df["route_short_name"].astype(str) + "  " + df["route_long_name"] + "</b>" +
        "<br><b>Early:</b>&nbsp;&nbsp;" + (df["ratio_early"] * 100).round(1).astype(str) + "%" +
        "<br><b>On-Time:</b>&nbsp;&nbsp;" + (df["ratio_on_time"] * 100).round(1).astype(str) + "%" +
        "<br><b>Late:</b>&nbsp;&nbsp;" + (df["ratio_late"] * 100).round(1).astype(str) + "%"
    )
    
    # Compute network-wide otp performance
    total_early = df["n_early"].sum()
    total_on_time = df["n_on_time"].sum()
    total_late = df["n_late"].sum()
    total_all = total_early + total_on_time + total_late

    # Compute ratios for the network average
    avg_ratios = {
        "ratio_early": total_early / total_all,
        "ratio_on_time": total_on_time / total_all,
        "ratio_late": total_late / total_all
    }

    avg_hover_text = (
        "<b>Network Average</b>" +
        "<br><b>Early:</b>&nbsp;&nbsp;" + f"{avg_ratios['ratio_early']*100:.1f}%" +
        "<br><b>On-Time:</b>&nbsp;&nbsp;" + f"{avg_ratios['ratio_on_time']*100:.1f}%" +
        "<br><b>Late:</b>&nbsp;&nbsp;" + f"{avg_ratios['ratio_late']*100:.1f}%"
    )


    fig = px.scatter_ternary(
        df,
        a= "ratio_on_time",
        b= "ratio_early", 
        c= "ratio_late",
        labels={"ratio_early": "Early", "ratio_late": "Late", "ratio_on_time": "On Time"}
    )

    fig.add_scatterternary(
        a= [0.7, 0.7, 1.0, 0.7], 
        b=[0.3, 0.0, 0.0, 0.3], 
        c=[0.0, 0.3, 0.0, 0.0],
        mode='none',
        fill='toself',
        fillcolor='rgba(0, 255, 0, 0.12)',  # soft green transparent overlay
        name='≥ 70% On-Time',
        hoverinfo='skip',
        showlegend=True
    )

    fig.add_scatterternary(
        a=[0.0, 0.0, 0.7, 0.7], 
        b=[1.0, 0.0, 0.0, 0.3],
        c=[0.0, 1.0, 0.3, 0.0],
        mode='none',
        fill='toself',
        fillcolor='rgba(255,0,0,0.10)',  # soft red transparent overlay
        name='< 70% On-Time',
        hoverinfo='skip',
        showlegend=True
    )

    fig.data = fig.data[::-1]

    fig.update_ternaries(
        aaxis=dict(tickvals=[0.2, 0.4, 0.6, 0.8, 1.0]),
        baxis=dict(tickvals=[0.2, 0.4, 0.6, 0.8, 1.0]),
        caxis=dict(tickvals=[0.2, 0.4, 0.6, 0.8, 1.0])
    )

    fig.update_traces(
        customdata=df["hover_text"],
        hovertemplate="%{customdata}",
        marker=dict(color="#8FAAE5", size=7, line=dict(width=1, color="white"))
    )

    # Add network average as a star
    fig.add_scatterternary(
        a=[avg_ratios["ratio_on_time"]], 
        b=[avg_ratios["ratio_early"]],
        c=[avg_ratios["ratio_late"]],
        mode='markers',
        marker=dict(symbol='star', size=14, color= "#FF671B"),
        hoverinfo='text',
        hovertext=[avg_hover_text],
        name='Network Average'
    )

    fig.update_layout(
        width=250,  # adjust width
        height=300,  # adjust height
        paper_bgcolor='#1c293d',
        plot_bgcolor= '#1c293d',
        ternary=dict(
            bgcolor='#1c293d',     # inside triangle background
            aaxis=dict(title=dict(text='On Time', font=dict(color='white')), tickcolor='white', gridcolor='#2d313e'),
            baxis=dict(title=dict(text='Early', font=dict(color='white')), tickcolor='white', gridcolor='#2d313e'),
            caxis=dict(title=dict(text='Late', font=dict(color='white')), tickcolor='white', gridcolor='#2d313e')
        ),
        font=dict(color='white'),
        margin=dict(l=40, r=40, t=40, b=40),
        legend=dict(
            bgcolor='#1c293d',            
            x=0,                         # position: x-axis (0=left)
            y=-0.3,                      # position: y-axis (below plot)
            xanchor='left',
            yanchor='top',
            font=dict(
            size=13
            )
        ),
        hoverlabel=dict(
            bgcolor='rgba(255,255,255,0.25)',  # white with 70% opacity
            bordercolor='white',               # white border (optional)
            font=dict(size = 13, color='black')           # black text
        )      
    )
        

    return fig

@st.cache_data
def get_ternary_mrt_feeder(df):
    """Generates a ternary scatter chart from a given dataframe."""
    df["hover_text"] = (
        "<b>Route " + df["route_id"].astype(str) + "</b>" +
        "<br><b>Early:</b>&nbsp;&nbsp;" + (df["ratio_early"] * 100).round(1).astype(str) + "%" +
        "<br><b>On-Time:</b>&nbsp;&nbsp;" + (df["ratio_on_time"] * 100).round(1).astype(str) + "%" +
        "<br><b>Late:</b>&nbsp;&nbsp;" + (df["ratio_late"] * 100).round(1).astype(str) + "%"
    )
    
    # Compute network-wide otp performance
    total_early = df["n_early"].sum()
    total_on_time = df["n_on_time"].sum()
    total_late = df["n_late"].sum()
    total_all = total_early + total_on_time + total_late

    # Compute ratios for the network average
    avg_ratios = {
        "ratio_early": total_early / total_all,
        "ratio_on_time": total_on_time / total_all,
        "ratio_late": total_late / total_all
    }

    avg_hover_text = (
        "<b>Network Average</b>" +
        "<br><b>Early:</b>&nbsp;&nbsp;" + f"{avg_ratios['ratio_early']*100:.1f}%" +
        "<br><b>On-Time:</b>&nbsp;&nbsp;" + f"{avg_ratios['ratio_on_time']*100:.1f}%" +
        "<br><b>Late:</b>&nbsp;&nbsp;" + f"{avg_ratios['ratio_late']*100:.1f}%"
    )

    fig = px.scatter_ternary(
        df,
        a= "ratio_on_time",
        b= "ratio_early", 
        c= "ratio_late",
        labels={"ratio_early": "Early", "ratio_late": "Late", "ratio_on_time": "On Time"}
    )

    fig.update_ternaries(
        aaxis=dict(tickvals=[0.2, 0.4, 0.6, 0.8, 1.0]),
        baxis=dict(tickvals=[0.2, 0.4, 0.6, 0.8, 1.0]),
        caxis=dict(tickvals=[0.2, 0.4, 0.6, 0.8, 1.0])
    )

    fig.add_scatterternary(
        a=[0.7, 0.7, 1.0, 0.7], 
        b=[0.3, 0.0, 0.0, 0.3], 
        c=[0.0, 0.3, 0.0, 0.0],
        mode='none',
        fill='toself',
        fillcolor='rgba(0, 255, 0, 0.12)',  # soft green transparent overlay
        name='≥ 70% On-Time',
        hoverinfo='skip',
        showlegend=True
    )

    fig.add_scatterternary(
        a=[0.0, 0.0, 0.7, 0.7], 
        b=[1.0, 0.0, 0.0, 0.3],
        c=[0.0, 1.0, 0.3, 0.0],
        mode='none',
        fill='toself',
        fillcolor='rgba(255,0,0,0.10)',  # soft red transparent overlay
        name='< 70% On-Time',
        hoverinfo='skip',
        showlegend=True
    )

    fig.data = fig.data[::-1]

    fig.update_traces(
        customdata=df["hover_text"],
        hovertemplate="%{customdata}",
        marker=dict(color="#FF671B", size=7, line=dict(width=1, color="white"))
    )

    # Add network average as a star
    fig.add_scatterternary(
        a=[avg_ratios["ratio_on_time"]], 
        b=[avg_ratios["ratio_early"]],
        c=[avg_ratios["ratio_late"]],
        mode='markers',
        marker=dict(symbol='star', size=14, color= "#8FAAE5"),
        hoverinfo='text',
        hovertext=[avg_hover_text],
        name='Network Average'
    )

    fig.update_layout(
        width=250,  # adjust width
        height=300,  # adjust height
        paper_bgcolor='#1c293d',
        plot_bgcolor= '#1c293d',
        ternary=dict(
            bgcolor='#1c293d',     # inside triangle background
            aaxis=dict(title=dict(text='On Time', font=dict(color='white')), tickcolor='white', gridcolor='#2d313e'),
            baxis=dict(title=dict(text='Early', font=dict(color='white')), tickcolor='white', gridcolor='#2d313e'),
            caxis=dict(title=dict(text='Late', font=dict(color='white')), tickcolor='white', gridcolor='#2d313e')
        ),
        font=dict(color='white'),
        margin=dict(l=40, r=40, t=40, b=40),
        legend=dict(
            bgcolor='#1c293d',            
            x=0,                         # position: x-axis (0=left)
            y=-0.3,                      # position: y-axis (below plot)
            xanchor='left',
            yanchor='top',
            font=dict(
            size=13
            )
        ),
        hoverlabel=dict(
            bgcolor='rgba(255,255,255,0.95)',  # white with 70% opacity
            bordercolor='white',               # white border (optional)
            font=dict(size=13, color='black')            # black text
        )     
    )
    
    return fig