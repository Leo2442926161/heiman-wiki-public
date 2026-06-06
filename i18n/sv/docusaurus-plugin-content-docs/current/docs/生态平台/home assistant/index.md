---
sidebar_position: 1
---
#Hemassistent

Haiman Technology gick officiellt med i certifieringsprogrammet **Works with Home Assistant** i februari 2026 och blev en av de första kinesiska partnerna i programmet.

## Autentiseringsenhet

Följande Heiman-enheter har certifierats officiellt för att säkerställa lokalisering och stabil kompatibilitet med Home Assistant:

| Utrustning | Region | Anslutningsmetod |
|------|------|---------|
| Smart Brandvarnare | USA | Matter över tråd |
| Smart Brandvarnare | EU / Kina | Matter över tråd |
| Smart kolmonoxidlarm | USA | Matter över tråd |
| Smart kolmonoxidlarm | EU / Kina | Matter över tråd |
| Människokroppens infraröda sensor M1-serien | Global | Matter / Zigbee |
| Vattennedsänkningsdetektor L1-serien | Global | Matter / Zigbee |
| Temperatur- och luftfuktighetsgivare H1-serien | Global | Matter / Zigbee |

## Integrationsmetod

### av Matter

1. Se till att du har en Matter over Thread-gränsrouter (som Home Assistant Green + Connect ZBT-2, Apple HomePod, Google Nest Hub, etc.)
2. Konfigurera Matter integration i Home Assistant
3. Lägg till enheten för att automatiskt upptäcka den

### via Zigbee2MQTT/ZHA

Hyman Zigbee-enheter stöds av Zigbee2MQTT och ZHA utan att ytterligare konfiguration krävs.

## Lokaliseringskontroll

Alla certifierade enheter stöder **lokaliserad kontroll** utan att förlita sig på molntjänster. Även om internet är nere kan sensorlarm och automationskopplingar fortfarande fungera normalt.

## Samhällsengagemang

Heyman deltar aktivt i diskussioner i Home Assistant-communityt och fortsätter att optimera produktupplevelsen baserat på feedback från användare.

> **Referens**: [Home Assistant officiellt meddelande - Heiman går med Works with Home Assistant](https://www.home-assistant.io/blog/2026/02/24/heiman-joins-works-with-home-assistant/)