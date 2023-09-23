#!/usr/bin/python3
# importing necessary python libraries
import rospy
from std_msgs.msg import Float32


x=0 # Creating a Global variable
y=0 # Creating a Global variable

# Defining callback2 function to view and perform operations on msg received from pulibsher node 1
def callback1(msg):
    global x # using the global variable int he current code block
    x =msg.data # Assigning the value received from Publisher Node 1 to Global variable x
    rospy.loginfo("Float value by Publisher 1: %f",msg.data) # printing the Info and the Float message sent by Publisher 1

# Defining callback2 function to view and perform operations on msg received from pulibsher node 2
def callback2(msg,):
    global y # using the global variable int he current code block
    y =msg.data # Assigning the value received from Publisher Node 2 to Global variable y
    rospy.loginfo("Float value by Publisher 2: %f",msg.data) # printing the Info and the Float message sent by Publisher 2

# Defining Publisher node
def publisher_node():

    # Creating a topic to publish data
    average_publisher=rospy.Publisher("avg_topic",Float32,queue_size=10)
    rate =rospy.Rate(1) # Describing the rate at which message is to be sent in Hz

    # Until stopped This node should continue to publish
    while not rospy.is_shutdown():
        global x # using the global variable in the current code block
        global y # using the global variable in the current code block
        average_msgs = Float32() # Message to be published. Here it is a Float with size of 32 bits or 4 bytes
        average_msgs =(x+y)/2 # Calculating of average of message published by Publisher 1 and 2
        average_publisher.publish(average_msgs) # Publishing the message
        print(average_msgs) # Printing the message to be sent
        rate.sleep()

if __name__=="__main__":
    try: #Error Handling

        # Creating a node
        rospy.init_node("subscriber_3",anonymous=True)

        # Subscribing to a topic of Publisher node 1 and calling the function callback1
        rospy.Subscriber("float_topic",Float32,callback1)

        # Subscribing to a topic of Publisher node 2 and calling the function callback2
        rospy.Subscriber("float_topic2",Float32,callback2)

        publisher_node() #Calling the publisher node function 
        rospy.spin()
    except rospy.ROSInterruptException: #If there occurs any type of error in "try block" then except code block would run
        pass