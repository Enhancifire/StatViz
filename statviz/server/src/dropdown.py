from typing import List
from dash import dcc, Dash, html
from . import ids


def render(
    app: Dash,
    options: List,
) -> html.Div:
    return html.Div(
        children=[
            dcc.Dropdown(
                id=ids.SELECTOR_DROPDOWN,
                options=[{"label": graph, "value": graph} for graph in options],
                searchable=False,
                value=options[0],
            )
        ],
    )
