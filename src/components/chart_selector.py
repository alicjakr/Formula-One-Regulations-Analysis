import dash_bootstrap_components as dbc
from dash import dcc, html


def get_chart_type():
    return html.Div(
        dbc.Stack([
            dbc.Button('Speed', id='btn-speed', outline=True, className='button'),
            dbc.Button('RPM', id='btn-rpm', outline=True, className='button'),
            dbc.Button('Gear shifts', id='btn-gear-shifts', outline=True, className='button'),
            dbc.Button('Throttle', id='btn-throttle', outline=True, className='button'),
            dbc.Button('Brake', id='btn-brake', outline=True,className='button'),
        ],
        gap=2),
        id='chart-type',
    )
