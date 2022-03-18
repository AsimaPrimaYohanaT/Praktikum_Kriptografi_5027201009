key=bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")


for order in range(256):
    possible_flag_ord = [order ^ o for o in key]
    possible_flag = "".join(chr(o) for o in possible_flag_ord)
    if possible_flag.startswith("crypto"):
        val = possible_flag
        break

print(val)
