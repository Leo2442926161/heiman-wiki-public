---
sidebar_position: 2
---
#Zigbee2MQTT

Zigbee2MQTT ist eine Open-Source-Zigbee-Gateway-Software, die Zigbee-Geräte mit dem MQTT-Protokoll verbindet und so die Integration mit Plattformen wie Home Assistant ermöglicht.

## Kompatibilität

Heiman Zigbee-Sensoren sind mit Zigbee2MQTT gut kompatibel und die meisten Geräte können automatisch erkannt werden und unterstützen alle wichtigen Funktionen:

- Rauch-/Kohlenmonoxidmelder: Alarmstatus, Fehlererkennung, Stummschaltung, Batterieleistung
- Sensoren: Temperatur, Luftfeuchtigkeit, Beleuchtung, Anwesenheitserkennung
- Türsensor: Offen-/Geschlossen-Status, Manipulationserkennung

## Empfohlene Hardware

- Koordinatoren der Serien CC2652P / CC1352P (wie SLZB-06, TubeZB, ZigStar)
- Zigbee-Gateways der HS6GW-Serie von Hyman können auch zusammen verwendet werden

## Konfigurationspunkte

„yaml
# Zigbee2MQTT-Konfigurationsbeispiel
Seriennummer:
  Port: /dev/ttyACM0
Fortgeschritten:
  Kanal: 15
  network_key: GENERIEREN
„

> **Referenz**: [Liste der von Zigbee2MQTT unterstützten Geräte](https://www.zigbee2mqtt.io/supported-devices/)