---
sidebar_position: 2
---
#Zigbee2MQTT

Zigbee2MQTT é um software de gateway Zigbee de código aberto que conecta dispositivos Zigbee ao protocolo MQTT, permitindo a integração com plataformas como Home Assistant.

## Compatibilidade

Os sensores Heiman Zigbee têm boa compatibilidade no Zigbee2MQTT, e a maioria dos dispositivos pode ser reconhecida automaticamente e suportar todas as funções principais:

Alarme de fumaça / monóxido de carbono: status do alarme, detecção de falhas, controle de mudo, energia da bateria
- Sensores: temperatura, umidade, iluminação, detecção de ocupação
Sensor de porta: status aberto/fechado, detecção de violação

## Hardware recomendado

- Coordenadores da série CC2652P / CC1352P (como SLZB-06, TubeZB, ZigStar)
- Os gateways Zigbee da série Hyman HS6GW também podem ser usados juntos

## Pontos de configuração

```yaml
# Exemplo de configuração Zigbee2MQTT
série:
  porta: /dev/ttyACM0
avançado:
  canal: 15
  chave_derede: GERAR
```

> **Referência**: [lista de dispositivos compatíveis com Zigbee2MQTT](https://www.zigbee2mqtt.io/supported-devices/)