import cv2
import os

path = os.listdir("./drawings")
dic = dict()
dic[0] =[170, 190]
dic[1] =[162, 330]
dic[2] =[176, 266]
dic[3] =[144, 100]
dic[4] =[157, 315]
dic[5] =[296, 221]
dic[6] =[93, 176]
dic[7] =[280, 70]

for i in path:
    img = cv2.imread('./drawings/{}'.format(i),1)
    print(img.shape)
    # id = dic[path.index(i)]
    # byte = img[id[1]][id[0]]
    # print(bin(byte[2]))