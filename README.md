# Formula One Regulations Change Telemetry Analysis

This repository contains tools and code for analyzing Formula One race data (seasons 2025–2026). It focuses on comparing races, drivers, and car behaviour under the new regulations, producing data transforms, visualizations, and interactive dashboards.

## Features
- Load and cache race telemetry and session data
- Comparative analysis across seasons, drivers, and teams
- Interactive visualizations and dashboards (Plotly / Dash)
- Reproducible data processing in src/

## Requirements
- Python 3.9+
- See requirements.txt for pinned dependencies

## Quick setup
1. Create and activate a virtual environment (recommended):
   ```
   python -m venv .venv
   source .venv/bin/activate  # macOS / Linux
   .venv\Scripts\activate     # Windows
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running
- Run the main app/dashboard (if present):
  ``` python src/app.py ```
- Run specific analysis scripts in src/ (open them to see usage and arguments).

## Project layout
- ``` src/ ```              — Main Python package and scripts
- ``` cache/ ```            — Downloaded/raw data and cached telemetry
- ``` requirements.txt ```  — Python dependencies

## Data
- Telemetry and session data are cached in cache/ to avoid re-downloading.
- Data sources and download scripts (if any) are in src/data or documented in scripts.

## Development
- Analyse upcoming races telemetry plotting.
- Add unit tests alongside code when possible.

## License
- See the LICENSE file in the repository root for licensing details.
