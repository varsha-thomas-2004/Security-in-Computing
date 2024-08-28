#Python program to encrypt and decrypt a message

import random
import string

chars = " " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"Characters: {chars}") 
#print(f"Key: {key}")

original_text = input("Enter the message: ")
cipher_text = ""

#Encryption
for letter in original_text:
    index = key.index(letter) #gets the index from "key" list
    cipher_text += chars[index] #appends cipher_text with corresponding element from "chars" list

print(f"Original text: {original_text}")
print(f"Cipher text: {cipher_text}")

cipher_text = input("Enter the encrypted message: ")
original_text = ""

#Decryption
for letter in cipher_text:
    index = chars.index(letter) #gets the index from "chars" list
    original_text += key[index] #appends original_text with corresponding element from "key" list

print(f"Cipher text: {cipher_text}")
print(f"Original text: {original_text}")