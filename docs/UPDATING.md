# Updating the data

This describes how to add a new month to the dashboard. No code changes are needed.

## 1. Produce the month's results

Run the R pipeline for both operators. For each operator it writes three
files for the month, under `Output/Final Result/<dataset>/<operator>/<year>/`:

- `monthly_bpi_YYYYMM.csv`
- `daily_bpi_YYYYMM.csv`
- `bus_stop_otp_YYYYMM.csv`

## 2. Collect and rename the 6 files

The R files have the same names for both operators, so copy them into one
folder and add the operator to each name:

| Rapid KL | MRT Feeder |
|---|---|
| `Rapid_kl_monthly_bpi_YYYYMM.csv` | `MRT_monthly_bpi_YYYYMM.csv` |
| `Rapid_kl_daily_bpi_YYYYMM.csv` | `MRT_daily_bpi_YYYYMM.csv` |
| `Rapid_kl_bus_stop_otp_YYYYMM.csv` | `MRT_bus_stop_otp_YYYYMM.csv` |

## 3. Add the month

From the repo root:

```bash
python -m scripts.append_month 202610 path/to/that/folder
```

The script checks all 6 files first and writes nothing if:
- the month is already in the shared files;
- a file or column is missing;
- a file contains another month or duplicate rows;
- a file has empty cells or non-numeric values (MRT route names may be blank);
- a Rapid KL row has no route name, because the route label is built from it
  and a blank one breaks the Route page.

The 3 shared files are updated together. If one cannot be written (for example
it is open in Excel), all 3 are left unchanged. If a run is killed mid-write,
delete any leftover `dataset/.*.tmp` files and check `git status` first.

## 4. Check and publish

1. Run `streamlit run app.py`, pick the new month and check every chart.
2. Commit `dataset/monthly_bpi.csv`, `dataset/daily_bpi.csv` and
   `dataset/stop_otp.csv`, open a PR and merge to main.
3. Reboot the app on share.streamlit.io if it does not refresh.
