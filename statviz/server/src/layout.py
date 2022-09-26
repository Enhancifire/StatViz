from dash import Dash, html, dcc
from . import ids
from . import dropdown
from .viz import bar, table


def create_components(app: Dash, data):

    return html.Div(
        className="app-div",
        children=[
            html.H1("Python Profiler"),
            html.Hr(),
            html.Div(
                id=ids.GRAPH_DIV,
                children=[
                    dropdown.render(app, ["Bar", "SunBurst", "TreeMap"]),
                    bar.render(app, data),
                ],
            ),
            html.Div(table.render(app, data)),
        ],
    )
