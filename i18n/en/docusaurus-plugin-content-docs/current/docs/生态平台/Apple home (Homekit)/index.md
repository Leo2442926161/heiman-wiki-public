---
sidebar_position: 6
---

# Apple Home (HomeKit)

Apple HomeKit is Apple's smart home platform, renowned for its strong privacy protection and local control capabilities.

## Integration Methods

### Matter Devices (Recommended)

Heiman Matter over Thread devices connect natively to Apple Home:

- Requires Apple HomePod (mini/2nd gen), Apple TV 4K, or HomePod as a Thread border router
- Device running iOS/iPadOS 16.4 or later
- Open the "Home" app → Add accessory → Scan the Matter pairing code

### Zigbee Devices

Heiman Zigbee devices can be bridged to Apple Home via a Homebridge plugin:

```bash
npm install -g homebridge-zigbee-nt
```

> **Note**: Matter devices are Works with Home Assistant certified and perform excellently in Apple Home as well
