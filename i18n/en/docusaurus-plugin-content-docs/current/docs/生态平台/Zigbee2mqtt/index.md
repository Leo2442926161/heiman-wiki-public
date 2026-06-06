---
sidebar_position: 2
---

# Zigbee2MQTT

Zigbee2MQTT is an open-source Zigbee gateway software that bridges Zigbee devices to the MQTT protocol, enabling integration with platforms such as Home Assistant.

## Compatibility

Heiman Zigbee sensors have excellent compatibility with Zigbee2MQTT. Most devices are automatically recognized and support all key functions:

- Smoke/CO alarms: alarm status, fault detection, silence control, battery level
- Sensors: temperature, humidity, illuminance, occupancy detection
- Door/window sensors: open/close status, tamper detection

## Recommended Hardware

- CC2652P / CC1352P series coordinators (e.g., SLZB-06, TubeZB, ZigStar)
- Heiman HS6GW series Zigbee gateways can also be used

## Configuration Notes

```yaml
# Zigbee2MQTT configuration example
serial:
  port: /dev/ttyACM0
advanced:
  channel: 15
  network_key: GENERATE
```

> **Reference**: [Zigbee2MQTT Supported Devices](https://www.zigbee2mqtt.io/supported-devices/)
