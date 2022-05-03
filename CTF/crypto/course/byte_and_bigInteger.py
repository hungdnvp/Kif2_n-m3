from Crypto.Util.number import *
#s = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

#by = long_to_bytes(s)
#print(by.decode())

encoded = "0x666967757265735f676f75726d65745f776561706f6e73"
result = bytes.fromhex(encoded[2:])
print(result)