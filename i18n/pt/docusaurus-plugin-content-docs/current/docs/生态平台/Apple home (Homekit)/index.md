---
sidebar_position: 6
---
#AppleHome(HomeKit)

Apple HomeKit é a plataforma doméstica inteligente da Apple, conhecida por sua forte proteção de privacidade e controle localizado.

## Método de integração

### Dispositivo de matéria (recomendado)

Os dispositivos Heymann Matter over Thread se conectam nativamente ao Apple Home:

- Requer Apple HomePod (mini/2ª geração), Apple TV 4K ou HomePod como roteador de borda Thread
- Dispositivos que usam iOS/iPadOS 16.4 e superior
- Abra o aplicativo "Home" → Adicionar acessórios → Digitalize o código de emparelhamento do Matter

### Dispositivos Zigbee

O plug-in Homebridge permite conectar dispositivos Heimann Zigbee ao Apple Home:

```bash
npm instalar -g homebridge-zigbee-nt
```

> **NOTA**: Os dispositivos Matter são certificados pelo Works with Home Assistant e funcionam bem com o Apple Home