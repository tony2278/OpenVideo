
#coding=utf-8

#使用python播放视频文件
import numpy as np
import cv2

cap = cv2.VideoCapture('D:/Workspace/OpenVideo/负样本（主码）.mp4')

while (cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

