import time, cv2

video = cv2.VideoCapture(0) # it trigers the video
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
        check, frame = video.read()
        print(check)
        print(frame)

        #time.sleep(2)
        faces = face_cascade.detectMultiScale(frame,
        scaleFactor = 1.05, minNeighbors = 5) # the function detects the coordinates of the detectef face
        for x,y,w,h in faces:
                frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (125,255,180),4)
        cv2.imshow("Capture",frame) #the first frame of the video is printed every 1 msec
        key = cv2.waitKey(1)
        if key == ord('q'):
                break

        
video.release()
cv2.destroyAllWindows()
