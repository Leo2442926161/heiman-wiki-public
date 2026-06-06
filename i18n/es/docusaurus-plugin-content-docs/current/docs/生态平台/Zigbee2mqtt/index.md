---
sidebar_position: 2
---
#Zigbee2MQTT

Zigbee2MQTT es un software de puerta de enlace Zigbee de código abierto que conecta los dispositivos Zigbee con el protocolo MQTT, permitiendo la integración con plataformas como Home Assistant.

## Compatibilidad

Los sensores Heiman Zigbee tienen buena compatibilidad en Zigbee2MQTT y la mayoría de los dispositivos pueden reconocerse automáticamente y admitir todas las funciones clave:

- Alarma de humo/monóxido de carbono: estado de alarma, detección de fallos, control de silencio, alimentación por batería
- Sensores: temperatura, humedad, iluminación, detección de ocupación.
- Sensor de puerta: estado de apertura/cierre, detección de manipulación

## Hardware recomendado

- Coordinadores de la serie CC2652P / CC1352P (como SLZB-06, TubeZB, ZigStar)
- Las puertas de enlace Zigbee de la serie Hyman HS6GW también se pueden utilizar juntas

## Puntos de configuración

```yaml
# Ejemplo de configuración de Zigbee2MQTT
de serie:
  puerto: /dev/ttyACM0
avanzado:
  canal: 15
  clave_red: GENERAR
```

> **Referencia**: [Lista de dispositivos compatibles con Zigbee2MQTT](https://www.zigbee2mqtt.io/supported-devices/)