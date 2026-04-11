from dash import dcc

def get_driver_selector(drivers: list):
    driver_sel = dcc.Dropdown(
        id = 'driver_selector',
        options = [{'label': driver, 'value': driver} for driver in drivers],
        placeholder = 'Select a driver',
        maxHeight=300,
    )
    return driver_sel