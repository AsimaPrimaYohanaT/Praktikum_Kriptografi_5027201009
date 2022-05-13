#dik : cipher text = (plaintext)^e mod n
# C = P^e mod n
# n = p * q (bilangan prima)

plaintext = 12
e = 65537
p, q = 17, 23
N = p * q

print(pow(plaintext, e, N))

#Hasil = 301

