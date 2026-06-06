---
sidebar_position: 2
---
#Zigbee2MQTT

Zigbee2MQTT は、Zigbee デバイスを MQTT プロトコルにブリッジし、ホーム アシスタントなどのプラットフォームとの統合を可能にするオープン ソースの Zigbee ゲートウェイ ソフトウェアです。

## 互換性

Heiman Zigbee センサーは Zigbee2MQTT との互換性が高く、ほとんどのデバイスが自動的に認識され、すべての主要な機能をサポートします。

- 煙/一酸化炭素警報: 警報ステータス、障害検出、ミュート制御、バッテリー電源
- センサー: 温度、湿度、照度、占有検知
- ドアセンサー：開閉状態、不正行為検知

## 推奨ハードウェア

- CC2652P / CC1352P シリーズコーディネーター (SLZB-06、TubeZB、ZigStar など)
- Hyman HS6GW シリーズ Zigbee ゲートウェイも併用可能

## 構成ポイント

```ヤムル
# Zigbee2MQTT 設定例
シリアル:
  ポート: /dev/ttyACM0
高度な:
  チャンネル: 15
  network_key: 生成
「」

> **参考**: [Zigbee2MQTT サポートデバイスリスト](https://www.zigbee2mqtt.io/supported-devices/)