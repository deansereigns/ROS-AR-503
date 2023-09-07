#!/usr/bin/pyhton3

import rospy 
from std_msgs.msg import Float32, Int32
# rospy.loginfo("hii")
def publisher_node():
    rospy.init_node('floatint_publisher', anonymous=True)

    #Create publishers for float and integer topics
    float_publisher =rospy.Publisher('float_topic',Float32,queue_size=10)
    int_publisher = rospy.Publisher('int_topic',Int32,queue_size=10)
    rate =rospy.Rate(1) # publishing rate 1Hz

    while not rospy.is_shutdown():
        #Create and populate messages
        float_msgs= Float32()
        float_msgs.data=3.14

        int_msgs=Int32()
        int_msgs.data=42

        #Publish messages
        float_publisher.publish(float_msgs)
        int_publisher.publish(int_msgs)

        rate.sleep()

if __name__=='__main__':
    try:
        # rospy.loginfo("Mayank")
        publisher_node()
        # rospy.loginfo("hello")
    except rospy.ROSInterruptExecption:
        pass