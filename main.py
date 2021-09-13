import cv2
import os
import random

img = cv2.imread('./images/1.png')
fps = 28
size = (img.shape[1],img.shape[0])
print(size)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
videoWrite = cv2.VideoWriter('./new_2.avi',fourcc,fps,size)

files = os.listdir('./images')

print(files)
out_num = len(files)

for _ in range(420):
    for i in files:
        fileName = "./images/"+ i
        img = cv2.imread(fileName)
        videoWrite.write(img)
videoWrite.release()
cv2.destroyAllWindows()