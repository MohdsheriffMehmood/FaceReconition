import cv2

#cv2.imread(),cv2 is a class and imread() is a method
# which fetch the image in the form of array or matrix
# in the matrix there are pixels of image in it.
img=cv2.imread('Luffy.jpg')

#imshow() method show the image.

cv2.imshow('Output Image',img)

cv2.imwrite('Output.jpg',img)# this method write the image in the form of png in the vary project folder.

cv2.imwrite('Output.png',img)# this also does the same thing

# how to get image information
print(img.shape)
print('Height of pixel',img.shape[0],'Width of pixel',img.shape[1],'Scale of pixel',img.shape[2])



cv2.waitKey(0)
cv2.destroyAllWindows()