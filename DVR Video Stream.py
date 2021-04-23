#!/bin/python
#### in rtsp server:
####  ffserver -f /etc/ffserver.conf &
#### ffmpeg -f v4l2 -i /dev/video0  -s 640x480 -r 24 -vcodec libx264 -an http://127.0.0.1:8090/feed1.ffm
#### sudo apt install python-opencv
import cv2

cap = cv2.VideoCapture("rtsp://admin:Alzaabix4@192.168.1.114:554/Streaming/Channels/202")
if cap.isOpened() :
  ret,frame=cap.read()
#  print "==== ret ===="
#  print ret
#  print "====print dir(frame)===="
#  print dir(frame)
#  print "====print frame.shape===="
#  print frame.shape
#  print "====print (frame.shape[0], frame.shape[1], frame.shape[2])===="
#  print (frame.shape[0], frame.shape[1], frame.shape[2])
#  print "====print frame.size===="
#  print frame.size
#  print "====print frame.data===="
##  print frame.data
#  print type(frame.data)
#  print "====print frame.copy===="
#  print frame.copy
#  print type(frame.copy)
#  print "====print frame.ctypes===="
##--------------------------------------------------------------------------------------------------------------------
## ! ! Frame.ctypes.data_as(c_char_p/c_void_p/...) can convert the image read by python opencv into
 ## C language is a format that is useful when passing parameters to a C library in Python.
 ## frame.ctypes.data_as(c_char_p): Convert the memory address of one frame of image to C language char* type
##---------------------------------------------------------------------------------------------------------------------
#  print frame.ctypes
#  print type(frame.ctypes)
##  print "====print frame.imag===="
##  print frame.imag
#  print type(frame.imag)
#  print "====print frame.tobytes===="
#  print frame.tobytes
#  print type(frame.tobytes)

##cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,640)
##cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,480)
while cap.isOpened():
    ret,frame=cap.read()
#        print ret
#        print dir(frame)
#        print frame.shape
    print (frame.shape[0], frame.shape[1], frame.shape[2])
#        print frame.size
#        print frame.data
    cv2.imshow("frame",frame)
    cv2.waitKey(10)
