---
sidebar_position: 6
---
#AppleHome(HomeKit)

Apple HomeKit ist die Smart-Home-Plattform von Apple, die für ihren starken Datenschutz und ihre lokale Steuerung bekannt ist.

## Integrationsmethode

### Matter-Gerät (empfohlen)

Heymann Matter over Thread-Geräte verbinden sich nativ mit Apple Home:

- Erfordert Apple HomePod (Mini/2. Generation), Apple TV 4K oder HomePod als Thread-Border-Router
- Geräte mit iOS/iPadOS 16.4 und höher
- Öffnen Sie die „Home“-App → Zubehör hinzufügen → Matter-Pairing-Code scannen

### Zigbee-Geräte

Mit dem Homebridge-Plugin können Sie Heimann Zigbee-Geräte mit Apple Home verbinden:

„Bash
npm install -g homebridge-zigbee-nt
„

> **HINWEIS**: Matter-Geräte sind „Works with Home Assistant“-zertifiziert und funktionieren gut mit Apple Home