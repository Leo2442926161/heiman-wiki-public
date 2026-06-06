---
sidebar_position: 11
---

# ZHA (Zigbee Home Automation)

ZHA is Home Assistant's built-in Zigbee integration solution, allowing direct management of Zigbee devices without additional software.

## Compatibility

Heiman Zigbee sensors have excellent compatibility with ZHA, supporting:

- **Smoke/CO alarms**: alarm status, fault detection, battery level, silence
- **Door/window sensors**: open/close, tamper
- **PIR motion sensors**: motion detection, illuminance
- **Temperature/humidity**: temperature, humidity
- **Water leak**: water leak alarm
- **Smart plugs**: on/off, power metering

## Hardware Requirements

- Zigbee coordinator: HUSBZB-1, Conbee II, SkyConnect, SLZB-06, etc.
- Connected to Home Assistant via USB or network

## Configuration

ZHA is simple to configure — select the serial port and region, and devices are automatically discovered during scanning. No manual configuration file editing required.

> **Reference**: [Home Assistant ZHA Documentation](https://www.home-assistant.io/integrations/zha/)
