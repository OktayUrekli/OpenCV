import cv2

# kamera açma

cap=cv2.VideoCapture(0) # 0 kameranın indexini temsil eder

width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # video genişliği
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # video yüksekliği

print(width,height)

writer=cv2.VideoWriter("video_kayit.mp4", cv2.VideoWriter_fourcc(*"DIVX"),20,(width, height)) 
#                       video ismi      - windows için kayıt parametresi -fps- video ölçüleri

while True:
    ret , frame=cap.read()
    cv2.imshow("video", frame)
    
    # video kayıt etme
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF==ord("q"): break

cap.release()
writer.release()
cv2.destroyAllWindows()