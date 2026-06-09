import typer
from rich import print
from db.db import init_db

app = typer.Typer()

@app.command()
def init():
    init_db()
    print("green]✓[/green]Base de donnée initialisée avec succès")

if __name__ == "__main__":
    app()