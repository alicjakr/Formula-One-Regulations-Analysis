from dash import Dash, html, callback, Output, Input, ctx, dcc
from dash.exceptions import PreventUpdate

from components import navbar, footer, session_selector, driver_selector, GP_selector, telemetry_chart, track_map, chart_selector
from data import loader, telemetry
import dash_bootstrap_components as dbc

BUTTON_CHANNEL_MAP = {
    'btn-speed': 'Speed',
    'btn-rpm': 'RPM',
    'btn-gear-shifts': 'nGear',
    'btn-throttle': 'Throttle',
    'btn-brake': 'Brake',
}

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
                dbc.Col(
                    dcc.Graph(id='main-graph'),
                width=8),
                dbc.Col([
                    session_selector.get_display_type(),
                    html.Br(),
                    html.Div(session_selector.get_display_mode(), id='display-mode-cont', style={'display': 'none'}),
                    html.Br(),
                    html.Div(session_selector.get_year(), id='year-cont', style={'display': 'none'}),
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
def update_drivers(gp, session_type):
    print(f"update")
    if not gp or not session_type:
        return []
    drivers = loader.get_common_drivers(gp, session_type)
    return [{'label': driver, 'value': driver} for driver in drivers]

@callback(
    Output('btn-speed', 'className'),
    Output('btn-rpm', 'className'),
    Output('btn-gear-shifts', 'className'),
    Output('btn-throttle', 'className'),
    Output('btn-brake', 'className'),
    Input('btn-speed', 'n_clicks'),
    Input('btn-rpm', 'n_clicks'),
    Input('btn-gear-shifts', 'n_clicks'),
    Input('btn-throttle', 'n_clicks'),
    Input('btn-brake', 'n_clicks'),
    prevent_initial_call=True,
)
def update_chart(b1, b2, b3, b4, b5):
    active = 'btn-active'
    inactive = 'btn'
    triggered = ctx.triggered_id
    return [
        active if triggered == btn_id else inactive for btn_id in BUTTON_CHANNEL_MAP.keys()
    ]

@callback(
    Output('year-cont', 'style'),
    Input('display-mode', 'value'),
    Input('display-type', 'value'),
)
def update_year(display_mode, display_type):
    if display_type == 'circuit':
        return {'display': 'block'}
    else:
        if display_mode == 'together':
            return {'display': 'none'}
        else:
            return {'display': 'block'}

@callback(
    Output('display-mode-cont', 'style'),
    Input('display-type', 'value'),
)
def update_display_mode(display_type):
    if display_type == 'circuit':
        return {'display': 'none'}
    else:
        return {'display': 'block'}

@callback(
    Output('main-graph', 'figure'),
    Input('btn-speed', 'n_clicks'),
    Input('btn-rpm', 'n_clicks'),
    Input('btn-gear-shifts', 'n_clicks'),
    Input('btn-throttle', 'n_clicks'),
    Input('btn-brake', 'n_clicks'),
    Input('gp-selector', 'value'),
    Input('driver-selector', 'value'),
    Input('session-type', 'value'),
    Input('display-type', 'value'),
    Input('year', 'value'),
    prevent_initial_call=True,
)
def update_graph(b1, b2, b3, b4, b5, gp, driver, session_type, display_type, year):
    print(f"triggered: {ctx.triggered_id}")
    print(f"gp: {gp}, driver: {driver}, session_type: {session_type}, display_type: {display_type}, year: {year}")

    if not gp or not driver or not session_type:
        print("PreventUpdate — missing inputs")
        raise PreventUpdate()

    triggered = ctx.triggered_id
    if triggered not in BUTTON_CHANNEL_MAP:
        print("PreventUpdate — trigger not a button")
        raise PreventUpdate()

    channel = BUTTON_CHANNEL_MAP[triggered]
    print(f"channel: {channel}")
    session = loader.load_session(int(year), gp, session_type)
    print(f"channel: {channel}")
    data = telemetry.get_lap_telemetry(session, driver)
    print(f"data keys: {data.keys()}")

    if display_type == 'circuit':
        print(f"figure created")
        return track_map.plot_circuit(data, channel)
    # else:
    #     return telemetry_chart.plot_graph(data, chart_type)


if __name__ == '__main__':
    app.run(debug=True)