from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

layout = html.Div(
    children=[
        html.H1("Python Profiler"),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
