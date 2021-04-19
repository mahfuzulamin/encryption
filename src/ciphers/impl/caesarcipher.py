class CaesarCipher:
    lowarCaseAsciiValueStart = ord("a")
    upperCaseAsciiValueStart = ord("A")

    def __init__(self, message, shiftIndex):
        self.message = message

    def encode(self):
        print(f"Caesar Cipher encode; received message is {self.message}.")
        result = ""
        for charStr in self.message:
            if charStr.isupper():
                result += chr((ord(charStr) + self.shiftIndex - upperCaseAsciiValueStart) % 26 + upperCaseAsciiValueStart)
            elif charStr.islower():
                result += chr((ord(charStr) + self.shiftIndex - lowarCaseAsciiValueStart) % 26 + lowarCaseAsciiValueStart)
            elif charStr.isspace():
                result += charStr    
        
        return result

    def decode(self):
        print(f"CaesarCipher decode; received message is {self.message}.")
        return self.applyCipher()