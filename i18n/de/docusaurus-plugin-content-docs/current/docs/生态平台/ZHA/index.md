---
sidebar_position: 11
---
#ZHA (Zigbee Home Automation)

ZHA ist die integrierte Zigbee-Integrationslösung von Home Assistant, mit der Zigbee-Geräte ohne zusätzliche Software direkt verwaltet werden können.

## Kompatibilität

Hyman Zigbee-Sensoren sind gut mit ZHA kompatibel und unterstützen:

- **Rauch-/CO-Alarm**: Alarmstatus, Fehlererkennung, Batteriestand, Stummschaltung
- **Türsensor**: Ein/Aus, Sabotage
- **Menschliches Infrarot**: Bewegungserkennung, Beleuchtung
- **Temperatur und Luftfeuchtigkeit**: Temperatur, Luftfeuchtigkeit
- **Überschwemmung**: Wasserleckalarm
- **Smarte Steckdose**: Schalter, Stromverbrauchsmessung

## Hardwareanforderungen

- Zigbee-Koordinator: HUSBZB-1, Conbee II, SkyConnect, SLZB-06 usw.
- Stellen Sie über USB oder Netzwerk eine Verbindung zum Home Assistant her

## Konfiguration

ZHA ist einfach zu konfigurieren. Wählen Sie einfach den seriellen Anschluss und den Bereich aus, um das Gerät automatisch zu scannen und zu erkennen. Es ist nicht erforderlich, Konfigurationsdateien manuell zu schreiben.

> **Referenz**: [Home Assistant ZHA-Dokument](https://www.home-assistant.io/integrations/zha/)