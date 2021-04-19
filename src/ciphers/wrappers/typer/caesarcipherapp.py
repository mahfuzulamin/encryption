import typer
 
from ...impl.caesarcipher import CaesarCipher

def get_caesarcipher_app():
    
    app = typer.Typer()

    @app.command("encode")
    def encode(message):
        """Encodes a message using the Caesar Cipher cipher"""
        caesarCipher = CaesarCipher(message)
        encodedMsg = caesarCipher.encode()
        print(f"Caesar Cipher encoded message is {encodedMsg}.")

    @app.command("decode")
    def decode(message):
        """Decodes a message using the Caesar Cipher cipher"""
        caesarCipher = CaesarCipher(message)
        decodedMsg = caesarCipher.decode()
        print(f"Caesar Cipher decoded message is {decodedMsg}.")


    return app