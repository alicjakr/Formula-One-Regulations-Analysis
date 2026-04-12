import dash_bootstrap_components as dbc
from dash import dcc


def get_display_mode():
    return dbc.Row([
        dbc.Col([
            dbc.Label('Display mode'),
            dcc.RadioItems(
                id='display-mode',
                options=[
                    {'label': 'separate', 'value': 'separate'},
                    {'label': 'together', 'value': 'together'},
                ],
                value='separate', className='radio-white',
            ),
        ], style={'width': '50%', 'display': 'inline-block', 'color': 'white'}),
        dbc.Col([])
    ])


def get_display_type():
    return dbc.Row([
        dbc.Col([
            dbc.Label('Display type'),
            dcc.RadioItems(
                id='display-type',
                options=[
                    {'label': 'circuit', 'value': 'circuit'},
                    {'label': 'plot', 'value': 'plot'},
                ],
                value='circuit', className='radio-white',
            ),
        ], style={'width': '50%', 'display': 'inline-block', 'color': 'white'}),
        dbc.Col([])
    ])


def get_session_type():
    return dbc.Row([
        dbc.Col([
            dbc.Label('Session type'),
            dcc.RadioItems(
                id='session-type',
                options=[
                    {'label': 'qualifying', 'value': 'qualifying'},
                    {'label': 'race', 'value': 'race'},
                ],
                value='qualifying', className='radio-white',
            ),
        ], style={'width': '50%', 'display': 'inline-block', 'color': 'white'}),
        dbc.Col([])
    ])
