
# Stealth Scan (Half-Open Scan)

Stealth Scan, also known as Half-Open Scan or TCP SYN Scan, is a TCP port scanning technique that identifies open ports without completing the TCP Three-Way Handshake.

Instead of establishing a full TCP connection, the scanner sends a SYN packet and analyzes the target's response.

## How Stealth Scan Works

The scanning process depends on the state of the target port.

### 1. When the Port Is Open

1. **SYN:** The scanner sends a TCP SYN packet to the target port.
2. **SYN/ACK:** The target responds with a SYN/ACK packet, indicating that the port is open.
3. **RST:** The scanner sends a TCP RST packet instead of completing the handshake.

The connection is not fully established.

### 2. When the Port Is Closed

1. The scanner sends a TCP SYN packet.
2. The target responds with a TCP RST packet.
3. The scanner identifies the port as closed.

## TCP SYN Scan Diagram

**Open Port:**

```text
Scanner                    Target
   |                          |
   | -------- SYN ----------> |
   |                          |
   | <------ SYN/ACK -------- |
   |                          |
   | -------- RST ----------> |
   |                          |
```

**Closed Port:**

```text
Scanner                    Target
   |                          |
   | -------- SYN ----------> |
   |                          |
   | <-------- RST ---------- |
   |                          |
```

## Nmap Command

Nmap uses the `-sS` option to perform a TCP SYN Scan.

```bash
nmap -sS 10.10.10.10
```

### Command Breakdown

- `nmap`: Runs the Nmap network scanner.
- `-sS`: Performs a TCP SYN Scan.
- `10.10.10.10`: Specifies the target IP address.

To scan a specific port:

```bash
nmap -sS -p 80 10.10.10.10
```

To scan multiple ports:

```bash
nmap -sS -p 22,80,443 10.10.10.10
```

To scan all TCP ports:

```bash
nmap -sS -p- 10.10.10.10
```

## Characteristics of Stealth Scan

- Does not complete the TCP Three-Way Handshake.
- Sends a TCP SYN packet to the target.
- Uses the target's response to determine port states.
- Usually requires raw packet privileges.
- Is generally faster than a TCP Connect Scan.
- May be less visible to some application-level logging systems, but it is not undetectable.
- Firewalls and intrusion detection systems can still detect and block SYN scans.

## Stealth Scan vs. TCP Connect Scan

### Stealth Scan (`-sS`)

- Sends SYN packets.
- Does not complete the TCP handshake.
- Sends RST after receiving SYN/ACK.
- Usually requires raw packet privileges.
- Commonly used for TCP port discovery.

### TCP Connect Scan (`-sT`)

- Establishes a complete TCP connection.
- Completes the Three-Way Handshake.
- Uses the operating system's `connect()` system call.
- Generally easier to detect through connection logging.

## Summary

Stealth Scan, also called Half-Open Scan or TCP SYN Scan, identifies TCP port states without establishing a complete connection.

The main steps for an open port are:

- SYN
- SYN/ACK
- RST

Nmap performs this scan using the `-sS` option.

---

## Related Links

- [Nmap SYN Scan Documentation](https://nmap.org/book/synscan.html) — Official explanation of TCP SYN scanning.
- [Nmap Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html) — Overview of TCP scanning methods, including SYN and Connect scans.
- [Nmap Reference Guide](https://nmap.org/book/man.html) — Complete Nmap command reference.
- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html) — TCP protocol specification and connection behavior.
- [Wireshark](https://www.wireshark.org/) — Tool for capturing and analyzing TCP packets.
- [Wireshark TCP Three-Way Handshake](https://wiki.wireshark.org/TCP_3_way_handshaking) — Explanation of TCP connection establishment.
