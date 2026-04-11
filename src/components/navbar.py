import dash_bootstrap_components as dbc
from dash import html


def get_navbar():
    navbar = dbc.Navbar(
        html.Div(
            html.H1('Formula One data telemetry comparison for seasons 2025 and 2026')
        ),
        className = 'app-navbar'
    )
    return navbar