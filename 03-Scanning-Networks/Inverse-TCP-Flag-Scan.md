
# Inverse TCP Flag Scan

Inverse TCP Flag Scan is a port scanning technique that sends TCP packets with unusual flag combinations to determine the state of target ports.

Unlike TCP SYN Scan, which uses the SYN flag, this technique uses other TCP flags, such as:

- FIN
- URG
- PSH
- NULL (no flags set)

The scanner analyzes the target's responses to identify port states.

## How Inverse TCP Flag Scan Works

The scanning process depends on the target port state.

### 1. When the Port Is Open

1. The scanner sends a TCP probe containing an unusual flag combination.
2. The target receives the packet.
3. If the port is open, the target typically does not respond.
4. The scanner interprets the absence of a response as an indication that the port may be open.

### 2. When the Port Is Closed

1. The scanner sends a TCP probe.
2. The target receives the packet.
3. If the port is closed, the target typically responds with a TCP RST packet.
4. The scanner identifies the port as closed.

## Scanning Behavior

**Open Port:**

```text
Scanner                    Target
   |                          |
   | -- FIN/URG/PSH/NULL ----> |
   |                          |
   |      No Response         |
   |                          |
```

**Closed Port:**

```text
Scanner                    Target
   |                          |
   | -- FIN/URG/PSH/NULL ----> |
   |                          |
   | <-------- RST ----------- |
   |                          |
```

## Types of Inverse TCP Flag Scans

Nmap provides three scanning techniques based on unusual TCP flag combinations:

### 1. FIN Scan

Sends TCP packets with only the FIN flag set.

```bash
nmap -sF 10.10.10.10
```

### 2. NULL Scan

Sends TCP packets without setting any TCP flags.

```bash
nmap -sN 10.10.10.10
```

### 3. Xmas Scan

Sends TCP packets with the FIN, PSH, and URG flags set.

```bash
nmap -sX 10.10.10.10
```

## Important Limitations

- These scanning techniques rely on expected TCP behavior defined by the protocol.
- Some operating systems, particularly Windows systems, may respond differently and send RST packets even for open ports.
- Firewalls may silently drop probes, making it difficult to distinguish open ports from filtered ports.
- No response does not always mean that a port is open.

Nmap may report the following states:

- **Open|Filtered:** Nmap cannot determine whether the port is open or filtered because no response was received.
- **Closed:** The target responded with a TCP RST packet.
- **Filtered:** A firewall or other filtering mechanism prevents Nmap from determining the port state.

## Summary

Inverse TCP Flag Scan uses unusual TCP flag combinations to identify port states.

Its main techniques include:

- FIN Scan (`-sF`)
- NULL Scan (`-sN`)
- Xmas Scan (`-sX`)

Typically, an open port does not respond to these probes, while a closed port responds with RST.

However, results depend on the target operating system and firewall configuration.

---

## Related Links

- [Nmap FIN, NULL, and Xmas Scans](https://nmap.org/book/scan-methods-null-fin-xmas-scan.html) — Official explanation of these TCP scanning techniques.
- [Nmap Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html) — Overview of Nmap port scanning methods.
- [Nmap Port States](https://nmap.org/book/man-port-scanning-basics.html) — Explains open, closed, filtered, and other port states.
- [Nmap Reference Guide](https://nmap.org/book/man.html) — Complete Nmap command reference.
- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html) — TCP specification, including TCP flags and packet handling.
- [Wireshark](https://www.wireshark.org/) — Network protocol analyzer for examining TCP flags and scan traffic.
