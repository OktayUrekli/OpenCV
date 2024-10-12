import cv2
import matplotlib.pyplot as plt

img=cv2.imread("doga.jpg")
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # görsel gri skalaya alındı

plt.figure()
plt.imshow(img,cmap="gray") # cmap = color map
plt.axis("off") # axisler kapatıldı
plt.show()


# eşikleme
_,thresh_img=cv2.threshold(img, thresh=100, maxval=255, type=cv2.THRESH_BINARY_INV)
# kaynak görsel, alt sınır , üst sınır, dönüşüm türü
# alt sınır ve üst sınır arasını girilen türe göre siyah ya da beyaz yapar
#type=cv2.THRESH_BINARY  = beyaz 
#type=cv2.THRESH_BINARY_INV = siyah
plt.figure()
plt.imshow(thresh_img,cmap="gray") 
plt.axis("off")
plt.show()



# uyarlamalı eşikleme - adaptive threshold

adp_thresh_img=cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV, 11, 8)
# kaynak görsel, üst sınır,yöntem , dönüşüm türü , komşu pixel sayısı, yöntemdeki C sabiti
plt.figure()
plt.imshow(adp_thresh_img,cmap="gray") 
plt.axis("off")
plt.show()

