import cv2
import matplotlib.pyplot as plt
import numpy as np


img=cv2.imread("Kokusen.png",0)
img1=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img1,cmap="gray")

img=cv2.resize(img,(640,470))
img2=cv2.putText(img, "kopek", (150,300), cv2.FONT_HERSHEY_PLAIN, 5, (255,255,0))
cv2.imshow("yazili",img2)


_,thresh_img=cv2.threshold(img, thresh=50, maxval=255, type=cv2.THRESH_BINARY)
plt.figure(),plt.imshow(thresh_img,cmap="gray")


gb=cv2.GaussianBlur(img, ksize=(15,15),sigmaX=20) 
plt.figure(),plt.imshow(gb) ,plt.title("GB Kokusen")


laplacian=cv2.Laplacian(img, ddepth=cv2.CV_16S)
plt.figure(),plt.imshow(laplacian) ,plt.axis("off") ,plt.title("Laplacian"),plt.show()

img_hist=cv2.calcHist(img, channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.figure(),plt.plot( img_hist)

cv2.waitKey(0)
cv2.destroyAllWindows()