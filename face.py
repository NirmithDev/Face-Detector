import cv2

# load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# choose an image for the code to detect a face in
img=cv2.imread('pic3.png')
print("Image Opened")
# (''->name of the window name,image name) this will show the image in the window of whose you want it to be
cv2.imshow('Face Detector',img)

# We need to make it grey scaled and much more appealing and available for the haar cascade algorithm to work


print("Image Opened")
# pauses the execution of the code otherwise it will close as soon as it opens
cv2.waitKey()



print("Code Completed")