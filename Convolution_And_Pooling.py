import cv2
import numpy
from matplotlib import pyplot as py

class Processing(object):
    def __init__(self,adress="images/cat.jpg"):
        self.img=cv2.imread(adress)
        self.Size()
        cv2.imshow("Main Image",self.img)

    def main(self):
        self.Convolution()
        self.Pooling(3,2)
        return self.GiveForNN()
        
    def Size(self):
 #       height=len(self.img)
 #       width=len(self.img[0])
 #        while height>640:
 #           height=height/1.25
 #       while width>360:
 #           width=width/1.25
        img = cv2.resize(self.img,(int(360),int(240)), interpolation = cv2.INTER_CUBIC)
        self.img=img
    
    def Convolution(self):
        actImg=[]
        img=self.img
        filt=[[0,1,0],[-1,0,-1],[0,1,0]]
        for i in range(len(img)-len(filt)):
            actImg.append([])
            for j in range(len(img[i])-len(filt)):
                total=0
                for k in range(len(img[i][j])):
                    for l in range(len(filt)):
                        for m in range(len(filt)):
                            total+=img[i+l][j+m][k]*filt[l][m]
                if total<0:#ReLu
                    total=0
                elif total>255:
                    total=255
                actImg[i].append(int(total))
        self.img=numpy.uint8(actImg)
        cv2.imshow("Convolution Image",self.img)

    def Pooling(self,slip,filt):
        img=self.img
        pool=[]
        for i in range(0,len(img)-filt,slip):
            pool.append([])
            for j in range(0,len(img[i])-filt,slip):
                max=0
                for k in range(filt):
                    for l in range(filt):
                        if max<img[i+k][j+l]:
                            max=img[i+k][j+l]
                pool[int(i/slip)].append(max)
        self.img=numpy.uint8(pool)
        cv2.imshow("Pooling Image",self.img)

    def GiveForNN(self):
        newImg=[]
        img=self.img
        for i in range(len(img)):
            for j in range(len(img[i])):
                newImg.append(img[i][j])
        return newImg
Processing().main()
