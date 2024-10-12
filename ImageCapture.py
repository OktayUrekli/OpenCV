import cv2 

# Resmi içe aktarma 
img=cv2.imread("sukuna.png",0) # image read kısaltmasıdır

#ekrana çıktı vermepython -m pip install
cv2.imshow("sukuna",img)

keyForClose=cv2.waitKey(0) & 0xFF

if keyForClose==27: # esc ascii code
    cv2.destroyAllWindows()
elif keyForClose==ord("s"):
    cv2.imwrite("sukunaGrey.png", img)
    cv2.destroyAllWindows()




