
# IP Address Decoy

IP Address Decoy is a network scanning technique used to make a scan appear as if it originates from multiple IP addresses.

Instead of showing only the real scanner's IP address, Nmap sends additional scan packets using spoofed source IP addresses called **decoys**.

The purpose is to make it more difficult for the target system or its Intrusion Detection System (IDS) to identify the actual source of the scan.

## 1. How IP Address Decoy Works

During a decoy scan:

1. The scanner selects one or more decoy IP addresses.
2. Nmap sends scanning packets that appear to originate from these addresses.
3. The target receives packets from multiple apparent sources.
4. Security monitoring systems may report several different IP addresses as scan sources.
5. The actual scanner's IP address becomes harder to distinguish from the decoys.

### Example

Suppose a scanner uses three decoy IP addresses.

The target may observe scanning activity from:

- Decoy IP 1
- Decoy IP 2
- Decoy IP 3
- Actual scanner IP

This can make it difficult for security administrators to determine which system initiated the scan.

## 2. IP Address Decoy with Nmap

Nmap uses the `-D` option to perform a decoy scan.

### Using Random Decoy IP Addresses

```bash
nmap -D RND:10 10.10.10.10
```

### Command Breakdown

- `nmap`: Runs the Nmap network scanner.
- `-D`: Enables decoy scanning.
- `RND:10`: Generates 10 random, non-reserved IPv4 decoy addresses.
- `10.10.10.10`: Specifies the target IP address.

This command makes the scan appear to originate from multiple IP addresses.

### Using Manually Specified Decoy Addresses

Nmap also allows users to specify decoy addresses manually.

```bash
nmap -D 192.168.1.100,192.168.1.101,192.168.1.102 10.10.10.10
```

In this example, three decoy addresses are specified.

## 3. The `ME` Keyword

Nmap provides the special keyword `ME` to represent the actual scanner's IP address in the decoy list.

For example:

```bash
nmap -D 192.168.1.100,ME,192.168.1.101 10.10.10.10
```

Here:

- `192.168.1.100` is the first decoy.
- `ME` represents the actual scanner.
- `192.168.1.101` is another decoy.

If `ME` is not specified, Nmap places the real scanner's address at a random position in the decoy sequence.

## 4. Important Characteristics

- Decoy scanning uses spoofed source IP addresses.
- It makes the target observe apparent scanning activity from multiple sources.
- It can make identifying the real scanner more difficult.
- It does not guarantee anonymity.
- Network monitoring systems may still identify the actual scanner through traffic analysis or network path information.

## 5. Limitations

- Decoy hosts should be reachable and active; otherwise, the scan may become less effective.
- Using too many decoys can slow down scanning and reduce accuracy.
- Some Internet Service Providers (ISPs) filter packets with spoofed source addresses.
- Decoy scanning does not work with TCP Connect Scan (`-sT`).
- It does not work with service and version detection (`-sV`).
- It can be detected by modern IDS and network monitoring systems.
- Random decoy address generation is currently supported for IPv4.

## 6. Defensive Considerations

Organizations can reduce the effectiveness of decoy scanning through:

- Monitoring suspicious scanning patterns.
- Correlating traffic with network routing information.
- Using stateful firewalls and IDS/IPS.
- Monitoring unusual traffic from spoofed or unexpected source addresses.
- Applying ingress and egress traffic filtering.
- Maintaining network logs for incident investigation.

## Summary

IP Address Decoy is an Nmap technique that makes a scan appear to originate from multiple IP addresses.

The main option is:

```bash
-D
```

Generate random decoy addresses:

```bash
nmap -D RND:10 10.10.10.10
```

Specify decoy addresses manually:

```bash
nmap -D 192.168.1.100,192.168.1.101 10.10.10.10
```

Use `ME` to specify the position of the real scanner:

```bash
nmap -D 192.168.1.100,ME,192.168.1.101 10.10.10.10
```

**Key Concept:** Decoy scanning does not hide the scanner completely. It attempts to make the real scanning source harder to distinguish among multiple apparent sources.

---

## Related Links

- [Nmap — Firewall/IDS Evasion and Spoofing](https://nmap.org/book/man-bypass-firewalls-ids.html) — Official documentation of the `-D` option and decoy scanning.
- [Nmap — Subverting Intrusion Detection Systems](https://nmap.org/book/subvert-ids.html) — Explains how decoys can affect IDS monitoring and detection.
- [Nmap Reference Guide](https://nmap.org/book/man.html) — Complete documentation of Nmap options.
- [Nmap Options Summary](https://nmap.org/book/man-briefoptions.html) — Quick reference for command-line switches.
- [Nmap Source Code](https://github.com/nmap/nmap) — Nmap source code and project information.
- [RFC 791 — Internet Protocol](https://www.rfc-editor.org/rfc/rfc791.html) — IPv4 packet structure and source address fields.
- [RFC 2827 — Network Ingress Filtering](https://www.rfc-editor.org/rfc/rfc2827.html) — Guidance on filtering spoofed IP traffic.
