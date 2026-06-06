---
sidebar_position: 10
---
#hubitat

Hubitat är en smart hemhub fokuserad på lokaliserad kontroll, som stöder Zigbee och Z-Wave-enheter, med all automatisering utförd lokalt utan behov av molntjänster.

## Integrationsmetod

### Zigbee-enheter

Hyman Zigbee-sensorer paras direkt med Hubitat Elevation-nav:

1. Gå in i Zigbee-parningsläget i Hubitat
2. Sätt Heiman-sensorn i parningsläge
3. Enheten kommer automatiskt att upptäckas och läggas till

### Z-Wave-enheter

Hyman Z-Wave-enheter stöder också direkt parning med Hubitat, vilket utnyttjar Hubitats inbyggda Z-Wave-chip.

### Anpassad drivrutin

Vissa Heiman-enheter kan kräva anpassade drivrutiner, och community-användare har skrivit kompatibla drivrutiner för vanliga sensorer.

## Fördelar

- **100% lokalisering**: All automatiseringslogik exekveras lokalt i Hubitat och är inte beroende av molnet
- **Låg latens**: Lokalt Zigbee/Z-Wave Mesh-nätverk, snabb respons
- **Rik Community**: Hubitat Community har ett stort antal Heiman-användares konfigurationsdelning

> **Referens**: [Hubitat Community - Heiman Equipment Discussion](https://community.hubitat.com/)