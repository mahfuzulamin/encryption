from ..interface.cipher_interface import CipherInterface
from ..util.cipher_util import is_empty
from ..error.validation_exception import ValidationException

class KeywordCipher(CipherInterface):
    lowarCaseAsciiValueStart = ord("a")
    upperCaseAsciiValueStart = ord("A")
    plaintext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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
        elif len(self.keyword) < len(self.keyword):
            raise ValidationException("Key cannont be longer than message.") 
            
    def _applyCipher(self):
        encoded = ""
        characterList = [False] * 26

        for key in self.keyword:
            if key.isupper():
                if key not in encoded:
                    encoded += key
                    characterList[ord(key) - self.upperCaseAsciiValueStart] = True
            elif key.islower():
                if key not in encoded:
                    encoded += chr(ord(key)- 32)
                    characterList[ord(key) - self.lowarCaseAsciiValueStart] = True

        for i in range(len(characterList)):
            if characterList[i] == False:
                encoded += chr(i + self.upperCaseAsciiValueStart)
                characterList[i] = True

        print(f"Keyword Cipher encoded string: {encoded}.")

        return encoded

    def _encode_text(self):
        print(f"Keyword Cipher encode; received message is {self.message}.")
        
        encodedMessage = self._applyCipher()       
        cipher = ""
  
        for charStr in self.message:
            if charStr.isupper():
                cipher += encodedMessage[ord(charStr) - self.upperCaseAsciiValueStart]
            elif charStr.islower():
                cipher += encodedMessage[ord(charStr) - self.lowarCaseAsciiValueStart]

        return cipher

    def _decode_text(self):
        print(f"Keyword decode; received message is {self.message}.")
        deCipher = ""
        encodedMessage = self._applyCipher()

        for charStr in self.message:
            if charStr.isupper():
                deCipher += self.plaintext[encodedMessage.index(charStr)]
            elif charStr.islower():
                deCipher += self.plaintext[encodedMessage.index(chr(ord(charStr) -32))]
            else:
              deCipher += charStr

        return deCipher