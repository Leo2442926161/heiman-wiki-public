---
sidebar_position: 5
---
# Collecteur de compteurs d'eau - collecteur de données de compteurs d'eau sans fil

## Aperçu

Le collecteur de compteurs d'eau est un dispositif de collecte de données sans fil wM-Bus lancé par Hyman pour le domaine de l'eau intelligent. Il fonctionne dans la bande de fréquence 868 MHz (norme EN 13757) et prend en charge le comptage d'impulsions et la transmission de données sans fil. Il est utilisé pour lire à distance les données de mesure des compteurs d’eau et les télécharger vers le système centralisé de relevé des compteurs. Il convient à des scénarios tels que les appartements, les zones résidentielles, les bâtiments commerciaux et la surveillance des eaux industrielles.

## Spécifications techniques

| Paramètre | Valeur |
|------|-----|
| Protocole de communication | wM-Bus (EN 13757) |
| Bande de fréquence de fonctionnement | 868 MHz (bande européenne SRD) |
| Taux de transmission | 4,8 kbps / 16,384 kbps / 100 kbps (mode T/S/R) |
| Distance de communication | Environ 100 à 300 mètres en intérieur, environ 500 à 1 000 mètres en espace ouvert |
| Interface du capteur | Commutateur à lames/entrée d'impulsion de capteur Hall |
| Méthode d'alimentation | Batterie au lithium industrielle (ER18505 / ER26500) |
| Autonomie de la batterie | 6 à 10 ans (généralement signalé 1 fois/jour) |
| Température de fonctionnement | -20°C ~ +60°C |
| Humidité de travail | ≤ 95 % HR |
| Niveau de protection | IP65 ~ IP68 (selon l'environnement d'installation) |
| Cryptage des données | AES-128 (facultatif) |

## Fonctionnalités

-Prend en charge la collecte d'impulsions du commutateur à lames/capteur Hall
- Comptage d'impulsions et conversion de débit, reporting automatique des données d'utilisation
-Supporte les trois modes de fonctionnement wM-Bus S/T/R
- Faible consommation d'énergie, sommeil profond, longue durée de vie de la batterie
- Cryptage des données AES-128 pour assurer la sécurité des communications
-Prise en charge de la mise à niveau du micrologiciel à distance
- Mécanisme de déconnexion, de reconnexion et de retransmission des données
- Prend en charge le protocole de couche application EN 13757-3
- Peut être utilisé avec le collecteur HS1-CM / la passerelle HS1-GW pour un téléchargement centralisé

## Normes de certification

- EN 13757-4 (Couche physique Wireless M-Bus)
- EN 13757-3 (couche applicative M-Bus)
-CE/ROUGE

## Documents associés

- Voir [Données techniques wM-Bus](../technical data.md)