import typer
 
from ...impl.vigenere_cipher import VigenereCipher

def get_vigenere_cipher_app():
    
    app = typer.Typer()

    @app.command("encode")
    def encode(keyword: str, message: str):
        """Encodes a message using the Vigenere Cipher cipher"""
        vigenereCipher = VigenereCipher(message, keyword)
        encodedMsg = vigenereCipher.encode()
        print(f"Vigenere Cipher encoded message is {encodedMsg}.")

    @app.command("decode")
    def decode(keyword: str, message: str):
        """Decodes a message using the Vigenere Cipher cipher"""
        vigenereCipher = VigenereCipher(message, keyword)
        decodedMsg = vigenereCipher.decode()
        print(f"Vigenere Cipher decoded message is {decodedMsg}.")

    return app