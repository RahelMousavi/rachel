
# Xmas Scan

Xmas Scan is a TCP port scanning technique that sends specially crafted TCP packets with three flags enabled:

- **FIN:** Indicates that the sender wants to terminate a connection.
- **PSH:** Requests that buffered data be pushed to the receiving application.
- **URG:** Indicates that the Urgent Pointer field is significant.

The combination of these three flags makes the packet look unusual, which is why this technique is called Xmas Scan.

## How Xmas Scan Works

Xmas Scan sends TCP packets with FIN, PSH, and URG flags enabled and analyzes the target's response.

### 1. When the Port Is Open

1. The scanner sends a TCP packet with FIN, PSH, and URG flags set.
2. The target receives the packet.
3. If the port is open, the target typically does not respond.
4. Nmap reports the port as `open|filtered`.

### 2. When the Port Is Closed

1. The scanner sends a TCP packet with FIN, PSH, and URG flags set.
2. The target receives the packet.
3. If the port is closed, the target responds with a TCP RST packet.
4. Nmap reports the port as `closed`.

## Xmas Scan Diagram

**Open Port:**

```text
Scanner                    Target
   |                          |
   | ---- FIN + PSH + URG ---> |
   |                          |
   |      No Response         |
   |                          |
```

**Closed Port:**

```text
Scanner                    Target
   |                          |
   | ---- FIN + PSH + URG ---> |
   |                          |
   | <-------- RST ----------- |
   |                          |
```

## Nmap Command

Nmap uses the `-sX` option to perform an Xmas Scan.

```bash
nmap -sX 10.10.10.10
```

### Command Breakdown

- `nmap`: Runs the Nmap network scanner.
- `-sX`: Performs an Xmas Scan.
- `10.10.10.10`: Specifies the target IP address.

To scan a specific port:

```bash
nmap -sX -p 80 10.10.10.10
```

To scan multiple ports:

```bash
nmap -sX -p 22,80,443 10.10.10.10
```

To scan all TCP ports:

```bash
nmap -sX -p- 10.10.10.10
```

## Characteristics of Xmas Scan

- Uses FIN, PSH, and URG TCP flags simultaneously.
- Does not establish a TCP connection.
- Typically receives no response from open ports.
- Typically receives RST responses from closed ports.
- Can be detected by firewalls and intrusion detection systems.
- May produce unreliable results on some operating systems.

## Limitations

Xmas Scan relies on specific TCP behavior.

According to the TCP specification, a closed port generally responds to an incoming segment that does not contain SYN, ACK, or RST with a RST packet.

However, some operating systems, particularly Windows, do not follow the expected behavior for these scans.

Firewalls may also drop the packets, making it difficult to determine whether a port is open or filtered.

Therefore, no response does not necessarily mean that a port is open.

## Summary

Xmas Scan is a TCP scanning technique that uses three TCP flags:

- FIN
- PSH
- URG

Nmap performs this scan using the `-sX` option.

Typical results:

- **Open|Filtered:** No response received.
- **Closed:** RST response received.
- **Filtered:** A filtering mechanism prevents Nmap from determining the port state.

---

## Related Links

- [Nmap Xmas Scan Documentation](https://nmap.org/book/scan-methods-null-fin-xmas-scan.html) — Official explanation of Xmas, FIN, and NULL scans.
- [Nmap Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html) — Overview of Nmap scanning methods.
- [Nmap Port States](https://nmap.org/book/man-port-scanning-basics.html) — Explains open, closed, filtered, and open|filtered states.
- [Nmap Reference Guide](https://nmap.org/book/man.html) — Complete Nmap command reference.
- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html) — TCP specification and flag behavior.
- [Wireshark](https://www.wireshark.org/) — Capture and inspect TCP packets and their flags.
