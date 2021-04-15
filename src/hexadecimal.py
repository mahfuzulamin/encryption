# import binascii

class Hexadecimal:
    def __init__(self, message):
        self.message = message

    def encode(self):
        print(f"Hex encode;message is {self.message}.")
        return self.message.encode("utf-8").hex()

    def decode(self):
        print(f"Hex decode; message is {self.message}.")
        return bytes.fromhex(self.message).decode('utf-8')