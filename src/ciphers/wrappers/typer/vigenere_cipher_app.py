import typer
 
from ...impl.vigenere_cipher import VigenereCipher

def get_vigenere_cipher_app():
    """Vigenere Cipher Typer wrapper implementation.

    Returns
    -------
    Typer
    """

    app = typer.Typer()
    vigenereCipher = VigenereCipher()

    @app.command("encode")
    def encode(keyword: str, message: str):
        """Encodes a message using the Vigenere Cipher cipher

        Parameters
        ----------
        keyword : str, optional
            Keyword for cipher   
        message : str
            Message to be encoded
        """

        encodedMsg = vigenereCipher.encode(message, None, keyword)
        print(f"Vigenere Cipher encoded message is {encodedMsg}")

    @app.command("decode")
    def decode(keyword: str, message: str):
        """Decodes a message using the Vigenere Cipher cipher
        
        Parameters
        ----------
        keyword : str, optional
            Keyword for cipher   
        message : str
            Message to be decoded
        """

        decodedMsg = vigenereCipher.decode(message, None, keyword)
        print(f"Vigenere Cipher decoded message is {decodedMsg}")

    return app