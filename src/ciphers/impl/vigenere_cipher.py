
from ..interface.cipher_interface import CipherInterface
from ..util.cipher_util import is_empty
from ..error.validation_exception import ValidationException

class VigenereCipher(CipherInterface):
    """
    Implements the Vigenere Cipher.

    ...

    Methods
    -------
    _applyCipher():
        Applies the cipher
    _encode_text():
        Encodes message   
    _decode_text():
        Decodes message   
    _initialize():
        Initializes input
    _validate_input():
        Validates input
    """

    upperCaseAsciiValueStart = ord("A")

    def __init__(self):
        pass

    def _initialize(self, message, shiftIndex=None, key=None):
        """Initialize input

        Parameters
        ----------
        message : str
            Message to be decoded
        shiftIndex : int, optional
            Shift character index (default is None)
        key : str, optional
            Keyword for cipher (default is None)    
        """

        self.message = message
        self.keyword = key

    def _validate_input(self):
        """Validates input
        
        Returns
        -------
        ValidationException for invalid input.
        """

        if is_empty(self.message) == True:
            raise ValidationException("Message cannont be empty.")
        elif is_empty(self.keyword) == True:
            raise ValidationException("Key cannont be empty.")    
        elif len(self.keyword) < len(self.keyword):
            raise ValidationException("Key cannont be longer than message.")  

        self.message = self.message.upper()
        self.keyword = self.keyword.upper()

    def _applyCipher(self, key):
        """Apply the cipher on the message
        
        Returns
        -------
        Cipher message
        """

        msgLen = len(self.message)

        i = 0
        while len(key) < msgLen:
            key += key[i]
            i += 1
            
        #print(f"VigenereCipher key is {key}.")

        return key
    
    def _encode_text(self):
        """Encode the message

        Returns
        -------
        Encoded message string
        """

        print(f"Vigenere Cipher encode; received message is {self.message}")

        finalKey = self._applyCipher(self.keyword)
        cipherText = ""
        for i in range(len(self.message)):
            encodedCharSequence = (ord(self.message[i]) + ord(finalKey[i])) % 26
            cipherText += chr(encodedCharSequence + self.upperCaseAsciiValueStart)

        return cipherText

    def _decode_text(self):
        """Decode the message

        Returns
        -------
        Decoded message string
        """

        print(f"Vigenere Cipher decode; received message is {self.message}")

        finalKey = self._applyCipher(self.keyword)
        decipheredText = ""
        for i in range(len(self.message)):
            encodedCharSequence = (ord(self.message[i]) - ord(finalKey[i]) + 26) % 26
            decipheredText += chr(encodedCharSequence + self.upperCaseAsciiValueStart)

        return decipheredText