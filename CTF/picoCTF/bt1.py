s='145 167 233 272 344 91 395 393 433 92 77 414 344 318 420 263 87 186 96 103 91 354 161'
lst = s.split(' ')
def proEuclid(a,m):
    # a>m>0
    y0=0
    y1=1
    while(a>0):
        r = int(m%a)  
        if r==0:
            break
        q= int(m/a)
        y=y0-y1*q
        m=a
        a=r
        y0=y1
        y1=y
    if a>1:
        return "ko kha nghich"
    else:
        return y
plain =''
for i in lst:
    d = int(i) %41
    x = proEuclid(41,d)
    # print(x)
    y = x if (x>=0) else (x+41)
    # 1-26
    if y<=26 and y>=1:
        plain += chr(y+96)
    elif y == 37:
        plain += '_'
    else:
        plain += chr(y+21)
print('picoCTF{' + plain +'}')