---
sidebar_position: 6
---
#AppleHome(HomeKit)

Apple HomeKit is het slimme thuisplatform van Apple, bekend om zijn sterke privacybescherming en gelokaliseerde controle.

## Integratiemethode

### Matter-apparaat (aanbevolen)

Heymann Matter over Thread-apparaten maken standaard verbinding met Apple Home:

- Vereist Apple HomePod (mini/2e generatie), Apple TV 4K of HomePod als Thread border router
- Apparaten die iOS/iPadOS 16.4 en hoger gebruiken
- Open de app "Home" → Accessoires toevoegen → Scan de Matter-koppelingscode

### Zigbee-apparaten

Met de Homebridge-plug-in kunt u Heimann Zigbee-apparaten koppelen aan Apple Home:

``` bash
npm install -g homebridge-zigbee-nt
```

> **OPMERKING**: Matter-apparaten zijn Works with Home Assistant-gecertificeerd en werken goed met Apple Home