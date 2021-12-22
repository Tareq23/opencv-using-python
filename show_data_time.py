import cv2
import datetime

print('show date time on video')

vid_cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
vid_cap.set(cv2.CAP_PROP_FRAME_WIDTH,1080)
vid_cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
text = 'Width : '+str(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + '\nHeight : ' + str(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while vid_cap.isOpened():
    ret, frame = vid_cap.read()

    if (ret == True):
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width : ' + str(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + ' Height : ' + str(
            vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        color = (0,255,100)
        thickness = 2
        fontScale = 1
        # date_time = str(datetime.datetime.now().time)
        # date_time = str(datetime.date.today())
        date_time = str(datetime.datetime.now().strftime("%H:%M:%S"))
        cv2.putText(frame,text,(10,50),font,fontScale,color,thickness,cv2.LINE_AA)
        cv2.putText(frame,date_time,(10,100),font,fontScale,color,thickness,cv2.LINE_AA)
        window_name = 'Color Video Frame'



        # cv2.imshow('Color Video Frame', frame)
        cv2.imshow(window_name,frame)
        # cv2.imshow('Gray video frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

vid_cap.release()
cv2.destroyAllWindows()