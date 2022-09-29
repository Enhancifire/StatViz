from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    """Renders a Treemap using the Supplied Data"""
    fig = px.treemap(
        data,
        path=[
            data["filename:lineno(function)"][:10],
            data["filename:lineno(function)"][:10],
        ],
        values=data["cumtime"][:10],
    )
    return html.Div(
        children=dcc.Graph(
            figure=fig,
        ),
    )
