---
sidebar_position: 1
---
#ThuisAssistent

Haiman Technology nam in februari 2026 officieel deel aan het **Works with Home Assistant**-certificeringsprogramma en werd een van de eerste Chinese partners van het programma.

## Authenticatieapparaat

De volgende Heiman-apparaten zijn officieel gecertificeerd om lokalisatie en stabiele compatibiliteit met Home Assistant te garanderen:

| Uitrusting | Regio | Verbindingsmethode |
|------|------|----------|
| Slimme rookmelder | Verenigde Staten | Kwestie boven draad |
| Slimme rookmelder | EU/China | Kwestie boven draad |
| Slimme koolmonoxidemelder | Verenigde Staten | Kwestie boven draad |
| Slimme koolmonoxidemelder | EU/China | Kwestie boven draad |
| Menselijk lichaam infraroodsensor M1-serie | Globaal | Materie / Zigbee |
| Waterdompeldetector L1-serie | Globaal | Materie / Zigbee |
| Temperatuur- en vochtigheidssensor H1-serie | Globaal | Materie / Zigbee |

## Integratiemethode

### door materie

1. Zorg ervoor dat je een Matter over Thread-grensrouter hebt (zoals Home Assistant Green + Connect ZBT-2, Apple HomePod, Google Nest Hub, enz.)
2. Configureer Matter-integratie in Home Assistant
3. Voeg het apparaat toe om het automatisch te ontdekken

### via Zigbee2MQTT/ZHA

Hyman Zigbee-apparaten worden standaard ondersteund door Zigbee2MQTT en ZHA zonder dat aanvullende configuratie vereist is.

## Lokalisatiecontrole

Alle gecertificeerde apparaten ondersteunen **gelokaliseerde bediening** zonder afhankelijk te zijn van cloudservices. Zelfs als het internet uitvalt, kunnen sensoralarmen en automatiseringskoppelingen nog steeds normaal werken.

## Gemeenschapsbetrokkenheid

Heyman neemt actief deel aan discussies in de Home Assistant-gemeenschap en blijft de productervaring optimaliseren op basis van gebruikersfeedback.

> **Referentie**: [Officiële aankondiging van Home Assistant - Heiman sluit zich aan bij Works with Home Assistant](https://www.home-assistant.io/blog/2026/02/24/heiman-joins-works-with-home-assistant/)