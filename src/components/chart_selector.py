from dash import dcc, html


def get_chart_type():
    return html.Div(
        dcc.Button('Speed', id='btn-speed'),
        dcc.Button('RPM', id='btn-rpm'),
        dcc.Button('Gear shifts', id='btn-gear-shifts'),
        dcc.Button('Throttle', id='btn-throttle'),
        dcc.Button('Brake', id='btn-brake')
    )
