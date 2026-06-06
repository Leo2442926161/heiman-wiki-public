---
sidebar_position: 4
---
#AbiertoHAB

OpenHAB es una plataforma de automatización del hogar de código abierto centrada en la integración independiente del proveedor y del protocolo.

## Método de integración

### Encuadernación Zigbee

Con la conexión Zigbee de OpenHAB, los sensores Heymann Zigbee se pueden conectar directamente. Debe usarse con el coordinador Zigbee (como Conbee II, SLZB-06).

### Enlace de materia

OpenHAB 4.x y superiores admiten el protocolo Matter. Los dispositivos Hyman Matter se pueden integrar a través del enlace Matter, que requiere un enrutador de borde Thread.

### Método MQTT

Se utiliza con Zigbee2MQTT para recibir datos del sensor a través del enlace MQTT.

> **Referencia**: [Documento de enlace OpenHAB Zigbee](https://www.openhab.org/addons/bindings/zigbee/)