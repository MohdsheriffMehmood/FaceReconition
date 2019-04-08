import cv2

img=cv2.imread('Luffy.jpg')

cv2.imshow('original',img)
cv2.waitKey(0)

gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)# this method convert the original image into grayscale by cvtCOLOR() method.

cv2.imshow('Gray image',gray_image)
cv2.waitKey(0)

# converting RGB into Binary image

ret,bw=cv2.threshold(img,127,255,cv2.THRESH_BINARY)# this method return the tuple value that's why we have to take two values
cv2.imshow('Binary_image',bw)

cv2.waitKey(0)

img_HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HVE',img_HSV)
cv2.waitKey(0)

cv2.imshow('HVE',img_HSV[:,:,0])
cv2.waitKey(0)
cv2.imshow('HVE',img_HSV[:,:,1])
cv2.waitKey(0)
cv2.imshow('HVE',img_HSV[:,:,2])
cv2.waitKey(0)
cv2.destroyAllWindows()



