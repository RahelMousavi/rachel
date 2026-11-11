
# UDP Scanning

UDP Scanning is a port scanning technique used to identify open UDP ports and discover services running over the UDP protocol.

Unlike TCP, UDP is a connectionless transport-layer protocol. It does not establish a connection before transmitting data and does not use a Three-Way Handshake.

As a result, UDP scanning works differently from TCP scanning.

## How UDP Scanning Works

The scanner sends UDP packets to the target's ports and analyzes the responses.

The result depends on the target port state.

### 1. When the Port Is Open

1. The scanner sends a UDP packet to the target port.
2. The target receives the packet.
3. If the port is open, the service may respond with a UDP packet.
4. The scanner identifies the port as open.

However, many UDP services do not respond to empty or unexpected UDP packets.

Therefore, an open UDP port may not send a response.

### 2. When the Port Is Closed

1. The scanner sends a UDP packet to the target port.
2. The target receives the packet.
3. If the port is closed, the target typically responds with an ICMP Port Unreachable message.
4. The scanner identifies the port as closed.

### 3. When the Port Is Filtered

If a firewall or filtering device blocks the UDP packet, the scanner may receive no response or an ICMP error indicating that communication is administratively prohibited.

Nmap may classify the port as filtered.

## UDP Scanning Diagram

**Open Port:**

```text
Scanner                         Target
   |                               |
   | -------- UDP Packet --------> |
   |                               |
   |       No Response             |
   |                               |
```

The diagram illustrates a common situation in which an open UDP service does not respond to the probe.

**Closed Port:**

```text
Scanner                         Target
   |                               |
   | -------- UDP Packet --------> |
   |                               |
   | <--- ICMP Port Unreachable -- |
   |                               |
```

## Nmap Command

Nmap uses the `-sU` option to perform a UDP Scan.

```bash
nmap -sU 10.10.10.10
```

### Command Breakdown

- `nmap`: Runs the Nmap network scanner.
- `-sU`: Performs a UDP Scan.
- `10.10.10.10`: Specifies the target IP address.

### Scanning Specific UDP Ports

To scan a single UDP port:

```bash
nmap -sU -p 53 10.10.10.10
```

To scan multiple UDP ports:

```bash
nmap -sU -p 53,67,68,161 10.10.10.10
```

To scan all UDP ports:

```bash
nmap -sU -p- 10.10.10.10
```

## Understanding UDP Scan Results

Nmap uses four main states when interpreting UDP scan responses:

### 1. Open

An application is actively listening on the UDP port and has responded to the probe.

### 2. Closed

The target returns an ICMP Port Unreachable error (Type 3, Code 3).

This indicates that no UDP application is listening on the destination port.

### 3. Filtered

Nmap receives an ICMP error indicating that the probe is blocked, such as certain Destination Unreachable messages.

### 4. Open|Filtered

Nmap receives no response, even after retransmitting the probe.

It cannot determine whether:
- The UDP port is open but the application does not respond.
- A firewall is silently dropping the packet.

## Common UDP Services and Ports

Some commonly used UDP services include:

- **DNS:** Port 53
- **DHCP:** Ports 67 and 68
- **SNMP:** Ports 161 and 162
- **TFTP:** Port 69
- **NTP:** Port 123

These services are important targets during network security assessments because UDP services can also expose vulnerabilities.

## Combining TCP and UDP Scans

Nmap allows UDP scanning to be combined with a TCP scanning technique.

For example:

```bash
nmap -sS -sU 10.10.10.10
```

This command performs:
- TCP SYN Scan (`-sS`)
- UDP Scan (`-sU`)

Combining both scans helps identify services using either transport protocol.

## Characteristics of UDP Scanning

- Uses UDP packets instead of TCP packets.
- Does not establish a connection.
- Does not use a Three-Way Handshake.
- Relies on UDP responses and ICMP error messages.
- Can be slower than TCP scanning.
- Often produces `open|filtered` results because open UDP services may not respond to probes.
- Can be affected by firewalls and ICMP rate limiting.

## Why Is UDP Scanning Slower?

UDP scanning is often slower than TCP scanning for several reasons:

1. Open UDP ports may not respond to probes.
2. Nmap may need to retransmit packets before determining a port state.
3. Closed UDP ports usually respond with ICMP errors.
4. Many operating systems limit the rate of ICMP error messages.

As a result, Nmap may need more time to complete a UDP scan.

## Summary

UDP Scanning is used to discover open UDP ports and identify UDP-based services.

Nmap performs this scan using the `-sU` option.

The main UDP port states are:

- **Open:** A UDP response is received.
- **Closed:** An ICMP Port Unreachable message (Type 3, Code 3) is received.
- **Filtered:** An ICMP error indicates that the probe is blocked.
- **Open|Filtered:** No response is received, so Nmap cannot determine the actual state.

**Important:** No response does not necessarily mean that a UDP port is open. It may also indicate that a firewall is filtering the traffic.

---

## Related Links

### UDP Scanning

- [Nmap UDP Scan Documentation](https://nmap.org/book/scan-methods-udp-scan.html) — Official explanation of UDP scanning, port states, and scan optimization.
- [Nmap Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html) — Overview of TCP and UDP scanning methods.
- [Nmap Port Scanning Basics](https://nmap.org/book/man-port-scanning-basics.html) — Explains Nmap port states, including open, closed, filtered, and open|filtered.

### UDP Protocol

- [RFC 768 — User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768.html) — Original UDP protocol specification.
- [IANA Service Name and Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml) — Official registry of registered TCP and UDP ports.

### ICMP and Network Analysis

- [RFC 792 — Internet Control Message Protocol](https://www.rfc-editor.org/rfc/rfc792.html) — ICMP specification, including Destination Unreachable messages.
- [Wireshark](https://www.wireshark.org/) — Network protocol analyzer for inspecting UDP packets and ICMP responses.
- [Nmap Reference Guide](https://nmap.org/book/man.html) — Complete documentation of Nmap commands and options.

