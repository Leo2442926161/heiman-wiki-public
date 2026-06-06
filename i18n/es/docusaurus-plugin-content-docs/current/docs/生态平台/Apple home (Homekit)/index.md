---
sidebar_position: 6
---
#AppleHome (Kit de hogar)

Apple HomeKit es la plataforma de hogar inteligente de Apple, conocida por su sólida protección de la privacidad y control localizado.

## Método de integración

### Dispositivo Matter (recomendado)

Los dispositivos Heymann Matter over Thread se conectan de forma nativa a Apple Home:

- Requiere Apple HomePod (mini/segunda generación), Apple TV 4K o HomePod como enrutador Thread Border
- Dispositivos que utilizan iOS/iPadOS 16.4 y superior
- Abra la aplicación "Inicio" → Agregar accesorios → Escanee el código de emparejamiento de Matter

### Dispositivos Zigbee

El complemento Homebridge le permite conectar dispositivos Heimann Zigbee con Apple Home:

```golpecito
instalación npm -g homebridge-zigbee-nt
```

> **NOTA**: Los dispositivos Matter cuentan con la certificación Works with Home Assistant y funcionan bien con Apple Home