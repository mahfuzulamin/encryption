from .ciphers.wrappers.typer.hex_app import get_hex_app
from .ciphers.wrappers.typer.atbash_app import get_atbash_app
from .ciphers.wrappers.typer.caesarcipher_app import get_caesarcipher_app
from .ciphers.wrappers.typer.keyword_cipher_app import get_keyword_cipher_app
from .ciphers.wrappers.typer.vigenere_cipher_app import get_vigenere_cipher_app
 
import typer

def encryption_app() -> typer.Typer:
    """Facade design pattern implementation of cypher typer wrappers.
    
    Returns
    -------
    Typer
    """

    app = typer.Typer()

    app.add_typer(get_hex_app(), name="hex")
    app.add_typer(get_atbash_app(), name="atbash")
    app.add_typer(get_caesarcipher_app(), name="caesar")
    app.add_typer(get_keyword_cipher_app(), name="keyword")
    app.add_typer(get_vigenere_cipher_app(), name="vigenere")

    return app 