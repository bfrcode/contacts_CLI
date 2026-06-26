import typer

from rich import print
from rich.prompt import Confirm

from utils import add_render, confirm_action, show_cancelled,show_error, show_success
from models import Company, add_company

app = typer.Typer()

@app.command()
def add():
    new = add_render(Company())
    confirm = confirm_action("Confirmer l'enregistrement ?")
    if not confirm:
        show_cancelled("Enregistrement annulé.")
    else:
        try:
            add_company(conn, new, new.speciality)
        except ValueError as e:
            show_error(e)
            show_cancelled("Pas d'enregistrement effectué")
        
    
    

