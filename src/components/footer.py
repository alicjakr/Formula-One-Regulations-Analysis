from dash import html

def get_footer():
    footer = html.Footer(
        html.Div(children='This project uses the FastF1 library'),
        className = 'app-footer'
    )
    return footer