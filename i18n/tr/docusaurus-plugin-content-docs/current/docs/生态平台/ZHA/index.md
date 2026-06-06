---
sidebar_position: 11
---
#ZHA (Zigbee Ev Otomasyonu)

ZHA, Zigbee cihazlarını ek yazılım olmadan doğrudan yönetebilen, Home Assistant'ın yerleşik Zigbee entegrasyon çözümüdür.

## Uyumluluk

Hyman Zigbee sensörleri ZHA ve destek konusunda iyi bir uyumluluğa sahiptir:

- **Duman/CO Alarmı**: Alarm durumu, arıza tespiti, pil seviyesi, sessize alma
- **Kapı sensörü**: açık/kapalı, dış müdahale
- **İnsan kızılötesi**: hareket algılama, aydınlatma
- **Sıcaklık ve Nem**: sıcaklık, nem
- **Su baskını**: Su kaçağı alarmı
- **Akıllı soket**: anahtar, güç tüketimi ölçümü

## Donanım gereksinimleri

- Zigbee koordinatörü: HUSBZB-1, Conbee II, SkyConnect, SLZB-06 vb.
- Ev Asistanına USB veya ağ üzerinden bağlanın

## Yapılandırma

ZHA'nın yapılandırılması kolaydır. Cihazı otomatik olarak taramak ve keşfetmek için seri bağlantı noktasını ve alanı seçmeniz yeterlidir. Yapılandırma dosyalarını manuel olarak yazmaya gerek yoktur.

> **Referans**: [Ev Asistanı ZHA Belgesi](https://www.home-assistant.io/integrations/zha/)