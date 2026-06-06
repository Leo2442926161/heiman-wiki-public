---
sidebar_position: 6
---
# Apple Home（HomeKit）

Apple HomeKit 是苹果公司的智能家居平台，以其强大的隐私保护和本地化控制著称。

## 集成方式

### Matter 设备（推荐）

海曼 Matter over Thread 设备可原生接入 Apple Home：

- 需要 Apple HomePod（mini/2代）、Apple TV 4K 或 HomePod 作为 Thread 边界路由器
- 使用 iOS/iPadOS 16.4 及以上版本的设备
- 打开"家庭"App → 添加配件 → 扫描 Matter 配对码

### Zigbee 设备

通过 Homebridge 插件，可将海曼 Zigbee 设备桥接到 Apple Home：

```bash
npm install -g homebridge-zigbee-nt
```

> **注意**：Matter 设备已获得 Works with Home Assistant 认证，在 Apple Home 中同样表现出色
