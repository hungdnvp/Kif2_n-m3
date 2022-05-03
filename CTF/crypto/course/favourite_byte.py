from base64 import decode
import base64
from unittest import result

s = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
by = bytes.fromhex(s)
result = ""
for i in range(256):
    for j in by:
        result += chr(j^i)
    if "crypto" in result:
        print(result)
    result = ""