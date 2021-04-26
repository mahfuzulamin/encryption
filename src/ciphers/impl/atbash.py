from ..interface.cipher_interface import CipherInterface
from ..error.validation_exception import ValidationException
from ..util.cipher_util import is_empty

class AtBash(CipherInterface):
    """
    Implements the AtBash Cipher.

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

    lowarCaseAsciiTotal = ord('z') + ord('a')
    upperCaseAsciiTotal = ord('Z') + ord('A')

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

    def _validate_input(self):
        """Validates input
        
        Returns
        -------
        ValidationException for invalid input.
        """

        if is_empty(self.message) == True:
            raise ValidationException("Message cannont be empty.")

    def _applyCipher(self):
        """Apply the cipher on the message
        
        Returns
        -------
        Cipher message
        """

        cipherMsg = ''
        for charStr in self.message:
            if charStr.isalpha():
                if charStr.isupper():
                    cipherMsg += chr(self.upperCaseAsciiTotal - ord(charStr))
                else:
                    cipherMsg += chr(self.lowarCaseAsciiTotal - ord(charStr))
            else: 
                cipherMsg += charStr

        return cipherMsg

    def _encode_text(self):
        """Encode the message

        Returns
        -------
        Encoded message string
        """

        print(f"AtBash encode; received message is {self.message}")
        return self._applyCipher()

    def _decode_text(self):
        """Decode the message

        Returns
        -------
        Decoded message string
        """
            
        print(f"AtBash decode; received message is {self.message}")
        return self._applyCipher()