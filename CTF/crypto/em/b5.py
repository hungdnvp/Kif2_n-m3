from numpy import double


P={}
count =0
with open('vecto.txt','r') as f:
    while True:
        text = f.readline()
        if text == '':
            break
        P+=('X':text.split(' ')[0],'Y':text.split(' ')[1]}
        count +=1
print(P['X'])
print('so diem trong danh sach P la', count )

# def trongtam():
#     x=0
#     y=0
#     for i in P:
#         if i == 'X':
#             x += i.value
#         else:
#             y += i.value
#     return [x/count,y/count]
# print('toa do trong tam la ',trongtam())