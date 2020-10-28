# <center> <h2>PIZZATOR</h2> </center>	
## Authors: GUY - LECOCQ - MOUSSA	
## Project of creation of a pizza slicer robot 

Few words on the project :  
We had 20h to create a prototype with certains constraints such as using ROS, BLE, printing a 3D piece, ...  
We wanted to make a unique piece of art abble of cutting a pizza in a specific number of slices. You can choose the number of slices and see the progress of the cutting.
#
<center> <h3>Repository</h3> </center>

Hardware, software and technoligies used for this project :
* ROS
* Arduino IDE
* BLE (Bluetooth Low Energy)
* MIT App Inventor (Smartphone Application)
* 3D Printing (SolidEdge)
* 3 servomotors Dynamixel AX-12
* 1 analog sensor SHARP
* 1 ESP 32 TTGo T-Display (Wi-Fi + BLE)

*3D Print* :
* file with the .stl, piece ready for the printing 

*application* : 
* contains the code for the application

*servomoteur_ws* :
* workspace where we can find all the nodes and topics ROS to control the servomotors.  

*src_ESP32* :
* contain all ESP32 source files and data. The Folder BLE_reception include the source file in order to manage BLE reception and emmisions of data from the app/µContr

*link to our YouTube video* :
* <https://youtu.be/hC-m_DlMcJs>