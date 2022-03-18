#!/usr/bin/env python3
from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes

import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

print("Here is your flag:")

value = long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269)
print(value)