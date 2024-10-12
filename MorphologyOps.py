import cv2
import matplotlib.pyplot as plt
import numpy as np


img=cv2.imread("logo1.png",0)

plt.figure(),plt.imshow(img,cmap="gray") ,plt.axis("off") ,plt.title("Logo"),plt.show()

#erezyon
kernel=np.ones((5,5),np.uint8)
result=cv2.erode(img, kernel,iterations=2)

plt.figure(),plt.imshow(result,cmap="gray") ,plt.axis("off") ,plt.title("Erezyon"),plt.show()

#genişleme
result2=cv2.dilate(img, kernel,iterations=2)

plt.figure(),plt.imshow(result2,cmap="gray") ,plt.axis("off") ,plt.title("Genişleme"),plt.show()


# beyaz gürültü
whiteNoise=np.random.randint(0,2,img.shape[:2])
whiteNoise=whiteNoise*255

noise_img=whiteNoise+img
plt.figure(),plt.imshow(noise_img,cmap="gray") ,plt.axis("off") ,plt.title("Beyaz Gürültülü"),plt.show()

#açılma
open_img=cv2.morphologyEx(noise_img.astype(np.float32),cv2.MORPH_OPEN , kernel)
plt.figure(),plt.imshow(open_img,cmap="gray") ,plt.axis("off") ,plt.title("Açılma"),plt.show()


# siyah gürültü
blackNoise=np.random.randint(0,2,img.shape[:2])
blackNoise=blackNoise*-255
blck_noise_img=blackNoise+img
blck_noise_img[blck_noise_img<=-245]=0
plt.figure(),plt.imshow(blck_noise_img,cmap="gray") ,plt.axis("off") ,plt.title("Siyah Gürültülü"),plt.show()

# kapatma
close_img=cv2.morphologyEx(blck_noise_img.astype(np.float32),cv2.MORPH_CLOSE , kernel)
plt.figure(),plt.imshow(close_img,cmap="gray") ,plt.axis("off") ,plt.title("Kapatma"),plt.show()

# morfolojik gradient
morp_grad_img=cv2.morphologyEx(img,cv2.MORPH_GRADIENT , kernel)
plt.figure(),plt.imshow(morp_grad_img,cmap="gray") ,plt.axis("off") ,plt.title("Morp_Grad"),plt.show()


