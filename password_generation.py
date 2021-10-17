#!/usr/bin/env python3

import requests
import json
from random import randint, choice
import sys

#usage: password_generation.py [word/random] [required characters (optional)]

def gen_password(order):
    #order is string made of w's and n's representing words and numbers
    password = []
    for a in order:
        if(a == 'w'):
            #random word
            #send get request to https://random-word-api.herokuapp.com/word?number=1
            word = requests.get("https://random-word-api.herokuapp.com/word?number=1")
            word = json.loads(word.text)
            password.append(word[0].capitalize())
        elif(a == 'n'):
            #random number
            password.append(str(randint(0,9)))
        else:
            return None

    return("".join(password))


def gen_rand_password(length, required_chars):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = []
    for a in range(int(length)):
        password.append(choice(chars))
    if(required_chars != None):
        #replace last character with the required characters
        for count, value in enumerate(required_chars):
            password[-(int(count+1))] = value

    return("".join(password))


if __name__ == "__main__":
    if(sys.argv[1] == "word"):
        print(gen_password(sys.argv[2]))
    elif(sys.argv[1] == "random"):
        if(len(sys.argv) == 3):
            #no required characters
            required_chars = None
        else:
            #pass required chars within single quotes
            required_chars = sys.argv[3]

        print(gen_rand_password(sys.argv[2], required_chars))
