import typer
from .server import main

app = typer.Typer()

@app.command()
def main(file: str):
    typer.echo(f"Read {file}")

if __name__ == "__main__":
    app()