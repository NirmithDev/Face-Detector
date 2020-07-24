import cv2
from random import randrange
# load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# choose an image for the code to detect a face in
img=cv2.imread('pic7.png')
print("Image Opened")
#to capture the video from webcam
webcam=cv2.VideoCapture(0)

# Iterate Through Faces
while True:
    #read the current frame
    successful_frame_read,frame=webcam.read()
    # We need to make it grey scaled and much more appealing and available for the haar cascade algorithm to work
    grayscale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscale)
    # draw rectangles around the faces
    # here is what each parameter in this inbuilt function is img is the image x,y are the coordinates x+w y+h are also
    # coordinates then the next parameter is color code for the rectangle where mine is white ofcourse and the lat one is
    # the border size
    # We Use The Frame Mainly Cuz We Need The Circle To Come Onto The Face Rather Than To Come On To The Images Face In The Previous Test
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w+5,y+h+5),(0,255,0),4)

    # Show face from the webcam
    cv2.imshow('Face Detector',frame)
    key=cv2.waitKey(1)

    #to break outta the dame repetitive statement
    if key==81 or key==113:
        break

#release the Videocapture object
webcam.release()

print("Code Completed")