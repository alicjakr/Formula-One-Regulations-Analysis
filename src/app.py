from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

from components import navbar, footer

app = Dash(__name__)

# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })
#
# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# app.layout = html.Div(children=[
#     navbar.get_navbar(),
#     html.H1(children='Hello Dash'),
#
#     html.Div(children='''
#         Dash: A web application framework for your data.
#     '''),
#
#     # dcc.Graph(
#     #     id='example-graph',
#     #     figure=fig
#     # ),
#     footer.get_footer()
# ], style = {'backgroundColor': '#070F2B'})

app.layout = html.Div(
    id = 'parentDiv',
    children = [
        navbar.get_navbar(),
        html.H1(children='Hello Dash', style = {'color': 'white'}),
        footer.get_footer()
    ], style = {'backgroundColor': '#070F2B'}
)

if __name__ == '__main__':
    app.run(debug=True)
