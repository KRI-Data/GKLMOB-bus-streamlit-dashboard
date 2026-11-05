# GKLMOB-BUS-DASHBOARD

A Streamlit-based web dashboard for analysing bus performance and mobility patterns using General Transit Feed Specification (GTFS) real-time and static.

This dashboard visualises key metrics such as on-time performance and Bus Punctuality Index (BPI) — providing insights into public transport reliability.

## Getting Strated
### 1. Install Dependencies

To install Streamlit and the option menu component, run:

```bash
pip install streamlit streamlit_option_menu

```

### 2. Run the App

From the project directory, run:

```bash
streamlit run app.py
```

## Project Structure
The project is organised as follow:

```bash
GKLMOB-BUS-DASHBOARD/
├── app.py                     # Main Streamlit app
├── config.py                  # Network names, shared by the app and the scripts
├── .streamlit/                # Dashboard format
├── dataset/                   # Loaders and the 3 shared data files
│   ├── monthly_bpi.csv        # One row per network, route and month
│   ├── daily_bpi.csv          # One row per network, route and day
│   └── stop_otp.csv           # One row per network, route, stop and month
├── scripts/                   # Data tools (run with python -m)
├── graphs/                    # Helper functions for graphs
├── sections/                  # Helper functions for each sections
└── README.md                  # Documentation
```

## Monthly data update

No code changes are needed to add a month.

1. Run the R pipeline (GKLMOB-bus-dashboard_01) for both operators.
2. Copy and rename the 6 result CSVs into one folder, e.g. `Rapid_kl_monthly_bpi_202610.csv`.
3. From the repo root, add them to the shared files:

   ```bash
   python -m scripts.append_month 202610 path/to/that/folder
   ```

   Nothing is written if the month is already there, a file or column is missing,
   or a file contains another month or duplicate rows.
4. Run `streamlit run app.py`, pick the new month and check every chart.
5. Commit `dataset/monthly_bpi.csv`, `dataset/daily_bpi.csv` and `dataset/stop_otp.csv`,
   open a PR and merge to main.
6. Reboot the app on share.streamlit.io if it does not refresh.


```