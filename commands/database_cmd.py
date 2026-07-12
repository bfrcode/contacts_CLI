import typer

from database import init_db
from utils import show_cancelled, show_error, show_success

app = typer.Typer()

@app.command()
def init():
    try:
        init_db()
        show_success("Base de donnée initialisée avec succès")
    except ValueError as e:
        show_error(e)