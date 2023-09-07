#!usr/bin.python3

import rospy
from std_msgs.msg import Float32

def callback(msg):
    rospy.loginfo("Average: %f",msg.data)

def subscriber_node():
    rospy.init_node("avg_subsciber",anonymous=True)
    rospy.Subscriber("avg_topic",Float32,callback)
    rospy.spin()

if __name__=="__main__":
    try:
        subscriber_node()
    except rospy.ROSInterruptException:
        pass