#!/usr/bin/env python


import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64


class cmd_slice:
    
    

    def __init__(self):
        rospy.init_node('comm_slice_Noce', anonymous=False) #definition noeud
        self.pub_cmd_slice = rospy.Publisher('/pan_controller/command', Float64, queue_size=10) #definition publisher
        rospy.sleep(1) #pause pour laisser le temps au programme

    def envoyer_vit(self, vitesse):
        self.pos_float64 = Float64() #creation d un objet float 
        self.pos_float64.data = float(vitesse)  #on publie dans le topic /pan_controller/command 
        self.pub_cmd_slice.publish(self.pos_float64.data)
        


if __name__ == '__main__':
    p = cmd_slice()

    #______aller_______
    p.envoyer_vit(-5)
    rospy.sleep(7.5)

    #______pause_______
    p.envoyer_vit(0)

    #______retour______
    rospy.sleep(1)
    p.envoyer_vit(5)
    rospy.sleep(7.5)

    #______arret_______
    p.envoyer_vit(0)

    rospy.spin()


