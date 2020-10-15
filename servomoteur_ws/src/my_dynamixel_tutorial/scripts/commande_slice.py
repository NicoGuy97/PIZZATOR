#!/usr/bin/env python


import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64


class angle_pizza:
    
    

    def __init__(self):
        rospy.init_node('angleComSlide', anonymous=False)
        self.pub_pizza_angle = rospy.Publisher('/tilt_controller/command', Float64, queue_size=10)
        rospy.sleep(1)

    def envoyer_pos(self, position):
        self.pos_float64 = Float64()
        self.pos_float64.data = float(position)
        # rospy.loginfo('L angle envoye est : ' + self.angle.data)
        self.pub_pizza_angle.publish(self.pos_float64.data)
        rospy.sleep(3)
        


if __name__ == '__main__':
    p = angle_pizza()
    p.envoyer_pos(3)
    rospy.sleep(1)
    p.envoyer_pos(-3)
    rospy.spin()


