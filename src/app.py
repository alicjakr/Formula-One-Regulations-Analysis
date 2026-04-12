import dbc
from dash import Dash, html, callback, Output, Input
from components import navbar, footer, session_selector, driver_selector, GP_selector, telemetry_chart, track_map, chart_selector
from data import loader, telemetry
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div(
    id='parentDiv',
    children=[
        navbar.get_navbar(),
        html.Div(children=[
            dbc.Row([
                dbc.Col([
                    session_selector.get_session_type(),
                    html.Br(),
                    GP_selector.get_gp_selector(loader.get_common_events()),
                    html.Br(),
                    driver_selector.get_driver_selector(),
                    html.Br(),
                    chart_selector.get_chart_type(),
                ], width=2),
                dbc.Col([
                    #graph
                ], width=8),
                dbc.Col([
                    session_selector.get_display_mode(),
                    html.Br(),
                    session_selector.get_display_type(),
                ], width=2),
            ], justify='between'),
        ], style={'flex': '1', 'padding': '10px'}),
        footer.get_footer()
    ], style={'backgroundColor': '#070F2B', 'minHeight': '100vh', 'margin': '0', 'padding': '0', 'display': 'flex',
              'flexDirection': 'column'}
)


@callback(
    Output('driver-selector', 'options'),
    Input('gp-selector', 'value'),
    Input('session-type', 'value'),
)
@callback(
    Output('graph-type', 'circuit'),
    Input('gp-selector', 'value'),
    Input('driver-selector', 'value'),
    Input('session-type', 'value'),
)
def update_drivers(gp, session_type):
    print(f"update")
    if not gp or not session_type:
        return []
    drivers = loader.get_common_drivers(gp, session_type)
    return [{'label': driver, 'value': driver} for driver in drivers]


# @callback(
#     Output('main-graph', 'figure'),
#     Input('gp-selector', 'value'),
#     Input('driver-selector', 'value'),
#     Input('session-type', 'value'),
#     Input('display-mode', 'value'),
#     Input('display-type', 'value'),
#     Input('chart-type', 'value'),
# )
# def update_graph(gp, driver, session_type, display_mode, display_type, chart_type):
#     if not gp or not driver or not session_type:
#         return {}
#
#     session = loader.load_session(gp, session_type)
#     data = telemetry.get_lap_telemetry(driver, session)
#
#     if display_type == 'circuit':
#         return track_map.plot_circuit(data, chart_type)
#     else:
#         return telemetry_chart.plot_graph(data, chart_type)


if __name__ == '__main__':
    app.run(debug=True)
