#!/usr/bin/python3

import rospy  # Import ROS Python library
from std_msgs.msg import Float32  # Import the Float32 message type
import random
import time

def node1_publish():
    # Initialize a ROS node with the name 'node1_publisher'
    rospy.init_node('node1_publisher', anonymous=True)
    
    # Create a publisher that publishes Float32 messages to the 'random_float' topic
    pub = rospy.Publisher('random_float', Float32, queue_size=10)
    
    # Set the publish rate to 1 Hz
    rate = rospy.Rate(1)
    
    while not rospy.is_shutdown():
        # Generate a random float value between 0.0 and 1.0
        random_value = random.uniform(0.0, 1.0)
        
        # Log the message before publishing
        rospy.loginfo(f"Publishing random float: {random_value}")
        
        # Publish the random float value
        pub.publish(random_value)
        
        # Sleep to maintain the publish rate
        rate.sleep()

if __name__ == '__main__':
    try:
        node1_publish()
    except rospy.ROSInterruptException:
        pass
