from dash import Dash, html, dcc
import plotly.express as px
from .. import ids
import pandas as pd


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    data.sort_values(by="ct", ascending=False, inplace=True)
    fig = px.bar(
        data,
        x=data["Function Name"][:20],
        y=data["ct"][:20],
        height=600,
        labels=dict(x="Function", y="Cumulative Time"),
    )

    return html.Div(
        children=[
            dcc.Graph(
                id=ids.BAR_CUMTIME,
                figure=fig,
            )
        ]
    )
