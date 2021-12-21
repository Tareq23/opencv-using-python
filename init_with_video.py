import cv2


# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
# print(cap.isOpened())

# while(True):
while cap.isOpened() :
    ret, frame = cap.read()

    if ret == True :
        # width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        # height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        # print(height)
        # print(width)
        # print("frame : ",cap.get(7))

        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('gray color frame',gray)

        cv2.imshow('video frame',frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()