#!/usr/bin/python3

import rospy
from lab5.srv import AddTwoints, AddTwointsResponse

def add_two_ints_cb(req):
    rospy.loginfo("ready to add %d and %d", req.a, req.b)
    return AddTwointsResponse(req.a+req.b)

if __name__== "__main__":
    rospy.init_node("simple_service")

    service = rospy.Service("add_two_ints",AddTwoints,add_two_ints_cb)

    rospy.loginfo("The service is ready to add ints")

    rospy.spin()    