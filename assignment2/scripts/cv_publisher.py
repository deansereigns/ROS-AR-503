#!/usr/bin/python3

import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np

def camera_publisher():
    rospy.init_node('camera_publisher', anonymous=True)
    pub = rospy.Publisher('camera/image_raw', Image, queue_size=10)
    rate = rospy.Rate(30)  # Adjust the publishing rate as needed

    cap = cv2.VideoCapture(0)  # Use 0 for the default camera (change as needed)
    bridge = CvBridge()

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret:
            img_msg = bridge.cv2_to_imgmsg(frame, "bgr8")
            pub.publish(img_msg)

        rate.sleep()

if __name__ == '__main__':
    try:
        camera_publisher()
    except rospy.ROSInterruptException:
        pass