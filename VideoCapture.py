import cv2
import time

video_name="ToyRocketDevLog_3.mp4"

#video içe aktarma
capture=cv2.VideoCapture(video_name)

print("Genişlik: ",capture.get(3)) # 3 video genişlik indexidir
print("Yükseklik: ",capture.get(4))# 4 video yükseklik indexidir

if capture.isOpened()==False: print("Video Açılmadı") # video boş mu değil mi kontrolü

while True:
    ret , frame=capture.read()
    
    if ret==True:
        time.sleep(0.01)
        cv2.imshow("video", frame)
    else: break
    
    if cv2.waitKey(1) & 0xFF==ord("q"): break

capture.release()
cv2.destroyAllWindows()