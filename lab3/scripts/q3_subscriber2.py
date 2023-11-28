#!/usr/bin/python3

import rospy  # Import ROS Python library
from std_msgs.msg import Float32  # Import the Float32 message type

def node3_subscribe(data):
    # Log the received data
    rospy.loginfo(f"Node 3 received data: {data.data}")

def node3_listener():
    # Initialize a ROS node with the name 'node3_subscriber'
    rospy.init_node('node3_subscriber', anonymous=True)
    
    # Subscribe to the 'random_float' topic and call 'node3_subscribe' when data is received
    rospy.Subscriber('random_float', Float32, node3_subscribe)
    
    # Spin to keep the script running and handling incoming messages
    rospy.spin()

if __name__ == '__main__':
    node3_listener()
