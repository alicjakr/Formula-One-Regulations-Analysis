# Formula One Telemetry Analysis 🏎️

An interactive web dashboard for analysing and comparing Formula 1 telemetry data across the 2025 and 2026 seasons, built with Python, Dash, and FastF1.

![Dashboard Preview](assets/F1.png)

---

## Features

- **Circuit map view** — visualise telemetry channels (Speed, RPM, Gear, Throttle, Brake) overlaid on the track layout using colour gradients
- **Telemetry plot view** — standard time-series graphs of telemetry channels over lap distance
- **Season comparison** — plot the same driver's fastest lap from 2025 and 2026 on a single graph
- **Brake visualisation** — binary brake trace rendered as two separate colour-coded traces (braking / not braking)
- **Dynamic driver selector** — automatically populated based on the selected Grand Prix and session type
- **Past GPs only** — the GP selector only shows events that have already taken place in 2026
- **Graceful missing data handling** — displays an informative message when a driver has no telemetry for a given session

---

## Tech Stack

| Library | Purpose |
|---|---|
| [FastF1](https://github.com/theOehrly/Fast-F1) | F1 telemetry and session data |
| [Dash](https://dash.plotly.com/) | Web application framework |
| [Plotly](https://plotly.com/python/) | Interactive graphs and circuit maps |
| [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/) | UI layout and theming |
| [NumPy](https://numpy.org/) | Telemetry data processing |
| [Pandas](https://pandas.pydata.org/) | Data manipulation |

---

## Installation

**Prerequisites:** Python 3.10+

1. Clone the repository:
```bash
git clone https://github.com/alicjakr/Formula_One_analysis.git
cd Formula_One_analysis
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
python src/app.py
```

5. Open your browser at `http://localhost:8050`

---

## Usage

1. Select a **session type** (Qualifying or Race)
2. Choose a **Grand Prix** from the available 2026 events
3. Pick a **driver**
4. Select **Display type** — Circuit map or Plot
5. Click one of the telemetry buttons — **Speed, RPM, Gear Shifts, Throttle, Brake**
6. For Plot mode, choose **Separate** (single season) or **Together** (2025 vs 2026 comparison)

---

## Project Structure

```
Formula_One_analysis/
├── src/
│   ├── app.py                  # Main Dash app and callbacks
│   ├── components/
│   │   ├── navbar.py
│   │   ├── footer.py
│   │   ├── session_selector.py
│   │   ├── driver_selector.py
│   │   ├── GP_selector.py
│   │   ├── chart_selector.py
│   │   ├── telemetry_chart.py  # Standard plot rendering
│   │   └── track_map.py        # Circuit map rendering
│   └── data/
│       ├── loader.py           # Session loading and caching
│       └── telemetry.py        # Telemetry extraction
├── assets/
│   └── F1.png
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Known Limitations

- Only 2025 and 2026 seasons are supported for the comparison mode
- Drivers who did not finish or participate in a session will show a "no telemetry" message
- FastF1 data availability depends on the official F1 timing feed — some sessions may have incomplete data

---

## Acknowledgements

- Telemetry data provided by [FastF1](https://github.com/theOehrly/Fast-F1) — licensed under MIT
- F1 logo and branding are trademarks of Formula One Licensing B.V. and are used here solely for personal/educational purposes

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
