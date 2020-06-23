# Author: OMKAR PATHAK
# This program illustrates a simple example for encrypting/ decrypting your text

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS = LETTERS.lower()

def encrypt(message, key):
    ''' This function lets you to encrypt your message based on a key '''
    encrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num += key
            if num>25:
                num=num%25
                num=num-1
            encrypted =encrypted + LETTERS[num]

    return encrypted

def decrypt(message, key):
    ''' This function lets you to decrypt your message based on a key '''
    decrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            if num>25:
                num=num%25
                num=num-1
            num = num -key
            decrypted =decrypted+LETTERS[num]

    return decrypted

def main():
    message = str(input('Enter your message: '))
    key = int(input('Enter you key [1 - 26]: '))
    choice = input('Encrypt or Decrypt? [E/D]: ')

    if choice.lower().startswith('e'):
        print(encrypt(message, key))
    else:
        print(decrypt(message, key))

if __name__ == '__main__':
    main()

    # OUTPUT:
    # omkarpathak@omkarpathak-Inspiron-3542:~/Documents/GITs/Python-Programs/Programs$ python P40_CipherText.py
    # Enter your message: omkar
    # Enter you key [1 - 26]: 2
    # Encrypt or Decrypt? [E/D]: e
    # qomct
    #
    # omkarpathak@omkarpathak-Inspiron-3542:~/Documents/GITs/Python-Programs/Programs$ python P40_CipherText.py
    # Enter your message: qomct
    # Enter you key [1 - 26]: 2
    # Encrypt or Decrypt? [E/D]: d
    # omkar
