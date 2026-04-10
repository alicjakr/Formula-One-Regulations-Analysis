from dash import html

#CSS for the footer
footer_style = {
    'textAlign': 'center',
    'padding': '10px',
    'margin': '10px',
    'backgroundColor': '#070F2B',
    'border': '#535C91',
    'borderRadius': '5px',
    'color': '#9290C3',
}

def get_footer():
    footer = html.Footer(
        html.Div(children='This project uses the FastF1 library'),
        style=footer_style,
    )
    return footer