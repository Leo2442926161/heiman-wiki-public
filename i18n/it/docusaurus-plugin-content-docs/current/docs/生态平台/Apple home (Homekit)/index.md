---
sidebar_position: 6
---
#AppleHome(HomeKit)

Apple HomeKit è la piattaforma di casa intelligente di Apple, nota per la sua forte protezione della privacy e il controllo localizzato.

## Metodo di integrazione

### Dispositivo Matter (consigliato)

I dispositivi Heymann Matter over Thread si connettono nativamente ad Apple Home:

- Richiede Apple HomePod (mini/2a generazione), Apple TV 4K o HomePod come router di confine Thread
- Dispositivi che utilizzano iOS/iPadOS 16.4 e versioni successive
- Apri l'app "Home" → Aggiungi accessori → Scansiona il codice di abbinamento Matter

### Dispositivi Zigbee

Il plug-in Homebridge ti consente di collegare i dispositivi Heimann Zigbee ad Apple Home:

"bash."
npm install -g homebridge-zigbee-nt
```

> **NOTA**: i dispositivi Matter sono certificati Works with Home Assistant e funzionano bene con Apple Home