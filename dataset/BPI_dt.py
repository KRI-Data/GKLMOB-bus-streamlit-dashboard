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

    df_202512 = pd.read_csv("dataset/Rapid_kl_monthly_bpi_202512.csv")
    ratio_rapid_kl_202512 = df_202512[['route_short_name', 'route_long_name', 'month', 'n', 'n_on_time', 'n_early', 'n_late']]

    ratio_rapid_kl_202512['ratio_on_time'] = ratio_rapid_kl_202512['n_on_time'] / ratio_rapid_kl_202512['n']
    ratio_rapid_kl_202512['ratio_early'] = ratio_rapid_kl_202512['n_early'] / ratio_rapid_kl_202512['n']
    ratio_rapid_kl_202512['ratio_late'] = ratio_rapid_kl_202512['n_late'] / ratio_rapid_kl_202512['n']

    df_202601 = pd.read_csv("dataset/Rapid_kl_monthly_bpi_202601.csv")
    ratio_rapid_kl_202601 = df_202601[['route_short_name', 'route_long_name', 'month', 'n', 'n_on_time', 'n_early', 'n_late']]

    ratio_rapid_kl_202601['ratio_on_time'] = ratio_rapid_kl_202601['n_on_time'] / ratio_rapid_kl_202601['n']
    ratio_rapid_kl_202601['ratio_early'] = ratio_rapid_kl_202601['n_early'] / ratio_rapid_kl_202601['n']
    ratio_rapid_kl_202601['ratio_late'] = ratio_rapid_kl_202601['n_late'] / ratio_rapid_kl_202601['n']

    df_202602 = pd.read_csv("dataset/Rapid_kl_monthly_bpi_202602.csv")
    ratio_rapid_kl_202602 = df_202602[['route_short_name', 'route_long_name', 'month', 'n', 'n_on_time', 'n_early', 'n_late']]

    ratio_rapid_kl_202602['ratio_on_time'] = ratio_rapid_kl_202602['n_on_time'] / ratio_rapid_kl_202602['n']
    ratio_rapid_kl_202602['ratio_early'] = ratio_rapid_kl_202602['n_early'] / ratio_rapid_kl_202602['n']
    ratio_rapid_kl_202602['ratio_late'] = ratio_rapid_kl_202602['n_late'] / ratio_rapid_kl_202602['n']

    df_202603 = pd.read_csv("dataset/Rapid_kl_monthly_bpi_202603.csv")
    ratio_rapid_kl_202603 = df_202603[['route_short_name', 'route_long_name', 'month', 'n', 'n_on_time', 'n_early', 'n_late']]

    ratio_rapid_kl_202603['ratio_on_time'] = ratio_rapid_kl_202603['n_on_time'] / ratio_rapid_kl_202603['n']
    ratio_rapid_kl_202603['ratio_early'] = ratio_rapid_kl_202603['n_early'] / ratio_rapid_kl_202603['n']
    ratio_rapid_kl_202603['ratio_late'] = ratio_rapid_kl_202603['n_late'] / ratio_rapid_kl_202603['n']

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

    ratio_rapid_kl_202512 = ratio_rapid_kl_202512.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    ratio_rapid_kl_202601 = ratio_rapid_kl_202601.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    ratio_rapid_kl_202602 = ratio_rapid_kl_202602.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    ratio_rapid_kl_202603 = ratio_rapid_kl_202603.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    combined = pd.concat([ratio_rapid_kl, ratio_rapid_kl_new, ratio_rapid_kl_202512, ratio_rapid_kl_202601, ratio_rapid_kl_202602, ratio_rapid_kl_202603], ignore_index=True)

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

    df_202512 = pd.read_csv("dataset/MRT_monthly_bpi_202512.csv")
    ratio_mrt_feeder_202512 = df_202512[['route_id', 'month', 'n', 'n_on_time', 'n_early', 'n_late']]

    ratio_mrt_feeder_202512['ratio_on_time'] = ratio_mrt_feeder_202512['n_on_time'] / ratio_mrt_feeder_202512['n']
    ratio_mrt_feeder_202512['ratio_early'] = ratio_mrt_feeder_202512['n_early'] / ratio_mrt_feeder_202512['n']
    ratio_mrt_feeder_202512['ratio_late'] = ratio_mrt_feeder_202512['n_late'] / ratio_mrt_feeder_202512['n']

    df_202601 = pd.read_csv("dataset/MRT_monthly_bpi_202601.csv")
    ratio_mrt_feeder_202601 = df_202601[['route_id', 'month', 'n', 'n_on_time', 'n_early', 'n_late']]

    ratio_mrt_feeder_202601['ratio_on_time'] = ratio_mrt_feeder_202601['n_on_time'] / ratio_mrt_feeder_202601['n']
    ratio_mrt_feeder_202601['ratio_early'] = ratio_mrt_feeder_202601['n_early'] / ratio_mrt_feeder_202601['n']
    ratio_mrt_feeder_202601['ratio_late'] = ratio_mrt_feeder_202601['n_late'] / ratio_mrt_feeder_202601['n']

    df_202602 = pd.read_csv("dataset/MRT_monthly_bpi_202602.csv")
    ratio_mrt_feeder_202602 = df_202602[['route_id', 'month', 'n', 'n_on_time', 'n_early', 'n_late']]

    ratio_mrt_feeder_202602['ratio_on_time'] = ratio_mrt_feeder_202602['n_on_time'] / ratio_mrt_feeder_202602['n']
    ratio_mrt_feeder_202602['ratio_early'] = ratio_mrt_feeder_202602['n_early'] / ratio_mrt_feeder_202602['n']
    ratio_mrt_feeder_202602['ratio_late'] = ratio_mrt_feeder_202602['n_late'] / ratio_mrt_feeder_202602['n']

    df_202603 = pd.read_csv("dataset/MRT_monthly_bpi_202603.csv")
    ratio_mrt_feeder_202603 = df_202603[['route_id', 'month', 'n', 'n_on_time', 'n_early', 'n_late']]

    ratio_mrt_feeder_202603['ratio_on_time'] = ratio_mrt_feeder_202603['n_on_time'] / ratio_mrt_feeder_202603['n']
    ratio_mrt_feeder_202603['ratio_early'] = ratio_mrt_feeder_202603['n_early'] / ratio_mrt_feeder_202603['n']
    ratio_mrt_feeder_202603['ratio_late'] = ratio_mrt_feeder_202603['n_late'] / ratio_mrt_feeder_202603['n']

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

    ratio_mrt_feeder_202512 = ratio_mrt_feeder_202512.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    ratio_mrt_feeder_202601 = ratio_mrt_feeder_202601.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    ratio_mrt_feeder_202602 = ratio_mrt_feeder_202602.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    ratio_mrt_feeder_202603 = ratio_mrt_feeder_202603.round({
        'ratio_on_time': 4,
        'ratio_late': 4,
        'ratio_early': 4
    })

    combined = pd.concat([ratio_mrt_feeder, ratio_mrt_feeder_new, ratio_mrt_feeder_202512, ratio_mrt_feeder_202601, ratio_mrt_feeder_202602, ratio_mrt_feeder_202603], ignore_index=True)

    return combined

