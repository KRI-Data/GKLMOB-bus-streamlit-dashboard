# GKLMOB Bus Dashboard

A Streamlit dashboard for analysing bus on-time performance and punctuality in
Kuala Lumpur, built from General Transit Feed Specification (GTFS) static and
real-time data. It covers two operators: **Rapid KL Bus** and **MRT Feeder**.

Live app: https://bus-dashboard.streamlit.app

The dashboard shows:
- **On-time performance (OTP):** the share of bus arrivals that were on time,
  early or late.
- **Bus Punctuality Index (BPI):** a single punctuality score per route.

## Pages

- **Network:** network-wide ternary plots (on-time / early / late), BPI
  distributions and ranked route tables, by month.
- **Route:** for up to 6 selected routes, OTP by bus stop and the daily BPI
  over time.
- **About:** background on the data and method.

## Getting started

Requires Python 3.11.

```bash
pip install -r requirements.txt
streamlit run app.py
```

Run from the repository root. The app reads data with relative paths such as
`dataset/monthly_bpi.csv`.

## Project structure

```
GKLMOB-BUS-DASHBOARD/
├── app.py                     # Main Streamlit app
├── config.py                  # Network names, shared by the app and the scripts
├── requirements.txt           # Pinned dependencies
├── .streamlit/                # Theme and dashboard format
├── dataset/                   # Loaders and the 3 shared data files
│   ├── monthly_bpi.csv
│   ├── daily_bpi.csv
│   └── stop_otp.csv
├── scripts/                   # Data tools (run with python -m)
├── docs/                      # Maintenance guides
├── graphs/                    # Plotly figure builders and shared widgets
├── sections/                  # One module per page
└── README.md
```

## Data

The app does no GTFS processing. All results are precomputed from GTFS static
and real-time feeds and stored in three shared files in `dataset/`. They cover
2025-04 onwards, for Rapid KL Bus and MRT Feeder routes.

| File | One row per | Columns |
|---|---|---|
| `monthly_bpi.csv` | network, route, month | `network`, `route_id`, `route`, `route_short_name`, `route_long_name`, `month`, `n`, `n_on_time`, `n_early`, `n_late`, `otp`, `mae_ratio`, `BPI` |
| `daily_bpi.csv` | network, route, day | `network`, `route_id`, `route`, `date`, `month`, `BPI` |
| `stop_otp.csv` | network, route, stop, month | `network`, `route_id`, `route`, `stop_name`, `month`, `n_on_time`, `n_early`, `n_late` |

Notes:
- `route` is the label shown in the app. For Rapid KL it is
  `route_short_name (route_long_name)`. For MRT Feeder it is `route_id`
  (e.g. `T100`).
- MRT Feeder rows have blank `route_short_name` and `route_long_name`. The MRT
  data has no route names.
- `month` is `YYYY-MM`.

To add a new month of data, see [docs/UPDATING.md](docs/UPDATING.md).
