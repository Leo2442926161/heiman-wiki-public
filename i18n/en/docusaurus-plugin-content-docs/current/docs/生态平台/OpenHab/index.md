---
sidebar_position: 4
---

# OpenHAB

OpenHAB is an open-source home automation platform focused on vendor-neutral and protocol-agnostic integration.

## Integration Methods

### Zigbee Binding

Heiman Zigbee sensors can be directly connected via OpenHAB's Zigbee binding. Requires a Zigbee coordinator (e.g., Conbee II, SLZB-06).

### Matter Binding

OpenHAB 4.x and above supports the Matter protocol. Heiman Matter devices can be integrated via the Matter binding, requiring a Thread border router.

### MQTT Method

Use with Zigbee2MQTT to receive sensor data via the MQTT binding.

> **Reference**: [OpenHAB Zigbee Binding Documentation](https://www.openhab.org/addons/bindings/zigbee/)