@st.cache_data
def unique_months():
    df = pd.read_csv("dataset/BPI_Rapid_KL_relative.csv")
    df_new = pd.read_csv("dataset/BPI_Rapid_KL_new.csv")
    df_202512 = pd.read_csv("dataset/Rapid_kl_monthly_bpi_202512.csv")
    df_202601 = pd.read_csv("dataset/Rapid_kl_monthly_bpi_202601.csv")
    df_202602 = pd.read_csv("dataset/Rapid_kl_monthly_bpi_202602.csv")
    df_202603 = pd.read_csv("dataset/Rapid_kl_monthly_bpi_202603.csv")
    
    combined_months = pd.concat([
        df['month'],
        df_new['month'],
        df_202512['month'],
        df_202601['month'],
        df_202602['month'],
        df_202603['month']
    ])

    unique_months = sorted(combined_months.unique())
    
    return unique_months

@st.cache_data
def bpi_rapid_kl():
    df = pd.read_csv("dataset/BPI_Rapid_KL_relative.csv")
    df_new = pd.read_csv("dataset/BPI_Rapid_KL_new.csv")
    df_202512 = pd.read_csv("dataset/Rapid_kl_monthly_bpi_202512.csv")
    df_202601 = pd.read_csv("dataset/Rapid_kl_monthly_bpi_202601.csv")
    df_202602 = pd.read_csv("dataset/Rapid_kl_monthly_bpi_202602.csv")
    df_202603 = pd.read_csv("dataset/Rapid_kl_monthly_bpi_202603.csv")

    bpi_rapid_kl = df[['route_short_name', 'route_long_name','mae_ratio','otp', 'month', 'I_hat']].rename(columns={'I_hat': 'BPI', 'mae_ratio':'rMAE','otp':'OTP'})
    bpi_rapid_kl_new = df_new[['route_short_name', 'route_long_name','mae_ratio','otp', 'month', 'I_hat']].rename(columns={'I_hat': 'BPI', 'mae_ratio':'rMAE','otp':'OTP'})
    bpi_rapid_202512 = df_202512[['route_short_name', 'route_long_name','mae_ratio','otp', 'month', 'BPI']].rename(columns={'mae_ratio':'rMAE','otp':'OTP'})
    bpi_rapid_202601 = df_202601[['route_short_name', 'route_long_name','mae_ratio','otp', 'month', 'BPI']].rename(columns={'mae_ratio':'rMAE','otp':'OTP'})
    bpi_rapid_202602 = df_202602[['route_short_name', 'route_long_name','mae_ratio','otp', 'month', 'BPI']].rename(columns={'mae_ratio':'rMAE','otp':'OTP'})
    bpi_rapid_202603 = df_202603[['route_short_name', 'route_long_name','mae_ratio','otp', 'month', 'BPI']].rename(columns={'mae_ratio':'rMAE','otp':'OTP'})

    bpi_rapid_kl['rMAE'] = bpi_rapid_kl['rMAE'].clip(upper=1)
    bpi_rapid_kl_new['rMAE'] = bpi_rapid_kl_new['rMAE'].clip(upper=1)
    bpi_rapid_202512['rMAE'] =  bpi_rapid_202512['rMAE'].clip(upper=1)
    bpi_rapid_202601['rMAE'] =  bpi_rapid_202601['rMAE'].clip(upper=1)
    bpi_rapid_202602['rMAE'] =  bpi_rapid_202602['rMAE'].clip(upper=1)
    bpi_rapid_202603['rMAE'] =  bpi_rapid_202603['rMAE'].clip(upper=1)

    combined = pd.concat([bpi_rapid_kl, bpi_rapid_kl_new, bpi_rapid_202512, bpi_rapid_202601, bpi_rapid_202602, bpi_rapid_202603], ignore_index=True)

    return combined

