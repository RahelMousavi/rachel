
# ACK Flag Scanning

ACK Flag Scanning is a TCP scanning technique that sends TCP packets with only the ACK flag enabled.

Unlike SYN, FIN, and NULL scans, ACK Scan is mainly used to analyze firewall rules and determine whether ports are filtered or unfiltered.

It can help security professionals understand how a firewall handles unsolicited TCP packets.

## How ACK Flag Scanning Works

The scanner sends a TCP ACK packet to the target and analyzes the response.

### 1. When a Stateful Firewall Is Present

1. The scanner sends a TCP ACK packet to the target.
2. The stateful firewall checks whether the packet belongs to an established connection.
3. Since the packet is not associated with an existing connection, the firewall may drop it.
4. The scanner receives no response.

In this situation, Nmap may classify the port as `filtered`.

### 2. When No Firewall Is Present

1. The scanner sends a TCP ACK packet.
2. The target receives the packet.
3. Since the ACK packet does not belong to an established connection, the target typically responds with a TCP RST packet.
4. Nmap classifies the port as `unfiltered`.

## ACK Scan Diagram

**Stateful Firewall Present:**

```text
Scanner                 Stateful Firewall       Target
   |                            |                   |
   | -------- ACK ------------> |                   |
   |                            |                   |
   |                       Packet Dropped           |
   |                            |                   |
   |       No Response          |                   |
```

**No Firewall:**

```text
Scanner                                      Target
   |                                            |
   | --------------- ACK --------------------> |
   |                                            |
   | <--------------- RST -------------------- |
   |                                            |
```

## Nmap Command

Nmap uses the `-sA` option to perform a TCP ACK Scan.

```bash
nmap -sA 10.10.10.10
```

### Command Breakdown

- `nmap`: Runs the Nmap network scanner.
- `-sA`: Performs a TCP ACK Scan.
- `10.10.10.10`: Specifies the target IP address.

To scan specific ports:

```bash
nmap -sA -p 22,80,443 10.10.10.10
```

## Understanding ACK Scan Results

Nmap classifies the results based on the responses received:

- **Unfiltered:** A TCP RST response is received. The probe can reach the target, but the port may be open or closed.
- **Filtered:** No response is received, or an ICMP unreachable error indicates that the probe is blocked.

**Important:** ACK Scan does not determine whether a port is open or closed. Its main purpose is to identify filtering behavior and analyze firewall rules.

---

# TTL-Based ACK Flag Probe Scanning

TTL-Based ACK Scanning is a technique shown in the CEH slide that examines the TTL (Time To Live) value of TCP RST responses received from the target.

## What Is TTL?

TTL stands for Time To Live.

It is a field in the IP header that limits how many routers a packet can pass through before being discarded.

Each router decreases the TTL value by one. When it reaches zero, the packet is discarded.

TTL helps prevent packets from circulating indefinitely in a network.

## How TTL-Based ACK Scanning Works

1. The scanner sends TCP ACK probes to different target ports.
2. The target responds with TCP RST packets.
3. The scanner examines the TTL values in the received RST packets.
4. The slide describes comparing the TTL value against a boundary value of 64.

According to the slide's illustrated method:

- If the TTL value of an RST packet is lower than 64, the port is considered open.
- The example shows an RST response with TTL 50 for port 22, while other responses have TTL 80.

## Example from the Slide

```text
Host: 10.2.2.11

Port 20: RST -> TTL 80
Port 21: RST -> TTL 80
Port 22: RST -> TTL 50
Port 23: RST -> TTL 80
```

The slide identifies port 22 as open based on its lower TTL value.

## Important Limitation

TTL values are not a reliable general method for determining whether a TCP port is open.

The initial TTL, operating system, network path, and number of routers between systems can affect the observed value.

A lower TTL alone does not prove that a port is open.

---

# Window-Based ACK Flag Probe Scanning

Window-Based ACK Scanning examines the TCP Window field in RST responses received from the target.

The TCP Window field is related to the TCP flow-control mechanism and indicates how much data a receiver is willing to accept.

## How Window-Based ACK Scanning Works

1. The scanner sends TCP ACK packets to the target.
2. The target responds with TCP RST packets.
3. The scanner examines the TCP Window value in each RST response.
4. The slide uses the Window value to distinguish between open and closed ports.

According to the slide's illustrated method:

- **Non-zero Window value:** The port is considered open.
- **Zero Window value:** The port is considered closed.

## Example from the Slide

```text
Host: 10.2.2.12

Port 20: RST -> Window 0
Port 21: RST -> Window 0
Port 22: RST -> Window 512
Port 23: RST -> Window 0
```

In this example, port 22 is identified as open because its RST response contains a non-zero Window value.

## Nmap Window Scan

Nmap provides a related technique called TCP Window Scan.

It uses the `-sW` option:

```bash
nmap -sW 10.10.10.10
```

Window Scan is similar to ACK Scan, but it examines the TCP Window field in RST responses.

On some operating systems:

- A positive Window value may indicate an open port.
- A zero Window value may indicate a closed port.

However, this behavior depends on the target's TCP implementation and is not reliable on all systems.

---

# ACK Scan vs. Window Scan

## ACK Scan (`-sA`)

- Sends TCP packets with only the ACK flag enabled.
- Analyzes responses to identify filtered and unfiltered ports.
- Helps examine firewall filtering behavior.
- Does not distinguish open ports from closed ports.

## Window Scan (`-sW`)

- Uses ACK probes.
- Examines the TCP Window field in RST responses.
- May distinguish open and closed ports on certain operating systems.
- Depends on implementation-specific behavior.

## Summary

ACK-based scanning techniques are useful for examining firewall behavior and analyzing TCP responses.

The main techniques covered are:

- **ACK Scan (`-sA`):** Identifies filtered and unfiltered ports.
- **TTL-Based ACK Scanning:** Examines TTL values in RST responses, as illustrated in the slide.
- **Window-Based ACK Scanning:** Examines TCP Window values in RST responses.
- **Window Scan (`-sW`):** Nmap's implementation of TCP Window scanning.

**Important:** ACK Scan and Window Scan are not interchangeable. Standard Nmap ACK Scan does not identify open ports, and the TTL and Window interpretations shown in the slide should not be treated as universal rules.

---

## Related Links

### ACK Scan

- [Nmap TCP ACK Scan](https://nmap.org/book/scan-methods-ack-scan.html) — Official documentation explaining ACK Scan and its use in firewall analysis.
- [Nmap Determining Firewall Rules](https://nmap.org/book/determining-firewall-rules.html) — Explains how ACK scanning helps identify firewall filtering behavior.
- [Nmap Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html) — Overview of TCP scanning techniques and port states.

### Window Scan

- [Nmap Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html) — Describes TCP Window Scan (`-sW`) and how it examines TCP Window values.
- [Nmap Reference Guide](https://nmap.org/book/man.html) — Complete documentation of Nmap commands and options.

### TCP and Networking Concepts

- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html) — TCP specification, including flags and connection behavior.
- [RFC 791 — Internet Protocol](https://www.rfc-editor.org/rfc/rfc791.html) — IPv4 header fields, including TTL.
- [Wireshark](https://www.wireshark.org/) — Network protocol analyzer for inspecting TCP flags, TTL values, and Window fields.
- [Wireshark TCP Analysis](https://wiki.wireshark.org/TCP) — Resources for analyzing TCP packets.
