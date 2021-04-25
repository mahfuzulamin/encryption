from ..interface.cipher_interface import CipherInterface
from ..util.cipher_util import is_empty
from ..error.validation_exception import ValidationException

class CaesarCipher(CipherInterface):
    lowarCaseAsciiValueStart = ord("a")
    upperCaseAsciiValueStart = ord("A")

    def __init__(self):
        pass

    def _initialize(self, message, shiftIndex=None, key=None):
        self.message = message
        self.shiftIndex = shiftIndex

    def _validate_input(self):
        if is_empty(self.message) == True:
            raise ValidationException("Message cannont be empty.")
    
    def _applyCipher(self, encode):
        result = ""
        for charStr in self.message:
            charWithShiftIndex = ord(charStr) + self.shiftIndex if encode else ord(charStr) - self.shiftIndex

            if charStr.isupper():
                result += chr((charWithShiftIndex- self.upperCaseAsciiValueStart) % 26 + self.upperCaseAsciiValueStart)
            elif charStr.islower():
                result += chr((charWithShiftIndex - self.lowarCaseAsciiValueStart) % 26 + self.lowarCaseAsciiValueStart)
            elif charStr.isspace():
                result += charStr    
        
        return result

    def _encode_text(self):
        print(f"Caesar Cipher encode; received message is {self.message}.")       
        return self._applyCipher(True)

    def _decode_text(self):
        print(f"CaesarCipher decode; received message is {self.message}.")
        return self._applyCipher(False)