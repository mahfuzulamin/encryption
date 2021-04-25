import typer
 
from ...impl.caesarcipher import CaesarCipher

def get_caesarcipher_app():
    
    app = typer.Typer()
    caesarCipher = CaesarCipher()

    @app.command("encode")
    def encode(shift_index: int, message: str):
        """Encodes a message using the Caesar Cipher cipher"""
        encodedMsg = caesarCipher.encode(message, shift_index)
        print(f"Caesar Cipher encoded message is {encodedMsg}.")

    @app.command("decode")
    def decode(shift_index: int, message: str):
        """Decodes a message using the Caesar Cipher cipher"""
        decodedMsg = caesarCipher.decode(message, shift_index)
        print(f"Caesar Cipher decoded message is {decodedMsg}.")


    return app