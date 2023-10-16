#!usr/bin/pyhton3

import rospy
from std_msgs.msg import Float32,Int32

def float_callback(msg):
    #Print received float value with a log message
    rospy.loginfo("Received Float value: %f",msg.data)

def int_callback(msg):
    #Print received float value with a log message
    rospy.loginfo("Received Int value: %d",msg.data)

#Main function for the subscriber node
def  subscriber_node():
    # Initialize the ROS node with unique name
    rospy.init_node('custom_subscriber',anonymous=True)

    # Create subscribers for float and Integer topics
    rospy.Subscriber('float_topic',Float32,float_callback)
    rospy.Subscriber('int_topic',Int32,int_callback)

    rospy.spin()

if __name__=='__main__':
    try:
        subscriber_node()
    except rospy.ROSInterruptException:
        pass