import plotly.graph_objects as go
from fastf1 import plotting

CHANNEL_CONFIG = {
    'Speed': {'column': 'Speed', 'colorscale': 'plasma', 'range': [0, 360], 'label': 'Speed [km/h]'},
    'RPM': {'column': 'RPM', 'colorscale': 'RdYlGn', 'range': [0, 14000], 'label': 'RPM'},
    'nGear': {'column': 'nGear', 'colorscale': 'viridis', 'range': [1, 8], 'label': 'Gear'},
    'Throttle': {'column': 'Throttle', 'colorscale': 'cividis', 'range': [0, 100], 'label': 'Throttle [%]'},
    'Brake': {'column': 'Brake', 'colorscale': [[0, '#ff4444'], [1, '#44ff44']], 'range': [0, 1], 'label': 'Brake'},
}


def plot_graph(data: dict, channel: str):
    config = CHANNEL_CONFIG[channel]
    tel = data['telemetry']
    lap = data['lap']

    style = plotting.get_driver_style(identifier=lap['Driver'], style=['color', 'linestyle'], session=data['session'])

    tel = tel.dropna(subset=['X', 'Y', config['column']])
    tel['X'] = tel['X'].interpolate()
    tel['Y'] = tel['Y'].interpolate()
    fig = go.Figure(data=[
        go.Scatter(
            x=tel['Distance'],
            y=tel[config['column']],
            mode='lines',
            line=dict(
                color=style['color'],
                dash='dash' if style.get('linestyle') == '--' else 'solid'
            ),
            name=lap['Driver']
        )
    ])

    fig.update_layout(
        title=f"{lap['Driver']} - {config['label']}",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        xaxis=dict(title='Distance [m]'),
        yaxis=dict(title=config['label']+' [km/h]', range=config['range']),
        margin=dict(l=0, r=0, b=0, t=0)
    )

    return fig


def plot_together(data: list, channel: str):
    config = CHANNEL_CONFIG[channel]
    fig = go.Figure()

    for entry, year in zip(data, [2025, 2026]):
        tel = entry['telemetry']
        lap = entry['lap']
        fig.add_trace(go.Scatter(
            x=tel['Distance'],
            y=tel[config['column']],
            mode='lines',
            name=f"{lap['Driver']} {year}",
        ))

    fig.update_layout(
        title=dict(text=f"{lap['Driver']} - {config['label']}", font=dict(family="Arial", size=24), x=0.5, xanchor="center", yanchor="top"),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        xaxis=dict(title='Distance [m]'),
        yaxis=dict(title=config['label'], range=config['range']),
        margin=dict(l=0, r=0, b=0, t=50)
    )

    return fig