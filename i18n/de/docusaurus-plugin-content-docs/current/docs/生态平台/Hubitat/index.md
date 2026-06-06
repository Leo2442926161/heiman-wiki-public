---
sidebar_position: 10
---
#hubitat

Hubitat ist ein Smart-Home-Hub, der sich auf die lokale Steuerung konzentriert und Zigbee- und Z-Wave-Geräte unterstützt, wobei die gesamte Automatisierung lokal erfolgt, ohne dass Cloud-Dienste erforderlich sind.

## Integrationsmethode

### Zigbee-Geräte

Hyman Zigbee-Sensoren koppeln sich direkt mit Hubitat Elevation-Hubs:

1. Rufen Sie in Hubitat den Zigbee-Pairing-Modus auf
2. Versetzen Sie den Heiman-Sensor in den Kopplungsmodus
3. Das Gerät wird automatisch erkannt und hinzugefügt

### Z-Wave-Geräte

Hyman Z-Wave-Geräte unterstützen auch die direkte Kopplung mit Hubitat und nutzen dabei den integrierten Z-Wave-Chip von Hubitat.

### Benutzerdefinierter Treiber

Für einige Heiman-Geräte sind möglicherweise benutzerdefinierte Treiber erforderlich, und Community-Benutzer haben kompatible Treiber für gängige Sensoren geschrieben.

## Vorteile

- **100 % Lokalisierung**: Die gesamte Automatisierungslogik wird lokal in Hubitat ausgeführt und ist nicht auf die Cloud angewiesen
- **Geringe Latenz**: Lokales Zigbee/Z-Wave Mesh-Netzwerk, schnelle Reaktion
- **Reichhaltige Community**: Die Hubitat-Community verfügt über eine große Anzahl von Heiman-Benutzern, die ihre Konfiguration teilen

> **Referenz**: [Hubitat Community – Diskussion über Heiman-Ausrüstung](https://community.hubitat.com/)