import pytest

from ..ciphers.impl.hexadecimal import Hexadecimal

# class TestHexadecimal(unittest.TestCase):

    # @pytest.fixture(autouse=True)
def test_hexadecimal_encode():
    message = "test"
    hex = Hexadecimal(message)
    result = hex.encode()
    assert result == "74657374"
