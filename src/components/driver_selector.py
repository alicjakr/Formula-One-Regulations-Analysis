from dash import dcc

def get_driver_selector():
    driver_sel = dcc.Dropdown(
        id = 'driver-selector',
        options = [],
        placeholder = 'Select a driver',
        maxHeight=300,
    )
    return driver_sel