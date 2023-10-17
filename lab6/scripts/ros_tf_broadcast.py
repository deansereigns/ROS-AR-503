#! /usr/bin/python3

import rospy
import tf

def send_transform():
    # Broadcaster to send transforms
    bro = tf.TransformBroadcaster()

    # Transaltion of Transform
    x1, y1, z1 = 0.5, 0.2, 0.6
    x2, y2, z2 = 1, 1, 1.5
    x3, y3, z3 = -1, 0.6, 2.5

    # Rotation of Transform
    rota = tf.transformations.quaternion_from_euler(5,0,0)
    rota1 = tf.transformations.quaternion_from_euler(15,23,30)
    rota2= tf.transformations.quaternion_from_euler(30,-35,-15)

    # Parent and Child Links
    parent, child1,child2,child3 ="world", "link_1","link_2","link_3"

    #Sending the transform
    bro.sendTransform((x1,y1,z1),rota,rospy.Time.now(),child1,parent)
    bro.sendTransform((x2,y2,z2),rota1,rospy.Time.now(),child2,child1)
    bro.sendTransform((x3,y3,z3),rota2,rospy.Time.now(),child3,child2)

if __name__=="__main__":
    # Same as publisher
    rospy.init_node('custom_tf_broadcast',anonymous=False)
    rate =rospy.Rate(1)
    while(not rospy.is_shutdown()):
        send_transform()
        rate.sleep()