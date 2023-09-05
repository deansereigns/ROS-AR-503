#!usr/bin.python3

import rospy
from std_msgs.msg import Float32
x=0
def callback1(msg):
    global x 
    x =msg.data
    rospy.loginfo("Float value by Publisher 1: %f",msg.data)

def callback2(msg,):
    y =msg.data
    global x
    x=x+y
    x=x/2
    rospy.loginfo("Float value by Publisher 2: %f",msg.data)
    # rospy.loginfo("average Value: %f",x/2)

# def subscriber_node():
#     rospy.Subscriber("float_topic",Float32,callback1)
#     rospy.Subscriber("float_topic2",Float32,callback2)
#     rospy.spin()

def publisher_node():
    average_publisher=rospy.Publisher("avg_topic",Float32,queue_size=10)
    rate =rospy.Rate(1)

    while not rospy.is_shutdown():
        global x
        print(x)
        average_msgs = Float32()
        average_msgs =x
        # print(average_msgs)
        average_publisher.publish(average_msgs)
        rate.sleep()

if __name__=="__main__":
    try:
        rospy.init_node("subscriber_3",anonymous=True)
        rospy.Subscriber("float_topic",Float32,callback1)
        rospy.Subscriber("float_topic2",Float32,callback2)
        # subscriber_node()
        publisher_node()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass