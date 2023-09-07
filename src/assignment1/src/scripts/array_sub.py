#!usr/bin.python3
# importing necessary python libraries
import rospy
from std_msgs.msg import Float32MultiArray

# Defining callback function to view and perform operations on msg received from pulibsher node of a required topic
def callback(msg):
    rospy.loginfo("Float Message: %f",msg.data[0]) # printing the Info and the Float message received
    rospy.loginfo("Integer Message: %d",int(msg.data[1])) # printing the Info and the Integer message received

# Defining Subsciber node
def subscriber_node():
    # Creating a node
    rospy.init_node("subscriber_1",anonymous=True)
    # Subscribing to a topic and calling the function callback
    rospy.Subscriber("float_topic",Float32MultiArray,callback)
    rospy.spin()

if __name__=="__main__":
    try: #Error Handling
        subscriber_node() #Calling the Subscriber node function 
    except rospy.ROSInterruptException: #If there occurs any type of error in "try block" then except code block would run
        pass