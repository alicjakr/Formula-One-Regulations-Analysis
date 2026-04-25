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
                dbc.Col([
                    html.Div([
                        dcc.Graph(id='main-graph', style={'display': 'none', 'height': '450px'}),
                        html.Div(
                            html.Img(id='logo', src='assets/F1.png', style={
                                'maxWidth': '60%',
                                'maxHeight': '60%',
                            }),
                            id='logo-container',
                            style={
                                'position': 'absolute',
                                'top': '0',
                                'left': '0',
                                'width': '100%',
                                'height': '100%',
                                'display': 'flex',
                                'justifyContent': 'center',
                                'alignItems': 'center',
                            }
                        ),
                        html.Div(id='error-message', style={'display': 'none'})
                    ], style={
                        'position': 'relative',
                        'width': '100%',
                        'height': '450px',
                    }),
                ], width=8),
                dbc.Col([
                    session_selector.get_display_type(),
                    html.Br(),
                    html.Div(session_selector.get_display_mode(), id='display-mode-cont', style={'display': 'none'}),
                    html.Br(),
                    html.Div(session_selector.get_year(), id='year-cont', style={'display': 'none'}),
                ], width=2),
                dcc.Store(id='active-channel', data='Speed'),
                dcc.Store(id='graph-ready', data=False),
                dcc.Store(id='error-vis', data=None),
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
    Output('active-channel', 'data'),
    Input('btn-speed', 'n_clicks'),
    Input('btn-rpm', 'n_clicks'),
    Input('btn-gear-shifts', 'n_clicks'),
    Input('btn-throttle', 'n_clicks'),
    Input('btn-brake', 'n_clicks'),
    prevent_initial_call=True,
)
def store_channel(b1, b2, b3, b4, b5):
    return BUTTON_CHANNEL_MAP[ctx.triggered_id]

@callback(
    Output('main-graph', 'style'),
    Input('graph-ready', 'data'),
)
def update_main_graph(graph_ready):
    if graph_ready:
        return {'display': 'block'}
    else:
        return {'display': 'none'}

@callback(
    Output('logo-container', 'style'),
    Input('graph-ready', 'data'),
)
def update_logo(graph_ready):
    base = {
        'position': 'absolute',
        'top': '0', 'left': '0',
        'width': '100%', 'height': '100%',
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center',
    }
    if graph_ready:
        return {**base, 'display': 'none'}
    return base

@callback(
    Output('error-message', 'style'),
    Output('error-message', 'children'),
    Input('error-vis', 'data'),
)
def update_main_graph(error_vis):
    if error_vis:
        return {'display': 'block'}, error_vis
    else:
        return {'display': 'none'}, ''

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
    Output('graph-ready', 'data'),
    Output('error-vis', 'data'),
    Input('active-channel', 'data'),
    Input('gp-selector', 'value'),
    Input('driver-selector', 'value'),
    Input('session-type', 'value'),
    Input('display-type', 'value'),
    Input('display-mode', 'value'),
    Input('year', 'value'),
    prevent_initial_call=True,
)
def update_graph(channel, gp, driver, session_type, display_type, display_mode, year):
    if not channel or not gp or not driver or not session_type:
        raise PreventUpdate()

    if display_type == 'plot' and display_mode == 'together':
        sessions = [
            loader.load_session(2025, gp, session_type),
            loader.load_session(2026, gp, session_type),
        ]
        data = []
        for session in sessions:
            if telemetry.get_lap_telemetry(session, driver):
                data.append(telemetry.get_lap_telemetry(session, driver))
            else:
                return None, False, 'There is no lap telemetry for this session'
    else:
        if not year:
            raise PreventUpdate()
        session = loader.load_session(int(year), gp, session_type)
        data = telemetry.get_lap_telemetry(session, driver)
        if data is None:
            return None, False, 'There is no lap telemetry for this session'

    if display_type == 'circuit':
        return track_map.plot_circuit(data, channel), True, None
    else:
        if display_mode == 'together':
            return telemetry_chart.plot_together(data, channel), True, None
        else:
            return telemetry_chart.plot_graph(data, channel), True, None


if __name__ == '__main__':
    app.run(debug=True)