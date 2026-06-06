---
sidebar_position: 2
---
#Zigbee2MQTT

Zigbee2MQTT est un logiciel de passerelle Zigbee open source qui relie les appareils Zigbee au protocole MQTT, permettant l'intégration avec des plates-formes telles que Home Assistant.

## Compatibilité

Les capteurs Heiman Zigbee ont une bonne compatibilité dans Zigbee2MQTT, et la plupart des appareils peuvent être automatiquement reconnus et prendre en charge toutes les fonctions clés :

- Alarme de fumée/monoxyde de carbone : état de l'alarme, détection de défauts, contrôle de la sourdine, alimentation par batterie
- Capteurs : température, humidité, éclairage, détection de présence
- Capteur de porte : état d'ouverture/fermeture, détection d'effraction

## Matériel recommandé

- Coordonnateurs des séries CC2652P / CC1352P (tels que SLZB-06, TubeZB, ZigStar)
- Les passerelles Zigbee de la série Hyman HS6GW peuvent également être utilisées ensemble

## Points de configuration

```yaml
# Exemple de configuration Zigbee2MQTT
série :
  port : /dev/ttyACM0
avancé :
  canal : 15
  clé_réseau : GÉNÉRER
```

> **Référence** : [Liste des appareils pris en charge par Zigbee2MQTT](https://www.zigbee2mqtt.io/supported-devices/)