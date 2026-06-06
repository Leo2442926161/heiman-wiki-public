---
sidebar_position: 6
---
#애플홈(홈킷)

Apple HomeKit은 강력한 개인 정보 보호 및 현지화된 제어 기능으로 유명한 Apple의 스마트 홈 플랫폼입니다.

## 통합 방법

### Matter 장치(권장)

Thread 장치를 통한 Heymann Matter는 기본적으로 Apple Home에 연결됩니다.

- 스레드 보더 라우터로 Apple HomePod(미니/2세대), Apple TV 4K 또는 HomePod 필요
- iOS/iPadOS 16.4 이상을 사용하는 기기
- "홈" 앱 열기 → 액세서리 추가 → Matter 페어링 코드 스캔

### 지그비 장치

Homebridge 플러그인을 사용하면 Heimann Zigbee 장치를 Apple Home에 브리지할 수 있습니다.

``배쉬
npm 설치 -g homebridge-zigbee-nt
````

> **참고**: Matter 장치는 Works with Home Assistant 인증을 받았으며 Apple Home과 잘 작동합니다.