@st.cache_data
def bpi_mrt_feeder():
    df = pd.read_csv("dataset/BPI_MRT_Feeder_relative.csv")
    df_new = pd.read_csv("dataset/BPI_MRT_Feeder_new.csv")
    df_202512 = pd.read_csv("dataset/MRT_monthly_bpi_202512.csv")
    df_202601 = pd.read_csv("dataset/MRT_monthly_bpi_202601.csv")
    df_202602 = pd.read_csv("dataset/MRT_monthly_bpi_202602.csv")
    df_202603 = pd.read_csv("dataset/MRT_monthly_bpi_202603.csv")

    bpi_mrt_feeder = df[['route_id', 'mae_ratio','otp', 'month', 'I_hat']].rename(columns={'I_hat': 'BPI', 'mae_ratio':'rMAE','otp':'OTP' })
    bpi_mrt_feeder_new = df_new[['route_id', 'mae_ratio','otp', 'month', 'I_hat']].rename(columns={'I_hat': 'BPI', 'mae_ratio':'rMAE','otp':'OTP' })
    bpi_mrt_202512 = df_202512[['route_id', 'mae_ratio','otp', 'month', 'BPI']].rename(columns={'mae_ratio':'rMAE','otp':'OTP'})
    bpi_mrt_202601 = df_202601[['route_id', 'mae_ratio','otp', 'month', 'BPI']].rename(columns={'mae_ratio':'rMAE','otp':'OTP'})
    bpi_mrt_202602 = df_202602[['route_id', 'mae_ratio','otp', 'month', 'BPI']].rename(columns={'mae_ratio':'rMAE','otp':'OTP'})
    bpi_mrt_202603 = df_202603[['route_id', 'mae_ratio','otp', 'month', 'BPI']].rename(columns={'mae_ratio':'rMAE','otp':'OTP'})

    bpi_mrt_feeder['rMAE'] = bpi_mrt_feeder['rMAE'].clip(upper=1)
    bpi_mrt_feeder_new['rMAE'] = bpi_mrt_feeder_new['rMAE'].clip(upper=1)
    bpi_mrt_202512['rMAE'] = bpi_mrt_202512['rMAE'].clip(upper=1)
    bpi_mrt_202601['rMAE'] = bpi_mrt_202601['rMAE'].clip(upper=1)
    bpi_mrt_202602['rMAE'] = bpi_mrt_202602['rMAE'].clip(upper=1)
    bpi_mrt_202603['rMAE'] = bpi_mrt_202603['rMAE'].clip(upper=1)

    combined = pd.concat([bpi_mrt_feeder, bpi_mrt_feeder_new, bpi_mrt_202512, bpi_mrt_202601, bpi_mrt_202602, bpi_mrt_202603], ignore_index=True)

    return combined