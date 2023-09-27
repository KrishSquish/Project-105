import os
import cv2 

path = "Images/"

Images = []

for file in os.listdir(path):
    name,ext = os.path.splitext(file)

    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        fileName = path + "/"+ file
        Images.append(fileName)

imageNum = len(Images)

frame = cv2.imread(Images[0])

height, width, channels = frame.shape
size = (width,height)
print(size)

out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)


for i in range(0,imageNum-1):
    cv2.imread(Images[i])
    out.write(i)

print("“Done”")