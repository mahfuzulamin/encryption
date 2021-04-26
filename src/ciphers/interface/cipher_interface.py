import abc

class CipherInterface(metaclass=abc.ABCMeta):
    """
    This is an interface for cipher implementation and defines how subclass should be implemented.

    ...

    Methods
    -------
    encode(message, shiftIndex=None, key=None):
        Template Method Design Patern implementation of encode message and encodes a message based on subclass implementation.
    decode(message, shiftIndex=None, key=None):
        Template Method Design Patern implementation of decode message and decodes a message based on subclass implementation.
    _applyCipher():
        Subclass will implement the Abstract Method and apply relavent cipher
    _encode_text():
        Subclass will implement the Abstract Method and encode text   
    _decode_text():
        Subclass will implement the Abstract Method and decode text
    _initialize():
        Subclass will implement the initialize method
    _validate_input():
        Subclass will implement the method to validate input
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, '_encode_text') and 
                callable(subclass._encode_text) and 
                hasattr(subclass, '_decode_text') and 
                callable(subclass._decode_text) or 
                NotImplemented)

    def encode(self, message, shiftIndex=None, key=None):
        """Encode the message
        
        Parameters
        ----------
        message : str
            Message to be encoded
        shiftIndex : int, optional
            Shift character index (default is None)
        key : str, optional
            Keyword for cipher (default is None)
                
        Returns
        -------
        Encoded message string
        """
        
        self._initialize(message, shiftIndex, key)
        self._validate_input()
        return self._encode_text()

    def decode(self, message, shiftIndex=None, key=None):
        """Decode the message
        
        Parameters
        ----------
        message : str
            Message to be decoded
        shiftIndex : int, optional
            Shift character index (default is None)
        key : str, optional
            Keyword for cipher (default is None)    
        
        Returns
        -------
        Decoded message string
        """

        self._initialize(message, shiftIndex, key)    
        self._validate_input()    
        return self._decode_text()

    @abc.abstractmethod
    def _applyCipher(self):
        """Apply the cipher on the message

        Returns
        -------
        Cipher message
        """
        
        raise NotImplementedError

    @abc.abstractmethod
    def _encode_text(self):
        """Encode the message

        Returns
        -------
        Encoded message string
        """

        raise NotImplementedError

    @abc.abstractmethod
    def _decode_text(self):
        """Decode the message

        Returns
        -------
        Decoded message string
        """

        raise NotImplementedError        

    @abc.abstractmethod
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

        raise NotImplementedError       

    @abc.abstractmethod
    def _validate_input(self):
        """Validates input

        Returns
        -------
        ValidationException for invalid input.
        """

        raise NotImplementedError       