import json
import requests

URL_encrypt = "http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
URL_decrypt = "http://aes.cryptohack.org/ecbcbcwtf/decrypt/{ciphertext}/"

def get_cipher(plaintext):
    r = requests.get(URL_encrypt)
    json_ans = json.loads(r.text)
    return json_ans['ciphertext']

def get_plain(ciphertext):
    r = requests.get(URL_decrypt.format(ciphertext=ciphertext))
    json_ans = json.loads(r.text)
    return json_ans['plaintext']

def xor(itx, ity):
    return [x ^ y for x, y in zip(itx, ity)]

ciphertext = get_cipher('Dont care')
split_ciphertext = [ciphertext[i:i+32] for i in range(0, len(ciphertext), 32)] 

plaintext = [0]*(len(split_ciphertext) - 1)
for i in range(len(plaintext)):
    pi = bytes.fromhex(get_plain(split_ciphertext[i+1]))
    ci = bytes.fromhex(split_ciphertext[i])
    plaintext[i] = ''.join(map(chr, xor(pi, ci)))

print(f"Flag: {''.join(plaintext)}")
