import cv2
def click_events(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONUP:
        strXY=str(x)+','+str(y)
        cv2.putText(frame,strXY,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2,cv2.LINE_AA)
        cv2.imshow('Position Tracker',frame)
        print(x,y)
frame=cv2.imread('image1.webp',-1)
cv2.imshow('Position Tracker',frame)
cv2.setMouseCallback('Position Tracker',click_events)
cv2.waitKey(0)
cv2.destroyAllWindows()