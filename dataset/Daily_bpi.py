import pandas as pd
import streamlit as st

@st.cache_data
def daily_rapid_kl():
    df = pd.read_csv("dataset/Daily_BPI_Rapid_KL_relative.csv")
    df_new = pd.read_csv("dataset/Daily_BPI_Rapid_KL_relative_new.csv")
    daily_rapid_kl = df[['route_short_name','route_long_name', 'date', 'month', 'I_hat']]
    daily_rapid_kl_new = df_new[['route_short_name','route_long_name', 'date', 'month', 'I_hat']]

    daily_rapid_kl['route_id'] = daily_rapid_kl['route_short_name'] + " (" + daily_rapid_kl['route_long_name'] + ")"
    daily_rapid_kl = daily_rapid_kl[['route_id', 'date', 'month', 'I_hat']].rename(columns={'I_hat':'BPI', 'route_id':'Route', 'date': 'Date'})

    daily_rapid_kl_new['route_id'] = daily_rapid_kl_new['route_short_name'] + " (" + daily_rapid_kl_new['route_long_name'] + ")"
    daily_rapid_kl_new = daily_rapid_kl_new[['route_id', 'date', 'month', 'I_hat']].rename(columns={'I_hat':'BPI', 'route_id':'Route', 'date': 'Date'})

    combined = pd.concat([daily_rapid_kl, daily_rapid_kl_new], ignore_index=True)

    return combined

@st.cache_data
def daily_mrt_feeder():
    df = pd.read_csv("dataset/Daily_BPI_MRT_Feeder_relative.csv")
    df_new = pd.read_csv("dataset/Daily_BPI_MRT_Feeder_relative_new.csv")
    daily_mrt_feeder = df[['route_id', 'date', 'month', 'I_hat']]
    daily_mrt_feeder_new = df_new[['route_id', 'date', 'month', 'I_hat']]
    daily_mrt_feeder = daily_mrt_feeder[['route_id', 'date', 'month', 'I_hat']].rename(columns={'I_hat':'BPI', 'route_id':'Route', 'date': 'Date'})
    daily_mrt_feeder_new = daily_mrt_feeder_new[['route_id', 'date', 'month', 'I_hat']].rename(columns={'I_hat':'BPI', 'route_id':'Route', 'date': 'Date'})

    combined = pd.concat([daily_mrt_feeder, daily_mrt_feeder_new], ignore_index=True)

    return combined