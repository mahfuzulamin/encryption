
from ..interface.cipher_interface import CipherInterface

class Hexadecimal(CipherInterface):
    def __init__(self, message):
        self.message = message

    def _encode_text(self):
        print(f"Hex encode;message is {self.message}.")
        return self.message.encode("utf-8").hex()
        # return "74657374"

    def _decode_text(self):
        print(f"Hex decode; message is {self.message}.")
        return bytes.fromhex(self.message).decode('utf-8')