#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist
def function():
  rospy.init_node('turtle',anonymous=True)
  turtle1_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
  turtle2_publisher = rospy.Publisher('/w1/cmd_vel', Twist, queue_size=10)
  rate=rospy.Rate(1)
  twist = Twist()
  side_length = 2.0
  while not rospy.is_shutdown():
     # Calculate the linear and angular velocities for turtle1 to move in a circle.
     radius = 1.5  # Radius of the circular path
     angular_speed = 1.0  # Angular velocity (rad/s)
    # Publish the linear and angular velocities to turtle1.
     twist.linear.x = angular_speed * radius
     twist.angular.z = angular_speed
     turtle1_publisher.publish(twist)
     
     for _ in range(4):
        move_forward(turtle2_publisher, 2.0)  # Adjust the distance as needed
        rotate_left(turtle2_publisher, 90)  # Adjust the angle as needed
        rate.sleep()
       
def move_forward(pub, distance):
    twist = Twist()
    twist.linear.x = 1.0
    distance_moved = 0
    rate = rospy.Rate(10)  # 10 Hz
    while distance_moved < distance:
        pub.publish(twist)
        rate.sleep()
        distance_moved += 0.1
    twist.linear.x = 0.0
    pub.publish(twist)
def rotate_left(pub, angle_degrees):
    twist = Twist()
    twist.angular.z = 1.0
    angle_radians = angle_degrees * 3.14159265359 / 180.0
    rotated = 0
    rate = rospy.Rate(10)  # 10 Hz
    while rotated < angle_radians:
        pub.publish(twist)
        rate.sleep()
        rotated += 0.1
    twist.angular.z = 0.0
    pub.publish(twist)
if __name__ == '__main__':
  function()