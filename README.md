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
├── .streamlit/                # Dashboard format
├── dataset/                   # Dataset
├── graphs/                    # Helper functions for graphs
├── sections/                  # Helper functions for each sections
└── README.md                  # Documentation

```