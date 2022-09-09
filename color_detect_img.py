import cv2
import pandas as pd

img_path = r'colorful_image.jpg'
img = cv2.imread(img_path)
csv_path = 'colors.csv'

index = ['color', 'color_name', 'hex', 'R', 'G', 'B']

df = pd.read_csv(csv_path, names=index, header=None)


#print(img)

# global var
r = g = b = xpos = ypos = 0
clicked = False


def getColorName(R, G, B):
    minval = 10000
    for i in range(len(df)):
        z = abs(R-int(df.loc[i, 'R']))+abs(G -
                int(df.loc[i, 'G']))+abs(B-int(df.loc[i, 'B']))
        if z <= minval:
            minval = z
            colorName = df.loc[i, 'color_name']

    return colorName


def darwFunction(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global clicked, r, g, b, xpos, ypos
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('image')
cv2.setMouseCallback('image', darwFunction)


while True:
  cv2.imshow('image',img)
  if cv2.waitKey(20) & 0xFF==27:
      break
  
  if clicked:
    cv2.rectangle(img,(0,20),(600,60),(b,g,r),-1)
    text=getColorName(r,g,b)+' R='+str(r)+' G='+str(g)+' B='+str(b)
    if r+g+b>=600:
      cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
    else:
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    clicked=False

   

    



cv2.destroyAllWindows()
