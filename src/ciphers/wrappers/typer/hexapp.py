import typer
 
from ...impl.hexadecimal import Hexadecimal
# from ...interface.cipher_interface import CipherInterface

def get_hex_app():
    
    app = typer.Typer()

    @app.command("encode")
    def encode(message):
        """Encodes a message using the hex cipher"""
        hex = Hexadecimal(message)
        encodedMsg = hex.encode()
        print(f"Hex encoded message is {encodedMsg}.")

    @app.command("decode")
    def decode(message):
        """Decodes a message using the hex cipher"""
        hex = Hexadecimal(message)
        decodedMsg = hex.decode()
        print(f"Hex decoded message is {decodedMsg}.")


    return app