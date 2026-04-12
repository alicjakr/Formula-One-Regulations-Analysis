import plotly.graph_objects as go

CHANNEL_CONFIG = {
    'Speed': {'column': 'Speed', 'colorscale': 'plasma', 'range': [0, 350], 'label': 'Speed'},
    'RPM': {'column': 'RPM', 'colorscale': 'RdYlGn', 'range': [0, 14000], 'label': 'RPM'},
    'nGear': {'column': 'nGear', 'colorscale': 'viridis', 'range': [1, 8], 'label': 'Gear'},
    'Throttle': {'column': 'Throttle', 'colorscale': 'cividis', 'range': [0, 100], 'label': 'Throttle'},
    'Brake': {'column': 'Brake', 'colorscale': [[0, '#ff4444'], [1, '#44ff44']], 'range': [0, 1], 'label': 'Brake'},
}


def plot_graph(data: dict, channel: str):
    config = CHANNEL_CONFIG[channel]
    segments = data['segments']
    tel = data['telemetry']
    lap = data['lap']
    values = data['telemetry'][channel].to_numpy().astype(float)

    x = tel['X'].to_numpy()
    y = tel['Y'].to_numpy()

    fig = go.Figure()

    for i in range(len(segments)):
        fig.add_trace(go.Scatter(
            x=[segments[i][0][0], segments[i][1][0]],
            y=[segments[i][0][1], segments[i][1][1]],
            mode='lines',
            line=dict(
                color=values[i],
                colorscale=config['colorscale'],
                width=4,
                cmin=config['range'][0],
                cmax=config['range'][1],
            ),
            showlegend=False,
            hoverinfo='skip',
        ))

    fig.update_layout(
        title=f"{lap['Driver']} - {config['label']} {data['event_name']}",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        margin=dict(l=0, r=0, b=0, t=0),
        coloraxis=dict(
            colorscale=config['colorscale'],
            cmin=config['range'][0],
            cmax=config['range'][1],
            colorbar=dict(title=config['label']),
        ),
    )

    return fig
