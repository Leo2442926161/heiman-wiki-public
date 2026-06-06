---
sidebar_position: 1
---
#AsystentDomowy

Haiman Technology oficjalnie dołączyła do programu certyfikacji **Works with Home Assistant** w lutym 2026 roku i została jednym z pierwszych chińskich partnerów programu.

## Urządzenie uwierzytelniające

Następujące urządzenia Heiman zostały oficjalnie certyfikowane w celu zapewnienia lokalizacji i stabilnej kompatybilności z Home Assistant:

| Sprzęt | Region | Metoda połączenia |
|------|------|--------------|
| Inteligentny czujnik dymu | Stany Zjednoczone | Materia nad wątkiem |
| Inteligentny czujnik dymu | UE / Chiny | Materia nad wątkiem |
| Inteligentny alarm tlenku węgla | Stany Zjednoczone | Materia nad wątkiem |
| Inteligentny alarm tlenku węgla | UE / Chiny | Materia nad wątkiem |
| Czujnik podczerwieni ludzkiego ciała, seria M1 | Globalny | Materia / Zigbee |
| Detektor zanurzenia w wodzie Seria L1 | Globalny | Materia / Zigbee |
| Czujnik temperatury i wilgotności serii H1 | Globalny | Materia / Zigbee |

## Metoda integracji

### przez Materię

1. Upewnij się, że masz router graniczny Matter over Thread (np. Home Assistant Green + Connect ZBT-2, Apple HomePod, Google Nest Hub itp.)
2. Skonfiguruj integrację Matter w Home Assistant
3. Dodaj urządzenie, aby automatycznie je wykryć

### przez Zigbee2MQTT/ZHA

Urządzenia Hyman Zigbee są natywnie obsługiwane przez Zigbee2MQTT i ZHA bez konieczności dodatkowej konfiguracji.

## Kontrola lokalizacji

Wszystkie certyfikowane urządzenia obsługują **lokalną kontrolę** bez polegania na usługach w chmurze. Nawet jeśli Internet nie działa, alarmy czujników i połączenia automatyki mogą nadal działać normalnie.

## Zaangażowanie społeczności

Heyman aktywnie uczestniczy w dyskusjach w społeczności Home Assistant i stale optymalizuje doświadczenie produktu w oparciu o opinie użytkowników.

> **Odniesienie**: [oficjalne ogłoszenie Home Assistant – Heiman dołącza do programu Works with Home Assistant](https://www.home-assistant.io/blog/2026/02/24/heiman-joins-works-with-home-assistant/)