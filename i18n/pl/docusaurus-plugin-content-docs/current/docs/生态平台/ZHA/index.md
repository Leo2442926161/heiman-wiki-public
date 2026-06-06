---
sidebar_position: 11
---
#ZHA (automatyka domowa Zigbee)

ZHA to wbudowane w Home Assistant rozwiązanie integracyjne Zigbee, które może bezpośrednio zarządzać urządzeniami Zigbee bez dodatkowego oprogramowania.

## Zgodność

Czujniki Hyman Zigbee mają dobrą kompatybilność z ZHA i obsługują:

- **Alarm dymu/CO**: Stan alarmu, wykrycie usterki, poziom naładowania baterii, wyciszenie
- **Czujnik drzwi**: wł./wył., sabotaż
- **Ludzkie podczerwień**: detekcja ruchu, oświetlenie
- **Temperatura i wilgotność**: temperatura, wilgotność
- **Powódź**: Alarm wycieku wody
- **Inteligentne gniazdo**: włącznik, pomiar zużycia energii

## Wymagania sprzętowe

- Koordynator Zigbee: HUSBZB-1, Conbee II, SkyConnect, SLZB-06 itp.
- Połącz się z Home Assistant przez USB lub sieć

## Konfiguracja

ZHA jest łatwy w konfiguracji. Wystarczy wybrać port szeregowy i obszar, aby automatycznie przeskanować i wykryć urządzenie. Nie ma potrzeby ręcznego zapisywania plików konfiguracyjnych.

> **Odniesienie**: [Dokument Home Assistant ZHA](https://www.home-assistant.io/integrations/zha/)