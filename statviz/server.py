from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from .converter import stats_to_df

def main():
    app = Dash(__name__)

    layout = html.Div(
        children=[
            html.H1("Python Profiler"),
        ],
    )
    return app

if __name__ == "__main__":
    main().run_server(debug=True)
