import cv2
import matplotlib.pyplot as plt
import numpy as np


img=cv2.imread("Kokusen.png")
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

plt.figure(),plt.imshow(img) ,plt.title("KokuSen"),plt.show()


img_hist=cv2.calcHist(img, channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.figure(),plt.plot( img_hist)

color=("b","g","r")
plt.figure()
for i,c in enumerate(color):
    hist=cv2.calcHist(img, channels=[0], mask=None, histSize=[256], ranges=[0,256])
    plt.plot( hist,color=c)
    
    
    
# maskeleme
fight=cv2.imread("fight.png")
fight=cv2.cvtColor(fight, cv2.COLOR_BGR2RGB)

maske= np.zeros(fight.shape[:2],np.uint8)
plt.figure(),plt.imshow(maske,cmap="gray"),plt.title("maske")

maske[300:800,500:1000]=255

masked_fight_img=cv2.bitwise_and(fight, fight,mask=maske)
plt.figure(),plt.imshow(masked_fight_img,cmap="gray"),plt.title("masked Fight")

masked_fight_img_hist=cv2.calcHist([masked_fight_img], channels=[0], mask=maske, histSize=[256], ranges=[0,256])
plt.figure(),plt.plot(masked_fight_img_hist),plt.title("masked Fight hist")



# histogram eşitleme
# kontras arttırma

doga=cv2.imread("doga.jpg",0)
plt.figure(),plt.imshow(doga,cmap="gray") ,plt.title("doga"),plt.show()


doga_hist=cv2.calcHist([doga], channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.figure(),plt.plot( img_hist),plt.title("doga hist"),plt.show()

eql_doga=cv2.equalizeHist(doga)
plt.figure(),plt.imshow(eql_doga,cmap="gray"),plt.title("eql doga"),plt.show()

doga_eql_hist=cv2.calcHist([eql_doga], channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.figure(),plt.plot( doga_eql_hist),plt.title("doga eql hist"),plt.show()


