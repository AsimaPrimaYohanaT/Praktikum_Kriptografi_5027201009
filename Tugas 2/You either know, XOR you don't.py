var=bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

flag_format = b"crypto{"
key = [o1 ^ o2
       for (o1, o2) in zip(var, flag_format)] + [ord("y")]

val = []
key_len = len(key)
for i in range(len(var)):
    val.append(
        var[i] ^ key[i % key_len]
    )

val = "".join(chr(o) for o in val)

print(val)

