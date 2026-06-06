---
sidebar_position: 11
---
#ZHA (Zigbee Home Automation)

ZHA är Home Assistants inbyggda Zigbee-integrationslösning som direkt kan hantera Zigbee-enheter utan ytterligare programvara.

## Kompatibilitet

Hyman Zigbee-sensorer har bra kompatibilitet i ZHA och stöder:

- **Rök/CO-larm**: Larmstatus, feldetektering, batterinivå, tyst
- **Dörrsensor**: på/av, sabotage
- **Mänsklig infraröd**: rörelsedetektering, belysning
- **Temperatur och luftfuktighet**: temperatur, luftfuktighet
- **Översvämning**: Vattenläckagelarm
- **Smart uttag**: strömbrytare, mätning av strömförbrukning

## Hårdvarukrav

- Zigbee-koordinator: HUSBZB-1, Conbee II, SkyConnect, SLZB-06, etc.
- Anslut till Home Assistant via USB eller nätverk

## Konfiguration

ZHA är lätt att konfigurera. Välj bara serieporten och området för att automatiskt skanna och upptäcka enheten. Inget behov av att manuellt skriva konfigurationsfiler.

> **Referens**: [Home Assistant ZHA Document](https://www.home-assistant.io/integrations/zha/)