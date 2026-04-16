import pandas as pd
import streamlit as st

@st.cache_data
def stop_mrt_feeder():
    df = pd.read_csv("dataset/Stop_OTP_MRT_Feeder_relative.csv")
    stop_mrt_feeder = df[['route_id', 'stop_name', 'month', 'on time', 'early', 'late']]

    df_new = pd.read_csv("dataset/Stop_OTP_MRT_Feeder_new.csv")
    stop_mrt_feeder_new = df_new[['route_id', 'stop_name', 'month', 'on time', 'early', 'late']]

    df_202512 = pd.read_csv("dataset/MRT_bus_stop_otp_202512.csv")
    stop_mrt_feeder_202512 = df_202512[['route_id', 'stop_name', 'month', 'on time', 'early', 'late']]

    df_202601 = pd.read_csv("dataset/MRT_bus_stop_otp_202601.csv")
    stop_mrt_feeder_202601 = df_202601[['route_id', 'stop_name', 'month', 'on time', 'early', 'late']]

    df_202602 = pd.read_csv("dataset/MRT_bus_stop_otp_202602.csv")
    stop_mrt_feeder_202602 = df_202602[['route_id', 'stop_name', 'month', 'on time', 'early', 'late']]

    df_202603 = pd.read_csv("dataset/MRT_bus_stop_otp_202603.csv")
    stop_mrt_feeder_202603 = df_202603[['route_id', 'stop_name', 'month', 'on time', 'early', 'late']]

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

    stop_mrt_feeder_202512['total'] = stop_mrt_feeder_202512['on time'] + stop_mrt_feeder_202512['late'] + stop_mrt_feeder_202512['early']
    stop_mrt_feeder_202512['ratio_on_time'] = stop_mrt_feeder_202512['on time'] / stop_mrt_feeder_202512['total']
    stop_mrt_feeder_202512['ratio_early'] = stop_mrt_feeder_202512['early'] / stop_mrt_feeder_202512['total']
    stop_mrt_feeder_202512['ratio_late'] = stop_mrt_feeder_202512['late'] / stop_mrt_feeder_202512['total']

    stop_mrt_feeder_202512 = stop_mrt_feeder_202512.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    stop_mrt_feeder_202601['total'] = stop_mrt_feeder_202601['on time'] + stop_mrt_feeder_202601['late'] + stop_mrt_feeder_202601['early']
    stop_mrt_feeder_202601['ratio_on_time'] = stop_mrt_feeder_202601['on time'] / stop_mrt_feeder_202601['total']
    stop_mrt_feeder_202601['ratio_early'] = stop_mrt_feeder_202601['early'] / stop_mrt_feeder_202601['total']
    stop_mrt_feeder_202601['ratio_late'] = stop_mrt_feeder_202601['late'] / stop_mrt_feeder_202601['total']

    stop_mrt_feeder_202601 = stop_mrt_feeder_202601.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    stop_mrt_feeder_202602['total'] = stop_mrt_feeder_202602['on time'] + stop_mrt_feeder_202602['late'] + stop_mrt_feeder_202602['early']
    stop_mrt_feeder_202602['ratio_on_time'] = stop_mrt_feeder_202602['on time'] / stop_mrt_feeder_202602['total']
    stop_mrt_feeder_202602['ratio_early'] = stop_mrt_feeder_202602['early'] / stop_mrt_feeder_202602['total']
    stop_mrt_feeder_202602['ratio_late'] = stop_mrt_feeder_202602['late'] / stop_mrt_feeder_202602['total']

    stop_mrt_feeder_202602 = stop_mrt_feeder_202602.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    stop_mrt_feeder_202603['total'] = stop_mrt_feeder_202603['on time'] + stop_mrt_feeder_202603['late'] + stop_mrt_feeder_202603['early']
    stop_mrt_feeder_202603['ratio_on_time'] = stop_mrt_feeder_202603['on time'] / stop_mrt_feeder_202603['total']
    stop_mrt_feeder_202603['ratio_early'] = stop_mrt_feeder_202603['early'] / stop_mrt_feeder_202603['total']
    stop_mrt_feeder_202603['ratio_late'] = stop_mrt_feeder_202603['late'] / stop_mrt_feeder_202603['total']

    stop_mrt_feeder_202603 = stop_mrt_feeder_202603.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    combined = pd.concat([stop_mrt_feeder, stop_mrt_feeder_new, stop_mrt_feeder_202512, stop_mrt_feeder_202601, stop_mrt_feeder_202602, stop_mrt_feeder_202603], ignore_index=True)

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

    df_202512 = pd.read_csv("dataset/Rapid_kl_bus_stop_otp_202512.csv")
    stop_rapid_kl_202512 = df_202512[['route_short_name','route_long_name', 'stop_name', 'month', 'on time', 'early', 'late']]

    stop_rapid_kl_202512['route_id'] = stop_rapid_kl_202512['route_short_name'] + " (" + stop_rapid_kl_202512['route_long_name'] + ")"
    stop_rapid_kl_202512 = stop_rapid_kl_202512[['route_id', 'stop_name', 'month', 'on time', 'early', 'late']]

    stop_rapid_kl_202512['total'] = stop_rapid_kl_202512['on time'] + stop_rapid_kl_202512['late'] + stop_rapid_kl_202512['early']
    stop_rapid_kl_202512['ratio_on_time'] = stop_rapid_kl_202512['on time'] / stop_rapid_kl_202512['total']
    stop_rapid_kl_202512['ratio_early'] = stop_rapid_kl_202512['early'] / stop_rapid_kl_202512['total']
    stop_rapid_kl_202512['ratio_late'] = stop_rapid_kl_202512['late'] / stop_rapid_kl_202512['total']

    stop_rapid_kl_202512 = stop_rapid_kl_202512.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    df_202601 = pd.read_csv("dataset/Rapid_kl_bus_stop_otp_202601.csv")
    stop_rapid_kl_202601 = df_202601[['route_short_name','route_long_name', 'stop_name', 'month', 'on time', 'early', 'late']]

    stop_rapid_kl_202601['route_id'] = stop_rapid_kl_202601['route_short_name'] + " (" + stop_rapid_kl_202601['route_long_name'] + ")"
    stop_rapid_kl_202601 = stop_rapid_kl_202601[['route_id', 'stop_name', 'month', 'on time', 'early', 'late']]

    stop_rapid_kl_202601['total'] = stop_rapid_kl_202601['on time'] + stop_rapid_kl_202601['late'] + stop_rapid_kl_202601['early']
    stop_rapid_kl_202601['ratio_on_time'] = stop_rapid_kl_202601['on time'] / stop_rapid_kl_202601['total']
    stop_rapid_kl_202601['ratio_early'] = stop_rapid_kl_202601['early'] / stop_rapid_kl_202601['total']
    stop_rapid_kl_202601['ratio_late'] = stop_rapid_kl_202601['late'] / stop_rapid_kl_202601['total']

    stop_rapid_kl_202601 = stop_rapid_kl_202601.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    df_202602 = pd.read_csv("dataset/Rapid_kl_bus_stop_otp_202602.csv")
    stop_rapid_kl_202602 = df_202602[['route_short_name','route_long_name', 'stop_name', 'month', 'on time', 'early', 'late']]

    stop_rapid_kl_202602['route_id'] = stop_rapid_kl_202602['route_short_name'] + " (" + stop_rapid_kl_202602['route_long_name'] + ")"
    stop_rapid_kl_202602 = stop_rapid_kl_202602[['route_id', 'stop_name', 'month', 'on time', 'early', 'late']]

    stop_rapid_kl_202602['total'] = stop_rapid_kl_202602['on time'] + stop_rapid_kl_202602['late'] + stop_rapid_kl_202602['early']
    stop_rapid_kl_202602['ratio_on_time'] = stop_rapid_kl_202602['on time'] / stop_rapid_kl_202602['total']
    stop_rapid_kl_202602['ratio_early'] = stop_rapid_kl_202602['early'] / stop_rapid_kl_202602['total']
    stop_rapid_kl_202602['ratio_late'] = stop_rapid_kl_202602['late'] / stop_rapid_kl_202602['total']

    stop_rapid_kl_202602 = stop_rapid_kl_202602.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    df_202603 = pd.read_csv("dataset/Rapid_kl_bus_stop_otp_202603.csv")
    stop_rapid_kl_202603 = df_202603[['route_short_name','route_long_name', 'stop_name', 'month', 'on time', 'early', 'late']]

    stop_rapid_kl_202603['route_id'] = stop_rapid_kl_202603['route_short_name'] + " (" + stop_rapid_kl_202603['route_long_name'] + ")"
    stop_rapid_kl_202603 = stop_rapid_kl_202603[['route_id', 'stop_name', 'month', 'on time', 'early', 'late']]

    stop_rapid_kl_202603['total'] = stop_rapid_kl_202603['on time'] + stop_rapid_kl_202603['late'] + stop_rapid_kl_202603['early']
    stop_rapid_kl_202603['ratio_on_time'] = stop_rapid_kl_202603['on time'] / stop_rapid_kl_202603['total']
    stop_rapid_kl_202603['ratio_early'] = stop_rapid_kl_202603['early'] / stop_rapid_kl_202603['total']
    stop_rapid_kl_202603['ratio_late'] = stop_rapid_kl_202603['late'] / stop_rapid_kl_202603['total']

    stop_rapid_kl_202603 = stop_rapid_kl_202603.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    combined = pd.concat([stop_rapid_kl, stop_rapid_kl_new, stop_rapid_kl_202512, stop_rapid_kl_202601, stop_rapid_kl_202602, stop_rapid_kl_202603], ignore_index=True)

    return combined

import pandas as pd

def list_route():
    # Read datasets
    df_mrt = pd.read_csv("dataset/MRT_bus_stop_otp_202603.csv")
    df_kl = pd.read_csv("dataset/Rapid_kl_bus_stop_otp_202603.csv")

    # Ensure route_id exists for Rapid KL datasets
    df_kl["route_id"] = df_kl["route_short_name"] + " (" + df_kl["route_long_name"] + ")"

    # Collect unique routes using set (simplest + fastest)
    routes_kl = set(df_kl["route_id"])
    routes_mrt = set(df_mrt["route_id"])

    # Combine everything
    all_routes = sorted(routes_kl | routes_mrt)

    return all_routes
