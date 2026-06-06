---
sidebar_position: 11
---

# ZHA（Zigbee Home Automation）

ZHA 是 Home Assistant 内置的 Zigbee 集成方案，无需额外软件即可直接管理 Zigbee 设备。

## 兼容性

海曼 Zigbee 传感器在 ZHA 中拥有良好的兼容性，支持：

- **烟雾/CO 报警器**：报警状态、故障检测、电池电量、静音
- **门磁传感器**：开/关、 tamper
- **人体红外**：移动检测、光照度
- **温湿度**：温度、湿度
- **水浸**：漏水报警
- **智能插座**：开关、功耗计量

## 硬件要求

- Zigbee 协调器：HUSBZB-1、Conbee II、SkyConnect、SLZB-06 等
- 通过 USB 或网络连接到 Home Assistant

## 配置

ZHA 配置简单，选择串口和区域即可自动扫描发现设备。无需手动编写配置文件。

> **参考**：[Home Assistant ZHA 文档](https://www.home-assistant.io/integrations/zha/)
