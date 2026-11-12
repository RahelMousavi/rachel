
# Wireshark Display Filters

## What Are Display Filters?

Wireshark Display Filters are used to show only packets that match specific conditions.

They do not delete packets from the capture. They simply hide packets that do not match the filter.

Display filters are useful when analyzing large captures because they help focus on specific hosts, protocols, ports, or packet contents.

**Note:** Display filters are different from capture filters. Capture filters determine which packets are collected, while display filters determine which captured packets are shown.

## IP Address Filters

These filters help identify packets associated with a specific IP address.

### Filter by Source or Destination

```text
ip.addr == 10.0.0.1
```
Displays packets where `10.0.0.1` is either the source or destination.

```text
ip.src == 10.0.0.1
```
Displays packets originating from `10.0.0.1`.

```text
ip.dst == 10.0.0.1
```
Displays packets sent to `10.0.0.1`.

### Excluding an IP Address

```text
ip.src != 10.0.0.1
```
Displays packets whose source IP is not `10.0.0.1`.

## TCP and UDP Port Filters

These filters identify traffic based on port numbers.

### TCP Filters

```text
tcp.port == 80
```
Displays packets where either the source or destination TCP port is 80.

```text
tcp.srcport == 80
```
Displays packets originating from TCP port 80.

```text
tcp.dstport == 80
```
Displays packets sent to TCP port 80.

### UDP Filters

The same filtering logic applies to UDP:

```text
udp.port == 53
```

```text
udp.srcport == 53
```

```text
udp.dstport == 53
```

### Excluding a Port

```text
tcp.srcport != 80
```
Displays TCP packets whose source port is not 80.

## Protocol Filters

You can filter traffic by entering a protocol name.

Examples:

```text
icmp
```

```text
dns
```

```text
http
```

```text
arp
```

These filters display packets recognized as belonging to the specified protocols.

## HTTP Request Filters

Wireshark can filter HTTP requests based on their methods.

### GET Requests

```text
http.request.method == "GET"
```

Displays HTTP GET requests.

### POST Requests

```text
http.request.method == "POST"
```

Displays HTTP POST requests.

**Note:** These filters apply to visible HTTP traffic. HTTPS traffic is encrypted, so HTTP request details generally cannot be inspected without appropriate decryption.

## Logical Operators

Logical operators allow multiple filtering conditions to be combined.

### AND

Both conditions must be true.

```text
ip.dst == 10.0.0.1 and tcp.dstport == 80
```

Displays packets sent to `10.0.0.1` using destination TCP port 80.

### OR

At least one condition must be true.

```text
dns or icmp
```

Displays DNS or ICMP packets.

### NOT

Excludes packets matching a condition.

```text
not arp
```

Displays packets that are not ARP packets.

## MAC Address Filters

Ethernet addresses can also be used for filtering.

```text
eth.addr == 5d:55:b8:88:84:e5
```

Displays packets where the specified MAC address is either the source or destination.

Other useful fields include:

```text
eth.src == 5d:55:b8:88:84:e5
```

```text
eth.dst == 5d:55:b8:88:84:e5
```

## Packet Content Filters

The `contains` operator searches packet fields for a specified sequence of bytes or text.

Example:

```text
tcp contains "windowsupdate.com"
```

This searches TCP packet data for the specified text.

The result depends on whether the content is present and visible in the captured packet.

## ARP Filters

The following filter can help identify ARP duplicate-address detection events:

```text
arp.duplicate-address-detected
```

It can be useful when investigating possible IP address conflicts or suspicious ARP activity.

## Related Links

- [Wireshark Display Filter Reference](https://www.wireshark.org/docs/dfref/)
- [Wireshark Display Filters Documentation](https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html)
- [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/)

## Summary

Wireshark display filters help narrow down captured traffic based on IP addresses, ports, protocols, MAC addresses, and packet contents. Logical operators such as `and`, `or`, and `not` allow multiple conditions to be combined. Understanding these filters makes packet analysis faster and more effective.
