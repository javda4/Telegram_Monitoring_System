import cv2
import datetime as dt
from time import sleep


def image_monitor():
    video_capture = cv2.VideoCapture(0)

    while True:
        if not video_capture.isOpened():
            print('Unable to load camera.')
            sleep(5)
            break

        # Capture frame-by-frame
        ret, frame = video_capture.read()
        cv2.putText(frame, "Date: " + str(dt.datetime.now()), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        cv2.imwrite(filename='image.jpg', img=frame)
        print("Image Saved")
        print("Program End")
        break
    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
