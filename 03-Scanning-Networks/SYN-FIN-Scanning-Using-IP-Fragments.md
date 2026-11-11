
# SYN/FIN Scanning Using IP Fragments

SYN/FIN Scanning Using IP Fragments is not a separate scanning method. It is a modification of existing TCP scanning techniques, such as SYN Scan and FIN Scan.

In this technique, the scanner divides the TCP header into multiple smaller IP fragments before sending the packets to the target.

The purpose is to make it more difficult for some packet filters and security devices to identify the scanning activity.

## How IP Fragmentation Works

Normally, a TCP scanning probe is transmitted inside an IP packet containing the TCP header.

With IP fragmentation, the original IP packet is divided into smaller fragments.

Instead of receiving the complete TCP header in one packet, the target receives multiple IP fragments that can be reassembled.

### Scanning Process

1. The scanner creates a TCP probe, such as a SYN or FIN packet.
2. The IP packet is divided into smaller fragments.
3. The fragments are transmitted to the target.
4. The target's IP layer reassembles the fragments.
5. The target processes the reconstructed TCP packet.
6. The target responds according to the state of the destination port.

## Why Use IP Fragmentation?

Some packet filters inspect incoming packets to identify suspicious TCP flags and scanning activity.

When the TCP header is divided across multiple IP fragments, some filtering devices may have difficulty inspecting the complete TCP header.

This technique may help bypass certain improperly configured or older packet filters.

**Important:** Modern firewalls and intrusion detection systems can reassemble IP fragments before inspecting them. Therefore, fragmentation does not guarantee firewall or IDS evasion.

## SYN/FIN Scanning Using IP Fragments Diagram

The slide illustrates fragmented SYN/FIN probes sent to a target.

### When the Port Is Open

The target processes the reassembled TCP probe. The response depends on the scanning method being used.

For example, during a SYN Scan, an open port typically responds with SYN/ACK.

### When the Port Is Closed

The target responds with a TCP RST packet.

```text
Scanner                         Target
   |                               |
   | -- SYN/FIN (IP Fragments) --> |
   |                               |
   | <---------- RST ------------- |
   |       If Port Is Closed       |
```

## Nmap Command

Nmap provides the `-f` option to fragment scanning packets.

The command shown in the slide is:

```bash
nmap -sS -T4 -A -f -v 192.168.168.5
```

### Command Breakdown

- `nmap`: Runs the Nmap network scanner.
- `-sS`: Performs a TCP SYN Scan.
- `-T4`: Uses the aggressive timing template.
- `-A`: Enables aggressive scanning features, including OS detection, version detection, script scanning, and traceroute.
- `-f`: Fragments IP packets.
- `-v`: Enables verbose output.
- `192.168.168.5`: Specifies the target IP address.

## Using Fragmentation with Different Scan Types

The `-f` option can be combined with supported raw-packet scanning techniques.

### Fragmented SYN Scan

```bash
nmap -sS -f 192.168.168.5
```

### Fragmented FIN Scan

```bash
nmap -sF -f 192.168.168.5
```

In these examples:

- `-sS` selects SYN Scan.
- `-sF` selects FIN Scan.
- `-f` applies IP fragmentation to the probes.

## Important Nmap Options

### `-f`

Fragments packets into small IP fragments.

```bash
nmap -sS -f 192.168.168.5
```

### `-f -f`

Using `-f` twice increases the maximum fragment data size.

```bash
nmap -sS -f -f 192.168.168.5
```

### `--mtu`

Allows the user to specify the maximum transmission unit used for fragmentation.

The specified value must be a multiple of eight.

```bash
nmap -sS --mtu 16 192.168.168.5
```

**Note:** The `--mtu` option cannot be combined with `-f`.

## Limitations

- Some firewalls reassemble IP fragments before inspecting them.
- Some network devices drop fragmented packets.
- Some operating systems may reassemble outgoing packets before transmission.
- Fragmentation can increase packet-processing overhead.
- Fragmented scans may produce unexpected results on some networks.
- Not all Nmap features support fragmented packets.

Nmap supports fragmentation for raw-packet features, including TCP and UDP port scans (with certain exceptions) and OS detection. Version detection and NSE generally do not support fragmentation.

## Summary

SYN/FIN Scanning Using IP Fragments is a modification of existing scanning methods.

Its main characteristics include:

- Divides IP packets into smaller fragments.
- Splits the TCP header across multiple fragments.
- Makes inspection more difficult for some packet filters.
- Can be used with supported SYN and FIN scanning techniques.
- Does not guarantee bypassing modern firewalls or IDS systems.

The main Nmap option is:

```bash
-f
```

---

## Related Links

- [Nmap Firewall and IDS Evasion](https://nmap.org/book/firewall-subversion.html) — Official explanation of packet fragmentation and other firewall/IDS evasion techniques.
- [Nmap Fragmentation Options](https://nmap.org/book/man-bypass-firewalls-ids.html) — Documentation of `-f` and `--mtu`.
- [Nmap Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html) — Overview of SYN, FIN, and other scanning methods.
- [Nmap Reference Guide](https://nmap.org/book/man.html) — Complete documentation of Nmap commands and options.
- [RFC 791 — Internet Protocol](https://www.rfc-editor.org/rfc/rfc791.html) — IPv4 specification, including fragmentation and packet reassembly.
- [Wireshark](https://www.wireshark.org/) — Network protocol analyzer for inspecting fragmented IP packets.
- [Wireshark IP Protocol Reference](https://wiki.wireshark.org/Internet_Protocol) — Information about IPv4 headers and packet analysis.
