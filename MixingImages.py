import cv2
import matplotlib.pyplot as plt


img1=cv2.imread("fight.png")
img1=cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) # default olarak resim BGR türünde gelir
# BGR dan RGB ye dönüştürme kodu

img2=cv2.imread("sukuna.png")
img2=cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# resimleri karıştırma
blended=cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.5, gamma=0)
#kaynak1,kaynak1 alpha oranı ,kaynak2, kaynak2 beta oranı, gamma oranı

plt.figure()
plt.imshow(blended)

