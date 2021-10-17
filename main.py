#!/usr/bin/env python3

from flask import Flask, render_template, request
import password_generation
import encrypt
import subprocess


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/passwordgen", methods=["POST", "GET"])
def password_gen():
    if request.method == "POST":
        #get form data and pass to password generation function
        if(request.form["passRadio"] == "words"):
            #run words function
            return password_generation.gen_password(request.form["lengthOrder"])
        else:
            return password_generation.gen_rand_password(request.form["lengthOrder"], request.form["requirement"])
    elif request.method == "GET":
        return render_template("passwordgen.html")

@app.route("/encryption", methods=["POST", "GET"])
def encryption():
    if request.method == "POST":
        #get form data and pass to encryption function
        if(request.form["dirRadio"] == "encrypt"):
            return encrypt.rsa_encrypt(request.form["key"], request.form["data"])
        elif(request.form["dirRadio"] == "decrypt"):
            return encrypt.rsa_decrypt(request.form["key"], request.form["data"])
    elif request.method == "GET":
        return render_template("encryption.html")

@app.route("/hashing", methods=["POST", "GET"])
def hashing():
    if request.method == "POST":
        #save string to be hashed to file then run hashing file
        with open("data.txt", 'w') as file:
            file.write(request.form["data"])
        return subprocess.run(["java", "hash", request.form["algRadio"], "data.txt"], stdout=subprocess.PIPE).stdout.decode()
    elif request.method == "GET":
        return render_template("hashing.html")

if __name__ == "__main__":
    app.run()
