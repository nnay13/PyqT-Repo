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


def uncrypt(cipher_text, key):
    """Uncrypt  a string crypted with the tranposition Cipher

    Arguments:
        cipher_text {string} -- message to uncrypt
        key {int} -- cipher key

    Returns:
        string -- uncrypted message
    """
    if key >= len(cipher_text):
        return cipher_text

    nb_row = key
    nb_column = math.ceil(len(cipher_text)/key)
    nb_blank_boxes = (nb_column * nb_row)-len(cipher_text)
    message = ['']*nb_column
    row = 0
    column = 0

    for char in cipher_text:
        message[column] += char
        column += 1

        # if it's the last column 
        if (column == nb_column):
            row += 1
            column = 0
        # if there's blank box
        if ((column >= nb_column - 1) and (row >= nb_row - nb_blank_boxes)):
            row += 1
            column = 0

    return ''.join(message)
