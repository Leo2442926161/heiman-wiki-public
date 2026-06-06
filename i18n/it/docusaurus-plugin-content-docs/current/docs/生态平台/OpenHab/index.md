---
sidebar_position: 4
---
#OpenHAB

OpenHAB è una piattaforma di automazione domestica open source focalizzata sull'integrazione indipendente dal fornitore e dal protocollo.

## Metodo di integrazione

### Rilegatura Zigbee

Con il collegamento Zigbee di OpenHAB, i sensori Heymann Zigbee possono essere collegati direttamente. Necessita di essere utilizzato con il coordinatore Zigbee (come Conbee II, SLZB-06).

### Legame della materia

OpenHAB 4.x e versioni successive supportano il protocollo Matter. I dispositivi Hyman Matter possono essere integrati tramite l'associazione Matter, che richiede un router di confine Thread.

### Metodo MQTT

Utilizzato con Zigbee2MQTT per ricevere i dati del sensore tramite associazione MQTT.

> **Riferimento**: [Documento di rilegatura OpenHAB Zigbee](https://www.openhab.org/addons/bindings/zigbee/)