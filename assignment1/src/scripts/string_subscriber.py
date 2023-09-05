#!usr/bin.python3

import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("Received Message: %s",msg.data)

def subscriber_node():
    rospy.init_node("String_subscriber",anonymous=True)
    rospy.Subscriber("String_topic",String,callback)
    rospy.spin()

if __name__=="__main__":
    try:
        subscriber_node()
    except rospy.ROSInterruptException:
        pass