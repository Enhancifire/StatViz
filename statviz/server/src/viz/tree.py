from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    """Renders a Treemap using the Supplied Data"""
    fig = px.treemap(
        data,
        path=[
            data["Function Name"][:10],
        ],
        values=data["tt"][:10],
    )
    return html.Div(
        children=dcc.Graph(
            figure=fig,
        ),
    )
