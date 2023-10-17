#!/usr/bin/python3
# importing necessary python libraries
import rospy
import random
from std_msgs.msg import Float32

# Defining a publisher node
def publisher_node():

    # Initializing a node
    rospy.init_node("float_publisher2",anonymous=True)

    # Creating a topic to publish data
    float_publisher=rospy.Publisher("float_topic2",Float32,queue_size=10)
    rate = rospy.Rate(1) # Describing the rate at which message is to be sent in Hz

    # Until stopped This node should continue to publish
    while not rospy.is_shutdown():

        # Message of Float data type
        float_msgs = Float32() # Message to be published. Here it is a Float with size of 32 bits or 4 bytes

        #random.random() gives value in between 0 and 1
        float_msgs = random.random()*9999 # adding an element to the message variable between the range of 0 and 9999
        print(float_msgs) # Printing the message to be sent
        float_publisher.publish(float_msgs) # Publishing the message
        rate.sleep()

if __name__=="__main__":
    try: #Error Handling
        publisher_node() #Calling the publisher node function 
    except rospy.ROSInterruptExecption: #If there occurs any type of error in "try block" then except code block would run
        pass