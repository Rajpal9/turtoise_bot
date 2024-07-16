#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import numpy as np

import message_filters

def callback(left,right):
    bridge = CvBridge()
    frame = bridge.imgmsg_to_cv2(left, 'bgr8')
    frame = np.array(frame, dtype=np.uint8)
    cv2.imshow('left', frame)
    cv2.waitKey(10)

    bridge = CvBridge()
    frame = bridge.imgmsg_to_cv2(right, "32FC1")
    frame = np.array(frame)
    cv2.imshow('right', frame)
    cv2.waitKey(10)





rospy.init_node('image_viewer')

left = message_filters.Subscriber('/depth_camera/color/image_raw', Image)

right = message_filters.Subscriber('/depth_camera/depth/image_raw', Image)

ts = message_filters.TimeSynchronizer([left, right], 10)
ts.registerCallback(callback)


rospy.spin()


