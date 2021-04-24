from ..interface.cipher_interface import CipherInterface
from ..error.validation_exception import ValidationException
from ..util.cipher_util import is_empty

class AtBash(CipherInterface):
    lowarCaseAsciiTotal = ord('z') + ord('a')
    upperCaseAsciiTotal = ord('Z') + ord('A')

    def __init__(self, message):
        self.message = message

    def _validate_input(self):
        if is_empty(self.message) == True:
            raise ValidationException("Message cannont be empty.")

    def applyCipher(self):
        cipherMsg = ''
        for charStr in self.message:
            if charStr.isalpha():
                if charStr.isupper():
                    cipherMsg += chr(self.upperCaseAsciiTotal - ord(charStr))
                else:
                    cipherMsg += chr(self.lowarCaseAsciiTotal - ord(charStr))
        
        return cipherMsg

    def _encode_text(self):
        print(f"AtBash encode; received message is {self.message}.")
        return self.applyCipher()

    def _decode_text(self):
        print(f"AtBash decode; received message is {self.message}.")
        return self.applyCipher()