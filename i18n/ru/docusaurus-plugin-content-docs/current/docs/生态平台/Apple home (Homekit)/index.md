---
sidebar_position: 6
---
#AppleHome(HomeKit)

Apple HomeKit — это платформа умного дома от Apple, известная своей надежной защитой конфиденциальности и локализованным контролем.

## Метод интеграции

### Устройство Материи (рекомендуется)

Устройства Heymann Matter over Thread напрямую подключаются к Apple Home:

- Требуется Apple HomePod (мини/2-го поколения), Apple TV 4K или HomePod в качестве пограничного маршрутизатора Thread.
- Устройства с iOS/iPadOS 16.4 и более поздних версий.
- Откройте приложение «Домой» → Добавить аксессуары → Отсканируйте код сопряжения Matter.

### Устройства Zigbee

Плагин Homebridge позволяет подключать устройства Heimann Zigbee к Apple Home:

``` баш
npm install -g homebridge-zigbee-nt
```

> **ПРИМЕЧАНИЕ**. Устройства Matter сертифицированы для работы с Home Assistant и хорошо работают с Apple Home.