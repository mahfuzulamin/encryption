from ..interface.cipher_interface import CipherInterface
from ..util.cipher_util import is_empty
from ..error.validation_exception import ValidationException

class CaesarCipher(CipherInterface):
    """
    Implements the Caesar Cipher.

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

    lowarCaseAsciiValueStart = ord("a")
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
        self.shiftIndex = shiftIndex

    def _validate_input(self):
        """Validates input

        Returns
        -------
        ValidationException for invalid input.
        """

        if is_empty(self.message) == True:
            raise ValidationException("Message cannont be empty.")
    
    def _applyCipher(self, encode):
        """Apply the cipher on the message

        Returns
        -------
        Cipher message
        """

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
        """Encode the message

        Returns
        -------
        Encoded message string
        """    

        print(f"Caesar Cipher encode; received message is {self.message}")       
        return self._applyCipher(True)

    def _decode_text(self):
        """Decode the message

        Returns
        -------
        Decoded message string
        """

        print(f"Caesar Cipher decode; received message is {self.message}")
        return self._applyCipher(False)