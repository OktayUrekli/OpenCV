import cv2
import numpy as np

# siyah bir resim oluşturma
blackImg=np.zeros((512,512,3),np.uint8)

cv2.imshow("Siyah", blackImg)

# görsel üzerine çizgi çizdirme
cv2.line(blackImg, (100,100), (450,450), (0,0,255),5)
#    üzerine çizilecek resim , (başlangıç konumu) ,(bitiş konumu), rengi, kalınlığı
cv2.imshow("Cizgili siyah", blackImg)

# dikdörtgen çizdirme 
cv2.rectangle(blackImg,(200,200),(300,300), (255,0,0), cv2.FILLED)
#üzerine çizilecek resim ,(başlangıç konumu),(bitiş konumu),rengi,içi dolu mu boşmu
cv2.imshow("Dikdortgen", blackImg)

# çember çizdirme 
cv2.circle(blackImg,(150,325),25, (0,255,0), cv2.FILLED)
#üzerine çizilecek resim ,(merkez konumu),çapı,rengi,içi dolu mu boşmu
cv2.imshow("cember", blackImg)

# metin yazdırma
cv2.putText(blackImg, "oktay", (150,300), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (150,150,150))
#üzerine çizilecek resim ,metin,(başlangıç konumu),font,yazı büyüklüğü,rengi
cv2.imshow("metin", blackImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
