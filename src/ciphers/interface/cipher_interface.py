import abc

class CipherInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, '_encode_text') and 
                callable(subclass._encode_text) and 
                hasattr(subclass, '_decode_text') and 
                callable(subclass._decode_text) or 
                NotImplemented)

    def encode(self, message, shiftIndex=None, key=None):
        """Encode the message"""
        
        self._initialize(message, shiftIndex, key)
        self._validate_input()
        return self._encode_text()

    def decode(self, message, shiftIndex=None, key=None):
        """Decode the message"""

        self._initialize(message, shiftIndex, key)    
        self._validate_input()    
        return self._decode_text()

    @abc.abstractmethod
    def _applyCipher(self):
        """Apply the cipher on the message"""
        raise NotImplementedError

    @abc.abstractmethod
    def _encode_text(self):
        """Encode the message"""
        raise NotImplementedError

    @abc.abstractmethod
    def _decode_text(self):
        """Decode the message"""
        raise NotImplementedError        

    @abc.abstractmethod
    def _initialize(self, message, shiftIndex=None, key=None):
        """Validate input"""
        raise NotImplementedError       

    @abc.abstractmethod
    def _validate_input(self):
        """Validate input"""
        raise NotImplementedError       