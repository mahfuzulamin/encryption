import typer
 
from ...impl.atbash import AtBash

def get_atbash_app():
    """AtBash Cipher Typer wrapper implementation."""

    app = typer.Typer()
    atBash = AtBash()

    @app.command("encode")
    def encode(message):
        """Encodes a message using the AtBash cipher
        
        Parameters
        ----------
        message : str
            Message to be encoded
        """

        encodedMsg = atBash.encode(message)
        print(f"AtBash encoded message is {encodedMsg}.")

    @app.command("decode")
    def decode(message):
        """Decodes a message using the AtBash cipher
        
        Parameters
        ----------
        message : str
            Message to be decoded
        """

        decodedMsg = atBash.decode(message)
        print(f"AtBash decoded message is {decodedMsg}.")


    return app