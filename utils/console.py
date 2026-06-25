from rich.console import Console
from rich.prompt import Prompt, Confirm

from models import Company

# Affichage liés aux entreprises
def add_render(new: Company) -> Company:
    """Affichage de la fonction add_company"""

    new.name = Prompt.ask("Nom de l'entreprise")
    new.address = Prompt.ask("Adresse")
    new.phone = Prompt.ask("Téléphone")
    new.mail = Prompt.ask("Mail")
    new.speciality = Prompt.ask("Spécialité")
    new.note = Prompt.ask("Commentaire sur l'entreprise")
    confirm = Confirm.ask("Enregistrer l'entreprise ?")
    
    console = Console()

    if confirm != True:
        console.print("[red]Ajout de l'entreprise abandonné[/red]")
        return new
    else:
        console.print("[green]Entreprise ajouté avec succès ![/green]")
        return new
