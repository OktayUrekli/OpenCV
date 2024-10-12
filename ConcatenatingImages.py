import cv2
import numpy as np

img=cv2.imread("Kokusen.png")

imgResized=cv2.resize(img,(576,324))

cv2.imshow("kucukImg", imgResized)


#yatay birleştirme
horConcat=np.hstack((imgResized,imgResized))
cv2.imshow("Yatay", horConcat)

#dikey birleştirme
verConcat=np.vstack((imgResized,imgResized))
cv2.imshow("Dikey Img", verConcat)


cv2.waitKey(0)
cv2.destroyAllWindows()