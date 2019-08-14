"""Implements the transposition Cipher
"""
import math


def crypt(message, key):
    """Crypt a string with the  Transposition Cipher

    Arguments:
        message {string} -- String  to crypt
        key {int} -- key for the  transposition cipher

    Returns:
        String -- Crypted message
    """
    if key >= len(message):
        return message

    cipher_text = ['']*key
    for column in range(key):
        current_index = column
        while current_index < len(message):
            cipher_text[column] += message[current_index]
            current_index += key
    return ''.join(cipher_text) 


def uncrypt(message, key):
    return ""
