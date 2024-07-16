#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge,CvBridgeError
import numpy as np


def callback(img):
    bridge = CvBridge()
    frame = bridge.imgmsg_to_cv2(img, 'bgr8')
    frame = np.array(frame, dtype = np.uint8)
    cv2.imshow('Image', frame)
    cv2.waitKey(10)


rospy.init_node('image_viewer')
sub = rospy.Subscriber('/camera/rgb/image_raw', Image, callback)

rospy.spin()
