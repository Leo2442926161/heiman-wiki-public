---
sidebar_position: 11
---
#ZHA (Zigbee-huisautomatisering)

ZHA is de ingebouwde Zigbee-integratieoplossing van Home Assistant die Zigbee-apparaten rechtstreeks kan beheren zonder extra software.

## Compatibiliteit

Hyman Zigbee-sensoren hebben goede compatibiliteit in ZHA en ondersteunen:

- **Rook-/CO-alarm**: alarmstatus, foutdetectie, batterijniveau, dempen
- **Deursensor**: aan/uit, sabotage
- **Menselijk infrarood**: bewegingsdetectie, verlichting
- **Temperatuur en vochtigheid**: temperatuur, vochtigheid
- **Overstroming**: alarm voor waterlekkage
- **Smart socket**: schakelaar, meting van energieverbruik

## Hardwarevereisten

- Zigbee-coördinator: HUSBZB-1, Conbee II, SkyConnect, SLZB-06, enz.
- Maak verbinding met Home Assistant via USB of netwerk

## Configuratie

ZHA is eenvoudig te configureren. Selecteer gewoon de seriële poort en het gebied om het apparaat automatisch te scannen en te ontdekken. Het is niet nodig om handmatig configuratiebestanden te schrijven.

> **Referentie**: [Home Assistant ZHA-document](https://www.home-assistant.io/integrations/zha/)