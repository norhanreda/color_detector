import cv2
import pandas as pd

img_path='colorful_image.jpg'
csv_path='colors.csv'

index=['color','color_name','hex','R','G','B']

df=pd.read_csv(csv_path,names=index,header=None)

img=cv2.imread(img_path)

cv2.namedWindow('image')
cv2.imshow("image",img)

#global var
r=g=b=xpos=ypos=0
clicked=False

