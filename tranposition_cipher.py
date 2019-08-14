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

    column_of_text = ['']*key

    for index in range(key):




    return ""


def uncrypt(message, key):
    return ""
