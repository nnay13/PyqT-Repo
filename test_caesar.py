import unittest
import caesar


class CaesarCryptTest(unittest.TestCase):
    """ TestCase est utilisé pour tester le module de cryptage Caesar """

    def test_crypt(self):
        """ Test du Cryptage"""
        key = 2
        message = "ABCDE"
        cipher = caesar.crypt(message, key)
        self.assertEqual(cipher, "CDEFG")

    def test_key_equals_len_of_symbol(self):
        """ Quand la clef == len(SYMBOL)"""
        key = len(caesar.SYMBOL)
        message = "ArTH"
        cipher = caesar.crypt(message, key)
        self.assertEqual(cipher, "ArTH")

    def test_key_greater_than_len_of_symbol(self):
        """ Quand la clef > len(SYMBOL)"""
        key = len(caesar.SYMBOL) + 9
        message = "ABCDE"
        cipher = caesar.crypt(message, key)
        self.assertEqual(cipher, "JKLMN")

    def test_complex_message(self):
        """ Quand la clef > len(SYMBOL)"""
        key = 13
        message = "This is my secret message."
        cipher = caesar.crypt(message, key)
        self.assertEqual(cipher, "guv6Jv6Jz!J6rp5r7Jzr66ntrM")


class CaesarUncryptTest(unittest.TestCase):
    """ TestCase est utilisé pour tester le module de décryptage Caesar """

    def test_crypt(self):
        """ Test du décryptage"""
        key = 2
        message = "CDEFG"
        cipher = caesar.uncrypt(message, key)
        self.assertEqual(cipher, "ABCDE")

    def test_key_equals_len_of_symbol(self):
        """ Quand la clef == len(SYMBOL)"""
        key = len(caesar.SYMBOL)
        message = "ArTH"
        cipher = caesar.uncrypt(message, key)
        self.assertEqual(cipher, "ArTH")

    def test_key_greater_than_len_of_symbol(self):
        """ Quand la clef > len(SYMBOL)"""
        key = len(caesar.SYMBOL) + 9
        message = "JKLMN"
        cipher = caesar.uncrypt(message, key)
        self.assertEqual(cipher, "ABCDE")

    def test_complex_message(self):
        """ Quand la clef > len(SYMBOL)"""
        key = 13
        message = "guv6Jv6Jz!J6rp5r7Jzr66ntrM"
        cipher = caesar.crypt(message, key)
        self.assertEqual(cipher, "This is my secret message.")
