---
sidebar_position: 6
---
#AppleHome (HomeKit)

Apple HomeKit to platforma inteligentnego domu firmy Apple, znana z silnej ochrony prywatności i zlokalizowanej kontroli.

## Metoda integracji

### Urządzenie Matter (zalecane)

Urządzenia Heymann Matter over Thread natywnie łączą się z Apple Home:

- Wymaga Apple HomePod (mini/2. generacji), Apple TV 4K lub HomePod jako routera granicznego Thread
- Urządzenia z systemem iOS/iPadOS 16.4 i nowszym
- Otwórz aplikację „Home” → Dodaj akcesoria → Zeskanuj kod parowania Matter

### Urządzenia Zigbee

Wtyczka Homebridge umożliwia połączenie urządzeń Heimann Zigbee z Apple Home:

,,bicie
npm install -g homebridge-zigbee-nt
```

> **UWAGA**: Urządzenia Matter mają certyfikat Współpracy z Home Assistant i dobrze współpracują z Apple Home