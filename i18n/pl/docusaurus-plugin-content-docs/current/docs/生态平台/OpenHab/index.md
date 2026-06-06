---
sidebar_position: 4
---
#OpenHAB

OpenHAB to platforma automatyki domowej typu open source, skupiająca się na integracji neutralnej pod względem dostawców i protokołów.

## Metoda integracji

### Wiązanie Zigbee

Dzięki oprawie Zigbee OpenHAB czujniki Heymann Zigbee można podłączyć bezpośrednio. Należy używać z koordynatorem Zigbee (takim jak Conbee II, SLZB-06).

### Wiązanie materii

OpenHAB 4.x i nowsze wersje obsługują protokół Matter. Urządzenia Hyman Matter można zintegrować poprzez wiązanie Matter, które wymaga routera granicznego Thread.

### Metoda MQTT

Używany z Zigbee2MQTT do odbierania danych z czujników poprzez powiązanie MQTT.

> **Odniesienie**: [Dokument wiązania OpenHAB Zigbee](https://www.openhab.org/addons/bindings/zigbee/)