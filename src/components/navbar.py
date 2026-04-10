import dash_bootstrap_components as dbc

navbar_style = {
    'display': 'flex',
    'justifyContent': 'center',
    'alignItems': 'center',
    'backgroundColor': '#070F2B',
    'border': '#535C91',
    'borderRadius': '5px',
    'padding': '10px',
    'color': '#9290C3',
}

def get_navbar():
    navbar = dbc.Navbar(
        children=[],
        style=navbar_style,
    )
    return navbar