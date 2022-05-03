s = "label"
l = []
for i in s:
    l.append(ord(i)^13)
for i in l:
    print(chr(i),end="")