import os
import cv2
import numpy as np
from PIL import Image  #as we are capturing the images


# recognizer = cv2.createLBPHFaceRecognizer()
recognizer=cv2.face.LBPHFaceRecognizer_create()    #creating a recognizer

# recognizer = cv2.face.LBPHFaceRecognizer_create()

#path of samples
path='dataSet'

def getImagesWithID(path):
    #list for all images in folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]   # "for part" is fetching the images and putting in f, and then join method appending it to path   
    # print(imagePaths)	

    #looping for all the images
    faces=[]
    ids=[]

    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L')  #opening the image and L means converting to grayscale(although already converted)
        #now the faceImg is PIL(python image library) but opencv works with numpy array
        faceNp=np.array(faceImg,'uint8')    #unit8(unsigned int 8) is conversion format
        #getting user id of images  i.e. name of images
        ID=int(os.path.split(imagePath)[-1].split('.')[1])   #splitting the path, -1 denotes last part of path (ex-   user.1.1.jpg)
        faces.append(faceNp)
        print(ID)
        ids.append(ID)
        cv2.imshow("Training",faceNp)   #to see captured image
        cv2.waitKey(10)

    return(np.array(ids),faces)   #ids is integer array, but we need numpy array


ids,faces=getImagesWithID(path)

#to train the recognizer , we need face samples and corresponding levels
recognizer.train(faces,ids)
recognizer.save('recognizer/trainingData1.yml')
cv2.destroyAllWindows()

  
        
        
        
        
        
                



	
