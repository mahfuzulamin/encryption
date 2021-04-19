class CaesarCipher:
    lowarCaseAsciiValueStart = ord("a")
    upperCaseAsciiValueStart = ord("A")

    def __init__(self, message, shiftIndex):
        self.message = message
        self.shiftIndex = shiftIndex

    def applyCipher(self, encode):
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

    def encode(self):
        print(f"Caesar Cipher encode; received message is {self.message}.")       
        return self.applyCipher(True)

    def decode(self):
        print(f"CaesarCipher decode; received message is {self.message}.")
        return self.applyCipher(False)