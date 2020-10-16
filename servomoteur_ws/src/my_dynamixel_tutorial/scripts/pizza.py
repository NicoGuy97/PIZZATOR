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
        self.pourcentage_fait = 1.0
        self.DIAMETRE_PLATEAU = 28 #en cm
        self.VITESSE_MOTEUR_CM_S = 8     #Distance etalon parcourue par les moteurs

        rospy.init_node('pizza_Node', anonymous=False)

        rospy.Subscriber('/nb_part_node', std_msgs, self.callback_nb_part)
        #rospy.Subscriber('/emergency_msg', std_msgs, self.callback)
        #self.pub_progress = rospy.Publisher('/recept_progression', Float64, queue_size=10)

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
        print "DEBUT DE LA DECOUPE"
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

        self.isDecouped = True
        print "FIN DE LA DECOUPE"
    def effectuer_decoupe(self, nb_part ):
        """
        @brief: On calcul et effectue le nb de part
        @param: float nb_part
        @return: none
        """
        self.dist_cm_par_part = 2*math.pi*self.DIAMETRE_PLATEAU / nb_part
        self.dist_servo_par_part = self.dist_cm_par_part / self.VITESSE_MOTEUR_CM_S #ou dist_deg ou distance_par_part

        itera = nb_part/2 
        while(itera > 0):
            self.couper_Pizza()
            #while(self.isDecouped != True):
            rospy.sleep(1)
            if(nb_part != 2):    #Si on a besoin que de 2 part, pas de rot
                print "DEBUT ROTATION"
                self.envoyer_rot(5)
                rospy.sleep(self.dist_servo_par_part)
                self.envoyer_rot(0)
                print "FIN ROTATION"
            itera = itera - 1
            print(itera)
            self.pourcentage_fait = self.pourcentage_fait + (1 / nb_part) * 100
            print "Pourcentage effectue: " + str(self.pourcentage_fait)
        print " - - - - - - - Pizza prete - - - - - - - "

    def presentation_Pizza():
        print " - - - - - - - Presentation Pizza - - - - - - - "
        self.envoyer_rot(10)
        rospy.sleep(7*math.pi)
        self.envoyer_rot(0)

    def callback_nb_part(self, data):
        self.nb_part = float(data)



if __name__ == '__main__':
    try:
        pizza = pizza()
        pizza.envoyer_rot(0)
        pizza.envoyer_vit(0)
        pizza.effectuer_decoupe(pizza.nb_part)
        pizza.presentation_Pizza()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass




