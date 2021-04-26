
from ..interface.cipher_interface import CipherInterface
from ..util.cipher_util import is_empty
from ..error.validation_exception import ValidationException

class Hexadecimal(CipherInterface):

    def __init__(self):
        pass

    def _initialize(self, message, shiftIndex=None, key=None):
        self.message = message

    def _applyCipher(self, encode):
        pass

    def _validate_input(self):
        if is_empty(self.message) == True:
            raise ValidationException("Message cannont be empty.")

    def _encode_text(self):
        print(f"Hex encode;message is {self.message}.")
        return self.message.encode("utf-8").hex()

    def _decode_text(self):
        print(f"Hex decode; message is {self.message}.")
        return bytes.fromhex(self.message).decode('utf-8')