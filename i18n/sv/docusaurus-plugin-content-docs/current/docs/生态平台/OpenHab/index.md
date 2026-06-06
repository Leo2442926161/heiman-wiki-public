---
sidebar_position: 4
---
# OpenHAB

OpenHAB 是一个开源的家居自动化平台，专注于厂商中立和协议无关的集成。

## 集成方式

### Zigbee 绑定

通过 OpenHAB 的 Zigbee 绑定，海曼 Zigbee 传感器可直接接入。需配合 Zigbee 协调器（如 Conbee II、SLZB-06）使用。

### Matter 绑定

OpenHAB 4.x 及以上版本支持 Matter 协议，海曼 Matter 设备可通过 Matter 绑定集成，需 Thread 边界路由器。

### MQTT 方式

配合 Zigbee2MQTT 使用，通过 MQTT 绑定接收传感器数据。

> **参考**：[OpenHAB Zigbee Binding 文档](https://www.openhab.org/addons/bindings/zigbee/)
