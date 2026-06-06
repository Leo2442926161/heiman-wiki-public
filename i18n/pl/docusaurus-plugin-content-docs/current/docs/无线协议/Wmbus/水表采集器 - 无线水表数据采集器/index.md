---
sidebar_position: 5
---
# Kolektor wodomierza - bezprzewodowy zbieracz danych wodomierza

## Przegląd

Kolektor wodomierza to bezprzewodowe urządzenie do gromadzenia danych wM-Bus wprowadzone na rynek przez firmę Hyman dla inteligentnego pola wodnego. Pracuje w paśmie częstotliwości 868 MHz (norma EN 13757) i obsługuje zliczanie impulsów oraz bezprzewodową transmisję danych. Służy do zdalnego odczytu danych pomiarowych wodomierza i przesłania ich do centralnego systemu odczytu wodomierza. Nadaje się do scenariuszy takich jak mieszkania, obszary mieszkalne, budynki komercyjne i monitorowanie wody przemysłowej.

## Specyfikacje techniczne

| Parametr | Wartość |
|------|-----|
| Protokół komunikacyjny | wM-Bus (EN 13757) |
| Pasmo częstotliwości roboczej | 868 MHz (europejskie pasmo SRD) |
| Szybkość transmisji | 4,8 kbps / 16,384 kbps / 100 kbps (tryb T/S/R) |
| Odległość komunikacyjna | Około 100~300 metrów w pomieszczeniu, około 500~1000 metrów na otwartej przestrzeni |
| Interfejs czujnika | Kontaktron / wejście impulsowe czujnika Halla |
| Sposób zasilania | Przemysłowa bateria litowa (ER18505 / ER26500) |
| Żywotność baterii | 6 ~ 10 lat (zwykle zgłaszane 1 raz dziennie) |
| Temperatura pracy | -20°C ~ +60°C |
| Wilgotność robocza | ≤ 95% wilgotności względnej |
| Poziom ochrony | IP65 ~ IP68 (w zależności od środowiska instalacji) |
| Szyfrowanie danych | AES-128 (opcjonalnie) |

## Funkcje

-Obsługuje zbieranie impulsów kontaktronu/czujnika Halla
- Zliczanie impulsów i konwersja przepływu, automatyczne raportowanie danych użytkowania
-Obsługa trzech trybów pracy wM-Bus S/T/R
- Niskie zużycie energii, głęboki sen, długa żywotność baterii
- Szyfrowanie danych AES-128 w celu zapewnienia bezpieczeństwa komunikacji
-Obsługa zdalnej aktualizacji oprogramowania sprzętowego
- Mechanizm ponownego rozłączenia i retransmisji danych
- Obsługuje protokół warstwy aplikacji EN 13757-3
- Może być używany z modułem zbierającym HS1-CM / bramką HS1-GW w celu scentralizowanego przesyłania

## Standardy certyfikacji

- EN 13757-4 (warstwa fizyczna bezprzewodowej magistrali M-Bus)
- EN 13757-3 (warstwa aplikacji M-Bus)
-CE/CZERWONY

## Powiązane dokumenty

- Patrz [dane techniczne wM-Bus](../dane techniczne.md)