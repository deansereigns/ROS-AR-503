#!usr/bin/python3
# importing necessary python libraries
import rospy
from std_msgs.msg import String

# Defining callback function to view and perform operations on msg received from pulibsher node of a required topic
def callback(msg):
    rospy.loginfo("Received Message: %s",msg.data) # printing the Info and the String message received

# Defining Subsciber node
def subscriber_node():

    # Creating a node
    rospy.init_node("String_subscriber",anonymous=True)

    # Subscribing to a topic and calling the function callback
    rospy.Subscriber("String_topic",String,callback)
    rospy.spin()

if __name__=="__main__":
    try: #Error Handling
        subscriber_node() #Calling the Subscriber node function 
    except rospy.ROSInterruptException: #If there occurs any type of error in "try block" then except code block would run
        pass