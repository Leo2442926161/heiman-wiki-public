---
sidebar_position: 2
---
#Zigbee2MQTT

Zigbee2MQTT è un software gateway Zigbee open source che collega i dispositivi Zigbee al protocollo MQTT, consentendo l'integrazione con piattaforme come Home Assistant.

## Compatibilità

I sensori Heiman Zigbee hanno una buona compatibilità in Zigbee2MQTT e la maggior parte dei dispositivi può essere riconosciuta automaticamente e supporta tutte le funzioni chiave:

- Allarme fumo/monossido di carbonio: stato allarme, rilevamento guasti, controllo muto, alimentazione a batteria
- Sensori: temperatura, umidità, illuminazione, rilevamento presenza
- Sensore porta: stato aperto/chiuso, rilevamento manomissione

## Hardware consigliato

- Coordinatori serie CC2652P / CC1352P (come SLZB-06, TubeZB, ZigStar)
- I gateway Zigbee della serie Hyman HS6GW possono essere utilizzati anche insieme

## Punti di configurazione

```yaml
# Esempio di configurazione Zigbee2MQTT
seriale:
  porta: /dev/ttyACM0
avanzato:
  canale: 15
  chiave_rete: GENERARE
```

> **Riferimento**: [Elenco dei dispositivi supportati da Zigbee2MQTT](https://www.zigbee2mqtt.io/supported-devices/)