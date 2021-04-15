from .ciphers.wrappers.typer.hexapp import get_hex_app
 
import typer

def encryption_app() -> typer.Typer:
    
    app = typer.Typer()

    app.add_typer(get_hex_app(), name="hex")

    return app 