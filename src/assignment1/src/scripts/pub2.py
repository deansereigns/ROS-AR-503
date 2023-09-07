#!usr/bin/pyhton3

import rospy
import random
from std_msgs.msg import Float32

def publisher_node():
    rospy.init_node("float_publisher2",anonymous=True)
    float_publisher=rospy.Publisher("float_topic2",Float32,queue_size=10)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        float_msgs = Float32()
        float_msgs = random.random()
        print(float_msgs)
        float_publisher.publish(float_msgs)
        rate.sleep()

if __name__=="__main__":
    try:
        publisher_node()
    except rospy.ROSInterruptExecption:
        pass