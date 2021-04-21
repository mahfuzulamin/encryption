from ..interface.cipher_interface import CipherInterface

class KeywordCipher(CipherInterface):
    lowarCaseAsciiValueStart = ord("a")
    upperCaseAsciiValueStart = ord("A")
    plaintext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, message, keyword):
        self.message = message
        self.keyword = keyword

    def applyCipher(self):
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

    def encode(self):
        print(f"Keyword Cipher encode; received message is {self.message}.")
        
        encodedMessage = self.applyCipher()       
        cipher = ""
  
        for charStr in self.message:
            if charStr.isupper():
                cipher += encodedMessage[ord(charStr) - self.upperCaseAsciiValueStart]
            elif charStr.islower():
                cipher += encodedMessage[ord(charStr) - self.lowarCaseAsciiValueStart]

        return cipher

    def decode(self):
        print(f"Keyword decode; received message is {self.message}.")
        deCipher = ""
        encodedMessage = self.applyCipher()

        for charStr in self.message:
            if charStr.isupper():
                deCipher += self.plaintext[encodedMessage.index(charStr)]
            elif charStr.islower():
                deCipher += self.plaintext[encodedMessage.index(chr(ord(charStr) -32))]
            else:
              deCipher += charStr

        return deCipher