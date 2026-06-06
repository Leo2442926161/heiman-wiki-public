---
sidebar_position: 1
---
#AssistantÀ Domicile

Haiman Technology a officiellement rejoint le programme de certification **Works with Home Assistant** en février 2026 et est devenu l'un des premiers partenaires chinois du programme.

## Appareil d'authentification

Les appareils Heiman suivants ont été officiellement certifiés pour garantir la localisation et une compatibilité stable avec Home Assistant :

| Équipement | Région | Méthode de connexion |
|------|------|----------|
| Détecteur de fumée intelligent | États-Unis | La question avant le fil |
| Détecteur de fumée intelligent | UE / Chine | La question avant le fil |
| Alarme intelligente de monoxyde de carbone | États-Unis | La question avant le fil |
| Alarme intelligente de monoxyde de carbone | UE / Chine | La question avant le fil |
| Capteur infrarouge du corps humain série M1 | Mondial | Matière / Zigbee |
| Détecteur d'immersion dans l'eau série L1 | Mondial | Matière / Zigbee |
| Capteur de température et d'humidité série H1 | Mondial | Matière / Zigbee |

## Méthode d'intégration

### par Matière

1. Assurez-vous d'avoir un routeur de bordure Matter over Thread (comme Home Assistant Green + Connect ZBT-2, Apple HomePod, Google Nest Hub, etc.)
2. Configurer l'intégration de Matter dans Home Assistant
3. Ajoutez l'appareil pour le découvrir automatiquement

### via Zigbee2MQTT/ZHA

Les appareils Hyman Zigbee sont pris en charge nativement par Zigbee2MQTT et ZHA sans aucune configuration supplémentaire requise.

## Contrôle de localisation

Tous les appareils certifiés prennent en charge le **contrôle localisé** sans recourir aux services cloud. Même si Internet est en panne, les alarmes des capteurs et les liaisons d'automatisation peuvent toujours fonctionner normalement.

## Engagement communautaire

Heyman participe activement aux discussions de la communauté Home Assistant et continue d'optimiser l'expérience produit en fonction des commentaires des utilisateurs.

> **Référence** : [Annonce officielle de Home Assistant - Heiman rejoint Works with Home Assistant](https://www.home-assistant.io/blog/2026/02/24/heiman-joins-works-with-home-assistant/)