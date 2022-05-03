import hashlib

username_trial = b'FRASER'
data = hashlib.sha256(username_trial).hexdigest()
ketqua =''
l = [4,5,3,6,2,7,1,8]
for i in l:
    print(data[i],end='')