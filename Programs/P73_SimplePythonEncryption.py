# Author: OMKAR PATHAK

# This program illustrates a simple Python encryption example using the RSA Algotrithm

# RSA is an algorithm used by modern computers to encrypt and decrypt messages. It is an asymmetric
# cryptographic algorithm. Asymmetric means that there are two different keys (public and private).

# For installation: sudo pip3 install pycrypto

from Crypto.PublicKey import RSA
from Crypto import Random

randomGenerator = Random.new().read
# Generating a private key and a public key
# key stores both the keys
key = RSA.generate(1024, randomGenerator) # 1024 is the size of the key in bits
print(key)                                # Prints private key
print(key.publickey())                    # Prints public key

# Encryption using Public Key
publicKey = key.publickey()
encryptedData = publicKey.encrypt('My name is Omkar Pathak'.encode('utf-8'), 32)
print(encryptedData)

# Decryption using Private Key
decryptedData = key.decrypt(encryptedData)
print(decryptedData)
