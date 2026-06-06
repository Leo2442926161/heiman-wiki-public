---
sidebar_position: 1
---
#AssistenteCasa

Haiman Technology ha aderito ufficialmente al programma di certificazione **Works with Home Assistant** nel febbraio 2026 ed è diventato uno dei primi partner cinesi del programma.

## Dispositivo di autenticazione

I seguenti dispositivi Heiman sono stati ufficialmente certificati per garantire la localizzazione e la compatibilità stabile con Home Assistant:

| Attrezzatura | Regione | Metodo di connessione |
|------|------|----------|
| Rilevatore di fumo intelligente | Stati Uniti | Questione sul filo |
| Rilevatore di fumo intelligente | UE/Cina | Questione sul filo |
| Allarme intelligente per monossido di carbonio | Stati Uniti | Questione sul filo |
| Allarme intelligente per monossido di carbonio | UE/Cina | Questione sul filo |
| Sensore a infrarossi per il corpo umano serie M1 | Globale | Materia / Zigbee |
| Rilevatore di immersione in acqua Serie L1 | Globale | Materia / Zigbee |
| Sensore di temperatura e umidità serie H1 | Globale | Materia / Zigbee |

## Metodo di integrazione

### per Materia

1. Assicurati di avere un router di confine Matter over Thread (come Home Assistant Green + Connect ZBT-2, Apple HomePod, Google Nest Hub, ecc.)
2. Configura l'integrazione della materia in Home Assistant
3. Aggiungi il dispositivo per rilevarlo automaticamente

### tramite Zigbee2MQTT/ZHA

I dispositivi Hyman Zigbee sono supportati nativamente da Zigbee2MQTT e ZHA senza che sia richiesta alcuna configurazione aggiuntiva.

## Controllo della localizzazione

Tutti i dispositivi certificati supportano il **controllo localizzato** senza fare affidamento sui servizi cloud. Anche se Internet non è disponibile, gli allarmi dei sensori e i collegamenti di automazione possono ancora funzionare normalmente.

## Coinvolgimento della comunità

Heyman partecipa attivamente alle discussioni nella community di Home Assistant e continua a ottimizzare l'esperienza del prodotto in base al feedback degli utenti.

> **Riferimento**: [Annuncio ufficiale di Home Assistant - Heiman si unisce a Works with Home Assistant](https://www.home-assistant.io/blog/2026/02/24/heiman-joins-works-with-home-assistant/)