import dbc
from dash import Dash, html, callback, Output, Input
from components import navbar, footer, session_selector, driver_selector, GP_selector
from data import loader
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div(
    id = 'parentDiv',
    children = [
        navbar.get_navbar(),

        html.H1(children='Hello Dash', style = {'color': 'white'}),

        session_selector.get_display_mode(),
        session_selector.get_display_type(),
        session_selector.get_session_type(),

        GP_selector.get_gp_selector(loader.get_common_events()),
        driver_selector.get_driver_selector(),

        footer.get_footer()
    ], style = {'backgroundColor': '#070F2B'}
)

@callback(
    Output('driver-selector', 'options'),
    Input('gp-selector', 'value'),
    Input('session-type', 'value'),
)

def update_drivers(gp, session_type):
    print(f"update")
    if not gp or not session_type:
        return []
    drivers = loader.get_common_drivers(gp, session_type)
    return [{'label': driver, 'value': driver} for driver in drivers]

if __name__ == '__main__':
    app.run(debug=True)
