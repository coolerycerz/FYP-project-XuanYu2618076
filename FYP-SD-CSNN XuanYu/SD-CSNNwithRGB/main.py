import cv2

# reading the image
img = cv2.imread('P0001.png')
# convert to greyscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# create SIFT feature extractor
#sift = cv2.xfeatures2d.SIFT_create()
sift = cv2.SIFT_create()
# detect features from the image
keypoints, descriptors = sift.detectAndCompute(img, None)
# draw the detected key points
sift_image = cv2.drawKeypoints(gray, keypoints, img, 256)
# show the image
cv2.imshow('image', sift_image)
# save the image
cv2.imwrite("1111.jpg", sift_image)
cv2.waitKey(0)
cv2.destroyAllWindows()