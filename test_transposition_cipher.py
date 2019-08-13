import unittest

import tranposition_cipher


class TranspositionCryptTest(unittest.TestCase):
    """ TestCase pour testr le  module de cyptage par transposition"""

    def simple_crypt_test(self):
        message = "ABCDEFG"
        key = 3
        cipher = tranposition_cipher.crypt(message, key)
        self.assertEqual(cipher, "ADGBECF")

    def key_is_longer_than_len_of_message(self):
        message = "ABCDEFG"
        key = 10
        cipher = tranposition_cipher.crypt(message, key)
        self.assertEqual(cipher, "ABCDEFG")

class TranspositionUncryptTest(unittest.TestCase):
    """ TestCase pour testr le  module de cyptage par transposition"""

    def simple_uncrypt_test(self):
        message = "ADGBECF"
        key = 3
        cipher = tranposition_cipher.uncrypt(message, key)
        self.assertEqual(cipher, "ABCDEFG")
