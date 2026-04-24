import plotly.graph_objects as go

CHANNEL_CONFIG = {
    'Speed': {'column': 'Speed', 'colorscale': 'plasma', 'range': [0, 360], 'label': 'Speed'},
    'RPM': {'column': 'RPM', 'colorscale': 'RdYlGn', 'range': [0, 14000], 'label': 'RPM'},
    'nGear': {'column': 'nGear', 'colorscale': 'viridis', 'range': [1, 8], 'label': 'Gear'},
    'Throttle': {'column': 'Throttle', 'colorscale': 'cividis', 'range': [0, 100], 'label': 'Throttle'},
    'Brake': {'column': 'Brake', 'colorscale': ['#44ff44', '#ff4444'], 'range': [0, 1], 'label': 'Brake', 'binary': True},
}


def plot_circuit(data: dict, channel: str):
    config = CHANNEL_CONFIG[channel]
    tel = data['telemetry']
    lap = data['lap']

    fig = go.Figure()

    tel = tel.dropna(subset=['X', 'Y', config['column']])
    tel['X'] = tel['X'].interpolate()
    tel['Y'] = tel['Y'].interpolate()

    if config.get('binary'):
        for value, colour, label in zip([0, 1], config['colorscale'], ['Not braking', 'Braking']):
            mask = tel[config['column']] == value
            fig.add_trace(go.Scattergl(
                x=tel['X'][mask],
                y=tel['Y'][mask],
                mode='markers',
                name=label,
                marker=dict(
                    size=4,
                    color=colour,
                )
            ))
    else:
        fig.add_trace(go.Scattergl(
            x=tel['X'],
            y=tel['Y'],
            mode='markers',
            marker=dict(
                size=4,
                color=tel[config['column']],
                colorscale=config['colorscale'],
                cmin=config['range'][0],
                cmax=config['range'][1],
                showscale=True,
                colorbar=dict(title=config['label'])
            )
        ))

    fig.update_layout(
        title=f"{lap['Driver']} - {config['label']}",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        xaxis=dict(visible=False),
        yaxis=dict(visible=False, scaleanchor='x'),
        margin=dict(l=0, r=0, b=0, t=0)
    )

    return fig