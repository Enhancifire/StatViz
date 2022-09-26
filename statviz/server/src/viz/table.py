import plotly.graph_objects as go
from dash import Dash, html, dcc
from .. import ids


def render(app: Dash, data) -> html.Div:

    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=list(data.columns),
                    fill_color="paleturquoise",
                    align="left",
                ),
                cells=dict(
                    values=[
                        data.ncalls,
                        data.tottime,
                        data.percall,
                        data.cumtime,
                        data.percall,
                        data["filename:lineno(function)"],
                    ],
                    fill_color="lavender",
                    align="left",
                ),
            )
        ],
    )

    return html.Div(
        id=ids.INFO_GRAPH,
        children=[
            dcc.Graph(
                figure=fig,
            )
        ],
    )
