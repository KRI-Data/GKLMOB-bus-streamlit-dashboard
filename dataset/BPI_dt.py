import pandas as pd
import streamlit as st

@st.cache_data
def ratio_rapid_kl():
    df = pd.read_csv("dataset/BPI_Rapid_KL_relative.csv")
    ratio_rapid_kl = df[['route_short_name', 'route_long_name', 'month', 'n', 'n_on_time', 'n_early', 'n_late']]

    ratio_rapid_kl['ratio_on_time'] = ratio_rapid_kl['n_on_time'] / ratio_rapid_kl['n']
    ratio_rapid_kl['ratio_early'] = ratio_rapid_kl['n_early'] / ratio_rapid_kl['n']
    ratio_rapid_kl['ratio_late'] = ratio_rapid_kl['n_late'] / ratio_rapid_kl['n']

    df_new = pd.read_csv("dataset/BPI_Rapid_KL_new.csv")
    ratio_rapid_kl_new = df_new[['route_short_name', 'route_long_name', 'month', 'n', 'n_on_time', 'n_early', 'n_late']]

    ratio_rapid_kl_new['ratio_on_time'] = ratio_rapid_kl_new['n_on_time'] / ratio_rapid_kl_new['n']
    ratio_rapid_kl_new['ratio_early'] = ratio_rapid_kl_new['n_early'] / ratio_rapid_kl_new['n']
    ratio_rapid_kl_new['ratio_late'] = ratio_rapid_kl_new['n_late'] / ratio_rapid_kl_new['n']

    ratio_rapid_kl = ratio_rapid_kl.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    ratio_rapid_kl_new = ratio_rapid_kl_new.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    combined = pd.concat([ratio_rapid_kl, ratio_rapid_kl_new], ignore_index=True)

    return combined

@st.cache_data
def ratio_mrt_feeder():
    df = pd.read_csv("dataset/BPI_MRT_Feeder_relative.csv")
    ratio_mrt_feeder = df[['route_id', 'month', 'n', 'n_on_time', 'n_early', 'n_late']]

    ratio_mrt_feeder['ratio_on_time'] = ratio_mrt_feeder['n_on_time'] / ratio_mrt_feeder['n']
    ratio_mrt_feeder['ratio_early'] = ratio_mrt_feeder['n_early'] / ratio_mrt_feeder['n']
    ratio_mrt_feeder['ratio_late'] = ratio_mrt_feeder['n_late'] / ratio_mrt_feeder['n']

    df_new = pd.read_csv("dataset/BPI_MRT_Feeder_new.csv")
    ratio_mrt_feeder_new = df_new[['route_id', 'month', 'n', 'n_on_time', 'n_early', 'n_late']]

    ratio_mrt_feeder_new['ratio_on_time'] = ratio_mrt_feeder_new['n_on_time'] / ratio_mrt_feeder_new['n']
    ratio_mrt_feeder_new['ratio_early'] = ratio_mrt_feeder_new['n_early'] / ratio_mrt_feeder_new['n']
    ratio_mrt_feeder_new['ratio_late'] = ratio_mrt_feeder_new['n_late'] / ratio_mrt_feeder_new['n']

    ratio_mrt_feeder = ratio_mrt_feeder.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    ratio_mrt_feeder_new = ratio_mrt_feeder_new.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    combined = pd.concat([ratio_mrt_feeder, ratio_mrt_feeder_new], ignore_index=True)

    return combined

@st.cache_data
def unique_months():
    df = pd.read_csv("dataset/BPI_Rapid_KL_relative.csv")
    df_new = pd.read_csv("dataset/BPI_Rapid_KL_new.csv")
    
    combined_months = pd.concat([
        df['month'],
        df_new['month']
    ])

    unique_months = sorted(combined_months.unique())
    
    return unique_months

@st.cache_data
def bpi_rapid_kl():
    df = pd.read_csv("dataset/BPI_Rapid_KL_relative.csv")
    df_new = pd.read_csv("dataset/BPI_Rapid_KL_new.csv")
    bpi_rapid_kl = df[['route_short_name', 'route_long_name','mae_ratio','otp', 'month', 'I_hat']].rename(columns={'I_hat': 'BPI', 'mae_ratio':'rMAE','otp':'OTP'})
    bpi_rapid_kl_new = df_new[['route_short_name', 'route_long_name','mae_ratio','otp', 'month', 'I_hat']].rename(columns={'I_hat': 'BPI', 'mae_ratio':'rMAE','otp':'OTP'})

    bpi_rapid_kl['rMAE'] = bpi_rapid_kl['rMAE'].clip(upper=1)
    bpi_rapid_kl_new['rMAE'] = bpi_rapid_kl_new['rMAE'].clip(upper=1)

    combined = pd.concat([bpi_rapid_kl, bpi_rapid_kl_new], ignore_index=True)

    return combined

@st.cache_data
def bpi_mrt_feeder():
    df = pd.read_csv("dataset/BPI_MRT_Feeder_relative.csv")
    df_new = pd.read_csv("dataset/BPI_MRT_Feeder_new.csv")
    bpi_mrt_feeder = df[['route_id', 'mae_ratio','otp', 'month', 'I_hat']].rename(columns={'I_hat': 'BPI', 'mae_ratio':'rMAE','otp':'OTP' })
    bpi_mrt_feeder_new = df_new[['route_id', 'mae_ratio','otp', 'month', 'I_hat']].rename(columns={'I_hat': 'BPI', 'mae_ratio':'rMAE','otp':'OTP' })

    bpi_mrt_feeder['rMAE'] = bpi_mrt_feeder['rMAE'].clip(upper=1)
    bpi_mrt_feeder_new['rMAE'] = bpi_mrt_feeder_new['rMAE'].clip(upper=1)

    combined = pd.concat([bpi_mrt_feeder, bpi_mrt_feeder_new], ignore_index=True)

    return combined