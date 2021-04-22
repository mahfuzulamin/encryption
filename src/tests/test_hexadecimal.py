import pytest

from ..ciphers.impl.hexadecimal import Hexadecimal

class TestHexadecimal(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def test_hexadecimal_encode(self):
        message = "test"
        hex = Hexadecimal(message)
        result = hex.encode()
        self.assertEqual(result, "74657374")
