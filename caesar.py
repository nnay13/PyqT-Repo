# YGX 13/08/2019
"""Implements the simple CAESAR Cipher
"""
# import sys

# list  of characters available for the message
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."


def main():
    """Main loop"""
    my_message = input("Message à Cypter: \n")
    my_key = int(input("Clef de Cryptage : \n"))
    print("Message crypté %s" % crypt(my_message, my_key))


def crypt(message, key):
    """Crypt a string using the caesar cipher
    Arguments:
        message {string} -- The string to crypt
        key {int} -- The Cipher Key
    """
    cipher_text = [""] * len(message)
    current_index = 0
    for char in message:
        if char in SYMBOLS:
            pos = SYMBOLS.index(char) + key
            if pos < len(SYMBOLS):
                cipher_text[current_index] = SYMBOLS[pos]
            else:
                cipher_text[current_index] = SYMBOLS[pos - len(SYMBOLS)]
        else:
            cipher_text[current_index] = char
        current_index += 1
    return "".join(cipher_text)


def uncrypt(cipher_text, key):
    """Uncrypt a string using the caesar cipher
    Arguments:
        cipherText {string} -- The string to uncrypt
        key {int} -- The Cipher Key
    """
    message = [""] * len(cipher_text)
    current_index = 0
    for char in cipher_text:
        if char in SYMBOLS:
            pos = SYMBOLS.index(char) - key
            if pos < 0:
                message[current_index] = SYMBOLS[pos + len(SYMBOLS)]
            else:
                message[current_index] = SYMBOLS[pos]
        else:
            message[current_index] = char
        current_index += 1
    return "".join(message)


if __name__ == "__main__":
    main()
