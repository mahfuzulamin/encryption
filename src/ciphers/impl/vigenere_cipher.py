
from ..interface.cipher_interface import CipherInterface

class VigenereCipher(CipherInterface):
    upperCaseAsciiValueStart = ord("A")

    def __init__(self, message, keyword):
        self.message = message
        self.keyword = keyword

    def applyCipher(self, key):
        msgLen = len(self.message)

        i = 0
        while len(key) < msgLen:
            key += key[i]
            i += 1
            
        print(f"VigenereCipher key is {key}.")

        return key
        

    def encode(self):
        print(f"Hex encode;message is {self.message}.")

        finalKey = self.applyCipher(self.keyword)
        cipherText = ""
        for i in range(len(self.message)):
            encodedCharSequence = (ord(self.message[i]) + ord(finalKey[i])) % 26
            cipherText += chr(encodedCharSequence + self.upperCaseAsciiValueStart)

        return cipherText

    def decode(self):
        print(f"Hex decode; message is {self.message}.")

        finalKey = self.applyCipher(self.keyword)
        decipheredText = ""
        for i in range(len(self.message)):
            encodedCharSequence = (ord(self.message[i]) - ord(finalKey[i]) + 26) % 26
            decipheredText += chr(encodedCharSequence + self.upperCaseAsciiValueStart)

        return decipheredText