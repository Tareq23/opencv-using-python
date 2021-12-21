import cv2


vid_cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

print("WIDTH : ",cv2.CAP_PROP_FRAME_WIDTH)
print("HEIGHT : ",cv2.CAP_PROP_FRAME_HEIGHT)
print("width : ",vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("height : ",vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# vid_cap.set(3,1080) here 3 means cv2.CAP_PROP_FRAME_WIDTH
# vid_cap.set(4,720) here 4 means cv2.CAP_PROP_FRAME_HEIGHT

vid_cap.set(cv2.CAP_PROP_FRAME_WIDTH,1080)
vid_cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while vid_cap.isOpened():

    ret, frame = vid_cap.read()

    if (ret == True):
        cv2.imshow("frame",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break


vid_cap.release()
cv2.destroyAllWindows()