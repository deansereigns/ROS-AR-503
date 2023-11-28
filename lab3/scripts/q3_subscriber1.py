#!/usr/bin/python3

import rospy  # Import ROS Python library
from std_msgs.msg import Float32  # Import the Float32 message type

def node2_subscribe(data):
    # Log the received data
    rospy.loginfo(f"Node 2 received data: {data.data}")

def node2_listener():
    # Initialize a ROS node with the name 'node2_subscriber'
    rospy.init_node('node2_subscriber', anonymous=True)
    
    # Subscribe to the 'random_float' topic and call 'node2_subscribe' when data is received
    rospy.Subscriber('random_float', Float32, node2_subscribe)
    
    # Spin to keep the script running and handling incoming messages
    rospy.spin()

if __name__ == '__main__':
    node2_listener()
