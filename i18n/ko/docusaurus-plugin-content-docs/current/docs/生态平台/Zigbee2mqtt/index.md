---
sidebar_position: 2
---
#Zigbee2MQTT

Zigbee2MQTT는 Zigbee 장치를 MQTT 프로토콜에 연결하여 Home Assistant와 같은 플랫폼과 통합할 수 있게 해주는 오픈 소스 Zigbee 게이트웨이 소프트웨어입니다.

## 호환성

Heiman Zigbee 센서는 Zigbee2MQTT에서 우수한 호환성을 가지며 대부분의 장치는 자동으로 인식되고 모든 주요 기능을 지원할 수 있습니다.

- 연기/일산화탄소 경보: 경보 상태, 오류 감지, 음소거 제어, 배터리 전원
- 센서: 온도, 습도, 조명, 점유 감지
- 도어 센서: 개폐 상태, 훼손 감지

## 권장 하드웨어

- CC2652P / CC1352P 시리즈 코디네이터(예: SLZB-06, TubeZB, ZigStar)
- Hyman HS6GW 시리즈 Zigbee 게이트웨이도 함께 사용할 수 있습니다.

## 구성 포인트

``yaml
# Zigbee2MQTT 구성 예시
일련번호:
  포트: /dev/ttyACM0
고급:
  채널: 15
  network_key: 생성
````

> **참고**: [Zigbee2MQTT 지원 기기 목록](https://www.zigbee2mqtt.io/supported-devices/)