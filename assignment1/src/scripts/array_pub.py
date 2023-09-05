#!usr/bin/pyhton3

import rospy
import random
from std_msgs.msg import Float32MultiArray

def publisher_node():
    rospy.init_node("float_publisher",anonymous=True)
    float_publisher=rospy.Publisher("float_topic",Float32MultiArray,queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        arr =range(1,1000)
        float_arr_msgs = Float32MultiArray()
        float_arr_msgs.data.append(71.5)
        float_arr_msgs.data.append(random.choice(arr))
        print(float_arr_msgs)
        float_publisher.publish(float_arr_msgs)
        rate.sleep()

if __name__=="__main__":
    try:
        publisher_node()
    except rospy.ROSInterruptExecption:
        pass