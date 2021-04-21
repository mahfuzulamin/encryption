import abc

class CipherInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'encode') and 
                callable(subclass.encode) and 
                hasattr(subclass, 'decode') and 
                callable(subclass.decode) or 
                NotImplemented)

    @abc.abstractmethod
    def encode(self):
        """Encode the message"""
        raise NotImplementedError

    @abc.abstractmethod
    def decode(self):
        """Decode the message"""
        raise NotImplementedError