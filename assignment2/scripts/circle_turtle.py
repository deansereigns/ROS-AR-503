#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist

def move_turtles():
    rospy.init_node('move_turtles')

    turtle1_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    turtle2_pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)

    turtle1_msg = Twist()
    turtle2_msg = Twist()

    # Turtle1: Circular path
    turtle1_msg.linear.x = 0.0
    turtle1_msg.linear.y = 0.0
    turtle1_msg.angular.z = 1.0

    # Turtle2: Square path
    turtle2_msg.linear.x = 1.0
    turtle2_msg.linear.y = 0.0
    turtle2_msg.angular.z = 0.0

    while not rospy.is_shutdown():
        turtle1_pub.publish(turtle1_msg)
        turtle2_pub.publish(turtle2_msg)
        rospy.sleep(0.1)

if __name__ == '__main__':
    move_turtles()
