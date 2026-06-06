---
sidebar_position: 10
---
# Hubitat

Hubitat 是一个专注于本地化控制的智能家居中枢，支持 Zigbee 和 Z-Wave 设备，所有自动化均在本地执行，无需云服务。

## 集成方式

### Zigbee 设备

海曼 Zigbee 传感器可直接与 Hubitat Elevation 中枢配对：

1. 在 Hubitat 中进入 Zigbee 配对模式
2. 将海曼传感器进入配对模式
3. 设备将被自动发现并添加

### Z-Wave 设备

海曼 Z-Wave 设备同样支持与 Hubitat 直接配对，利用 Hubitat 的内置 Z-Wave 芯片。

### 自定义驱动

部分海曼设备可能需要自定义 Driver，社区用户已为常见传感器编写了兼容驱动。

## 优势

- **100% 本地化**：所有自动化逻辑在 Hubitat 本地执行，不依赖云端
- **低延迟**：本地 Zigbee/Z-Wave Mesh 网络，响应快速
- **丰富社区**：Hubitat Community 有大量海曼用户的配置分享

> **参考**：[Hubitat Community - Heiman 设备讨论](https://community.hubitat.com/)
