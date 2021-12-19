import cv2

# img = cv2.imread('lena.jpg',0)// using 0 to read greyScale mode
# img = cv2.imread('lena.jpg',1) # using 1 to read color mode
# img = cv2.imread('lena.jpg',0) #
# print(img)
#
# cv2.imshow('image',img)
# # cv2.waitKey(5000)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


img = cv2.imread('lena.jpg',0)

cv2.imshow('image',img)

wait_key = cv2.waitKey(0)


if wait_key == 27:
    cv2.destroyAllWindows()
elif wait_key == ord('s'):
    cv2.imwrite('lena_copy.png',img)
    cv2.destroyAllWindows()
