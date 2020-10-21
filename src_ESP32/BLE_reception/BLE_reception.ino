

#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>
#include <BLE2902.h>


String valeur_part;
bool first_init = false;
/* Creation of global variables */
BLEServer *pServer = NULL;
BLECharacteristic *pCharacteristic_1 = NULL;
BLECharacteristic *pCharacteristic_2 = NULL;
BLECharacteristic *pCharacteristic_3 = NULL;
bool deviceConnected = false;
bool oldDeviceConnected = false;


#define SERVICE_UUID        "ad98364f-23d7-44d6-b096-0435adc622ad"
#define CHARACTERISTIC_UUID_1 "44fb90c4-cf6d-4adb-81cf-f3d2d56f7e19"
#define CHARACTERISTIC_UUID_2 "345eb7a1-29b3-4d9b-b792-abb3bb621544"
#define CHARACTERISTIC_UUID_3 "8cfa9c3b-172c-4520-85ce-34bc43f623c3"

/* *Call back pour renvoyer des notifs */
class MyServerCallbacks: public BLEServerCallbacks 
{
    void onConnect(BLEServer *pServer) 
    {
      deviceConnected = true;
    };

    void onDisconnect(BLEServer *pServer) {

      deviceConnected = false;
    }
};


/* Classe de Callback appelé a en cas de write  */
class MyCallbacks_1: public BLECharacteristicCallbacks 
{
  //On recupere le nombre de part 
    void onWrite(BLECharacteristic *pCharacteristic) 
    {
      std::string value = pCharacteristic->getValue();
      if (value.length() > 0) 
      {
        valeur_part = "" ;
        Serial.println("*********");
        Serial.print("Valeur entrée: ");
        for (int i = 0; i < value.length(); i++)
        {
          //Serial.print(value[i]);
          valeur_part = valeur_part + value[i] ;
        }
        Serial.println();
        Serial.println(valeur_part);
        Serial.println("*********");
      }
    }
};

class MyCallbacks_2: public BLECharacteristicCallbacks 
{
    void onRead(BLECharacteristic *pCharacteristic) 
    { 
        // On effectue l'arret d'urgence 
        if (first_init == true)
        {
          Serial.println(" / * / * / * / * / EMERGENCY INITIALIZED * $ * $ * $ * $ * ");
        }
    }
};

void setup() {
  Serial.begin(115200);
  Serial.println("----------------------------------------------------------");
  Serial.println("Démarrage du Service de reception Bluetooth LE");
  Serial.println("Nom de Réseau: . . . . . . PIZZATOR");
  Serial.println("Type de donnée recu:");
  Serial.println(" . . . . . . . . . . . . . nb_part");
  Serial.println(" . . . . . . . . . . . . . xxxxxxx");
  
  // On init le device BLE 
  BLEDevice::init("PIZZATOR"); 

  // Create the BLE Server
  pServer = BLEDevice::createServer();
  pServer->setCallbacks(new MyServerCallbacks());
  BLEService *pService = pServer->createService(SERVICE_UUID);
  //BLEService *pService2 = pServer->createService(SERVICE_UUID);
  
  // Recuperation du nombre de part
  pCharacteristic_1 = pService->createCharacteristic(
                      CHARACTERISTIC_UUID_1,
                      BLECharacteristic::PROPERTY_READ   |
                      BLECharacteristic::PROPERTY_WRITE  |
                      BLECharacteristic::PROPERTY_NOTIFY |
                      BLECharacteristic::PROPERTY_INDICATE );

  pCharacteristic_1->addDescriptor(new BLE2902());
  pCharacteristic_1->setCallbacks(new MyCallbacks_1());

//Recuepration de la commande RESET 
  pCharacteristic_2 = pService->createCharacteristic(
                      CHARACTERISTIC_UUID_2,
                      BLECharacteristic::PROPERTY_READ |
                      BLECharacteristic::PROPERTY_NOTIFY);

  pCharacteristic_2->addDescriptor(new BLE2902());
  pCharacteristic_2->setCallbacks(new MyCallbacks_2());

  /* Gestion du chargement du PIZZATOR */
  pCharacteristic_3 = pService->createCharacteristic(
                      CHARACTERISTIC_UUID_3,
                      BLECharacteristic::PROPERTY_READ   |
                      BLECharacteristic::PROPERTY_WRITE  |
                      BLECharacteristic::PROPERTY_NOTIFY |
                      BLECharacteristic::PROPERTY_INDICATE );

  pCharacteristic_3->addDescriptor(new BLE2902());
  //pCharacteristic_3->setCallbacks(new MyCallbacks_3());
 
  /* Demmarage du Service */
  pService->start();

  /* Demmarage de l'advertising */
  set_Advertising();
  Serial.println("Attente d'une connection d'un client pour notify...");
}

void loop()
{

    if (deviceConnected) 
    {
      std::string val = "NB_PART" ;
      std::string val2 = "WANT TO CANCEL PIZZATOR ?" ;
      std::string val3 = "Avancement: " ;
      envoyer_val(pCharacteristic_1, val) ;
      envoyer_val(pCharacteristic_2, val2) ;
      envoyer_val(pCharacteristic_3, val3) ;
      first_init = true;
 
    }
    // disconnecting
    if (!deviceConnected && oldDeviceConnected) 
    {
        Serial.println("* * * * * * ¡End of Connection! * * * * * * ");
        delay(500); // give the bluetooth stack the chance to get things ready
        pServer->startAdvertising(); // restart advertising
        Serial.println("start advertising");
        oldDeviceConnected = deviceConnected;
    }
    // connecting
    if (deviceConnected && !oldDeviceConnected) 
    {
        Serial.println("* * * * * * ¡New Connection! * * * * * * ");
        // do stuff here on connecting
        oldDeviceConnected = deviceConnected;
    }

    //Serial.print(" ------ > LA VALEUR DE LA PART EST: ");
    //Serial.print(valeur_part);
    //Serial.println();
}

void envoyer_val(BLECharacteristic *pCharacteristic, std::string valeur_send)
{
    pCharacteristic->setValue(valeur_send); 
    pCharacteristic->notify();
    delay(10); // bluetooth stack will go into congestion, if too many packets are sent.

} 

void set_Advertising()
{
  /* Début de  l'advertising */
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->addServiceUUID(SERVICE_UUID);
  pAdvertising->setScanResponse(false);
  pAdvertising->setMinPreferred(0x0);  
  BLEDevice::startAdvertising();
}
