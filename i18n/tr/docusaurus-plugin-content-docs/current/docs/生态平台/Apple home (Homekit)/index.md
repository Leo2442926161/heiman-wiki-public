---
sidebar_position: 6
---
#AppleHome(HomeKit)

Apple HomeKit, güçlü gizlilik koruması ve yerelleştirilmiş kontrolüyle bilinen Apple'ın akıllı ev platformudur.

## Entegrasyon yöntemi

### Madde cihazı (önerilir)

Heymann Matter over Thread cihazları yerel olarak Apple Home'a bağlanır:

- Thread border router olarak Apple HomePod (mini/2. nesil), Apple TV 4K veya HomePod gerekir
- iOS/ıpados 16.4 ve üstünü kullanan cihazlar
- "Ev" Uygulamasını açın → Aksesuar ekleyin → Madde eşleştirme kodunu tarayın

### Zigbee Cihazları

Homebridge eklentisi, Heimann Zigbee cihazlarını Apple Home'a bağlamanıza olanak tanır:

``` bash
npm kurulumu -g homebridge-zigbee-nt
''''

> **NOT**: Matter cihazları Ev Asistanı ile Çalışır sertifikalıdır ve Apple Home ile iyi çalışır