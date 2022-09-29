from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    """Renders a Sun Burst Chart using the Supplied Data"""
    fig = px.pie(
        data,
        names=data["filename:lineno(function)"][:10],
        values=data["cumtime"][:10],
    )
    # fig = px.sunburst(
    #     data,
    #     names=data["filename:lineno(function)"][:10],
    #     values=data["cumtime"][:10],
    # )
    return html.Div(
        children=dcc.Graph(
            figure=fig,
        ),
    )
