import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

from components import navbar, footer, session_selector, driver_selector, GP_selector

app = Dash(__name__)

app.layout = html.Div(
    id = 'parentDiv',
    children = [
        navbar.get_navbar(),

        html.H1(children='Hello Dash', style = {'color': 'white'}),

        session_selector.get_display_mode(),
        session_selector.get_display_type(),
        session_selector.get_session_type(),

        GP_selector.get_gp_selector(),
        driver_selector.get_driver_selector(),

        footer.get_footer()
    ], style = {'backgroundColor': '#070F2B'}
)

if __name__ == '__main__':
    app.run(debug=True)
