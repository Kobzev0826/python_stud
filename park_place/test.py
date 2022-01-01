import cv2

camera = cv2.VideoCapture("test_images/parking.mp4")
car_cascade = cv2.CascadeClassifier('cars.xml')

# Get frames per second from video file. Syntax depends on OpenCV version:
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
if int(major_ver)  < 3 :
    fps = camera.get(cv2.cv.CV_CAP_PROP_FPS)
else :
    fps = camera.get(cv2.CAP_PROP_FPS)
#:if
intTimeToNextFrame=int(1000.0/fps)-12 # '-12' estimation of time for processing
while True:
    (grabbed,frame) = camera.read()
    grayvideo = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(grayvideo, 1.1, 1)
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),1)
    cv2.imshow("video",frame)
    if cv2.waitKey(intTimeToNextFrame)== ord('q'):
        break
camera.release()
cv2.destroyAllWindows()