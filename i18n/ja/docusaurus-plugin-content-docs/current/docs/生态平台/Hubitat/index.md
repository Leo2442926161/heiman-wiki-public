---
sidebar_position: 10
---
#フビタット

Hubitat は、ローカル制御に重点を置いたスマート ホーム ハブで、Zigbee および Z-Wave デバイスをサポートし、クラウド サービスを必要とせずにすべての自動化がローカルで実行されます。

## 統合方法

### Zigbee デバイス

Hyman Zigbee センサーは、Hubitat Elevation ハブと直接ペアリングします。

1.Hubitat で Zigbee ペアリング モードに入る
2. Heiman センサーをペアリング モードにします。
3. デバイスは自動的に検出され、追加されます。

### Z-Wave デバイス

Hyman Z-Wave デバイスは、Hubitat の内蔵 Z-Wave チップを活用して、Hubitat との直接ペアリングもサポートしています。

### カスタムドライバー

一部の Heiman デバイスにはカスタム ドライバーが必要な場合があり、コミュニティ ユーザーが一般的なセンサー用の互換性のあるドライバーを作成しています。

## 利点

- **100% ローカライゼーション**: すべての自動化ロジックは Hubitat でローカルに実行され、クラウドに依存しません。
- **低遅延**: ローカル Zigbee/Z-Wave メッシュ ネットワーク、高速応答
- **豊富なコミュニティ**: Hubitat コミュニティには、多数の Heiman ユーザーの構成共有があります。

> **参考**: [Hubitat コミュニティ - Heiman Equipment Discussion](https://community.hubitat.com/)