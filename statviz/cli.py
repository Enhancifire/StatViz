import typer
from .server.serv import main as server
from .converter import stats_to_df

app = typer.Typer()


@app.command()
def main(file: str):
    """Takes path to .prof file and runs the server"""
    df = stats_to_df(file)
    server(df)


if __name__ == "__main__":
    app()