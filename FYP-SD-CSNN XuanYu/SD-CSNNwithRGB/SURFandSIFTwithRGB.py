import cv2
import numpy as np

# read image
img = cv2.imread('road24.png')

# turn gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#if you want to use surf key point extraction, please change here
sift = cv2.SIFT_create()
#surf = cv2.SIFT_create()
# key point
keypoints, descriptors = sift.detectAndCompute(img, None)
#keypoints, descriptors = surf.detectAndCompute(img, None)

# RGB filter
mask = 255 * np.ones(gray.shape, dtype=np.uint8)
lower_black = np.array([0, 0, 0], dtype=np.uint8)
upper_black = np.array([225, 225, 26], dtype=np.uint8)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask_bg = cv2.inRange(hsv, lower_black, upper_black)
mask = cv2.bitwise_and(mask, mask_bg)
gray_filtered = cv2.bitwise_and(gray, gray, mask=mask)
keypoints_filtered, descriptors_filtered = sift.detectAndCompute(gray_filtered, None)

# filter key points become red
sift_image_filtered = cv2.drawKeypoints(gray_filtered, keypoints_filtered, img, color=(0, 0, 255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# plot show
cv2.imshow('image', sift_image_filtered)
# save
cv2.imwrite("24_filtered.jpg", sift_image_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
