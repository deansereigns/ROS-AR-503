#!/usr/bin/python3

import rospy
from assignment2.msg import custom
import random

def publisher_node():
    # print(1)
    rospy.init_node('message_publisher',anonymous=True)
    pub = rospy.Publisher('floatintarray',custom,queue_size=10)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        # print(2)
        message = custom()
        message.myFloat =random.random()*10
        message.myInt = int(random.random()*500)
        # arr =range(0,9999)
        message.myArray=[1,2,3,4,5]
        pub.publish(message)
        print(message)
        rate.sleep()

if __name__ =="__main__":
    # publisher_node()
    try:
        publisher_node()
    except ROSInterruptExecption :
        pass