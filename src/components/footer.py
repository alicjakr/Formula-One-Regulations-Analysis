from dash import html

def get_footer():
    return html.Footer(
        html.Div(children='This project uses the FastF1 library'),
        className='app-footer'
    )