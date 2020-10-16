#!/usr/bin/env python


import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64


class angle_pizza:
    
    

    def __init__(self):
        rospy.init_node('angle_pizza_Node', anonymous=False)
        self.pub_angle_pizza = rospy.Publisher('/pan_rotate/command', Float64, queue_size=10)
        self.pub_comm_slice = rospy.Publisher('/pan_slice/command', Float64, queue_size=10)
        rospy.sleep(1)
        self.envoyer_pos(2)

    def envoyer_pos(self, position):
        self.pos_float64 = Float64()
        self.pos_float64.data = float(position)
        self.pub_comm_slice.publish(self.pos_float64.data)

    def envoyer_rot(self, rotation):
        self.rot_float64 = Float64()
        self.rot_float64.data = float(rotation)
        self.pub_angle_pizza.publish(self.rot_float64.data)

    def choix_ratotion(self, nb_part):

        if nb_part == 2:
            envoyer_pos(4) 
            rospy.sleep(4)
            envoyer_pos(-4) 

        else if nb_part == 4:
            envoyer_pos(4) 
            rospy.sleep(4)
            envoyer_pos(-4) 
            rospy.sleep(1)

            envoyer_rot(4) # faire tourner servomoteur
            rospy.sleep(4) # huigt sec = 90°

            envoyer_pos(4) 
            rospy.sleep(4)
            envoyer_pos(-4) 
            rospy.sleep(1)


        


if __name__ == '__main__':
    p = angle_pizza_Node()
    p.choix_ratotion(4)
    rospy.spin()


