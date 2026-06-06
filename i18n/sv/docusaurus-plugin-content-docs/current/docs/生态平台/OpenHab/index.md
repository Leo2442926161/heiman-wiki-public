---
sidebar_position: 4
---
#OpenHAB

OpenHAB är en hemautomatiseringsplattform med öppen källkod fokuserad på leverantörsneutral och protokollneutral integration.

## Integrationsmetod

### Zigbee-bindning

Med OpenHAB:s Zigbee-bindning kan Heymann Zigbee-sensorer kopplas in direkt. Behöver användas med Zigbee-koordinator (som Conbee II, SLZB-06).

### Materiabindande

OpenHAB 4.x och senare stöder Matter-protokollet. Hyman Matter-enheter kan integreras genom Matter-bindning, vilket kräver en trådkantsrouter.

### MQTT-metod

Används med Zigbee2MQTT för att ta emot sensordata via MQTT-bindning.

> **Referens**: [OpenHAB Zigbee Binding Document](https://www.openhab.org/addons/bindings/zigbee/)