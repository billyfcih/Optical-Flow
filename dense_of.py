import cv2
import numpy as np

cap = cv2.VideoCapture("cars.mp4")

ret, frame1 = cap.read()
previous_frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[..., 1] = 255

while 1:
    _, frame2 = cap.read()
    next_frame = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(previous_frame, next_frame, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    hsv[..., 0] = ang*180/np.pi/2
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow('Dense optical flow', cv2.add(rgb, frame2))
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    previous_frame = next_frame

cap.release()
cv2.destroyAllWindows()
