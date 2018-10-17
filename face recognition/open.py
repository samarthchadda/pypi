import cv2
import numpy as np


faceDetect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   #calling the classifier for face detection

#to capture image from webcam
cam=cv2.VideoCapture(0)   #0 is id for webcam


#now capturing frames one by one and detect the faces and showing in window
#creating a loop


while(1):
	ret,img=cam.read()
	#img will be coloured but for classifier we need greyscale image
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#list for storing the faces
	faces=faceDetect.detectMultiScale(gray,1.3,5)   #this will detect all faces in current frame and return the coordinates of frame
	for(x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

	#showing image in another window
	cv2.imshow("Face",img)   #face is name of window

	if(cv2.waitKey(1)==ord('q')):
		break


cam.release()

cv2.destroyAllWindows()