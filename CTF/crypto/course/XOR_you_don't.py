from base64 import decode
import base64
from pwn import xor
cipher = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
key_byte = bytes.fromhex(cipher)
format_key = b"crypto{"
# secret_key có vẻ thiếu 'y' cộng thêm 'y' cho đúng dạng
secret_key = xor(key_byte[:7],format_key) + b'y'
# lặp lại cho phù hợp với độ dài của chuỗi
key = secret_key * (len(key_byte)//len(secret_key)) + secret_key[:(len(key_byte)%len(secret_key))]
# chính là key = secret_key* 5 + secret_key[:2]
print(xor(key_byte,key))
