import typer
 
from ...impl.caesarcipher import CaesarCipher

def get_caesarcipher_app():
    
    app = typer.Typer()

    @app.command("encode")
    def encode(shift_index: int, message: str):
        """Encodes a message using the Caesar Cipher cipher"""
        caesarCipher = CaesarCipher(message, shift_index)
        encodedMsg = caesarCipher.encode()
        print(f"Caesar Cipher encoded message is {encodedMsg}.")

    @app.command("decode")
    def decode(shift_index: int, message: str):
        """Decodes a message using the Caesar Cipher cipher"""
        caesarCipher = CaesarCipher(message, shift_index)
        decodedMsg = caesarCipher.decode()
        print(f"Caesar Cipher decoded message is {decodedMsg}.")


    return app