#!/usr/bin/python3
import rospy
from std_msgs.msg import Float32

def callback(D):
	X=D.data
	print(X)
if __name__=="__main__":
	rospy.init_node("sub_num_py",anonymous=True)
	rospy.Subscriber("pub_num_topic",Float32,callback)
	rospy.spin()
