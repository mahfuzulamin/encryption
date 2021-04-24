import pytest

from ..ciphers.impl.hexadecimal import Hexadecimal
from ..ciphers.error.validation_exception import ValidationException

def test_hexadecimal_encode():
    message = "test"
    hex = Hexadecimal(message)
    result = hex.encode()
    assert result == "74657374"

def test_hexadecimal_encode_none_message():
    message = None
    hex = Hexadecimal(message)

    try:
        result = hex.encode()
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."

def test_hexadecimal_encode_empty_message():
    message = "  "
    hex = Hexadecimal(message)

    try:
        result = hex.encode()
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."

def test_hexadecimal_decode():
    message = "74657374"
    hex = Hexadecimal(message)
    result = hex.decode()
    assert result == "test"

def test_hexadecimal_decode_none_message():
    message = None
    hex = Hexadecimal(message)

    try:
        result = hex.decode()
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."

def test_hexadecimal_decode_empty_message():
    message = "  "
    hex = Hexadecimal(message)

    try:
        result = hex.decode()
    except ValidationException as e:
        assert str(e) == "Message cannont be empty."        