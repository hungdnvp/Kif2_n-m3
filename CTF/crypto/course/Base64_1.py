import base64

s = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf" #hex
b = bytes.fromhex(s)
c = base64.b64encode(b)
print(c.decode())