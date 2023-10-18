#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Twist

def square_turtle():
    rospy.init_node('square_turtle', anonymous=True)
    turtle_vel = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(1)  # 1 Hz (adjust this to control the speed of the turtle)

    move_cmd = Twist()
    move_cmd.linear.x = 1.0  # Linear velocity
    move_cmd.angular.z = 0.0  # Angular velocity (causes straight-line motion)

    for _ in range(4):
        # Move forward for 2 seconds (adjust this as needed)
        for _ in range(2):
            turtle_vel.publish(move_cmd)
            rate.sleep()

        # Stop and turn 90 degrees
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 1.57  # Angular velocity (pi/2 radians/s)
        for _ in range(5):  # Adjust this for a 90-degree turn
            turtle_vel.publish(move_cmd)
            rate.sleep()

    # Ensure the turtle stops at the end
    move_cmd.linear.x = 0.0
    move_cmd.angular.z = 0.0
    turtle_vel.publish(move_cmd)

if __name__ == '__main__':
    try:
        square_turtle()
    except rospy.ROSInterruptException:
        pass
