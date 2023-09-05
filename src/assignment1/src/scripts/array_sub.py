#!usr/bin.python3

import rospy
from std_msgs.msg import Float32MultiArray

def callback(msg):
    rospy.loginfo(msg.data)

def subscriber_node():
    rospy.init_node("subscriber_1",anonymous=True)
    rospy.Subscriber("float_topic",Float32MultiArray,callback)
    rospy.spin()

if __name__=="__main__":
    try:
        subscriber_node()
    except rospy.ROSInterruptException:
        pass