---
sidebar_position: 10
---
#hubitat

Hubitat est un hub de maison intelligente axé sur le contrôle localisé, prenant en charge les appareils Zigbee et Z-Wave, avec toute l'automatisation effectuée localement sans avoir besoin de services cloud.

## Méthode d'intégration

### Appareils Zigbee

Les capteurs Hyman Zigbee s'associent directement aux hubs Hubitat Elevation :

1. Entrez en mode de couplage Zigbee dans Hubitat
2. Mettez le capteur Heiman en mode d'appairage
3. L'appareil sera automatiquement découvert et ajouté

### Appareils Z-Wave

Les appareils Hyman Z-Wave prennent également en charge le couplage direct avec Hubitat, en tirant parti de la puce Z-Wave intégrée de Hubitat.

### Pilote personnalisé

Certains appareils Heiman peuvent nécessiter des pilotes personnalisés et les utilisateurs de la communauté ont écrit des pilotes compatibles pour les capteurs courants.

## Avantages

- **100 % de localisation** : toute la logique d'automatisation est exécutée localement dans Hubitat et ne repose pas sur le cloud
- **Faible latence** : réseau local Zigbee/Z-Wave Mesh, réponse rapide
- **Communauté riche** : la communauté Hubitat dispose d'un grand nombre de partages de configuration d'utilisateurs Heiman

> **Référence** : [Communauté Hubitat - Discussion sur l'équipement Heiman](https://community.hubitat.com/)