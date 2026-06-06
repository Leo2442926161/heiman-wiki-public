---
sidebar_position: 2
---
#Zigbee2MQTT

Zigbee2MQTT, Zigbee cihazlarını MQTT protokolüne bağlayan ve Home Assistant gibi platformlarla entegrasyonu sağlayan açık kaynaklı bir Zigbee ağ geçidi yazılımıdır.

## Uyumluluk

Heiman Zigbee sensörleri Zigbee2MQTT ile iyi bir uyumluluğa sahiptir ve çoğu cihaz otomatik olarak tanınabilir ve tüm temel işlevleri destekleyebilir:

- Duman/karbon monoksit alarmı: alarm durumu, arıza tespiti, sessize alma kontrolü, pil gücü
- Sensörler: sıcaklık, nem, aydınlatma, doluluk algılama
- Kapı sensörü: açık/kapalı durumu, kurcalama algılama

## Önerilen donanım

- CC2652P / CC1352P serisi koordinatörler (SLZB-06, TubeZB, ZigStar gibi)
- Hyman HS6GW serisi Zigbee ağ geçitleri de birlikte kullanılabilir

## Yapılandırma noktaları

```yaml
# Zigbee2MQTT yapılandırma örneği
seri:
  bağlantı noktası: /dev/ttyACM0
gelişmiş:
  kanal: 15
  ağ_anahtarı: OLUŞTUR
''''

> **Referans**: [Zigbee2MQTT desteklenen cihaz listesi](https://www.zigbee2mqtt.io/supported-devices/)