import typer

from database import get_connection
from models import Company, add_company, show_company
from utils import add_render, confirm_action, show_cancelled, show_error, show_success

app = typer.Typer()

@app.command()
def add():
    new = add_render(Company())
    confirm = confirm_action("Confirmer l'enregistrement ?")
    if not confirm:
        show_cancelled("Enregistrement annulé.")
    else:
        conn = get_connection()
        try:
            add_company(conn, new, new.speciality)
        except ValueError as e:
            show_error(e)
            show_cancelled("Pas d'enregistrement effectué")
        finally:
            conn.close()
        
@app.command()
def show(name: str):
    conn = get_connection()
    company = show_company(conn, name)

    if not company.name:
        show_error("Pas d'entreprise trouvée")
    else:
        show_render(company)
    
    conn.close()
    

    
    

