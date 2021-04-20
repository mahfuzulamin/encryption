from .ciphers.wrappers.typer.hexapp import get_hex_app
from .ciphers.wrappers.typer.atbashapp import get_atbash_app
from .ciphers.wrappers.typer.caesarcipherapp import get_caesarcipher_app
from .ciphers.wrappers.typer.keyword_cipher_app import get_keyword_cipher_app
 
import typer

def encryption_app() -> typer.Typer:
    
    app = typer.Typer()

    app.add_typer(get_hex_app(), name="hex")
    app.add_typer(get_atbash_app(), name="atbash")
    app.add_typer(get_caesarcipher_app(), name="caesar")
    app.add_typer(get_keyword_cipher_app(), name="keyword")

    return app 