
from dataclasses import fields

from rich.console import Console
from rich.prompt import Prompt, Confirm

from models import Company

FIELD_LABELS = {
    "name": "Nom de l'entreprise",
    "address": "Adresse",
    "phone": "Téléphone",
    "mail": "E-mail",
    "speciality": "Spécialité",
    "note": "Note",
}

# Initialise la console
console = Console()

# Affichage divers
def confirm_action(action:str) -> bool:
    """Demande une confirmation d'action à l'utilisateur"""
    return Confirm.ask(action)

def show_cancelled(message:str) -> None:
    """Affiche une confirmation d'action abandonnée"""
    console.print(f"[red]Cancelled : [/red] {message}")

def show_error(e: Exception) -> None:
    """Affiche une erreur"""
    console.print(f"[red]Erreur :[/red] {e}")

def show_success(message:str) -> None:
    """Affiche une confirmation d'action réussie"""
    console.print(f"[green]Success : [/green] {message}")

# Affichage liés aux entreprises
def add_render(new: Company) -> Company:
    """Affichage de la fonction add_company"""
    for f in fields(new):
        if f.name == "id":
            continue
        label = FIELD_LABELS.get(f.name, f.name)
        current_value = getattr(new, f.name)
        new_value = Prompt.ask(label, default=str(current_value) if current_value is not None else "")
        setattr(new, f.name, new_value or None)
    return new

def show_render(company: Company) -> None:
    """Affichage de la fonction show_company"""
    