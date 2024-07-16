#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge,CvBridgeError
import numpy as np

import message_filters


def callback(left, right):
    bridge = CvBridge()
    frame = bridge.imgmsg_to_cv2(left, 'bgr8')
    frame = np.array(frame, dtype = np.uint8)
    cv2.imshow('left', frame)
    frame = bridge.imgmsg_to_cv2(right, 'bgr8')
    frame = np.array(frame, dtype = np.uint8)
    cv2.imshow('right', frame)
    cv2.waitKey(10)


rospy.init_node('image_viewer1')
left = message_filters.Subscriber('/multisense_sl/camera/left/image_raw', Image)


# rospy.init_node('image_viewer2')
right = message_filters.Subscriber('/multisense_sl/camera/right/image_raw', Image)


ts = message_filters.TimeSynchronizer([left, right], 10)
ts.registerCallback(callback)

rospy.spin()
