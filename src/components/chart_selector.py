import dash_bootstrap_components as dbc
from dash import dcc, html


def get_chart_type():
    return html.Div(
        dbc.Stack([
            dbc.Button('Speed', id='btn-speed', outline=True, color='#535C91'),
            dbc.Button('RPM', id='btn-rpm', outline=True, color='#535C91'),
            dbc.Button('Gear shifts', id='btn-gear-shifts', outline=True, color='#535C91'),
            dbc.Button('Throttle', id='btn-throttle', outline=True, color='#535C91'),
            dbc.Button('Brake', id='btn-brake', outline=True, color='#535C91'),
        ]),
        id='chart-type',
    )
