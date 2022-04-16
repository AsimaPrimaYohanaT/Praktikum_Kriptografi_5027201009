#!/usr/bin/env python
import requests

BASE_URL="http://aes.cryptohack.org/symmetry"
BLOCKSIZE = 32

def encrypt_flag():
    encrypt_flag_request = requests.get(f"{BASE_URL}/encrypt_flag/")
    return encrypt_flag_request.json()["ciphertext"]

def encrypt(plaintext, iv):
    encrypt_request = requests.get(f"{BASE_URL}/encrypt/{plaintext}/{iv}/")
    return encrypt_request.json()["ciphertext"]

def hex_to_ascii(hex):
    bytes_object = bytes.fromhex(hex)
    return bytes_object.decode("ASCII")

ciphertext = encrypt_flag()
plaintext_hex = encrypt(ciphertext[32:], ciphertext[:32])
FLAG = hex_to_ascii(plaintext_hex)

print(f"FLAG: {FLAG}")
