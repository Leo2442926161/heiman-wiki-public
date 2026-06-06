---
sidebar_position: 6
---
#AppleHome(HomeKit)

Apple HomeKit est la plate-forme de maison intelligente d'Apple, connue pour sa solide protection de la vie privée et son contrôle localisé.

## Méthode d'intégration

### Appareil Matter (recommandé)

Les appareils Heymann Matter over Thread se connectent nativement à Apple Home :

- Nécessite Apple HomePod (mini/2ème génération), Apple TV 4K ou HomePod comme routeur de bordure Thread
- Appareils utilisant iOS/iPadOS 16.4 et supérieur
- Ouvrez l'application « Accueil » → Ajouter des accessoires → Scannez le code d'appairage Matter

### Appareils Zigbee

Le plug-in Homebridge vous permet de relier les appareils Heimann Zigbee à Apple Home :

```bash
npm install -g homebridge-zigbee-nt
```

> **REMARQUE** : les appareils Matter sont certifiés Works with Home Assistant et fonctionnent bien avec Apple Home