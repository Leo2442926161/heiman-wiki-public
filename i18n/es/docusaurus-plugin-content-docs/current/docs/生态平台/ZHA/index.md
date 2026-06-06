---
sidebar_position: 11
---
#ZHA (Domótica Zigbee)

ZHA es la solución de integración Zigbee integrada de Home Assistant que puede administrar directamente dispositivos Zigbee sin software adicional.

## Compatibilidad

Los sensores Hyman Zigbee tienen buena compatibilidad en ZHA y admiten:

- **Alarma de humo/CO**: estado de alarma, detección de fallas, nivel de batería, silencio
- **Sensor de puerta**: encendido/apagado, manipulación
- **Infrarrojo humano**: detección de movimiento, iluminación
- **Temperatura y Humedad**: temperatura, humedad
- **Inundación**: alarma de fuga de agua
- **Toma inteligente**: interruptor, medición del consumo de energía

## Requisitos de hardware

- Coordinador Zigbee: HUSBZB-1, Conbee II, SkyConnect, SLZB-06, etc.
- Conéctese a Home Assistant a través de USB o red

## Configuración

ZHA es fácil de configurar. Simplemente seleccione el puerto serie y el área para escanear y descubrir automáticamente el dispositivo. No es necesario escribir archivos de configuración manualmente.

> **Referencia**: [Documento ZHA de Home Assistant](https://www.home-assistant.io/integrations/zha/)