import cv2
import matplotlib.pyplot as plt


img=cv2.imread("Kokusen.png",0)
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(img) ,plt.axis("off") ,plt.title("KokuSen"),plt.show()

#x gradian
sobelx=cv2.Sobel(img, ddepth=cv2.CV_16S, dx=1, dy=0,ksize=5)
plt.figure(),plt.imshow(sobelx) ,plt.axis("off") ,plt.title("sobel x"),plt.show()


#y gradian
sobely=cv2.Sobel(img, ddepth=cv2.CV_16S, dx=0, dy=1,ksize=5)
plt.figure(),plt.imshow(sobely) ,plt.axis("off") ,plt.title("sobel Y"),plt.show()

#laplacian gradyan
laplacian=cv2.Laplacian(img, ddepth=cv2.CV_16S)
plt.figure(),plt.imshow(laplacian) ,plt.axis("off") ,plt.title("Laplacian"),plt.show()



