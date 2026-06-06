---
sidebar_position: 1
---
# Home Assistant

海曼科技于 2026 年 2 月正式加入 **Works with Home Assistant** 认证计划，成为该计划的首批中国合作伙伴之一。

## 认证设备

以下海曼设备已通过官方认证，确保与 Home Assistant 的本地化、稳定兼容：

| 设备 | 地区 | 连接方式 |
|------|------|----------|
| 智能烟雾报警器 | 美国 | Matter over Thread |
| 智能烟雾报警器 | 欧盟 / 中国 | Matter over Thread |
| 智能一氧化碳报警器 | 美国 | Matter over Thread |
| 智能一氧化碳报警器 | 欧盟 / 中国 | Matter over Thread |
| 人体红外传感器 M1 系列 | 全球 | Matter / Zigbee |
| 水浸探测器 L1 系列 | 全球 | Matter / Zigbee |
| 温湿度传感器 H1 系列 | 全球 | Matter / Zigbee |

## 集成方式

### 通过 Matter

1. 确保拥有 Matter over Thread 边界路由器（如 Home Assistant Green + Connect ZBT-2、Apple HomePod、Google Nest Hub 等）
2. 在 Home Assistant 中配置 Matter 集成
3. 添加设备即可自动发现

### 通过 Zigbee2MQTT / ZHA

海曼 Zigbee 设备可被 Zigbee2MQTT 和 ZHA 原生支持，无需额外配置。

## 本地化控制

所有认证设备均支持**本地化控制**，无需依赖云服务。即使互联网中断，传感器报警和自动化联动仍可正常运行。

## 社区参与

海曼在 Home Assistant 社区中积极参与讨论，持续根据用户反馈优化产品体验。

> **参考**：[Home Assistant 官方公告 - Heiman joins Works with Home Assistant](https://www.home-assistant.io/blog/2026/02/24/heiman-joins-works-with-home-assistant/)
