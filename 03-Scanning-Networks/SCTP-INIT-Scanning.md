
# SCTP INIT Scanning

SCTP INIT Scan is a port scanning technique used to identify open and closed ports on systems that support the Stream Control Transmission Protocol (SCTP).

It is similar to TCP SYN Scan because it initiates the connection process but does not complete the full association handshake.

Nmap uses the `-sY` option to perform an SCTP INIT Scan.

## What Is SCTP?

SCTP stands for **Stream Control Transmission Protocol**.

It is a transport-layer protocol that combines some characteristics of TCP and UDP while providing additional features.

Some important SCTP features include:

- **Reliable Data Transfer:** Provides reliable data delivery.
- **Multi-Streaming:** Supports multiple independent streams within a single association.
- **Multi-Homing:** Allows an endpoint to use multiple IP addresses for redundancy and fault tolerance.
- **Association-Based Communication:** Establishes an association between two endpoints before normal data transfer.

SCTP is used in applications such as telecommunications signaling.

## How SCTP INIT Scan Works

The scanner sends an SCTP packet containing an INIT chunk to the target port and analyzes the response.

### 1. When the Port Is Open

1. The scanner sends an SCTP INIT chunk to the target.
2. The target responds with an INIT-ACK chunk.
3. The scanner identifies the port as open.
4. The scanner does not continue the association establishment process.

**Result:** The port is identified as open.

### 2. When the Port Is Closed

1. The scanner sends an SCTP INIT chunk to the target.
2. The target responds with an ABORT chunk.
3. The scanner identifies the port as closed.

**Result:** The port is identified as closed.

## SCTP INIT Scan Diagram

### Open Port

```text
Scanner                         Target
   |                               |
   | -------- INIT Chunk --------> |
   |                               |
   | <------ INIT-ACK Chunk ------ |
   |                               |
   |       Port Is Open            |
```

### Closed Port

```text
Scanner                         Target
   |                               |
   | -------- INIT Chunk --------> |
   |                               |
   | <------- ABORT Chunk -------- |
   |                               |
   |       Port Is Closed          |
```

## SCTP Four-Way Handshake

SCTP uses a four-way handshake to establish an association between two endpoints.

The four main steps are:

1. **INIT:** The client sends an INIT chunk to initiate an association.
2. **INIT-ACK:** The server responds with an INIT-ACK chunk containing a State Cookie.
3. **COOKIE-ECHO:** The client returns the State Cookie to the server.
4. **COOKIE-ACK:** The server acknowledges the cookie, and the association is established.

### Handshake Diagram

```text
Client                              Server
   |                                   |
   | ----------- INIT --------------> |
   |                                   |
   | <--------- INIT-ACK ------------ |
   |                                   |
   | -------- COOKIE-ECHO ----------> |
   |                                   |
   | <-------- COOKIE-ACK ------------ |
   |                                   |
   |      Association Established      |
```

**Important:** SCTP INIT Scan does not complete this four-way handshake. It stops after receiving the INIT-ACK response and does not send the COOKIE-ECHO chunk.

## Nmap Command

Nmap uses the `-sY` option to perform an SCTP INIT Scan.

```bash
nmap -sY 10.10.10.10
```

### Command Breakdown

- `nmap`: Runs the Nmap network scanner.
- `-sY`: Performs an SCTP INIT Scan.
- `10.10.10.10`: Specifies the target IP address.

To scan a specific SCTP port:

```bash
nmap -sY -p 2905 10.10.10.10
```

To scan multiple SCTP ports:

```bash
nmap -sY -p 2905,3868,5060 10.10.10.10
```

## Characteristics of SCTP INIT Scan

- Uses SCTP INIT chunks to probe target ports.
- Does not complete the SCTP association handshake.
- An INIT-ACK response indicates an open port.
- An ABORT response indicates a closed port.
- Is similar in concept to TCP SYN Scan.
- Can be used to discover SCTP-based services.
- Requires appropriate privileges to send and receive raw SCTP packets on typical Unix-like systems.

## SCTP INIT Scan vs. TCP SYN Scan

### SCTP INIT Scan (`-sY`)

- Uses SCTP INIT chunks.
- Receives INIT-ACK from an open port.
- Does not complete the SCTP association handshake.

### TCP SYN Scan (`-sS`)

- Uses TCP SYN packets.
- Receives SYN-ACK from an open port.
- Does not complete the TCP Three-Way Handshake.

Both techniques initiate communication without completing the full connection establishment process.

## Summary

SCTP INIT Scan is used to discover open and closed SCTP ports.

Its main steps are:

- Send an INIT chunk.
- Receive INIT-ACK if the port is open.
- Receive ABORT if the port is closed.

Nmap performs this scan using the `-sY` option.

---

## Related Links

- [Nmap SCTP INIT Scan Documentation](https://nmap.org/book/man-port-scanning-techniques.html) — Official documentation of SCTP INIT scanning (`-sY`).
- [Nmap Reference Guide](https://nmap.org/book/man.html) — Complete Nmap command reference.
- [RFC 9260 — Stream Control Transmission Protocol](https://www.rfc-editor.org/rfc/rfc9260.html) — Official SCTP specification, including association establishment and SCTP chunks.
- [RFC 9260 — Association Initialization](https://www.rfc-editor.org/rfc/rfc9260.html#section-5.1) — Explains the SCTP four-way handshake.
- [Wireshark](https://www.wireshark.org/) — Network protocol analyzer for capturing and examining SCTP packets.
- [Wireshark SCTP Display Filter Reference](https://www.wireshark.org/docs/dfref/s/sctp.html) — SCTP fields and display filters for packet analysis.
