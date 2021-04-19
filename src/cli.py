from .ciphers.wrappers.typer.hexapp import get_hex_app
from .ciphers.wrappers.typer.atbashapp import get_atbash_app
 
import typer

def encryption_app() -> typer.Typer:
    
    app = typer.Typer()

    app.add_typer(get_hex_app(), name="hex")
    app.add_typer(get_atbash_app(), name="atbash")

    return app 