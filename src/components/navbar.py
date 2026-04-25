import dash_bootstrap_components as dbc
from dash import html

def get_navbar():
    return dbc.Navbar(
        dbc.Container(
            html.H1(
                "Formula One - '25 and '26 regulations telemetry comparison",
                className='text-center w-100 mb=0',
                style={'color': '#bfbde2'},
            ),
            fluid=True,
        ),
        color='dark',
        dark=True,
        className='app-navbar'
    )
