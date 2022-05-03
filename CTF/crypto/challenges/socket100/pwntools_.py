from unittest import result
from pwn import *  # pip install pwntools
import json

r = remote('socket.cryptohack.org', 13377, level='debug')


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)



# print("Received type: ",end=' ')
# print(received["type"])
# print("Received encoded value: ",end=' ')
# print(received["encoded"])

# to_send = {
#     "decoded": "changeme"
# }


def slove():
    if received['type'] == "hex":
        result = bytes.fromhex(received['encoded']).decode()
    elif received['type'] == 'base64':
        result = base64.b64decode(received['encoded']).decode()
    elif received['type'] == "rot13":
        s = received['encoded']
        result = ''
        for i in s:
            if ord(i) >122 or ord(i) <97:
                result += i
            elif (ord(i) + 13) <= 122 :
                result += chr(ord(i) + 13)
            else:
                result += chr(ord(i) + 12 - 122 + 97)
    elif received['type'] == 'bigint':
        result = bytes.fromhex(received['encoded'][2:]).decode()
    else:
        result = ''.join(chr(i) for i in received['encoded'])
    return {"decoded": result.strip()}


for i in range(101):
    received = json_recv()
    json_send(slove())
