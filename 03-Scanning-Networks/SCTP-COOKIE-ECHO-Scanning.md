
# SCTP COOKIE ECHO Scanning

SCTP COOKIE ECHO Scan is an advanced port scanning technique used to identify SCTP ports.

It sends SCTP packets containing a COOKIE ECHO chunk to the target and analyzes the responses to determine port states.

Unlike SCTP INIT Scan, which uses INIT chunks, this technique uses COOKIE ECHO chunks during the scanning process.

## How SCTP COOKIE ECHO Scan Works

The scanning process depends on the state of the target port.

### 1. When the Port Is Open

1. The scanner sends an SCTP COOKIE ECHO chunk to the target.
2. The target receives the packet.
3. If the port is open, the target should silently discard the unexpected COOKIE ECHO chunk.
4. No response is received.
5. Nmap reports the port as `open|filtered`.

### 2. When the Port Is Closed

1. The scanner sends an SCTP COOKIE ECHO chunk to the target.
2. The target receives the packet.
3. If the port is closed, the target responds with an SCTP ABORT chunk.
4. Nmap identifies the port as closed.

## SCTP COOKIE ECHO Scan Diagram

### Open Port

```text
Scanner                         Target
   |                               |
   | ----- COOKIE ECHO Chunk ----> |
   |                               |
   |         No Response           |
   |                               |
   |      Port: Open|Filtered      |
```

### Closed Port

```text
Scanner                         Target
   |                               |
   | ----- COOKIE ECHO Chunk ----> |
   |                               |
   | <-------- ABORT Chunk ------- |
   |                               |
   |         Port: Closed          |
```

## Nmap Command

Nmap uses the `-sZ` option to perform an SCTP COOKIE ECHO Scan.

```bash
nmap -sZ 10.10.10.10
```

### Command Breakdown

- `nmap`: Runs the Nmap network scanner.
- `-sZ`: Performs an SCTP COOKIE ECHO Scan.
- `10.10.10.10`: Specifies the target IP address.

To scan a specific SCTP port:

```bash
nmap -sZ -p 2905 10.10.10.10
```

To scan multiple SCTP ports:

```bash
nmap -sZ -p 2905,3868,5060 10.10.10.10
```

## Characteristics of SCTP COOKIE ECHO Scan

- Uses SCTP COOKIE ECHO chunks.
- Does not complete the SCTP association handshake.
- Typically receives no response from open ports.
- Receives an ABORT chunk from closed ports.
- Is less obvious than SCTP INIT Scan.
- May pass through some stateless firewall rules that block INIT chunks but allow COOKIE ECHO chunks.
- Can still be detected by advanced Intrusion Detection Systems (IDS).

## Limitations

SCTP COOKIE ECHO Scan has an important limitation:

It cannot reliably distinguish between open and filtered ports.

Both situations may result in no response, so Nmap reports the port as:

`open|filtered`

This means the port may be open, or a firewall may be silently dropping the probe.

## SCTP COOKIE ECHO Scan vs. SCTP INIT Scan

### SCTP INIT Scan (`-sY`)

- Sends an INIT chunk.
- Receives INIT-ACK from an open port.
- Receives ABORT from a closed port.
- Can distinguish open, closed, and filtered states.

### SCTP COOKIE ECHO Scan (`-sZ`)

- Sends a COOKIE ECHO chunk.
- Typically receives no response from an open port.
- Receives ABORT from a closed port.
- Cannot distinguish open from filtered ports when no response is received.

## Summary

SCTP COOKIE ECHO Scan is an advanced SCTP port scanning technique that uses COOKIE ECHO chunks to examine target ports.

Nmap performs this scan using the `-sZ` option.

The main results are:

- **Open|Filtered:** No response received.
- **Closed:** ABORT chunk received.

Although this technique may be less obvious than SCTP INIT Scan, it is not invisible and can still be detected by security monitoring systems.

---

## Related Links

- [Nmap Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html) — Official documentation of SCTP COOKIE ECHO Scan (`-sZ`) and other scanning methods.
- [Nmap Reference Guide](https://nmap.org/book/man.html) — Complete Nmap command reference.
- [RFC 9260 — Stream Control Transmission Protocol](https://www.rfc-editor.org/rfc/rfc9260.html) — Official SCTP specification, including INIT, COOKIE ECHO, COOKIE ACK, and ABORT chunks.
- [RFC 9260 — SCTP Association Initialization](https://www.rfc-editor.org/rfc/rfc9260.html#section-5.1) — Explains the SCTP association establishment process.
- [Wireshark](https://www.wireshark.org/) — Network protocol analyzer for capturing and examining SCTP packets.
- [Wireshark SCTP Display Filter Reference](https://www.wireshark.org/docs/dfref/s/sctp.html) — SCTP packet fields and display filters.
