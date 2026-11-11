
# FIN Scan

FIN Scan is a TCP port scanning technique that sends TCP packets with only the FIN flag enabled.

It is used to identify open and closed ports without establishing a complete TCP connection.

## How FIN Scan Works

The scanner sends a TCP packet with the FIN flag set and analyzes the target's response.

### 1. When the Port Is Open

1. The scanner sends a TCP FIN packet to the target.
2. The target receives the packet.
3. If the port is open, the target typically does not respond.
4. Nmap reports the port as `open|filtered`.

### 2. When the Port Is Closed

1. The scanner sends a TCP FIN packet.
2. The target receives the packet.
3. If the port is closed, the target typically responds with a TCP RST packet.
4. Nmap identifies the port as closed.

## FIN Scan Diagram

**Open Port:**

```text
Scanner                    Target
   |                          |
   | -------- FIN ----------> |
   |                          |
   |      No Response         |
   |                          |
```

**Closed Port:**

```text
Scanner                    Target
   |                          |
   | -------- FIN ----------> |
   |                          |
   | <-------- RST ---------- |
   |                          |
```

## Nmap Command

Nmap uses the `-sF` option to perform a FIN Scan.

```bash
nmap -sF 10.10.10.10
```

### Command Breakdown

- `nmap`: Runs the Nmap network scanner.
- `-sF`: Performs a TCP FIN Scan.
- `10.10.10.10`: Specifies the target IP address.

To scan a specific port:

```bash
nmap -sF -p 80 10.10.10.10
```

To scan multiple ports:

```bash
nmap -sF -p 22,80,443 10.10.10.10
```

To scan all TCP ports:

```bash
nmap -sF -p- 10.10.10.10
```

## Characteristics of FIN Scan

- Uses only the FIN TCP flag.
- Does not establish a complete TCP connection.
- Typically receives no response from open ports.
- Typically receives RST responses from closed ports.
- Can be affected by firewalls and operating system behavior.
- May be detected by network security monitoring systems.

## Limitations

FIN Scan relies on expected TCP behavior.

Some operating systems, particularly Windows systems, do not respond to FIN probes in the expected way. This can make the results unreliable.

Firewalls may also silently drop FIN packets.

Therefore, no response does not necessarily mean that a port is open.

## Summary

FIN Scan is a TCP port scanning technique that sends packets with only the FIN flag enabled.

Nmap performs this scan using the `-sF` option.

Typical results:

- **Open|Filtered:** No response received.
- **Closed:** RST response received.

---

# NULL Scan

NULL Scan is a TCP port scanning technique that sends TCP packets without setting any TCP flags.

In other words, all TCP control flags are set to zero.

It is used to identify port states by analyzing the target's response.

## How NULL Scan Works

The scanner sends a TCP packet with no flags enabled and examines the response.

### 1. When the Port Is Open

1. The scanner sends a TCP packet with no flags set.
2. The target receives the packet.
3. If the port is open, the target typically does not respond.
4. Nmap reports the port as `open|filtered`.

### 2. When the Port Is Closed

1. The scanner sends a TCP packet without any flags.
2. The target receives the packet.
3. If the port is closed, the target typically responds with a TCP RST packet.
4. Nmap identifies the port as closed.

## NULL Scan Diagram

**Open Port:**

```text
Scanner                    Target
   |                          |
   | ----- NULL Packet -----> |
   |                          |
   |      No Response         |
   |                          |
```

**Closed Port:**

```text
Scanner                    Target
   |                          |
   | ----- NULL Packet -----> |
   |                          |
   | <-------- RST ---------- |
   |                          |
```

## Nmap Command

Nmap uses the `-sN` option to perform a NULL Scan.

```bash
nmap -sN 10.10.10.10
```

### Command Breakdown

- `nmap`: Runs the Nmap network scanner.
- `-sN`: Performs a TCP NULL Scan.
- `10.10.10.10`: Specifies the target IP address.

To scan a specific port:

```bash
nmap -sN -p 80 10.10.10.10
```

To scan multiple ports:

```bash
nmap -sN -p 22,80,443 10.10.10.10
```

To scan all TCP ports:

```bash
nmap -sN -p- 10.10.10.10
```

## Characteristics of NULL Scan

- Sends TCP packets without any flags enabled.
- Does not establish a TCP connection.
- Typically receives no response from open ports.
- Typically receives RST responses from closed ports.
- Can be affected by firewall rules.
- May produce unreliable results on some operating systems.

## Limitations

Like FIN and Xmas scans, NULL Scan relies on specific TCP behavior.

Some operating systems, particularly Windows, do not respond according to the expected behavior of these scans.

Firewalls can also drop NULL packets, making it difficult to determine the actual port state.

No response does not necessarily indicate an open port.

## Summary

NULL Scan is a TCP scanning technique that sends packets without setting any TCP flags.

Nmap performs this scan using the `-sN` option.

Typical results:

- **Open|Filtered:** No response received.
- **Closed:** RST response received.

---

# FIN Scan vs. NULL Scan

Both techniques belong to the family of TCP flag-based scans, but they differ in the packets they send.

## FIN Scan

- Uses the FIN flag.
- Nmap option: `-sF`.
- Sends a TCP packet with FIN enabled.

## NULL Scan

- Does not enable any TCP flags.
- Nmap option: `-sN`.
- Sends a TCP packet with all flags disabled.

## Comparison Summary

| Feature | FIN Scan | NULL Scan |
|---|---|---|
| TCP flags | FIN | None |
| Nmap option | `-sF` | `-sN` |
| Open port response | Usually none | Usually none |
| Closed port response | RST | RST |
| TCP connection | Not established | Not established |

---

## Related Links

### FIN Scan

- [Nmap FIN, NULL, and Xmas Scan Documentation](https://nmap.org/book/scan-methods-null-fin-xmas-scan.html) — Official explanation of FIN scanning.
- [Nmap Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html) — Overview of Nmap scanning methods.

### NULL Scan

- [Nmap FIN, NULL, and Xmas Scan Documentation](https://nmap.org/book/scan-methods-null-fin-xmas-scan.html) — Official explanation of NULL scanning.
- [Nmap Reference Guide](https://nmap.org/book/man.html) — Complete Nmap command reference.

### General TCP Scanning Resources

- [Nmap Port States](https://nmap.org/book/man-port-scanning-basics.html) — Explains open, closed, filtered, and open|filtered states.
- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html) — TCP specification, including TCP flags and packet handling.
- [Wireshark](https://www.wireshark.org/) — Network protocol analyzer for inspecting FIN and other TCP flags.
- [Wireshark TCP Analysis](https://wiki.wireshark.org/TCP) — Information about TCP packet analysis.
