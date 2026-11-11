
# Source Port Manipulation

Source Port Manipulation is a network scanning technique that changes the source port number of packets sent by a scanner.

It can be used to test firewall configurations that incorrectly trust incoming traffic based only on its source port number.

For example, some poorly configured firewalls may allow traffic originating from commonly trusted ports, such as:

- Port 53: DNS
- Port 80: HTTP
- Port 20: FTP Data

An attacker may attempt to use one of these source ports to bypass incorrectly configured firewall rules.

## 1. How Source Port Manipulation Works

Normally, a network packet contains two port numbers:

- **Source Port:** Identifies the port from which the packet originates.
- **Destination Port:** Identifies the port of the target service.

Source Port Manipulation changes the source port while keeping the destination port associated with the intended target service.

### Example

Assume a firewall blocks incoming packets originating from source port 242 but allows packets originating from source port 80.

The scanner sends a packet with:

- Actual source port: 242
- Destination port: 80

The firewall blocks the packet because its source port is 242.

The scanner then changes the source port to 80.

The firewall may allow the packet because it incorrectly trusts traffic originating from port 80.

```text
Scanner                 Firewall                 Target
   |                        |                       |
   | Source Port: 242       |                       |
   |----------------------->|                       |
   |                        | BLOCKED               |
   |                        |                       |
   | Source Port: 80        |                       |
   |----------------------->|                       |
   |                        | ALLOWED               |
   |                        |---------------------->|
   |                        |                       |
```

This illustrates how an insecure firewall rule can be exploited.

## 2. Source Port Manipulation with Nmap

Nmap provides two equivalent options for manipulating the source port:

- `-g`
- `--source-port`

### Using `-g`

```bash
nmap -g 80 10.10.10.10
```

This command asks Nmap to use source port 80 for supported scanning packets.

### Using `--source-port`

```bash
nmap --source-port 80 10.10.10.10
```

This performs the same function as the previous command.

### Combining Source Port Manipulation with SYN Scan

```bash
nmap -sS -g 80 10.10.10.10
```

Command breakdown:

- `nmap`: Runs the Nmap scanner.
- `-sS`: Performs a TCP SYN Scan.
- `-g 80`: Sets the source port to 80 where supported.
- `10.10.10.10`: Specifies the target IP address.

## 3. Why Does This Technique Work?

Some firewall configurations make decisions based only on the source port number instead of properly validating the traffic.

For example, a firewall may allow packets from source port 53 because it expects DNS responses to originate from that port.

However, an attacker can create packets that use source port 53 without actually being legitimate DNS responses.

This is an example of an insecure firewall configuration.

A properly configured firewall should inspect connection state and, where necessary, validate traffic at the application or protocol level rather than trusting a source port alone.

## 4. Limitations

- Source port manipulation does not bypass correctly configured firewalls automatically.
- Modern firewalls can inspect connection states and application protocols.
- Not all Nmap scanning techniques support source port manipulation.
- The option works with raw-packet scanning methods such as SYN and UDP scans.
- It does not affect TCP Connect Scan (`-sT`), service version detection (`-sV`), or OS detection (`-O`).

## 5. Defensive Measures

To protect networks against Source Port Manipulation:

- Avoid trusting traffic based only on source port numbers.
- Use stateful firewall inspection.
- Validate traffic according to expected protocols and connection states.
- Apply restrictive firewall rules.
- Monitor unusual traffic patterns.
- Regularly test firewall configurations.

## Summary

Source Port Manipulation changes the source port of scanning packets to test or exploit weak firewall rules.

The main Nmap options are:

```bash
-g <port>
--source-port <port>
```

For example:

```bash
nmap -sS -g 80 10.10.10.10
```

**Key Concept:** Source Port Manipulation changes the source port, not the destination port. Its effectiveness depends on insecure firewall rules that trust traffic based only on its source port.

---

## Related Links

- [Nmap — Source Port Manipulation](https://nmap.org/book/firewall-subversion.html) — Official explanation of source port manipulation and firewall misconfigurations.
- [Nmap Firewall and IDS Evasion](https://nmap.org/book/man-bypass-firewalls-ids.html) — Documentation for `-g`, `--source-port`, and other firewall evasion options.
- [Nmap Reference Guide](https://nmap.org/book/man.html) — Complete reference for Nmap command-line options.
- [Nmap Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html) — Details about SYN, UDP, and other scanning methods.
- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html) — TCP specification, including source and destination ports.
- [RFC 768 — User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768.html) — UDP specification and port fields.
- [NIST SP 800-41 Rev. 1 — Guidelines on Firewalls and Firewall Policy](https://csrc.nist.gov/pubs/sp/800/41/r1/final) — Guidance on secure firewall configuration and traffic filtering.
- [Wireshark](https://www.wireshark.org/) — Capture and inspect packets to verify source and destination port values.
