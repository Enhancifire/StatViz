# 3rd-Party Components
from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP
import plotly.express as px
import pandas as pd

# Core Components
from .src import layout


def main(data: pd.DataFrame):
    app = Dash(
        __name__,
        external_stylesheets=[BOOTSTRAP],
    )
    app.title = "StatViz"

    app.layout = layout.create_components(app, data)

    # Running the server
    app.run_server(debug=True)
