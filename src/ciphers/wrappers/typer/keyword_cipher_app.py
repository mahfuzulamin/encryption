import typer
 
from ...impl.keyword_cipher import KeywordCipher

def get_keyword_cipher_app():
    """Keyword Cipher Typer wrapper implementation."""

    app = typer.Typer()
    keywordCipher = KeywordCipher()

    @app.command("encode")
    def encode(keyword: str, message: str):
        """Encodes a message using the Keyword Cipher cipher

        Parameters
        ----------
        keyword : str, optional
            Keyword for cipher   
        message : str
            Message to be encoded
        """

        keywordCipher = KeywordCipher()
        encodedMsg = keywordCipher.encode(message, None, keyword)
        print(f"Caesar Cipher encoded message is {encodedMsg}")

    @app.command("decode")
    def decode(keyword: str, message: str):
        """Decodes a message using the Keyword Cipher cipher

        Parameters
        ----------
        keyword : str, optional
            Keyword for cipher   
        message : str
            Message to be decoded
        """

        decodedMsg = keywordCipher.decode(message, None, keyword)
        print(f"Caesar Cipher decoded message is {decodedMsg}")

    return app