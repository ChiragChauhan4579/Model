import cv2
import numpy as np
import pickle

names = {0 : 'Mask',1 : 'Without Mask'}

svm = pickle.load(open('model.pickle','rb'))

haar_data = cv2.CascadeClassifier('./haar-cascade-files/haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)
data = []
font = cv2.FONT_HERSHEY_COMPLEX
i = 0
while True:
    flag,img = capture.read()
    if flag:
        faces = haar_data.detectMultiScale(img)
        for x,y,w,h in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,255), 4)
            face = img[y:y+h,x:x+w,:]
            face = cv2.resize(face,(50,50))
            face = face.reshape(1,-1)
            print(face.shape)
            pred = svm.predict(face)[0]
            i += 1
            if i<10:
                n = names[int(pred)]
                cv2.putText(img,n,(x,y),font,1,(255,0,255),2)
                print(n)
                res = n
            else:
                if res=='Without Mask':
                    print('No Entry')
                else:
                    print('Entry Granted')
        cv2.imshow('result',img)
        if cv2.waitKey(2) == 27:
            break
            
capture.release()
cv2.destroyAllWindows()