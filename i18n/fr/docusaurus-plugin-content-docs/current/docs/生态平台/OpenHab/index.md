---
sidebar_position: 4
---
#OpenHAB

OpenHAB est une plate-forme domotique open source axée sur une intégration neutre en termes de fournisseur et de protocole.

## Méthode d'intégration

### Liaison Zigbee

Grâce à la liaison Zigbee d'OpenHAB, les capteurs Heymann Zigbee peuvent être branchés directement. Doit être utilisé avec le coordinateur Zigbee (tel que Conbee II, SLZB-06).

### Liaison de matière

OpenHAB 4.x et versions ultérieures prennent en charge le protocole Matter. Les appareils Hyman Matter peuvent être intégrés via la liaison Matter, qui nécessite un routeur de bordure Thread.

### Méthode MQTT

Utilisé avec Zigbee2MQTT pour recevoir les données du capteur via la liaison MQTT.

> **Référence** : [Document de liaison OpenHAB Zigbee](https://www.openhab.org/addons/bindings/zigbee/)