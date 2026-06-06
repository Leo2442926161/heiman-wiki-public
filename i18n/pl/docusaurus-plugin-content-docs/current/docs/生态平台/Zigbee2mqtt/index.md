---
sidebar_position: 2
---
#Zigbee2MQTT

Zigbee2MQTT to oprogramowanie bramy Zigbee o otwartym kodzie źródłowym, które łączy urządzenia Zigbee z protokołem MQTT, umożliwiając integrację z platformami takimi jak Home Assistant.

## Zgodność

Czujniki Heiman Zigbee mają dobrą kompatybilność z Zigbee2MQTT, a większość urządzeń może zostać automatycznie rozpoznana i obsługuje wszystkie kluczowe funkcje:

- Alarm dymu/tlenku węgla: stan alarmu, wykrywanie usterek, kontrola wyciszenia, moc baterii
- Czujniki: temperatury, wilgotności, oświetlenia, wykrywania obecności
- Czujnik drzwi: stan otwarcia/zamknięcia, detekcja sabotażu

## Zalecany sprzęt

- Koordynatory serii CC2652P / CC1352P (takie jak SLZB-06, TubeZB, ZigStar)
- Bramki Zigbee serii Hyman HS6GW mogą być również używane razem

## Punkty konfiguracyjne

```yaml
# Przykład konfiguracji Zigbee2MQTT
serial:
  port: /dev/ttyACM0
zaawansowane:
  kanał: 15
  klucz_sieciowy: GENERUJ
```

> **Odniesienie**: [lista obsługiwanych urządzeń Zigbee2MQTT](https://www.zigbee2mqtt.io/supported-devices/)