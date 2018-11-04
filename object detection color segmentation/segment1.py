import cv2
import numpy as np




#lower and upper boundary values for green
lowerBound=np.array([33,80,40])
upperBound=np.array([102,255,255])



cam=cv2.VideoCapture(0)

kernelOpen=np.ones((5,5))       
kernelClose=np.ones((20,20))    #close larger holes

font = cv2.FONT_HERSHEY_SIMPLEX


while True:
    ret,img=cam.read()
    img=cv2.resize(img,(400,350))

    #converting image in BGR to HSV format
    imgHsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    #filtering green portion of image  i.i.  creating a mask
    mask=cv2.inRange(imgHsv,lowerBound,upperBound)


    #morphology (removing that dotted pixels)
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)  #remove dots outside image  
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)   #remove dots inside image

    
    maskFinal=maskClose
    _,conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    cv2.drawContours(img,conts,-1,(255,0,0),3)      #blue boundary arround objects of thickness 3
    for i in range(len(conts)):
        x,y,w,h=cv2.boundingRect(conts[i])           
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)         #drawing rectangles
        cv2.putText(img,str(i+1),(x,y+h+20),font,0.55,(0,255,255),2)

    
    
    cv2.imshow("Mask",mask)
    cv2.imshow("Cam",img)
    cv2.imshow("MaskOpen",maskOpen)
    cv2.imshow("MaskClose",maskClose)
    
    cv2.waitKey(10)




    
