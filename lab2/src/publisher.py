#!/usr/bin/python3
#import the necessary library for using ROS in Python
import rospy
from std_msgs.msg import Float32 #import the datad type Float32 from the std_msgs package
#This function will be called when the code is run
def callback():
	#initialize the Ros node with a unnique name
	rospy.init_node("pub-num_py",anonymous=True)
	
	#Create a publisher that sends messages of type float32 to the "pub_num_topic" topic
	publisher =rospy.Publisher("pub_num_topic",Float32,queue_size=10)
	
	#Set the publishing rate to 10 messages per second
	rate =rospy.Rate(10)
	
	#Run the loop until the script is interrupted
	while not rospy.is_shutdown():
		number=3.14 #set the value of the number to be published
		print(number) #Print hte numberto the console
		
		# Publish the nimberto the topic
		publisher.publish(number)
		
		#Pause the loop to acievethe desired publishing rate
		rate.sleep()
		
	#This block of code gets executed only if the script is run directly(not imported as a module)
	if__name__=="__main__":
		try :
			callback() #call the defined function
		except rospy.ROSInterruptExecution:
			pass # Ignore the exception if the script is interrupted
