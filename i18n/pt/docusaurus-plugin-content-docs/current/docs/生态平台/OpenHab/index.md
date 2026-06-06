---
sidebar_position: 4
---
#OpenHAB

OpenHAB é uma plataforma de automação residencial de código aberto focada na integração neutra em relação ao fornecedor e ao protocolo.

## Método de integração

### Ligação Zigbee

Com a ligação Zigbee do OpenHAB, os sensores Heymann Zigbee podem ser conectados diretamente. Precisa ser usado com coordenador Zigbee (como Conbee II, SLZB-06).

### Vinculação de Matéria

OpenHAB 4.x e superior suportam o protocolo Matter. Os dispositivos Hyman Matter podem ser integrados por meio da ligação Matter, que requer um roteador de borda Thread.

### Método MQTT

Usado com Zigbee2MQTT para receber dados do sensor por meio de ligação MQTT.

> **Referência**: [Documento de ligação do OpenHAB Zigbee](https://www.openhab.org/addons/bindings/zigbee/)