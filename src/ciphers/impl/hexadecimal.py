
from ..interface.cipher_interface import CipherInterface
from ..util.cipher_util import is_empty
from ..error.validation_exception import ValidationException

class Hexadecimal(CipherInterface):
    """
    Implements the Hexadecimal Cipher.

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

    def _applyCipher(self, encode):
        """Apply the cipher on the message is not implemented"""
        pass

    def _validate_input(self):
        """Validates input

        Returns
        -------
        ValidationException for invalid input.
        """

        if is_empty(self.message) == True:
            raise ValidationException("Message cannont be empty.")

    def _encode_text(self):
        """Encode the message

        Returns
        -------
        Encoded message string
        """

        print(f"Hex encode; received message is {self.message}")
        return self.message.encode("utf-8").hex()

    def _decode_text(self):
        """Decode the message

        Returns
        -------
        Decoded message string
        """

        print(f"Hex decode; received message is {self.message}")
        return bytes.fromhex(self.message).decode('utf-8')