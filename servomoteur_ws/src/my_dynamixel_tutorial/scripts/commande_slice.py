#!/usr/bin/env python


import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64


class cmd_slice:
    """
    @brief: On effectue la decoupe de la pizza
    @param: constant (tazille plateau)
    @return: none
    """       
    isDecouped = False

    def init(self):
        self.isDecouped = False #notre pizza est initialement pas decoupes

        #rospy.init_node('comm_slice_Node', anonymous=False) #definition noeud
        self.pub_cmd_slice = rospy.Publisher('/pan_slice/command', Float64, queue_size=10) #definition publisher
        rospy.sleep(1) #pause pour laisser le temps au programme

    def envoyer_vit(self, vitesse):
        """
        @brief: On publish notre vitesse demande
        @param: float vitesse
        @return: none
        """   
        self.pos_float64 = Float64() #On creer un objet Float qui sera envoye aux commandes
        self.pos_float64.data = float(vitesse)
        self.pub_cmd_slice.publish(self.pos_float64.data) #Envoi de notre data

    def couper_Pizza(self):
        #______aller_______
        self.envoyer_vit(-5)
        rospy.sleep(7.5)

        #______pause_______
        self.envoyer_vit(0)

        #______retour______
        rospy.sleep(1)
        self.envoyer_vit(5)
        rospy.sleep(7.5)
    
        #______arret_______
        self.envoyer_vit(0)

        self.isDecouped = true  

    def getStatusDecoupe(self):
        return self.isDecouped     

"""
if __name__ == '__main__':
    try:
       # p = cmd_slice()
       # p.couper_Pizza()
       # rospy.spin()
    except rospy.ROSInterruptException:
        pass
"""


