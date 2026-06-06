---
sidebar_position: 17
---
# Akıllı Ağ Geçidi

Akıllı Ağ Geçidi, çeşitli Zigbee sensörlerini bağlamaktan ve cihazlar arasındaki bağlantı kontrolünü gerçekleştirmekten sorumlu, Haiman akıllı ev sisteminin temel merkezidir.

## Ürün Serisi

| Serisi | İletişim yöntemleri | Özellikler |
|------|----------|------|
| HS1GW Serisi | Zigbee + Wi-Fi / Ethernet | Temel Ağ Geçidi |
| HS3GW Serisi | Zigbee + Wi-Fi / Ethernet | Geliştirilmiş |
| HS5GW Serisi | Zigbee + Wi-Fi / Ethernet | Yüksek Performanslı Ağ Geçidi |
| HS6GW Serisi | Zigbee + Wi-Fi / Ethernet + Konu | En son model, hem Zigbee'yi hem de Matter over Thread'i destekliyor |

## Temel işlevler

- Zigbee Ağ Koordinatörü
- İnternete bağlanmak için Wi-Fi / Ethernet desteği
- Otomatik cihaz keşfi ve eşleştirme
- Yerel sahne bağlantısı (bazı modellerde)
- Uzaktan erişim (Heiman Bulut Platformu aracılığıyla)
- 128'e kadar alt cihazı destekler (modele bağlı olarak)

## Uygulanabilir senaryolar

- Heiman'ın tüm kuruma yönelik istihbaratının temel bağlantı noktası
- Uzaktan izlemeyi gerçekleştirmek için Haiman APP ile işbirliği yapın
- Küçük ve orta ölçekli ticari projelerin yerel merkezi yönetimi

## Diğer ağ geçitlerinden farklar

Haiman Geçidi resmi ekosistemin girişidir. Üçüncü taraf bir platform kullanmak isteyen kullanıcıların Zigbee2MQTT/ZHA ile evrensel Zigbee koordinatörünü kullanmaları önerilir.