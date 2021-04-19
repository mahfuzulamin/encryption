import typer
 
from ...impl.atbash import AtBash

def get_atbash_app():
    
    app = typer.Typer()

    @app.command("encode")
    def encode(message):
        """Encodes a message using the AtBash cipher"""
        atBash = AtBash(message)
        encodedMsg = atBash.encode()
        print(f"AtBash encoded message is {encodedMsg}.")

    @app.command("decode")
    def decode(message):
        """Decodes a message using the AtBash cipher"""
        atBash = AtBash(message)
        decodedMsg = atBash.decode()
        print(f"AtBash decoded message is {decodedMsg}.")


    return app