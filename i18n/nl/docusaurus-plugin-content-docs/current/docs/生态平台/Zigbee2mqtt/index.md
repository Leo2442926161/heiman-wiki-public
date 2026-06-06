---
sidebar_position: 2
---
#Zigbee2MQTT

Zigbee2MQTT is open source Zigbee-gatewaysoftware die Zigbee-apparaten overbrugt naar het MQTT-protocol, waardoor integratie met platforms zoals Home Assistant mogelijk wordt.

## Compatibiliteit

Heiman Zigbee-sensoren hebben een goede compatibiliteit in Zigbee2MQTT en de meeste apparaten kunnen automatisch worden herkend en ondersteunen alle belangrijke functies:

- Rook-/koolmonoxidemelder: alarmstatus, foutdetectie, mute-bediening, batterijvoeding
- Sensoren: temperatuur, vochtigheid, verlichting, aanwezigheidsdetectie
- Deursensor: open/dicht-status, sabotagedetectie

## Aanbevolen hardware

- CC2652P / CC1352P serie coördinatoren (zoals SLZB-06, TubeZB, ZigStar)
- Zigbee-gateways uit de Hyman HS6GW-serie kunnen ook samen worden gebruikt

## Configuratiepunten

```jaml
# Zigbee2MQTT-configuratievoorbeeld
serieel:
  poort: /dev/ttyACM0
gevorderd:
  kanaal: 15
  netwerksleutel: GENEREREN
```

> **Referentie**: [Zigbee2MQTT ondersteunde apparatenlijst](https://www.zigbee2mqtt.io/supported-devices/)