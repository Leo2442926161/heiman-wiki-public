---
sidebar_position: 2
---

# Zigbee2MQTT

Zigbee2MQTT 是一个开源 Zigbee 网关软件，可将 Zigbee 设备桥接到 MQTT 协议，从而实现与 Home Assistant 等平台的集成。

## 兼容性

海曼 Zigbee 传感器在 Zigbee2MQTT 中具有良好的兼容性，大部分设备可被自动识别并支持所有关键功能：

- 烟雾/一氧化碳报警器：报警状态、故障检测、静音控制、电池电量
- 传感器：温度、湿度、光照度、占位检测
- 门磁：开/关状态、 tamper 检测

## 推荐硬件

- CC2652P / CC1352P 系列协调器（如 SLZB-06、TubeZB、ZigStar）
- 海曼 HS6GW 系列 Zigbee 网关也可配合使用

## 配置要点

```yaml
# Zigbee2MQTT 配置示例
serial:
  port: /dev/ttyACM0
advanced:
  channel: 15
  network_key: GENERATE
```

> **参考**：[Zigbee2MQTT 支持设备列表](https://www.zigbee2mqtt.io/supported-devices/)
