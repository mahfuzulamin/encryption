import typer
 
from ...impl.keyword_cipher import KeywordCipher

def get_keyword_cipher_app():
    
    app = typer.Typer()

    @app.command("encode")
    def encode(keyword: str, message: str):
        """Encodes a message using the Keyword Cipher cipher"""
        keywordCipher = KeywordCipher(message, keyword)
        encodedMsg = keywordCipher.encode()
        print(f"Caesar Cipher encoded message is {encodedMsg}.")

    @app.command("decode")
    def decode(keyword: str, message: str):
        """Decodes a message using the Keyword Cipher cipher"""
        keywordCipher = KeywordCipher(message, keyword)
        decodedMsg = keywordCipher.decode()
        print(f"Caesar Cipher decoded message is {decodedMsg}.")

    return app