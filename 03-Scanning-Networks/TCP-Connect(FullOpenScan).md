
# TCP Connect / Full Open Scan

TCP Connect Scan, also known as Full Open Scan, is a TCP port scanning technique that attempts to establish a complete TCP connection with the target port.

Unlike a Half-Open Scan, this method completes the TCP Three-Way Handshake.

## How TCP Connect Scan Works

The scanning process depends on whether the target port is open or closed.

### 1. When the Port Is Open

If the target port is open, the following steps occur:

1. **SYN:** The scanner sends a TCP SYN packet to the target port.
2. **SYN/ACK:** The target responds with a SYN/ACK packet, indicating that the port is open.
3. **ACK:** The scanner sends an ACK packet and completes the TCP Three-Way Handshake.
4. **RST:** The scanner terminates the connection by sending a TCP RST packet.

The successful handshake confirms that the port is open.

### 2. When the Port Is Closed

If the target port is closed:

1. The scanner sends a TCP SYN packet.
2. The target responds with a TCP RST packet.
3. The scanner identifies the port as closed.

## TCP Connect Scan Diagram

**Open Port:**

```text
Scanner                    Target
   |                          |
   | -------- SYN ----------> |
   |                          |
   | <------ SYN/ACK -------- |
   |                          |
   | -------- ACK ----------> |
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

Nmap uses the `-sT` option to perform a TCP Connect Scan.

```bash
nmap -sT 10.10.10.10
```

### Command Breakdown

- `nmap`: Runs the Nmap network scanner.
- `-sT`: Performs a TCP Connect Scan.
- `10.10.10.10`: Specifies the target IP address.

To scan a specific port:

```bash
nmap -sT -p 80 10.10.10.10
```

To scan multiple ports:

```bash
nmap -sT -p 22,80,443 10.10.10.10
```

To scan all TCP ports:

```bash
nmap -sT -p- 10.10.10.10
```

## Characteristics of TCP Connect Scan

- Establishes a complete TCP connection with open ports.
- Uses the operating system's `connect()` system call.
- Does not require raw packet privileges in the same way as SYN scanning.
- Is generally easier to detect and log because it establishes complete connections.
- Can generate more network traffic than a Half-Open Scan.

## TCP Connect Scan vs. TCP SYN Scan

### TCP Connect Scan (`-sT`)

- Completes the TCP Three-Way Handshake.
- Establishes a full connection with the target.
- Uses the operating system's connection functionality.
- Is generally more detectable.

### TCP SYN Scan (`-sS`)

- Sends a SYN packet and analyzes the response.
- Does not complete the TCP Three-Way Handshake.
- Typically sends an RST after receiving SYN/ACK.
- Is commonly called a Half-Open or Stealth Scan.
- Usually requires raw packet privileges.

## Summary

TCP Connect Scan is a port scanning technique that establishes a complete TCP connection to determine whether a port is open.

The main steps are:

- SYN
- SYN/ACK
- ACK
- Connection termination using RST

Nmap performs this scan using the `-sT` option.

---

## Related Links

- [Nmap TCP Connect Scan Documentation](https://nmap.org/book/scan-methods-connect-scan.html) — Official explanation of TCP Connect scanning.
- [Nmap Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html) — Overview of Nmap scanning methods, including `-sT` and `-sS`.
- [Nmap Reference Guide](https://nmap.org/book/man.html) — Complete documentation of Nmap commands and options.
- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html) — TCP specification, including connection establishment and termination.
- [Wireshark](https://www.wireshark.org/) — Network protocol analyzer for observing TCP handshakes and RST packets.
- [Wireshark TCP Three-Way Handshake](https://wiki.wireshark.org/TCP_3_way_handshaking) — Visual explanation of TCP connection establishment.
