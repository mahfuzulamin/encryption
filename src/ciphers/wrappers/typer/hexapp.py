import typer
 
from ...impl.hexadecimal import Hexadecimal
# from ...interface.cipher_interface import CipherInterface

def get_hex_app():
    
    app = typer.Typer()
    hex = Hexadecimal()

    @app.command("encode")
    def encode(message):
        """Encodes a message using the hex cipher"""
        encodedMsg = hex.encode(message)
        print(f"Hex encoded message is {encodedMsg}.")

    @app.command("decode")
    def decode(message):
        """Decodes a message using the hex cipher"""
        decodedMsg = hex.decode(message)
        print(f"Hex decoded message is {decodedMsg}.")


    return app