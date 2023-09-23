#!/usr/bin/python3
import rospy
from std_msgs.msg import Float32
def callback():
	rospy.init_node("pub_num_py",anonymous=True)
	
	publisher =rospy.Publisher("pub_num_topic",Float32,queue_size=100)

	rate =rospy.Rate(500)
	
	
	while not rospy.is_shutdown():
		number=999999999 
		print(number) 
		
		publisher.publish(number)
		
		
		rate.sleep()
if __name__=="__main__":
		try:
			callback()
		except rospy.ROSInterruptException:
			pass
