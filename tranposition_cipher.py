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

    nb_of_row = key
    nb_of_column  = math.ceil(len(cipher_text)/key)
    nb_of_grey_boxes = (nb_of_column * nb_of_row)-len(cipher_text)
    message = ['']*nb_of_column
    row = 0
    column = 0

    for char in cipher_text:
        message[column] += char
        column += 1

        if (column == nb_of_column) or ((column >= nb_of_column - 1) and (row >= nb_of_row-nb_of_grey_boxes)):
            row += 1
            column = 0


    return ''.join(message)
