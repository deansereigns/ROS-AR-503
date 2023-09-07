#!usr/bin/python3
# importing necessary python libraries
import rospy
from std_msgs.msg import String

# Defining a publisher node
def publisher_node():

    # Initializing a node
    rospy.init_node("string_publisher",anonymous=True)

    # Creating a topic to publish data
    string_publisher=rospy.Publisher("String_topic",String,queue_size=100)
    rate = rospy.Rate(10) # Describing the rate at which message is to be sent in Hz

    # Until stopped This node should continue to publish
    while not rospy.is_shutdown():

        # Message of String data type
        string_msgs = String() # Message to be published. Here it is an  String: "Hello from Publisher"

        string_msgs = "Hello from Publisher" # Desried Message
        print(string_msgs) # Printing the message to be sent
        string_publisher.publish(string_msgs)  # Publishing the message
        rate.sleep()

if __name__=="__main__":
    try: #Error Handling
        publisher_node() #Calling the publisher node function 
    except rospy.ROSInterruptExecption: #If there occurs any type of error in "try block" then except code block would run
        pass