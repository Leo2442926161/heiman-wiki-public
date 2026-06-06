---
sidebar_position: 4
---
#OpenHAB

OpenHAB ist eine Open-Source-Hausautomationsplattform, die sich auf herstellerneutrale und protokollneutrale Integration konzentriert.

## Integrationsmethode

### Zigbee-Bindung

Mit der Zigbee-Anbindung von OpenHAB können Heymann Zigbee-Sensoren direkt angeschlossen werden. Muss mit einem Zigbee-Koordinator (z. B. Conbee II, SLZB-06) verwendet werden.

### Materiebindung

OpenHAB 4.x und höher unterstützen das Matter-Protokoll. Hyman Matter-Geräte können über Matter-Bindung integriert werden, was einen Thread-Border-Router erfordert.

### MQTT-Methode

Wird mit Zigbee2MQTT verwendet, um Sensordaten über MQTT-Bindung zu empfangen.

> **Referenz**: [OpenHAB Zigbee Binding Document](https://www.openhab.org/addons/bindings/zigbee/)