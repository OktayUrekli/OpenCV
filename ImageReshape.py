import cv2 

img=cv2.imread("Kokusen.png")
print("Resim Boyutu",img.shape)

# resim yeniden boyutlandırma
imgResized=cv2.resize(img,(400,400))
print("Yeniden şekilllenmiş resim Boyutu",imgResized.shape)
cv2.imshow("kokusen", imgResized)


# resim kırpma
imgCroped=img[:300,:500]
cv2.imshow("kokusenCroped", imgCroped)

cv2.waitKey(0)
cv2.destroyAllWindows()