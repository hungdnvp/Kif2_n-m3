A = []
with open('dayso.txt','r') as f:
    while True:
        text = f.readline()
        if text == '':
            break
        A += [int(x) for x in text.strip().split(' ')]
        
print('danh sach A la ' ,A)
print('so le co 3 chu so : ')
for i in A:
    if i>99 and i<999 and i%2==1:
        print(i,end=' ')

