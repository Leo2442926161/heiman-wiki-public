---
sidebar_position: 10
---
#hubitat

Hubitat to inteligentny hub domowy skupiający się na zlokalizowanym sterowaniu, obsługujący urządzenia Zigbee i Z-Wave, przy czym cała automatyzacja odbywa się lokalnie, bez konieczności korzystania z usług w chmurze.

## Metoda integracji

### Urządzenia Zigbee

Czujniki Hyman Zigbee łączą się bezpośrednio z koncentratorami Hubitat Elevation:

1. Wejdź w tryb parowania Zigbee w Hubitacie
2. Przełącz czujnik Heiman w tryb parowania
3. Urządzenie zostanie automatycznie wykryte i dodane

### Urządzenia Z-Wave

Urządzenia Hyman Z-Wave obsługują również bezpośrednie parowanie z Hubitatem, wykorzystując wbudowany chip Z-Wave Hubitata.

### Niestandardowy sterownik

Niektóre urządzenia Heimana mogą wymagać niestandardowych sterowników, a użytkownicy społeczności napisali kompatybilne sterowniki dla popularnych czujników.

## Zalety

- **100% lokalizacja**: Cała logika automatyzacji jest wykonywana lokalnie w Hubitacie i nie opiera się na chmurze
- **Niskie opóźnienia**: Lokalna sieć Zigbee/Z-Wave Mesh, szybka reakcja
- **Bogata społeczność**: Społeczność Hubitat ma dużą liczbę możliwości udostępniania konfiguracji użytkownikom Heimana

> **Odniesienie**: [Społeczność Hubitat – dyskusja na temat sprzętu Heiman](https://community.hubitat.com/)