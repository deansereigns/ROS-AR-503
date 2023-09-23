#!/usr/bin/python3

import rospy
from lab5.srv import AddTwoints

import sys

if __name__=="__main__":

    if len(sys.argv)==3:
        a =int(sys.argv[1])
        b =int(sys.argv[2])

    else:
        print("requested two arguments")
        sys.exit(-1)

    print("requesting sum of", a, b)

    rospy.wait_for_service("add_two_ints")

    add_two_ints = rospy.ServiceProxy("add_two_ints",AddTwoints)

    response = add_two_ints(a,b)

    print("service Response", response)