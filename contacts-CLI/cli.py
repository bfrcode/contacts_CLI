import typer

from commands import company_cmd, database_cmd

app = typer.Typer()
app.add_typer(company_cmd.app, name="company")
app.add_typer(database_cmd.app, name="database")

if __name__ == "__main__":
    app()