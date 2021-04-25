import pytest

from ..ciphers.impl.atbash import AtBash
from ..ciphers.error.validation_exception import ValidationException

atbash = AtBash()

def test_atbash_encode():
    message = "Flee at once."
    result = atbash.encode(message)
    assert result == "Uovv zg lmxv."

def test_atbash_encode_none_message():
    message = None
    try:
        result = atbash.encode(message)
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."

def test_atbash_encode_empty_message():
    message = "  "
    try:
        result = atbash.encode(message)
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."

def test_atbash_decode():
    message = "Uovv zg lmxv."
    result = atbash.decode(message)
    assert result == "Flee at once."

def test_atbash_decode_none_message():
    message = None
    try:
        result = atbash.decode(message)
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."

def test_atbash_decode_empty_message():
    message = "  "
    try:
        result = atbash.decode(message)
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."        