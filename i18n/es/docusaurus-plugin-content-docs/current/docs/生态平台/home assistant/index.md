---
sidebar_position: 1
---
#AsistenteDeCasa

Haiman Technology se unió oficialmente al programa de certificación **Works with Home Assistant** en febrero de 2026 y se convirtió en uno de los primeros socios chinos del programa.

## Dispositivo de autenticación

Los siguientes dispositivos Heiman han sido certificados oficialmente para garantizar la localización y la compatibilidad estable con Home Assistant:

| Equipos | Región | Método de conexión |
|------|------|----------|
| Alarma de humo inteligente | Estados Unidos | Asunto sobre Hilo |
| Alarma de humo inteligente | UE / China | Asunto sobre Hilo |
| Alarma inteligente de monóxido de carbono | Estados Unidos | Asunto sobre Hilo |
| Alarma inteligente de monóxido de carbono | UE / China | Asunto sobre Hilo |
| Sensor infrarrojo del cuerpo humano Serie M1 | Mundial | Materia / Zigbee |
| Detector de inmersión en agua Serie L1 | Mundial | Materia / Zigbee |
| Sensor de temperatura y humedad Serie H1 | Mundial | Materia / Zigbee |

## Método de integración

### por materia

1. Asegúrese de tener un enrutador de borde Matter over Thread (como Home Assistant Green + Connect ZBT-2, Apple HomePod, Google Nest Hub, etc.)
2. Configurar la integración de Matter en Home Assistant
3. Añade el dispositivo para descubrirlo automáticamente.

### vía Zigbee2MQTT/ZHA

Los dispositivos Hyman Zigbee son compatibles de forma nativa con Zigbee2MQTT y ZHA sin necesidad de configuración adicional.

## Control de localización

Todos los dispositivos certificados admiten **control localizado** sin depender de servicios en la nube. Incluso si Internet no funciona, las alarmas de sensores y los enlaces de automatización aún pueden funcionar con normalidad.

## Participación comunitaria

Heyman participa activamente en debates en la comunidad de Home Assistant y continúa optimizando la experiencia del producto en función de los comentarios de los usuarios.

> **Referencia**: [Anuncio oficial de Home Assistant: Heiman se une a Works with Home Assistant](https://www.home-assistant.io/blog/2026/02/24/heiman-joins-works-with-home-assistant/)