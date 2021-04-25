import pytest

from ..ciphers.impl.caesarcipher import CaesarCipher
from ..ciphers.error.validation_exception import ValidationException

caesarCipher = CaesarCipher()

def test_caesar_cipher_encode():
    message = "HELLO WORLD"
    result = caesarCipher.encode(message, 3)
    assert result == "KHOOR ZRUOG"

def test_caesar_cipher_encode_none_message():
    message = None
    try:
        result = caesarCipher.encode(message, 5)
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."

def test_caesar_cipher_encode_empty_message():
    message = "  "
    try:
        result = caesarCipher.encode(message, 1)
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."

def test_caesar_cipher_decode():
    message = "KHOOR ZRUOG"
    result = caesarCipher.decode(message, 3)
    assert result == "HELLO WORLD"

def test_caesar_cipher_decode_none_message():
    message = None
    try:
        result = caesarCipher.decode(message, 3)
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."

def test_caesar_cipher_decode_empty_message():
    message = "  "
    try:
        result = caesarCipher.decode(message, 4)
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."        