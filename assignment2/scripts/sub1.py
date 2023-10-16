#!/usr/bin/python3
import rospy
from assignment2.msg import integer
from std_msgs.msg import Float32

average =0
def callback(msg):
    global average
    average =average +msg.num
    rospy.loginfo(msg.num)

def publisher_node():
    rospy.init_node("avg_publisher",anonymous=True)
    pub = rospy.Publisher("average",Float32,queue_size=10)
    rate = rospy.Rate(10)
    sub1 = rospy.Subscriber("integer1",integer,callback=callback)
    sub2 = rospy.Subscriber("integer2",integer,callback=callback)
    global average
    while not rospy.is_shutdown():
        print(average)
        avg =Float32()
        avg = (average)/2
        pub.publish(avg)
        print(avg)
        average=0
        rate.sleep()   
    rospy.spin()
if __name__=="__main__":
    try:
        publisher_node()
    except rospy.ROSInterruptException:
        pass