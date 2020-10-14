/*
    Based on Neil Kolban example for IDF: https://github.com/nkolban/esp32-snippets/blob/master/cpp_utils/tests/BLE%20Tests/SampleWrite.cpp
    Ported to Arduino ESP32 by Evandro Copercini
*/

#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>

// See the following for generating UUIDs:
// https://www.uuidgenerator.net/

#define SERVICE_UUID        "ad98364f-23d7-44d6-b096-0435adc622ad"
#define CHARACTERISTIC_UUID "44fb90c4-cf6d-4adb-81cf-f3d2d56f7e19"


/* Classe de Callback appelé a chaque interuption */
class MyCallbacks: public BLECharacteristicCallbacks 
{
    void onWrite(BLECharacteristic *pCharacteristic) 
    {
      std::string value = pCharacteristic->getValue();
      if (value.length() > 0) 
      {
        
        Serial.println("*********");
        Serial.print("Valeur entrée: ");
        for (int i = 0; i < value.length(); i++)
          Serial.print(value[i]);
        Serial.println();
        Serial.println("*********");
      }
      if(value[0] == '1')
      {
        Serial.println("WOOOOOOOOW T'es dingue mec !!!!!");
      }
    }
};

void setup() {
  Serial.begin(115200);


  Serial.println("Démarrage du Service de reception Bluetooth LE");
  Serial.println("Nom de Réseau: . . . . . . PIZZATOR");
  Serial.println("Type de donnée recu:");
  Serial.println(" . . . . . . . . . . . . . nb_part");
  Serial.println(" . . . . . . . . . . . . . xxxxxxx");
  
  BLEDevice::init("PIZZATOR");  // On init le device BLE 
  BLEServer *pServer = BLEDevice::createServer();
  BLEService *pService = pServer->createService(SERVICE_UUID);
  // On lui affecte des characteristique par default (UUID ...)
  BLECharacteristic *pCharacteristic = pService->createCharacteristic(
                                         CHARACTERISTIC_UUID,
                                         BLECharacteristic::PROPERTY_READ |
                                         BLECharacteristic::PROPERTY_WRITE
                                       );

  pCharacteristic->setCallbacks(new MyCallbacks()); // On lui affecte une callback
  // Valeur par defaut dans la charachteristic de base:
  pCharacteristic->setValue("NO_VALUE"); 
  /* Demmarage du Service */
  pService->start();
  /* Début de  l'advertising */
  BLEAdvertising *pAdvertising = pServer->getAdvertising();
  pAdvertising->start();
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(2000);
}
