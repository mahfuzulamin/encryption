import pytest

from ..ciphers.impl.hexadecimal import Hexadecimal
from ..ciphers.error.validation_exception import ValidationException

hex = Hexadecimal()

def test_hexadecimal_encode():
    message = "test"
    result = hex.encode(message)
    assert result == "74657374"

def test_hexadecimal_encode_none_message():
    message = None
    try:
        result = hex.encode(message)
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."

def test_hexadecimal_encode_empty_message():
    message = "  "
    try:
        result = hex.encode(message)
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."

def test_hexadecimal_decode():
    message = "74657374"
    result = hex.decode(message)
    assert result == "test"

def test_hexadecimal_decode_none_message():
    message = None
    try:
        result = hex.decode(message)
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."

def test_hexadecimal_decode_empty_message():
    message = "  "
    try:
        result = hex.decode(message)
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."        