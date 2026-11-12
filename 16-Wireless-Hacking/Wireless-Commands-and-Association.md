
# Wireless Commands and Association

## Wireless Commands in Windows

Windows provides the `netsh wlan` command-line utility for managing and inspecting wireless network configurations.

The following commands can be used to retrieve wireless network information.

### Show Wireless Interfaces

Displays information about wireless interfaces:

```cmd
netsh wlan show interfaces
```

### Show Wireless Drivers

Displays information about installed wireless drivers:

```cmd
netsh wlan show drivers
```

### Show Available Wireless Networks

Displays available wireless networks:

```cmd
netsh wlan show networks
```

### Show Saved Wireless Profiles

Displays saved wireless network profiles:

```cmd
netsh wlan show profiles
```

### Connect to a Wireless Network

Connects to a wireless network using its profile name:

```cmd
netsh wlan connect name="test"
```

### Show a Saved Profile's Security Key

Displays the details of a saved wireless profile, including its key when available:

```cmd
netsh wlan show profiles name="test" key=clear
```

### Generate a Wireless Network Report

Generates a wireless network report:

```cmd
netsh wlan show wlanreport
```

### Wireless Profiles Location

Windows stores wireless network profiles in the following directory:

```text
C:\ProgramData\Microsoft\Wlansvc\Profiles\Interfaces
```

## Wireless Association Process

Association is the process through which a wireless station connects to an Access Point (AP).

When a mobile station enters the range of an AP, it identifies its identity and requirements to establish a connection.

The association process consists of the following steps:

### 1. Probe Request

The wireless station sends a Probe Request management frame to discover available Access Points.

### 2. Probe Response

All Access Points that receive the Probe Request respond with a Probe Response frame.

### 3. Association Request

The station selects an Access Point and sends an Association Request frame to it.

### 4. Association Response

The Access Point responds with an Association Response frame.

### 5. Disassociation

When a station leaves the wireless network, it sends a Disassociation frame.

## Summary

Windows provides the `netsh wlan` utility to inspect wireless interfaces, drivers, networks, profiles, and connection information.

The wireless association process involves Probe Request, Probe Response, Association Request, and Association Response frames. When a station leaves the network, it sends a Disassociation frame.

## Related Links

- [Microsoft - Netsh Commands for Wireless Local Area Network (WLAN)](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netsh-wlan)
