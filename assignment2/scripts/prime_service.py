#!/usr/bin/python3

import rospy
from assignment2.srv import CheckPrime, CheckPrimeResponse

def isPrime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i ==0:
            return False
    return True

def check_prime(req):
    rospy.loginfo("numbers to check whether are prime or not %d, %d, %d respectively", req.a, req.b,req.c)
    response = CheckPrimeResponse()
    response.is_prime_a=isPrime(req.a)
    response.is_prime_b=isPrime(req.b)
    response.is_prime_c=isPrime(req.c)
    return response

if __name__== "__main__":
    rospy.init_node("check_prime_server")

    service = rospy.Service("check_prime_service",CheckPrime,check_prime)

    rospy.loginfo("The service is ready to find whether prime or not prime")

    rospy.spin()    