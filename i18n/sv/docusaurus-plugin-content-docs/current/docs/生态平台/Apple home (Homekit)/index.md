---
sidebar_position: 6
---
#AppleHome(HomeKit)

Apple HomeKit är Apples smarta hemplattform, känd för sitt starka integritetsskydd och lokaliserade kontroll.

## Integrationsmetod

### Matter-enhet (rekommenderas)

Heymann Matter over Thread-enheter ansluter inbyggt till Apple Home:

- Kräver Apple HomePod (mini/2:a generationen), Apple TV 4K eller HomePod som trådkantsrouter
- Enheter som använder iOS/iPadOS 16.4 och senare
- Öppna "Hem"-appen → Lägg till tillbehör → Skanna Matter-parningskoden

### Zigbee-enheter

Homebridge-plugin-programmet låter dig koppla Heimann Zigbee-enheter till Apple Home:

``` bash
npm installera -g homebridge-zigbee-nt
```

> **OBS**: Matter-enheter är Works with Home Assistant-certifierade och fungerar bra med Apple Home