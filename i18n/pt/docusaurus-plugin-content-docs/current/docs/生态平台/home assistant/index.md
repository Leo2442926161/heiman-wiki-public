---
sidebar_position: 1
---
#HomeAssistente

A Haiman Technology ingressou oficialmente no programa de certificação **Works with Home Assistant** em fevereiro de 2026 e se tornou um dos primeiros parceiros chineses do programa.

## Dispositivo de autenticação

Os seguintes dispositivos Heiman foram oficialmente certificados para garantir localização e compatibilidade estável com o Home Assistant:

| Equipamento | Região | Método de conexão |
|------|------|----------|
| Alarme de fumaça inteligente | Estados Unidos | Matéria sobre Tópico |
| Alarme de fumaça inteligente | UE/China | Matéria sobre Tópico |
| Alarme inteligente de monóxido de carbono | Estados Unidos | Matéria sobre Tópico |
| Alarme inteligente de monóxido de carbono | UE/China | Matéria sobre Tópico |
| Sensor infravermelho para corpo humano série M1 | Globais | Matéria / Zigbee |
| Detector de imersão em água Série L1 | Globais | Matéria / Zigbee |
| Sensor de Temperatura e Umidade Série H1 | Globais | Matéria / Zigbee |

## Método de integração

### por Matéria

1. Certifique-se de ter um roteador de borda Matter over Thread (como Home Assistant Green + Connect ZBT-2, Apple HomePod, Google Nest Hub, etc.)
2. Configure a integração do Matter no Home Assistant
3. Adicione o dispositivo para descobri-lo automaticamente

### via Zigbee2MQTT/ZHA

Os dispositivos Hyman Zigbee são suportados nativamente por Zigbee2MQTT e ZHA sem necessidade de configuração adicional.

## Controle de localização

Todos os dispositivos certificados suportam **controle localizado** sem depender de serviços de nuvem. Mesmo que a Internet esteja desligada, os alarmes dos sensores e as ligações de automação ainda podem funcionar normalmente.

## Envolvimento da comunidade

Heyman participa ativamente de discussões na comunidade Home Assistant e continua a otimizar a experiência do produto com base no feedback do usuário.

> **Referência**: [Anúncio oficial do Home Assistant - Heiman ingressa no Works with Home Assistant](https://www.home-assistant.io/blog/2026/02/24/heiman-joins-works-with-home-assistant/)