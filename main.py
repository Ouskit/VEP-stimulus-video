import cv2
import os

img = cv2.imread('./images/black-white/0.png') # Gain size

fps = 28

size = (img.shape[1],img.shape[0])

fourcc = cv2.VideoWriter_fourcc(*'MJPG')

videoWrite = cv2.VideoWriter('./output/14Hz Black White.avi',fourcc,fps,size)

path = './images/black-white/'

files = os.listdir(path)

out_num = len(files)

for _ in range(420):
    for i in files:
        fileName = path + i
        img = cv2.imread(fileName)
        videoWrite.write(img)
videoWrite.release()
cv2.destroyAllWindows()