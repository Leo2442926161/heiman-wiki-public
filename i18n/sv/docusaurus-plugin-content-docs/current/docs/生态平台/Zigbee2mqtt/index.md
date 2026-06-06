---
sidebar_position: 2
---
#Zigbee2MQTT

Zigbee2MQTT är en Zigbee-gateway-mjukvara med öppen källkod som överbryggar Zigbee-enheter till MQTT-protokollet, vilket möjliggör integration med plattformar som Home Assistant.

## Kompatibilitet

Heiman Zigbee-sensorer har god kompatibilitet i Zigbee2MQTT, och de flesta enheter kan kännas igen automatiskt och stöder alla nyckelfunktioner:

- Rök/kolmonoxidlarm: larmstatus, feldetektering, mute-kontroll, batteridrift
- Sensorer: temperatur, luftfuktighet, belysning, närvarodetektering
- Dörrsensor: status för öppen/stängning, sabotagedetektering

## Rekommenderad hårdvara

- CC2652P / CC1352P seriekoordinatorer (som SLZB-06, TubeZB, ZigStar)
- Hyman HS6GW-serien Zigbee-gateways kan också användas tillsammans

## Konfigurationspunkter

``` jaml
# Zigbee2MQTT-konfigurationsexempel
serie:
  port: /dev/ttyACM0
avancerad:
  kanal: 15
  nätverksnyckel: GENERERA
```

> **Referens**: [lista över enheter som stöds av Zigbee2MQTT](https://www.zigbee2mqtt.io/supported-devices/)