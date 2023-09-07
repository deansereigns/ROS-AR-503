#!usr/bin/python3
# importing necessary python libraries
import rospy
from std_msgs.msg import Float32

# Defining callback function to view and perform operations on msg received from pulibsher node of a required topic
def callback(msg):
    rospy.loginfo("Average: %f",msg.data) # printing the Info and the Float message received

# Defining Subsciber node
def subscriber_node():

    # Creating a node
    rospy.init_node("avg_subsciber",anonymous=True)

    # Subscribing to a topic and calling the function callback
    rospy.Subscriber("avg_topic",Float32,callback)
    rospy.spin()

if __name__=="__main__":
    try: #Error Handling
        subscriber_node() #Calling the Subscriber node function 
    except rospy.ROSInterruptException: #If there occurs any type of error in "try block" then except code block would run
        pass