import pytest

from ..ciphers.impl.vigenere_cipher import VigenereCipher
from ..ciphers.error.validation_exception import ValidationException

vigenereCipher = VigenereCipher()

def test_vigenere_cipher_encode():
    message = "ATTACKATDAWN"
    result = vigenereCipher.encode(message, None, "LEMONLEMONLE")
    assert result == "LXFOPVEFRNHR"

def test_vigenere_cipher_encode_none_message():
    message = None
    try:
        result = vigenereCipher.encode(message, None, "LEMONLEMONLE")
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."

def test_vigenere_cipher_encode_empty_message():
    message = "  "
    try:
        result = vigenereCipher.encode(message, None, "LEMONLEMONLE")
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."

def test_vigenere_cipher_encode_none_key():
    message = "ATTACKATDAWN"
    try:
        result = vigenereCipher.encode(message, None, None)
    except ValidationException as e:
        assert str(e) == "Key cannont be empty."

def test_vigenere_cipher_encode_empty_key():
    message = "ATTACKATDAWN"
    try:
        result = vigenereCipher.encode(message, None, " ")
    except ValidationException as e:
        assert str(e) == "Key cannont be empty."

def test_vigenere_cipher_encode_key_longer_than_message():
    message = "ATTACKATDAWN"
    try:
        result = vigenereCipher.decode(message, None, "LEMONLEMONLEMON")
    except ValidationException as e:
        assert str(e) == "Key cannont be longer than message."             

def test_vigenere_cipher_decode():
    message = "LXFOPVEFRNHR"
    result = vigenereCipher.decode(message, None, "LEMONLEMONLE")
    assert result == "ATTACKATDAWN"

def test_vigenere_cipher_decode_none_message():
    message = None
    try:
        result = vigenereCipher.decode(message, None, "LEMONLEMONLE")
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."

def test_vigenere_cipher_decode_empty_message():
    message = "  "
    try:
        result = vigenereCipher.decode(message, None, "LEMONLEMONLE")
    except ValidationException as e:
        assert str(e) == "Message cannont be empty." 

def test_vigenere_cipher_decode_key_longer_than_message():
    message = "CRYP"
    try:
        result = vigenereCipher.decode(message, None, "LEMONLEMONLE")
    except ValidationException as e:
        assert str(e) == "Key cannont be longer than message."           