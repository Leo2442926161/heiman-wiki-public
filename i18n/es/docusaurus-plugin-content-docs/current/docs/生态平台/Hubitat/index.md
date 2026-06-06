---
sidebar_position: 10
---
#hubitat

Hubitat es un centro de hogar inteligente centrado en el control localizado, que admite dispositivos Zigbee y Z-Wave, y toda la automatización se realiza localmente sin necesidad de servicios en la nube.

## Método de integración

### Dispositivos Zigbee

Los sensores Hyman Zigbee se emparejan directamente con los concentradores Hubitat Elevation:

1. Ingrese al modo de emparejamiento Zigbee en Hubitat
2. Pon el sensor Heiman en modo de emparejamiento.
3. El dispositivo será descubierto y agregado automáticamente.

### Dispositivos Z-Wave

Los dispositivos Hyman Z-Wave también admiten el emparejamiento directo con Hubitat, aprovechando el chip Z-Wave integrado de Hubitat.

### Controlador personalizado

Algunos dispositivos Heiman pueden requerir controladores personalizados y los usuarios de la comunidad han escrito controladores compatibles para sensores comunes.

## Ventajas

- **100% localización**: toda la lógica de automatización se ejecuta localmente en Hubitat y no depende de la nube.
- **Baja latencia**: red local Zigbee/Z-Wave Mesh, respuesta rápida
- **Comunidad rica**: la comunidad Hubitat comparte la configuración de una gran cantidad de usuarios de Heiman.

> **Referencia**: [Comunidad Hubitat - Discusión sobre equipos Heiman](https://community.hubitat.com/)