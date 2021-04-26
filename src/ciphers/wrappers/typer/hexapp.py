import typer
 
from ...impl.hexadecimal import Hexadecimal

def get_hex_app():
    """Hexadecimal Cipher Typer wrapper implementation."""

    app = typer.Typer()
    hex = Hexadecimal()

    @app.command("encode")
    def encode(message):
        """Encodes a message using the hex cipher

        Parameters
        ----------
        message : str
            Message to be encoded
        """

        encodedMsg = hex.encode(message)
        print(f"Hex encoded message is {encodedMsg}")

    @app.command("decode")
    def decode(message):
        """Decodes a message using the hex cipher
        
        Parameters
        ----------
        message : str
            Message to be decoded
        """

        decodedMsg = hex.decode(message)
        print(f"Hex decoded message is {decodedMsg}")


    return app