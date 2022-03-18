string="label"
val =""

for i in string:
    val += chr(ord(i)^13)

print("crypto{"+val+"}")
