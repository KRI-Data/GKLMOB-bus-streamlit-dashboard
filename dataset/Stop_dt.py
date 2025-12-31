import pandas as pd
import streamlit as st

@st.cache_data
def stop_mrt_feeder():
    df = pd.read_csv("dataset/Stop_OTP_MRT_Feeder_relative.csv")
    stop_mrt_feeder = df[['route_id', 'stop_name', 'month', 'on time', 'early', 'late']]

    df_new = pd.read_csv("dataset/Stop_OTP_MRT_Feeder_new.csv")
    stop_mrt_feeder_new = df_new[['route_id', 'stop_name', 'month', 'on time', 'early', 'late']]

    stop_mrt_feeder['total'] = stop_mrt_feeder['on time'] + stop_mrt_feeder['late'] + stop_mrt_feeder['early']
    stop_mrt_feeder['ratio_on_time'] = stop_mrt_feeder['on time'] / stop_mrt_feeder['total']
    stop_mrt_feeder['ratio_early'] = stop_mrt_feeder['early'] / stop_mrt_feeder['total']
    stop_mrt_feeder['ratio_late'] = stop_mrt_feeder['late'] / stop_mrt_feeder['total']

    stop_mrt_feeder = stop_mrt_feeder.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    stop_mrt_feeder_new['total'] = stop_mrt_feeder_new['on time'] + stop_mrt_feeder_new['late'] + stop_mrt_feeder_new['early']
    stop_mrt_feeder_new['ratio_on_time'] = stop_mrt_feeder_new['on time'] / stop_mrt_feeder_new['total']
    stop_mrt_feeder_new['ratio_early'] = stop_mrt_feeder_new['early'] / stop_mrt_feeder_new['total']
    stop_mrt_feeder_new['ratio_late'] = stop_mrt_feeder_new['late'] / stop_mrt_feeder_new['total']

    stop_mrt_feeder_new = stop_mrt_feeder_new.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    combined = pd.concat([stop_mrt_feeder, stop_mrt_feeder_new], ignore_index=True)

    return combined

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

    df_new = pd.read_csv("dataset/Stop_OTP_Rapid_KL_new.csv")
    stop_rapid_kl_new = df_new[['route_short_name','route_long_name', 'stop_name', 'month', 'on time', 'early', 'late']]

    stop_rapid_kl_new['route_id'] = stop_rapid_kl_new['route_short_name'] + " (" + stop_rapid_kl_new['route_long_name'] + ")"
    stop_rapid_kl_new = stop_rapid_kl_new[['route_id', 'stop_name', 'month', 'on time', 'early', 'late']]

    stop_rapid_kl_new['total'] = stop_rapid_kl_new['on time'] + stop_rapid_kl_new['late'] + stop_rapid_kl_new['early']
    stop_rapid_kl_new['ratio_on_time'] = stop_rapid_kl_new['on time'] / stop_rapid_kl_new['total']
    stop_rapid_kl_new['ratio_early'] = stop_rapid_kl_new['early'] / stop_rapid_kl_new['total']
    stop_rapid_kl_new['ratio_late'] = stop_rapid_kl_new['late'] / stop_rapid_kl_new['total']

    stop_rapid_kl_new = stop_rapid_kl_new.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    combined = pd.concat([stop_rapid_kl, stop_rapid_kl_new], ignore_index=True)

    return combined

import pandas as pd

def list_route():
    # Read datasets
    df_mrt = pd.read_csv("dataset/Stop_OTP_MRT_Feeder_relative.csv")
    df_kl = pd.read_csv("dataset/Stop_OTP_Rapid_KL_relative.csv")

    df_mrt_new = pd.read_csv("dataset/Stop_OTP_MRT_Feeder_new.csv")
    df_kl_new = pd.read_csv("dataset/Stop_OTP_Rapid_KL_new.csv")

    # Ensure route_id exists for Rapid KL datasets
    for df in [df_kl, df_kl_new]:
        df["route_id"] = df["route_short_name"] + " (" + df["route_long_name"] + ")"

    # Collect unique routes using set (simplest + fastest)
    routes_kl = set(df_kl["route_id"]) | set(df_kl_new["route_id"])
    routes_mrt = set(df_mrt["route_id"]) | set(df_mrt_new["route_id"])

    # Combine everything
    all_routes = sorted(routes_kl | routes_mrt)

    return all_routes
