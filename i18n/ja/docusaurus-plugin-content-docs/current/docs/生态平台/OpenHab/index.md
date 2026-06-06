---
sidebar_position: 4
---
#OpenHAB

OpenHAB は、ベンダー中立およびプロトコル中立の統合に重点を置いたオープンソースのホーム オートメーション プラットフォームです。

## 統合方法

### Zigbee バインディング

OpenHAB の Zigbee バインディングを使用すると、Heymann Zigbee センサーを直接接続できます。 Zigbee コーディネーター (Conbee II、SLZB-06 など) と併用する必要があります。

### 物質の結合

OpenHAB 4.x 以降は Matter プロトコルをサポートしています。 Hyman Matter デバイスは Matter バインディングを通じて統合できますが、これにはスレッド ボーダー ルーターが必要です。

### MQTT方式

MQTT バインディング経由でセンサー データを受信するために Zigbee2MQTT とともに使用されます。

> **参考**: [OpenHAB Zigbee バインディング ドキュメント](https://www.openhab.org/addons/bindings/zigbee/)