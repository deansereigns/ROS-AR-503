#!usr/bin.python3

import rospy
from std_msgs.msg import Float32

def callback(msg):
    rospy.loginfo("Received Float value by Subscriber 1: %f",msg.data)

def subscriber_node():
    rospy.init_node("subscriber_1",anonymous=True)
    rospy.Subscriber("float_topic",Float32,callback)
    rospy.spin()

if __name__=="__main__":
    try:
        subscriber_node()
    except rospy.ROSInterruptException:
        pass