from dash import Dash, html, dcc
import plotly.express as px
from .. import ids


def render(app: Dash, data) -> html.Div:
    fig = px.bar(data, x="filename:lineno(function)", y="cumtime")

    return html.Div(
        children=[
            dcc.Graph(
                id=ids.BAR_CUMTIME,
                figure=fig,
            )
        ]
    )
