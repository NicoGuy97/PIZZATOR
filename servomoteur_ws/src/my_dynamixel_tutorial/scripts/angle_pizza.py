#!/usr/bin/env python


import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64


class angle_pizza:
    
    

    def __init__(self):
        rospy.init_node('angle_pizza_Node', anonymous=False)
        self.pub_angle_pizza = rospy.Publisher('/pan_controller/command', Float64, queue_size=10)
        rospy.sleep(1)
        self.envoyer_pos(2)

    def envoyer_pos(self, position):
        self.pos_float64 = Float64()
        self.pos_float64.data = float(position)
        self.pub_angle_pizza.publish(self.pos_float64.data)

    def choix_ratotion(self, nb_part)
        if nb_part == 4
            #commande_slice # couper 
            envoyer_pos(4) # faire tourner servomoteur
            rospy.sleep(8) # huigt sec = 90°
            #commande_slice

        if nb_part == 6
            #commande_slice # couper
            envoyer_pos(4)
            rospy.sleep(4) # quatre sec = 45°

            #commande_slice # couper
            envoyer_pos(4)
            rospy.sleep() # quatre sec = 45°

            #commande_slice #couper


        


if __name__ == '__main__':
    p = angle_pizza_Node()
    rospy.spin()


