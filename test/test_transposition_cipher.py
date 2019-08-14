import random
import unittest

import tranposition_cipher


class TranspositionCryptTest(unittest.TestCase):
    """ TestCase pour le  module de cyptage par transposition"""

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

    def test_crypt(self):
        """Test Complexe"""
        message = "Une phrase Longue."
        key = 8
        cipher = tranposition_cipher.crypt(message, key)
        self.assertEqual(cipher, "Usene.e  Lpohnrgau")


class TranspositionUncryptTest(unittest.TestCase):
    """ TestCase pour testr le  module de cyptage par transposition"""

    def test_simple_uncrypt(self):
        """Test  simple """
        message = "ADGBECF"
        key = 3
        cipher = tranposition_cipher.uncrypt(message, key)
        self.assertEqual(cipher, "ABCDEFG")

    def test_uncrypt(self):
        """Test Complexe"""
        message = "Usene.e  Lpohnrgau"
        key = 8
        cipher = tranposition_cipher.uncrypt(message, key)
        self.assertEqual(cipher, "Une phrase Longue.")


class TranspositionFullTest(unittest.TestCase):
    """TestCase du cryptage et du décryptage """

    def test_random_string(self):
        """Test  à partir d'une chaine randomisée"""
        # on génère une chaine de caractères aléatoire
        symbols = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef")
        random.seed()
        random.shuffle(symbols)
        message = ''.join(symbols)

        # on génère une clef aléatoire
        key = random.randint(4, 30)

        # on vérifie que le cryptage est bijectif
        cipher = tranposition_cipher.crypt(message, key)
        uncrypted_message = tranposition_cipher.uncrypt(cipher, key)
        self.assertEqual(uncrypted_message, message)
