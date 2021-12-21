import numpy as np
import cv2

print("Drawing function using opencv")

img = np.zeros([512,512,3],np.uint8)
# img = cv2.imread('lena.jpg',0)
# img = cv2.imread('lena.jpg',1)



# img = cv2.line(img,start_point_tuple,end_point_tuple,rgb_color,thickness,line_type)
img = cv2.line(img,(0,0),(255,255),(255,0,0),10,cv2.LINE_AA)

#img = cv2.circle(img,center_point_tuple,radius,thickness,line_type)
# if circle thickness -1 then fill circle with provided color
img = cv2.circle(img,(255,255),50,(0,0,255),5,cv2.LINE_8)
img = cv2.arrowedLine(img,(0,125),(350,125),(0,225,0),4,cv2.LINE_AA)
img = cv2.rectangle(img,(330,330),(480,480),(112,255,0),5)

cv2.imshow('Image showing',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

