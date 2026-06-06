---
sidebar_position: 1
---

# Home Assistant

Heiman Technology officially joined the **Works with Home Assistant** certification program in February 2026, becoming one of the first Chinese partners in the program.

## Certified Devices

The following Heiman devices are officially certified, ensuring local, stable compatibility with Home Assistant:

| Device | Region | Connectivity |
|------|------|----------|
| Smart Smoke Alarm | US | Matter over Thread |
| Smart Smoke Alarm | EU / China | Matter over Thread |
| Smart CO Alarm | US | Matter over Thread |
| Smart CO Alarm | EU / China | Matter over Thread |
| PIR Motion Sensor M1 Series | Global | Matter / Zigbee |
| Water Leak Detector L1 Series | Global | Matter / Zigbee |
| Temperature & Humidity Sensor H1 Series | Global | Matter / Zigbee |

## Integration Methods

### Via Matter

1. Ensure you have a Matter over Thread border router (e.g., Home Assistant Green + Connect ZBT-2, Apple HomePod, Google Nest Hub, etc.)
2. Configure the Matter integration in Home Assistant
3. Devices will be automatically discovered

### Via Zigbee2MQTT / ZHA

Heiman Zigbee devices are natively supported by Zigbee2MQTT and ZHA with no additional configuration needed.

## Local Control

All certified devices support **local control** without relying on cloud services. Sensor alarms and automation scenes will continue to function even if the internet goes down.

## Community Involvement

Heiman actively participates in discussions within the Home Assistant community and continuously improves product experience based on user feedback.

> **Reference**: [Home Assistant Official Blog - Heiman joins Works with Home Assistant](https://www.home-assistant.io/blog/2026/02/24/heiman-joins-works-with-home-assistant/)
