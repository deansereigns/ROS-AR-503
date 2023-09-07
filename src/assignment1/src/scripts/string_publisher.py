#!usr/bin/pyhton3

import rospy
from std_msgs.msg import String

def publisher_node():
    rospy.init_node("string_publisher",anonymous=True)
    string_publisher=rospy.Publisher("String_topic",String,queue_size=100)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        string_msgs = String()
        string_msgs = "Hello from Publisher"
        print(string_msgs)
        string_publisher.publish(string_msgs)
        rate.sleep()

if __name__=="__main__":
    try:
        publisher_node()
    except rospy.ROSInterruptExecption:
        pass