import pandas as pd
import streamlit as st

@st.cache_data
def daily_rapid_kl():
    df = pd.read_csv("dataset/Daily_BPI_Rapid_KL_relative.csv")
    df_new = pd.read_csv("dataset/Daily_BPI_Rapid_KL_relative_new.csv")
    df_202512 = pd.read_csv("dataset/Rapid_kl_daily_bpi_202512.csv")
    df_202601 = pd.read_csv("dataset/Rapid_kl_daily_bpi_202601.csv")
    df_202602 = pd.read_csv("dataset/Rapid_kl_daily_bpi_202602.csv")

    daily_rapid_kl = df[['route_short_name','route_long_name', 'date', 'month', 'I_hat']]
    daily_rapid_kl_new = df_new[['route_short_name','route_long_name', 'date', 'month', 'I_hat']]
    daily_rapid_kl_202512 = df_202512[['route_short_name','route_long_name', 'date', 'month', 'BPI']]
    daily_rapid_kl_202601 = df_202601[['route_short_name','route_long_name', 'date', 'month', 'BPI']]
    daily_rapid_kl_202602 = df_202602[['route_short_name','route_long_name', 'date', 'month', 'BPI']]

    daily_rapid_kl['route_id'] = daily_rapid_kl['route_short_name'] + " (" + daily_rapid_kl['route_long_name'] + ")"
    daily_rapid_kl = daily_rapid_kl[['route_id', 'date', 'month', 'I_hat']].rename(columns={'I_hat':'BPI', 'route_id':'Route', 'date': 'Date'})

    daily_rapid_kl_new['route_id'] = daily_rapid_kl_new['route_short_name'] + " (" + daily_rapid_kl_new['route_long_name'] + ")"
    daily_rapid_kl_new = daily_rapid_kl_new[['route_id', 'date', 'month', 'I_hat']].rename(columns={'I_hat':'BPI', 'route_id':'Route', 'date': 'Date'})

    daily_rapid_kl_202512['route_id'] = daily_rapid_kl_202512['route_short_name'] + " (" + daily_rapid_kl_202512['route_long_name'] + ")"
    daily_rapid_kl_202512 = daily_rapid_kl_202512[['route_id', 'date', 'month', 'BPI']].rename(columns={'route_id':'Route', 'date': 'Date'})

    daily_rapid_kl_202601['route_id'] = daily_rapid_kl_202601['route_short_name'] + " (" + daily_rapid_kl_202601['route_long_name'] + ")"
    daily_rapid_kl_202601 = daily_rapid_kl_202601[['route_id', 'date', 'month', 'BPI']].rename(columns={'route_id':'Route', 'date': 'Date'})

    daily_rapid_kl_202602['route_id'] = daily_rapid_kl_202602['route_short_name'] + " (" + daily_rapid_kl_202602['route_long_name'] + ")"
    daily_rapid_kl_202602 = daily_rapid_kl_202602[['route_id', 'date', 'month', 'BPI']].rename(columns={'route_id':'Route', 'date': 'Date'})

    combined = pd.concat([daily_rapid_kl, daily_rapid_kl_new, daily_rapid_kl_202512, daily_rapid_kl_202601, daily_rapid_kl_202602], ignore_index=True)

    return combined

@st.cache_data
def daily_mrt_feeder():
    df = pd.read_csv("dataset/Daily_BPI_MRT_Feeder_relative.csv")
    df_new = pd.read_csv("dataset/Daily_BPI_MRT_Feeder_relative_new.csv")
    df_202512 = pd.read_csv("dataset/MRT_daily_bpi_202512.csv")
    df_202601 = pd.read_csv("dataset/MRT_daily_bpi_202601.csv")
    df_202602 = pd.read_csv("dataset/MRT_daily_bpi_202602.csv")
    
    daily_mrt_feeder = df[['route_id', 'date', 'month', 'I_hat']]
    daily_mrt_feeder_new = df_new[['route_id', 'date', 'month', 'I_hat']]
    daily_mrt_feeder_new = df_new[['route_id', 'date', 'month', 'I_hat']]
    daily_mrt_feeder = daily_mrt_feeder[['route_id', 'date', 'month', 'I_hat']].rename(columns={'I_hat':'BPI', 'route_id':'Route', 'date': 'Date'})
    daily_mrt_feeder_new = daily_mrt_feeder_new[['route_id', 'date', 'month', 'I_hat']].rename(columns={'I_hat':'BPI', 'route_id':'Route', 'date': 'Date'})
    daily_mrt_feeder_202512 = df_202512[['route_id', 'date', 'month', 'BPI']].rename(columns={'route_id':'Route', 'date': 'Date'})
    daily_mrt_feeder_202601 = df_202601[['route_id', 'date', 'month', 'BPI']].rename(columns={'route_id':'Route', 'date': 'Date'})
    daily_mrt_feeder_202602 = df_202602[['route_id', 'date', 'month', 'BPI']].rename(columns={'route_id':'Route', 'date': 'Date'})

    combined = pd.concat([daily_mrt_feeder, daily_mrt_feeder_new, daily_mrt_feeder_202512, daily_mrt_feeder_202601, daily_mrt_feeder_202602], ignore_index=True)

    return combined