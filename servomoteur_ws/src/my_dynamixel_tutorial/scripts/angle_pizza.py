#!/usr/bin/env python


import rospy
import math
from std_msgs.msg import String
from std_msgs.msg import Float64

class pizza:
    """
    @brief: Permet de mettre le moteur dans une position precise
    @param: none
    @return: none
    """ 
    isDecouped = False

    def __init__(self):
        self.isDecouped = False #notre pizza est initialement pas decoupes
        self.pourcentage_fait = 0.0  
        self.DIAMETRE_PLATEAU = 28 #en cm
        self.CONSTANTE_MOT = 5       #Distance etalon parcourue par les moteurs

        rospy.init_node('pizza_Node', anonymous=False)
        self.pub_angle_pizza = rospy.Publisher('/pan_rotate/command', Float64, queue_size=10)
        self.pub_cmd_slice = rospy.Publisher('/pan_slice/command', Float64, queue_size=10) #definition publisher
        rospy.sleep(1)

    def envoyer_rot(self, position):
        """
        @brief: On publish notre rotation demande
        @param: float position
        @return: none
        """   
        self.pos_float64 = Float64() #On creer un objet Float qui sera envoye aux commandes
        self.pos_float64.data = float(position)
        self.pub_angle_pizza.publish(self.pos_float64.data) #Envoi de notre data


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

    def effectuer_decoupe(self, nb_part ):
        """
        @brief: On calcul et effectue le nb de part 
        @param: float nb_part
        @return: none
        """  
        self.distance_par_part = nb_part /(2* math.pi) #On regarde la distance de plateau a effectuer
        self.dist_deg = math.degrees(self.distance_par_part)
        self.dist_cm_par_part = 2*math.pi*self.DIAMETRE_PLATEAU
        self.dist_servo_par_cm = self.CONSTANTE_MOT 
        self.dist_servo_par_part = dist_servo_par_cm * dist_cm_par_part #ou dist_deg ou distance_par_part

        itera = nb_part/2 - 2
        while(itera <= 0):
            self.couper_Pizza()
            while(self.getStatusDecoupe() != true):
                rospy.sleep(1)
            if(nb_part != 2):    #Si on a besoin que de 2 part, pas de rot
                self.envoyer_rot(self.dist_servo_par_part)
                rospy.sleep(self.dist_servo_par_part)    
            itera = itera - 1
            self.pourcentage_fait += (1 / nb_part) * 100
        #Fin de la decoupe 



if __name__ == '__main__':
    try:
        pizza = pizza()
        pizza.effectuer_decoupe(2)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass




