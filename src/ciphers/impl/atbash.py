class AtBash:
    lowarCaseAsciiTotal = ord('z') + ord('a')
    upperCaseAsciiTotal = ord('Z') + ord('A')

    def __init__(self, message):
        self.message = message

    def applyCipher(self):
        cipherMsg = ''
        for charStr in self.message:
            if charStr.isalpha():
                if charStr.isupper():
                    cipherMsg += chr(self.upperCaseAsciiTotal - ord(charStr))
                else:
                    cipherMsg += chr(self.lowarCaseAsciiTotal - ord(charStr))
        
        return cipherMsg

    def encode(self):
        print(f"AtBash encode; received message is {self.message}.")
        return self.applyCipher()

    def decode(self):
        print(f"AtBash decode; received message is {self.message}.")
        return self.applyCipher()