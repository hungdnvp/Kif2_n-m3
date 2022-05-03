import os

from charset_normalizer import from_bytes
path ="."
os.chdir(path)
def crack(path,filename):
    data = b''
    with open(path,'rb') as f:
        index = f.read(1)
        while index != b'':
            data += index
            index = f.read(1)
        mod = data.replace(bytes.fromhex('75 1E'),bytes.fromhex('90 90'))
    with open(filename + '-p.exe','wb') as f:
        f.write(mod)
for file in os.listdir():
    filename = os.path.splitext(file)[0]
    if '.exe' in file:
        crack(file,filename)