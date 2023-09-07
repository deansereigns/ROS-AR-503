#!usr/bin/python3
# importing necessary python libraries
import rospy
import random
from std_msgs.msg import Float32MultiArray

# Defining a publisher node
def publisher_node():
    
    # Initializing a node
    rospy.init_node("float_publisher",anonymous=True)
    
    # Creating a topic to publish data
    float_publisher=rospy.Publisher("float_topic",Float32MultiArray,queue_size=10)
    rate = rospy.Rate(10) # Describing the rate at which message is to be sent in Hz

    # Until stopped This node should continue to publish
    while not rospy.is_shutdown():
        arr =range(0,999) # and array in the range between 0 and 999

        # Array of Float data type
        float_arr_msgs = Float32MultiArray() # Message to be published. Here it is an array of Float datatype with size of 32 bits or 4 bytes

        #random.random() gives value in between 0 and 1
        float_arr_msgs.data.append(random.random()*999) # adding an element to the message array between the range of 0 and 999
        float_arr_msgs.data.append(random.choice(arr)) # adding an element to the message array of integer datatype from the random choice from arr/
        print(float_arr_msgs) # Printing the message to be sent
        float_publisher.publish(float_arr_msgs) # Publishing the message in form of an array
        rate.sleep()

if __name__=="__main__":
    try: #Error Handling
        publisher_node() #Calling the publisher node function 
    except rospy.ROSInterruptExecption: #If there occurs any type of error in "try block" then except code block would run
        pass