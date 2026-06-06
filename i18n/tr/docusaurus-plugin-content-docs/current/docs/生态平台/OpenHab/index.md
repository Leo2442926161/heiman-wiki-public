---
sidebar_position: 4
---
#AçıkHAB

OpenHAB, satıcıdan bağımsız ve protokolden bağımsız entegrasyona odaklanan açık kaynaklı bir ev otomasyon platformudur.

## Entegrasyon yöntemi

### Zigbee bağlama

OpenHAB'ın Zigbee bağlantısıyla Heymann Zigbee sensörleri doğrudan takılabilir. Zigbee koordinatörüyle (Conbee II, SLZB-06 gibi) kullanılması gerekir.

### Madde Bağlayıcı

OpenHAB 4.x ve üzeri Matter protokolünü destekler. Hyman Matter cihazları, Thread sınır yönlendiricisi gerektiren Matter bağlama yoluyla entegre edilebilir.

### MQTT yöntemi

MQTT bağlama yoluyla sensör verilerini almak için Zigbee2MQTT ile birlikte kullanılır.

> **Referans**: [OpenHAB Zigbee Bağlama Belgesi](https://www.openhab.org/addons/bindings/zigbee/)