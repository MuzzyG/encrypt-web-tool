#!/usr/bin/env python3

import sys
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import base64

#usage: encrypt.py [encrypt/decrypt] [key file] [data file]

def rsa_encrypt(key, data):
    key = RSA.importKey(key)
    cipher = PKCS1_OAEP.new(key)
    return base64.b64encode(cipher.encrypt(data.encode())).decode()

def rsa_decrypt(key, data):
    key = RSA.importKey(key)
    cipher = PKCS1_OAEP.new(key)
    return cipher.decrypt(base64.b64decode(data)).decode()

if __name__ == "__main__":
    with open(sys.argv[2], 'r') as file:
        key = file.read()
    with open(sys.argv[3], 'r') as file:
        data = file.read()
    if(sys.argv[1] == "encrypt"):
        print(rsa_encrypt(key, data))
    elif(sys.argv[1] == "decrypt"):
        print(rsa_decrypt(key, data))
