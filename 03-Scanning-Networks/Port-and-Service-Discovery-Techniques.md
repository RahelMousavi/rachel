
# Port and Service Discovery Techniques

Port and Service Discovery is the process of identifying open ports and discovering services running on target systems.

Different scanning techniques use different protocols and packet types to examine the target network.

## Overview of Scanning Techniques

The diagram classifies scanning techniques into several main categories:

### 1. TCP Scanning

TCP scanning uses TCP packets to identify the state of ports on a target system.

It includes three main groups:

#### Open TCP Scanning Methods

- **TCP Connect / Full Open Scan:** Establishes a complete TCP connection with the target port to determine whether it is open.

#### Stealth TCP Scanning Methods

These techniques attempt to gather information without completing a normal TCP connection.

- **Half-Open Scan:** Sends a SYN packet and analyzes the response without completing the TCP three-way handshake.
- **Inverse TCP Flag Scan:** Sends TCP packets with unusual flag combinations to analyze how the target responds.
- **ACK Flag Probe Scan:** Sends TCP ACK packets to examine how packets are handled by the target or its firewall.
- **IDLE / IPID Header Scan:** Uses a third-party host (zombie) and IP ID values to infer the state of ports on another target.

#### Third-Party and Spoofed TCP Scanning Methods

These methods involve using spoofed source addresses or third-party systems during scanning.

Some related techniques shown in the diagram include:

- **Xmas Scan:** Sends TCP packets with FIN, PSH, and URG flags set.
- **FIN Scan:** Sends TCP packets with the FIN flag set.
- **NULL Scan:** Sends TCP packets without any flags set.
- **Maimon Scan:** Sends TCP packets with FIN and ACK flags set.
- **TTL-Based Scan:** Uses TTL behavior to analyze network responses.
- **Window Scan:** Examines the TCP window field in RST responses to infer port states on certain systems.

### 2. UDP Scanning

UDP scanning is used to discover open UDP ports and identify services that communicate using UDP.

Unlike TCP, UDP is connectionless and does not use a three-way handshake.

Nmap option:

```bash
nmap -sU 10.10.10.10
```

### 3. SCTP Scanning

SCTP (Stream Control Transmission Protocol) is a transport-layer protocol that provides reliable communication between endpoints.

The diagram identifies two SCTP scanning methods:

- **SCTP INIT Scanning:** Sends SCTP INIT packets to identify the state of SCTP ports.
- **SCTP COOKIE ECHO Scanning:** Uses SCTP COOKIE ECHO packets to probe the target.

### 4. SSDP Scanning

SSDP (Simple Service Discovery Protocol) is used by devices to advertise and discover network services.

It is commonly associated with UPnP (Universal Plug and Play).

SSDP typically uses UDP and multicast communication for device and service discovery.

### 5. IPv6 Scanning

IPv6 scanning involves discovering hosts, open ports, and services in networks that use IPv6 addresses.

It requires scanning techniques and tools that support IPv6.

Nmap option:

```bash
nmap -6 -sT 2001:db8::10
```

The address above is an example IPv6 documentation address.

---

## Summary

Port and Service Discovery techniques can be classified according to the protocols and packet types they use.

The main categories shown in this diagram are:

- TCP Scanning
- UDP Scanning
- SCTP Scanning
- SSDP Scanning
- IPv6 Scanning

TCP scanning includes several methods, such as TCP Connect, Half-Open, FIN, NULL, Xmas, ACK, and IDLE scans.

These techniques are used to examine port states, identify services, and understand how target systems and network security devices respond to different packets.

## Related Links

- [Nmap Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html) — Official explanation of TCP, UDP, SCTP, and other Nmap scanning techniques.
- [Nmap Reference Guide](https://nmap.org/book/man.html) — Complete reference for Nmap options and commands.
- [Nmap TCP Scan Techniques](https://nmap.org/book/scan-methods.html) — Detailed explanation of TCP scanning methods.
- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html) — TCP protocol specification.
- [RFC 768 — User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768) — UDP protocol specification.
- [RFC 9260 — Stream Control Transmission Protocol](https://www.rfc-editor.org/rfc/rfc9260.html) — SCTP protocol specification.
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — HTTP semantics and related protocol concepts.
- [UPnP Device Architecture](https://openconnectivity.org/developer/specifications/upnp-resources/upnp/) — Resources about UPnP and service discovery.
- [RFC 8200 — Internet Protocol, Version 6 (IPv6)](https://www.rfc-editor.org/rfc/rfc8200.html) — IPv6 protocol specification.
