from dash import dcc


def get_driver_selector():
    return dcc.Dropdown(
        id='driver-selector',
        options=[],
        placeholder='Select a driver',
        maxHeight=300,
        className='dropdown',
    )