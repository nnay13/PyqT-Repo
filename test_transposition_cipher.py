import unittest

import tranposition_cipher


class TranspositionCryptTest(unittest.TestCase):
    """ TestCase pour testr le  module de cyptage par transposition"""

    def test_simple_crypt(self):
        """Test Simple"""
        message = "ABCDEFG"
        key = 3
        cipher = tranposition_cipher.crypt(message, key)
        self.assertEqual(cipher, "ADGBECF")

    def test_key_is_longer_than_len_of_message(self):
        """Quand la clef est trop longue pas de cryptage"""
        message = "ABCDEFG"
        key = 10
        cipher = tranposition_cipher.crypt(message, key)
        self.assertEqual(cipher, "ABCDEFG")

class TranspositionUncryptTest(unittest.TestCase):
    """ TestCase pour testr le  module de cyptage par transposition"""

    def test_simple_uncrypt(self):
        """Test  simple """
        message = "ADGBECF"
        key = 3
        cipher = tranposition_cipher.uncrypt(message, key)
        self.assertEqual(cipher, "ABCDEFG")
