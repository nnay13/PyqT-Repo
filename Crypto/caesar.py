# YGX 13/08/2019
"""Implements the simple CAESAR Cipher
"""
# import sys


SYMBOL = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.:!"


def main():
    myMessage = input("Message à Cypter: \n")
    myKey = int(input("Clef de Cryptage : \n"))
    print("Message crypté %s" % caesarCrypt(myMessage, myKey))


def caesarCrypt(message, key):
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
            if (pos) <= len(SYMBOL):
                cipherText[currentIndex] = SYMBOL[pos]
            else:
                cipherText[currentIndex] = SYMBOL[pos - len(SYMBOL) + 1]
        else:
            cipherText[currentIndex] = char
        currentIndex += 1
    return "".join(cipherText)


if __name__ == "__main__":
    main()
