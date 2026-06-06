---
sidebar_position: 4
---
#오픈HAB

OpenHAB는 공급업체 중립적, 프로토콜 중립적 통합에 초점을 맞춘 오픈 소스 홈 자동화 플랫폼입니다.

## 통합 방법

### 지그비 바인딩

OpenHAB의 Zigbee 바인딩을 사용하면 Heymann Zigbee 센서를 직접 연결할 수 있습니다. Zigbee 코디네이터(예: Conbee II, SLZB-06)와 함께 사용해야 합니다.

### 물질 바인딩

OpenHAB 4.x 이상은 Matter 프로토콜을 지원합니다. Hyman Matter 장치는 스레드 경계 라우터가 필요한 Matter 바인딩을 통해 통합될 수 있습니다.

### MQTT 방식

MQTT 바인딩을 통해 센서 데이터를 수신하기 위해 Zigbee2MQTT와 함께 사용됩니다.

> **참고**: [OpenHAB Zigbee 바인딩 문서](https://www.openhab.org/addons/bindings/zigbee/)