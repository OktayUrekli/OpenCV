import cv2
import matplotlib.pyplot as plt
import numpy as np


img=cv2.imread("Kokusen.png")
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

plt.figure(),plt.imshow(img) ,plt.axis("off") ,plt.title("KokuSen"),plt.show()

# ortalama bulanıklaştırma
dst1=cv2.blur(img, ksize=(15,15))
plt.figure(),plt.imshow(dst1) ,plt.axis("off") ,plt.title("KokuSenBlurred"),plt.show()



# Gaussian bulanıklaştırma
gb=cv2.GaussianBlur(img, ksize=(15,15),sigmaX=20) 
# sigmaY yazılmazsa otomatik olarak sigmaX ile eşit oluyor
plt.figure(),plt.imshow(gb) ,plt.axis("off") ,plt.title("GB Kokusen"),plt.show()

# Median bulanıklaştırma
mb=cv2.medianBlur(img, ksize=15) 
plt.figure(),plt.imshow(mb) ,plt.axis("off") ,plt.title("MB Kokusen"),plt.show()



# adding Noise
def gaussianNoise(image):
    row,col,ch=image.shape;
    mean=0
    var=0.05
    sigma=var**0.5
    
    gauss=np.random.normal(mean,sigma,(row,col,ch))
    gauss=gauss.reshape(row,col,ch)
    noisy=image+gauss
    
    return noisy


kokusen=cv2.imread("Kokusen.png")
kokusen=cv2.cvtColor(kokusen, cv2.COLOR_BGR2RGB) / 255

noisy_kokusen=gaussianNoise(kokusen)

plt.figure(),plt.imshow(noisy_kokusen) ,plt.axis("off") ,plt.title("KokuSen with Noise"),plt.show()

# noise + gauss blur

bluredNoise_kokusen=cv2.GaussianBlur(noisy_kokusen, ksize=(5,5),sigmaX=10) 
plt.figure(),plt.imshow(bluredNoise_kokusen) ,plt.axis("off") ,plt.title("bluredNoise_kokusen"),plt.show()



# salt pepper noise ekleme

def saltPepperNoise(image):
    row,col,ch=image.shape;
    salt_rate=0.5
    pepper_rate=1-salt_rate
    
    amount=0.004
    
    spNoisy=np.copy(image)
    
    # salt ekleme
    num_of_salt=np.ceil(salt_rate*image.size*amount)
    coordinates=[np.random.randint(0,i-1,int(num_of_salt) )for i in image.shape]
    spNoisy[coordinates]=1 # 1 beyaza denk geliyor
    
    # pepper ekleme
    num_of_pepper=np.ceil(pepper_rate*image.size*amount)
    coordinates=[np.random.randint(0,i-1 ,int(num_of_pepper))for i in image.shape]
    spNoisy[coordinates]=0 # 0 siyaha denk geliyor

    return spNoisy

spImage=saltPepperNoise(kokusen) 
plt.figure(),plt.imshow(spImage) ,plt.axis("off") ,plt.title("saltPepper_kokusen"),plt.show()

mb2=cv2.medianBlur(spImage.astype(np.float32), ksize=15) 
plt.figure(),plt.imshow(mb2) ,plt.axis("off") ,plt.title("MB+SP Kokusen"),plt.show()


