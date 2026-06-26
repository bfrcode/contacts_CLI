
from dataclasses import fields

from rich.console import Console
from rich.prompt import Prompt, Confirm

from models import Company

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
    new.name = Prompt.ask("Nom de l'entreprise")
    new.address = Prompt.ask("Adresse")
    new.phone = Prompt.ask("Téléphone")
    new.mail = Prompt.ask("Mail")
    new.speciality = Prompt.ask("Spécialité")
    new.note = Prompt.ask("Commentaire sur l'entreprise")
    return new