#!/usr/bin/env python


import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64
from commande_slice import *
from angle_pizza import *

if __name__ == '__main__':
    plateau = angle_pizza()
    plateau.effectuer_decoupe(2, slicer)
    rospy.spin()



