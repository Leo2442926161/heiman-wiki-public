---
sidebar_position: 11
---
#ZHA (automação residencial Zigbee)

ZHA é a solução de integração Zigbee integrada do Home Assistant que pode gerenciar diretamente dispositivos Zigbee sem software adicional.

## Compatibilidade

Os sensores Hyman Zigbee têm boa compatibilidade em ZHA e suporte:

- **Alarme de fumaça/CO**: status do alarme, detecção de falhas, nível de bateria, mudo
- **Sensor de porta**: ligar/desligar, violação
- **Infravermelho humano**: detecção de movimento, iluminação
- **Temperatura e Umidade**: temperatura, umidade
- **Inundação**: Alarme de vazamento de água
- **Soquete inteligente**: interruptor, medição de consumo de energia

## Requisitos de hardware

- Coordenador Zigbee: HUSBZB-1, Conbee II, SkyConnect, SLZB-06, etc.
- Conecte-se ao Home Assistant via USB ou rede

## Configuração

ZHA é fácil de configurar. Basta selecionar a porta serial e a área para digitalizar e descobrir o dispositivo automaticamente. Não há necessidade de gravar manualmente os arquivos de configuração.

> **Referência**: [Documento ZHA do Home Assistant](https://www.home-assistant.io/integrations/zha/)