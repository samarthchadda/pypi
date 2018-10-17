import cv2
import numpy as np


faceDetect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   #calling the classifier for face detection

#to capture image from webcam
cam=cv2.VideoCapture(0)   #0 is id for webcam


#creating recognizer again
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer/trainingData1.yml")

id=0
#font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,15,20,5,8)
font = cv2.FONT_HERSHEY_SIMPLEX


#now capturing frames one by one and detect the faces and showing in window
#creating a loop


while(1):
    count=0
    ret,img=cam.read()
    #img will be coloured but for classifier we need greyscale image
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #list for storing the faces
    faces=faceDetect.detectMultiScale(gray,1.3,5)   #this will detect all faces in current frame and return the coordinates of frame
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                #predicting user id of face
        id,config=rec.predict(gray[y:y+h,x:x+w])
        
        #printing that number below the face
        #cv2.putText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255)

    

        #to give name on face
        #if(id==1):
         #   id="SAMARTH"

        #elif(id==2):
         #   id="SAKSHAM"



        if(config<50):
            if(id==1):
                id="SAMARTH"
            elif(id==2):
                id="SAKSHAM"
            elif(id==4 and id==5):
                id="OBAMA"
        else:
            id="Unknown"


            
        cv2.putText(img,str(id),(x,y+h+20),font,0.55,(255,0,0),2)
        


    
    

    
    #showing image in another window
    cv2.imshow("Face",img)   #face is name of window

    if(cv2.waitKey(1)==ord('q')):
        break

    




cam.release()

cv2.destroyAllWindows()
