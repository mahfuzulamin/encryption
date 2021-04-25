
from ..interface.cipher_interface import CipherInterface
from ..util.cipher_util import is_empty
from ..error.validation_exception import ValidationException

class VigenereCipher(CipherInterface):
    upperCaseAsciiValueStart = ord("A")

    def __init__(self):
        pass

    def _initialize(self, message, shiftIndex=None, key=None):
        self.message = message
        self.keyword = key

    def _validate_input(self):
        if is_empty(self.message) == True:
            raise ValidationException("Message cannont be empty.")
        elif is_empty(self.keyword) == True:
            raise ValidationException("Key cannont be empty.")    
    
    def _applyCipher(self, key):
        msgLen = len(self.message)

        i = 0
        while len(key) < msgLen:
            key += key[i]
            i += 1
            
        print(f"VigenereCipher key is {key}.")

        return key
    
    def _encode_text(self):
        print(f"Hex encode;message is {self.message}.")

        finalKey = self._applyCipher(self.keyword)
        cipherText = ""
        for i in range(len(self.message)):
            encodedCharSequence = (ord(self.message[i]) + ord(finalKey[i])) % 26
            cipherText += chr(encodedCharSequence + self.upperCaseAsciiValueStart)

        return cipherText

    def _decode_text(self):
        print(f"Hex decode; message is {self.message}.")

        finalKey = self._applyCipher(self.keyword)
        decipheredText = ""
        for i in range(len(self.message)):
            encodedCharSequence = (ord(self.message[i]) - ord(finalKey[i]) + 26) % 26
            decipheredText += chr(encodedCharSequence + self.upperCaseAsciiValueStart)

        return decipheredText