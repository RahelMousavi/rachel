
# Creating Custom Packets in Nmap

Nmap provides several options for customizing the data carried inside network packets.

These options allow users to modify packet payloads by adding random data, custom text, or hexadecimal data.

Custom packet data can be useful when testing how network devices, firewalls, and security systems handle different packet contents.

## 1. The `--data-length` Option

The `--data-length` option adds a specified number of random bytes to packets sent during a scan.

### Syntax

```bash
nmap --data-length <number> <target>
```

### Example

```bash
nmap --data-length 10 10.10.10.10
```

In this example:

- `--data-length`: Specifies the amount of additional data.
- `10`: Adds 10 random bytes to the packets.
- `10.10.10.10`: Specifies the target IP address.

This option changes the size of the packet by adding extra payload data.

## 2. The `--data-string` Option

The `--data-string` option allows users to append a custom ASCII string to packets.

### Syntax

```bash
nmap --data-string "<string>" <target>
```

### Example

```bash
nmap --data-string "CEH Network Scan" 10.10.10.10
```

In this example, Nmap adds the specified text to the packet payload.

This can be useful for testing how network devices and applications handle packets containing specific text.

## 3. The `--data` Option

Nmap also provides the `--data` option to append custom hexadecimal data to packets.

### Syntax

```bash
nmap --data <hex-string> <target>
```

### Example

```bash
nmap --data "434548" 10.10.10.10
```

The hexadecimal value `434548` represents the ASCII characters `CEH`.

This option provides more control over the exact bytes included in the packet payload.

## 4. Important Considerations

- These options modify packet payload data; they do not directly change TCP flags or source IP addresses.
- Additional payload data increases packet size.
- Larger packets may encounter MTU limitations or fragmentation.
- Custom payloads may affect how firewalls and IDS/IPS systems inspect network traffic.
- The exact effect depends on the scan type, protocol, and target system.

## 5. Comparison of Nmap Data Options

- `--data-length <number>`: Adds a specified number of random bytes.
- `--data-string "<text>"`: Adds custom ASCII text.
- `--data <hex-string>`: Adds custom hexadecimal data.

## Summary

Nmap supports custom packet payloads through three main options:

```bash
# Add 10 random bytes
nmap --data-length 10 10.10.10.10

# Add custom ASCII text
nmap --data-string "CEH Network Scan" 10.10.10.10

# Add custom hexadecimal data
nmap --data "434548" 10.10.10.10
```

**Key Concept:** These options customize the payload of packets sent by Nmap, allowing security professionals to test how network devices handle different packet contents.

---

## Related Links

- [Nmap — Firewall and IDS Evasion](https://nmap.org/book/man-bypass-firewalls-ids.html) — Official documentation of packet customization and evasion options.
- [Nmap Reference Guide](https://nmap.org/book/man.html) — Complete documentation of Nmap command-line options.
- [Nmap Options Summary](https://nmap.org/book/man-briefoptions.html) — Quick reference for Nmap switches.
- [Nmap Data Length Option](https://nmap.org/book/man-bypass-firewalls-ids.html) — Documentation covering `--data-length`, `--data-string`, and `--data`.
- [RFC 791 — Internet Protocol](https://www.rfc-editor.org/rfc/rfc791.html) — IPv4 packet structure and fragmentation.
- [Wireshark](https://www.wireshark.org/) — Capture and inspect packet payloads and headers.
