# YGX 13/08/2019
"""Implements the simple CAESAR Cipher
"""
# import sys


SYMBOL = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
# SYMBOL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    myMessage = input("Message à Cypter: \n")
    myKey = int(input("Clef de Cryptage : \n"))
    print("Message crypté %s" % crypt(myMessage, myKey))


def crypt(message, key):
    """Crypt a string using the caesar cipher
    Arguments:
        message {string} -- The string to crypt
        key {int} -- The Cipher Key
    """
    cipherText = [""] * len(message)
    currentIndex = 0
    for char in message:
        if char in SYMBOL:
            pos = SYMBOL.index(char) + key
            if pos < len(SYMBOL):
                cipherText[currentIndex] = SYMBOL[pos]
            else:
                cipherText[currentIndex] = SYMBOL[pos - len(SYMBOL)]
        else:
            cipherText[currentIndex] = char
        currentIndex += 1
    return "".join(cipherText)


def uncrypt(cipherText, key):
    """Uncrypt a string using the caesar cipher
    Arguments:
        cipherText {string} -- The string to uncrypt
        key {int} -- The Cipher Key
    """
    message = [""] * len(cipherText)
    currentIndex = 0
    for char in cipherText:
        if char in SYMBOL:
            pos = SYMBOL.index(char) - key
            if pos < 0:
                message[currentIndex] = SYMBOL[pos + len(SYMBOL)]
            else:
                message[currentIndex] = SYMBOL[pos]
        else:
            message[currentIndex] = char
        currentIndex += 1
    return "".join(message)


if __name__ == "__main__":
    main()
