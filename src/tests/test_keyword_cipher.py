import pytest

from ..ciphers.impl.keyword_cipher import KeywordCipher
from ..ciphers.error.validation_exception import ValidationException

keywordCipher = KeywordCipher()

def test_keyword_cipher_encode():
    message = "CRYPTOGRAPHYISCOOL"
    result = keywordCipher.encode(message, None, "kryptos")
    assert result == "YLXINHSLKIAXBMYHHE"

def test_keyword_cipher_encode_none_message():
    message = None
    try:
        result = keywordCipher.encode(message, None, "kryptos")
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."

def test_keyword_cipher_encode_empty_message():
    message = "  "
    try:
        result = keywordCipher.encode(message, None, "kryptos")
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."

def test_keyword_cipher_encode_none_key():
    message = "CRYPTOGRAPHYISCOOL"
    try:
        result = keywordCipher.encode(message, None, None)
    except ValidationException as e:
        assert str(e) == "Key cannont be empty."

def test_keyword_cipher_encode_empty_key():
    message = "CRYPTOGRAPHYISCOOL"
    try:
        result = keywordCipher.encode(message, None, " ")
    except ValidationException as e:
        assert str(e) == "Key cannont be empty."

def test_keyword_cipher_decode():
    message = "YLXINHSLKIAXBMYHHE"
    result = keywordCipher.decode(message, None, "kryptos")
    assert result == "CRYPTOGRAPHYISCOOL"

def test_keyword_cipher_decode_none_message():
    message = None
    try:
        result = keywordCipher.decode(message, None, "kryptos")
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."

def test_keyword_cipher_decode_empty_message():
    message = "  "
    try:
        result = keywordCipher.decode(message, None, "kryptos")
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."        