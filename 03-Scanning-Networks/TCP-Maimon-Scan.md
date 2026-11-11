
# TCP Maimon Scan

TCP Maimon Scan is a TCP port scanning technique that sends specially crafted TCP packets with both FIN and ACK flags enabled.

It is named after its creator, Uriel Maimon.

Like FIN, NULL, and Xmas scans, it does not establish a complete TCP connection. Instead, it analyzes how the target responds to unusual TCP packets.

## How TCP Maimon Scan Works

The scanner sends a TCP packet with FIN and ACK flags set and examines the target's response.

### 1. When the Port Is Open

1. The scanner sends a TCP FIN/ACK packet to the target.
2. The target receives the packet.
3. According to the behavior described by this scanning technique, an open port does not respond.
4. Nmap reports the port as `open|filtered`.

### 2. When the Port Is Closed

1. The scanner sends a TCP FIN/ACK packet.
2. The target receives the packet.
3. The target responds with a TCP RST packet.
4. Nmap identifies the port as closed.

## TCP Maimon Scan Diagram

**Open Port:**

```text
Scanner                    Target
   |                          |
   | ------ FIN/ACK --------> |
   |                          |
   |      No Response         |
   |                          |
```

**Closed Port:**

```text
Scanner                    Target
   |                          |
   | ------ FIN/ACK --------> |
   |                          |
   | <-------- RST ---------- |
   |                          |
```

## Nmap Command

Nmap uses the `-sM` option to perform a TCP Maimon Scan.

```bash
nmap -sM 10.10.10.10
```

### Command Breakdown

- `nmap`: Runs the Nmap network scanner.
- `-sM`: Performs a TCP Maimon Scan.
- `10.10.10.10`: Specifies the target IP address.

To scan a specific port:

```bash
nmap -sM -p 80 10.10.10.10
```

To scan multiple ports:

```bash
nmap -sM -p 22,80,443 10.10.10.10
```

To scan all TCP ports:

```bash
nmap -sM -p- 10.10.10.10
```

## Characteristics of TCP Maimon Scan

- Uses TCP FIN and ACK flags together.
- Does not complete the TCP Three-Way Handshake.
- Typically receives no response from open ports under the expected behavior.
- Typically receives RST responses from closed ports.
- Can be affected by firewall rules and operating system implementations.
- May produce unreliable results on systems that do not follow the expected TCP behavior.

## TCP Maimon Scan vs. Other TCP Flag Scans

- **FIN Scan (`-sF`):** Sends a packet with only the FIN flag set.
- **NULL Scan (`-sN`):** Sends a packet without any TCP flags set.
- **Xmas Scan (`-sX`):** Sends a packet with FIN, PSH, and URG flags set.
- **Maimon Scan (`-sM`):** Sends a packet with FIN and ACK flags set.

## Summary

TCP Maimon Scan is a TCP port scanning technique that uses FIN/ACK packets to examine the state of target ports.

Nmap performs this scan using the `-sM` option.

Typical results:

- **Open|Filtered:** No response received.
- **Closed:** RST response received.

The accuracy of this technique depends on the target operating system and network filtering behavior.

---

## Related Links

- [Nmap Maimon Scan Documentation](https://nmap.org/book/scan-methods-maimon-scan.html) — Official explanation of TCP Maimon scanning.
- [Nmap Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html) — Overview of TCP scanning methods.
- [Nmap Port States](https://nmap.org/book/man-port-scanning-basics.html) — Explains open, closed, filtered, and open|filtered states.
- [Nmap Reference Guide](https://nmap.org/book/man.html) — Complete Nmap command reference.
- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html) — TCP specification and flag behavior.
- [Wireshark](https://www.wireshark.org/) — Network protocol analyzer for examining TCP flags and packets.
