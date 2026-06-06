---
sidebar_position: 11
---
#ZHA (Domotica Zigbee)

ZHA è la soluzione di integrazione Zigbee integrata di Home Assistant in grado di gestire direttamente i dispositivi Zigbee senza software aggiuntivo.

## Compatibilità

I sensori Hyman Zigbee hanno una buona compatibilità in ZHA e supportano:

- **Allarme fumo/CO**: stato allarme, rilevamento guasti, livello batteria, disattivazione audio
- **Sensore porta**: on/off, tamper
- **Infrarossi umani**: rilevamento del movimento, illuminazione
- **Temperatura e Umidità**: temperatura, umidità
- **Alluvione**: Allarme perdita d'acqua
- **Presa intelligente**: interruttore, misurazione del consumo energetico

## Requisiti hardware

- Coordinatore Zigbee: HUSBZB-1, Conbee II, SkyConnect, SLZB-06, ecc.
- Connettiti a Home Assistant tramite USB o rete

##Configurazione

ZHA è facile da configurare. Basta selezionare la porta seriale e l'area per scansionare e rilevare automaticamente il dispositivo. Non è necessario scrivere manualmente i file di configurazione.

> **Riferimento**: [Documento Home Assistant ZHA](https://www.home-assistant.io/integrations/zha/)