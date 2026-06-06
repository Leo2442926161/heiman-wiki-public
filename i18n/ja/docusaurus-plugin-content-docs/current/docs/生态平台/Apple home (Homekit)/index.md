---
sidebar_position: 6
---
#AppleHome(ホームキット)

Apple HomeKit は、強力なプライバシー保護とローカライズされた制御で知られる Apple のスマート ホーム プラットフォームです。

## 統合方法

### Matter デバイス (推奨)

Heymann Matter over Thread デバイスは Apple Home にネイティブに接続します。

- スレッド ボーダー ルーターとして Apple HomePod (ミニ/第 2 世代)、Apple TV 4K、または HomePod が必要です
- iOS/iPadOS 16.4以降を使用するデバイス
- 「ホーム」アプリを開く→アクセサリを追加→Matter ペアリング コードをスキャンします

### Zigbee デバイス

Homebridge プラグインを使用すると、Heimann Zigbee デバイスを Apple Home にブリッジできます。

「」バッシュ
npm install -g homebridge-zigbee-nt
「」

> **注意**: Matter デバイスは Works with Home Assistant 認定を受けており、Apple Home と適切に連携します。