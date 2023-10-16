#!/usr/bin/python3

import rospy
from assignment2.srv import CheckPrime

import sys

if __name__=="__main__":
    rospy.init_node("check_prime_client")
    # print(sys.argv[0])
    a =int(input("Enter First Number: "))
    b =int(input("Enter Second Number: "))
    c =int(input("Enter Third Number: "))
    # if len(sys.argv)==4:
    #     a =int(sys.argv[1])
    #     b =int(sys.argv[2])
    #     c= int(sys.argv[3])

    # else:
    #     print("requested three arguments")
    #     sys.exit(-1)


    rospy.wait_for_service("check_prime_service")
    print("requesting prime or not prime of ",a,b,c)

    check_prime = rospy.ServiceProxy("check_prime_service",CheckPrime)

    response = check_prime(a,b,c)

    print("service Response for ",a,response.is_prime_a)
    print("service Response for ",b,response.is_prime_b)
    print("service Response for ",c,response.is_prime_c)