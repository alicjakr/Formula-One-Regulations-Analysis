from dash import dcc


def get_gp_selector(gps: list):
    return dcc.Dropdown(
        id='gp-selector',
        options=[{'label': gp, 'value': gp} for gp in gps],
        placeholder='Select a GP',
        maxHeight=300,
        className='dropdown',
    )
