import pandas as pd
import streamlit as st

@st.cache_data
def stop_mrt_feeder():
    df = pd.read_csv("dataset/Stop_OTP_MRT_Feeder_relative.csv")
    stop_mrt_feeder = df[['route_id', 'stop_name', 'month', 'on time', 'early', 'late']]

    stop_mrt_feeder['total'] = stop_mrt_feeder['on time'] + stop_mrt_feeder['late'] + stop_mrt_feeder['early']
    stop_mrt_feeder['ratio_on_time'] = stop_mrt_feeder['on time'] / stop_mrt_feeder['total']
    stop_mrt_feeder['ratio_early'] = stop_mrt_feeder['early'] / stop_mrt_feeder['total']
    stop_mrt_feeder['ratio_late'] = stop_mrt_feeder['late'] / stop_mrt_feeder['total']

    stop_mrt_feeder = stop_mrt_feeder.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    return stop_mrt_feeder

@st.cache_data
def stop_rapid_kl():
    df = pd.read_csv("dataset/Stop_OTP_Rapid_KL_relative.csv")
    stop_rapid_kl = df[['route_short_name','route_long_name', 'stop_name', 'month', 'on time', 'early', 'late']]

    stop_rapid_kl['route_id'] = stop_rapid_kl['route_short_name'] + " (" + stop_rapid_kl['route_long_name'] + ")"
    stop_rapid_kl = stop_rapid_kl[['route_id', 'stop_name', 'month', 'on time', 'early', 'late']]

    stop_rapid_kl['total'] = stop_rapid_kl['on time'] + stop_rapid_kl['late'] + stop_rapid_kl['early']
    stop_rapid_kl['ratio_on_time'] = stop_rapid_kl['on time'] / stop_rapid_kl['total']
    stop_rapid_kl['ratio_early'] = stop_rapid_kl['early'] / stop_rapid_kl['total']
    stop_rapid_kl['ratio_late'] = stop_rapid_kl['late'] / stop_rapid_kl['total']

    stop_rapid_kl = stop_rapid_kl.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    return stop_rapid_kl

def list_route():
    df = pd.read_csv("dataset/Stop_OTP_MRT_Feeder_relative.csv")
    df1 = pd.read_csv("dataset/Stop_OTP_Rapid_KL_relative.csv")

    df1['route_id'] = df1['route_short_name'] + " (" + df1['route_long_name'] + ")"
    stop_rapid_kl = df1[['route_id']]

    routes_kl = df1['route_id'].unique()
    routes_mrt = df['route_id'].unique()  # Get all unique route IDs

    all_routes = list(routes_kl) + list(routes_mrt)
    return sorted(all_routes)