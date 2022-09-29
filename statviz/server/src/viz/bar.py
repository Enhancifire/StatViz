from dash import Dash, html, dcc
import plotly.express as px
from .. import ids


def render(app: Dash, data) -> html.Div:
    fig = px.bar(data, x=data["filename:lineno(function)"][:10], y=data["cumtime"][:10])

    return html.Div(
        children=[
            dcc.Graph(
                id=ids.BAR_CUMTIME,
                figure=fig,
            )
        ]
    )
