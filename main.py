import cv2
from PIL import Image
from util import get_limits

blue = [255,0,0]  # red in BGR colorspace

cap = cv2.VideoCapture(0)

while True :
    ret , frame = cap.read()
    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

    lower , upper = get_limits(blue)
    mask = cv2.inRange(hsv , lower ,upper )

    maskP = Image.fromarray(mask)
    bbox = maskP.getbbox()
    #print(bbox)

    if bbox is not None :
        x1 , y1 , x2 , y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1) , (x2 , y2 ) , ( 0 , 255 , 0 ) , 4 )

    cv2.imshow('FRAME ', frame)
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()