#!/usr/bin/python3
import rospy
from assignment2.msg import integer
import random

def publisher_node():
   rospy.init_node("publisher1",anonymous=True)
   pub = rospy.Publisher('integer1', integer, queue_size=10)
   rate = rospy.Rate(10) # 10hz
   while not rospy.is_shutdown():
      message =integer()
      message.num= (int)(random.random()*500)
      # message.num= 50
      rospy.loginfo(message)
      pub.publish(message)
      rate.sleep()

if __name__=="__main__":
   try:
      publisher_node()
   except rospy.ROSInterruptException:
      pass