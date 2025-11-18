import pandas as pd
import streamlit as st

@st.cache_data
def ratio_rapid_kl():
    df = pd.read_csv("dataset/BPI_Rapid_KL_relative.csv")
    ratio_rapid_kl = df[['route_short_name', 'route_long_name', 'month', 'n', 'n_on_time', 'n_early', 'n_late']]

    ratio_rapid_kl['ratio_on_time'] = ratio_rapid_kl['n_on_time'] / ratio_rapid_kl['n']
    ratio_rapid_kl['ratio_early'] = ratio_rapid_kl['n_early'] / ratio_rapid_kl['n']
    ratio_rapid_kl['ratio_late'] = ratio_rapid_kl['n_late'] / ratio_rapid_kl['n']

    ratio_rapid_kl = ratio_rapid_kl.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    return ratio_rapid_kl

@st.cache_data
def ratio_mrt_feeder():
    df = pd.read_csv("dataset/BPI_MRT_Feeder_relative.csv")
    ratio_mrt_feeder = df[['route_id', 'month', 'n', 'n_on_time', 'n_early', 'n_late']]

    ratio_mrt_feeder['ratio_on_time'] = ratio_mrt_feeder['n_on_time'] / ratio_mrt_feeder['n']
    ratio_mrt_feeder['ratio_early'] = ratio_mrt_feeder['n_early'] / ratio_mrt_feeder['n']
    ratio_mrt_feeder['ratio_late'] = ratio_mrt_feeder['n_late'] / ratio_mrt_feeder['n']

    ratio_mrt_feeder = ratio_mrt_feeder.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    return ratio_mrt_feeder

@st.cache_data
def unique_months():
    df = pd.read_csv("dataset/BPI_Rapid_KL_relative.csv")
    
    # Get sorted unique months
    unique_months = sorted(df['month'].unique())
    
    return unique_months

@st.cache_data
def bpi_rapid_kl():
    df = pd.read_csv("dataset/BPI_Rapid_KL_relative.csv")
    bpi_rapid_kl = df[['route_short_name', 'route_long_name','mae_ratio','otp', 'month', 'I_hat']].rename(columns={'I_hat': 'BPI', 'mae_ratio':'rMAE','otp':'OTP'})

    bpi_rapid_kl['rMAE'] = bpi_rapid_kl['rMAE'].clip(upper=1)

    return bpi_rapid_kl

@st.cache_data
def bpi_mrt_feeder():
    df = pd.read_csv("dataset/BPI_MRT_Feeder_relative.csv")
    bpi_mrt_feeder = df[['route_id', 'mae_ratio','otp', 'month', 'I_hat']].rename(columns={'I_hat': 'BPI', 'mae_ratio':'rMAE','otp':'OTP' })

    bpi_mrt_feeder['rMAE'] = bpi_mrt_feeder['rMAE'].clip(upper=1)

    return bpi_mrt_feeder