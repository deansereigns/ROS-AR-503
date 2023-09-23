#! /usr/bin/python3

import rospy
import tf

if __name__=="__main__":
    rospy.init_node('custom_tf_listener')

    listener = tf.TransformListener()

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        try:
            (transfor,rotation) = listener.lookupTransform('/world','/link_3',rospy.Time(0))
        except (tf.LookupException,tf.ConnectivityException,tf.ExtrapolationException):
            continue
    
    print(transfor,rotation)
    rate.sleep()
