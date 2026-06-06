---
sidebar_position: 11
---
#ZHA (Domotique Zigbee)

ZHA est la solution d'intégration Zigbee intégrée de Home Assistant qui peut gérer directement les appareils Zigbee sans logiciel supplémentaire.

## Compatibilité

Les capteurs Hyman Zigbee ont une bonne compatibilité dans ZHA et prennent en charge :

- **Alarme de fumée/CO** : état de l'alarme, détection de défauts, niveau de batterie, sourdine
- **Capteur de porte** : marche/arrêt, sabotage
- **Infrarouge humain** : détection de mouvement, éclairage
- **Température et Humidité** : température, humidité
- **Inondation** : alarme de fuite d'eau
- **Prise intelligente** : interrupteur, mesure de la consommation électrique

## Configuration matérielle requise

- Coordinateur Zigbee : HUSBZB-1, Conbee II, SkyConnect, SLZB-06, etc.
- Connectez-vous à Home Assistant via USB ou réseau

##Configuration

ZHA est facile à configurer. Sélectionnez simplement le port série et la zone pour analyser et découvrir automatiquement l'appareil. Pas besoin d'écrire manuellement les fichiers de configuration.

> **Référence** : [Document ZHA de Home Assistant](https://www.home-assistant.io/integrations/zha/)