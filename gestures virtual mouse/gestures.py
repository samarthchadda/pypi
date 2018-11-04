import cv2
import numpy as np
from pynput.mouse import Button,Controller   #button will select which mouse button left or rightor middle, controller will blink mouse movement mouse operation 
import wx


#mouse object
mouse=Controller()

#screen size of monitor
app=wx.App(False)
(sx,sy)=wx.GetDisplaySize()    #this will give size of our monitor
(camx,camy)=(320,240)               #camera will capture image in this resolution




#lower and upper boundary values for green
lowerBound=np.array([33,80,40])
upperBound=np.array([102,255,255])



cam=cv2.VideoCapture(0)
cam.set(3,camx)      #setting the resolution
cam.set(4,camy)


kernelOpen=np.ones((5,5))       
kernelClose=np.ones((20,20))    #close larger holes

#dampening , it will not allow mouse to move very rapidly i.e. we dampen the movement
mlocOld=np.array([0,0])
mouseLoc=np.array([0,0])     #mouse cordinate after dampening

dampingFactor=2     #can be changed accordingly , but  should be >1


pinchFlag=0




while True:
    ret,img=cam.read()
    #img=cv2.resize(img,(400,350))

    #converting image in BGR to HSV format
    imgHsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    #filtering green portion of image  i.i.  creating a mask
    mask=cv2.inRange(imgHsv,lowerBound,upperBound)


    #morphology (removing that dotted pixels)
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)  #remove dots outside image  
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)   #remove dots inside image

    
    maskFinal=maskClose
    _,conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    

    if(len(conts)==2):              #means two objects i.e. open position

        if(pinchFlag==1):

            pinchFlag=0
            mouse.release(Button.left)
        
        x1,y1,w1,h1=cv2.boundingRect(conts[0])
        x2,y2,w2,h2=cv2.boundingRect(conts[1])
        cv2.rectangle(img,(x1,y1),(x1+w1,y1+w1),(255,0,0),2)
        cv2.rectangle(img,(x2,y2),(x2+w2,y2+w2),(255,0,0),2)
        
        #finding centre of each object
        cx1=int(x1+w1/2)
        cy1=int(y1+h1/2)

        cx2=int(x2+w2/2)
        cy2=int(y2+h2/2)

        #finding centre of line
        cx=int((cx1+cx2)/2)
        cy=int((cy1+cy2)/2)
        
        

        #creating line at centre
        cv2.line(img,(cx1,cy1),(cx2,cy2),(255,0,0),2)
        #dot at centre of line
        cv2.circle(img,(cx,cy),2,(0,0,255),3)                   #2 is here radius , small as dot (3rd parameter)
        
        #mouseLoc=mlocOld+(targetLoc-mlocOld)/damingFactor
        mouseLoc=mlocOld+((cx,cy)-mlocOld)/dampingFactor


        #mouse movement
        mouse.position=(sx-(mouseLoc[0]*sx/camx),mouseLoc[1]*sy/camy)   #this will convert  camera coordinates to screen coordinates

        if mouse.position!=(sx-(mouseLoc[0]*sx/camx),mouseLoc[1]*sy/camy):
           pass          #waiting for mouse to be in above position
        

        mlocOld=mouseLoc

        
    
    elif(len(conts)==1):                    #only one object i.e close

        if(pinchFlag==0):

            pinchFlag=1
            #when fingers are joined, then mouse is clicked
            mouse.press(Button.left)
            
        
        x,y,w,h=cv2.boundingRect(conts[0])
        cv2.rectangle(img,(x,y),(x+w,y+w),(255,0,0),2)
        cx=int(x+w/2)
        cy=int(y+h/2)
        cv2.circle(img,(cx,cy),int((w+h)/4),(0,0,255),3)

        
        mouseLoc=mlocOld+((cx,cy)-mlocOld)/dampingFactor

        #mouse movement
        mouse.position=(sx-(mouseLoc[0]*sx/camx),mouseLoc[1]*sy/camy)   #this will convert  camera coordinates to screen coordinates

        if mouse.position!=(sx-(mouseLoc[0]*sx/camx),mouseLoc[1]*sy/camy):
           pass          #waiting for mouse to be in above position
        

        mlocOld=mouseLoc


      

        

    
    
    #cv2.imshow("Mask",mask)
    #cv2.imshow("MaskOpen",maskOpen)
    #cv2.imshow("MaskClose",maskClose)
    cv2.imshow("Cam",img)
    
    cv2.waitKey(5)




    
