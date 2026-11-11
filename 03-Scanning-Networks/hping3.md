
# hping3 Switches

## What Is hping3?

hping3 is a command-line network tool used to generate and send customized TCP, UDP, and ICMP packets.

Unlike traditional `ping`, which mainly uses ICMP Echo Requests, hping3 allows users to control packet headers, TCP flags, ports, and other network parameters.

It can be used for:

- Testing network connectivity.
- Examining firewall behavior.
- Performing TCP and UDP probing.
- Analyzing network responses.
- Testing network security in authorized environments.
- Inspecting TCP/IP behavior.

## 1. ICMP Ping

The `-1` option enables ICMP mode.

```bash
hping3 -1 10.0.0.25
```

This command sends ICMP Echo Request packets to the target.

## 2. ACK Scan

The `-A` option sets the TCP ACK flag.

```bash
hping3 -A 10.0.0.25 -p 80
```

This command sends TCP packets with the ACK flag set to port 80.

It can be used to examine how a target or firewall handles unsolicited ACK packets.

## 3. UDP Scan

The `-2` option enables UDP mode.

```bash
hping3 -2 10.0.0.25 -p 80
```

This command sends UDP packets to port 80.

## 4. Collecting Initial Sequence Numbers

The `-Q` option displays TCP sequence numbers.

```bash
hping3 192.168.1.103 -Q -p 139 -s 0
```

This example sends TCP packets to port 139 and displays sequence-number information.

- `-Q`: Displays only the TCP sequence number.
- `-p 139`: Sets the destination port to 139.
- `-s 0`: Sets the source port to 0.

## 5. Firewall Testing and TCP Timestamps

The `--tcp-timestamp` option enables TCP timestamp information in outgoing packets.

```bash
hping3 -S 72.14.207.99 -p 80 --tcp-timestamp
```

- `-S`: Sets the SYN flag.
- `-p 80`: Specifies destination port 80.
- `--tcp-timestamp`: Enables the TCP timestamp option.

TCP timestamps can provide information about TCP communication and may be useful when examining firewall behavior and TCP/IP characteristics.

## 6. SYN Scan on a Range of Ports

The `-8` option enables hping3 scan mode.

```bash
hping3 -8 50-56 -S 10.0.0.25 -V
```

This command scans TCP ports 50 through 56 using SYN packets.

- `-8`: Enables scan mode.
- `50-56`: Specifies the port range.
- `-S`: Sets the SYN flag.
- `-V`: Enables verbose output.

**Note:** The slide labels this example as a scan of ports 50–60, but the command itself specifies ports 50–56.

## 7. FIN, PUSH, and URG Scan

hping3 allows multiple TCP flags to be set in a packet.

```bash
hping3 -F -P -U 10.0.0.25 -p 80
```

- `-F`: Sets the FIN flag.
- `-P`: Sets the PSH (Push) flag.
- `-U`: Sets the URG (Urgent) flag.
- `-p 80`: Specifies destination port 80.

This creates a TCP probe with FIN, PSH, and URG flags set, similar to the flag combination used in an Xmas Scan.

## 8. Scanning a Subnet for Live Hosts

The `--rand-dest` option enables random destination address mode.

```bash
hping3 -1 10.0.1.x --rand-dest -I eth0
```

- `-1`: Uses ICMP mode.
- `--rand-dest`: Selects random destination addresses.
- `-I eth0`: Uses the `eth0` network interface.

The slide illustrates using this mode to probe addresses within a subnet.

## 9. Intercepting HTTP Traffic

The `-9` option enables hping3 listen mode.

```bash
hping3 -9 HTTP -I eth0
```

- `-9`: Enables listen mode.
- `HTTP`: Specifies the signature or pattern to look for.
- `-I eth0`: Selects the network interface.

This example illustrates listening for traffic containing an HTTP signature.

## 10. SYN Flooding

The slide also demonstrates a SYN flooding example:

```bash
hping3 -S 192.168.1.1 -a 192.168.1.254 -p 22 --flood
```

Command components:

- `-S`: Sets the TCP SYN flag.
- `-a`: Specifies a spoofed source IP address.
- `-p 22`: Sets destination port 22.
- `--flood`: Sends packets as fast as possible without displaying individual replies.

**Security Warning:** SYN flooding is a Denial-of-Service (DoS) technique that can disrupt network services. This command can generate substantial traffic and must not be executed against public or third-party systems. Study its behavior only in an isolated, explicitly authorized lab.

## Important hping3 Options

### Protocol Selection

- `-1`: ICMP mode.
- `-2`: UDP mode.
- Default mode: TCP.

### TCP Flags

- `-S`: SYN
- `-A`: ACK
- `-F`: FIN
- `-R`: RST
- `-P`: PSH
- `-U`: URG

### Port and Interface Options

- `-p`: Destination port.
- `-s`: Source port.
- `-I`: Network interface.

### Other Options

- `-c`: Number of packets to send.
- `-V`: Verbose output.
- `-Q`: Display TCP sequence numbers.
- `-8`: Scan mode.
- `-9`: Listen mode.
- `--flood`: Send packets as fast as possible.
- `--tcp-timestamp`: Enable TCP timestamp information.

## Summary

hping3 is a flexible packet-crafting and network-testing tool.

Its main advantage is the ability to customize network packets and control protocol-specific fields.

Unlike ordinary ping, hping3 can work with TCP, UDP, and ICMP, making it useful for network analysis, connectivity testing, and authorized security assessments.

---

## Related Links

- [Kali Linux Tools — hping3](https://www.kali.org/tools/hping3/) — Installation instructions, usage examples, and available command-line options.
- [hping3 Official Website](https://www.hping.org/) — Project information and documentation.
- [hping3 Manual (Debian)](https://sources.debian.org/src/hping3/3.a2.ds2-7/docs/hping3.8) — Detailed explanation of hping3 options and packet modes.
- [hping3 Source Code](https://github.com/antirez/hping) — Source code and project documentation.
- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html) — TCP protocol specification and header information.
- [RFC 768 — User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768.html) — UDP protocol specification.
- [RFC 792 — Internet Control Message Protocol](https://www.rfc-editor.org/rfc/rfc792.html) — ICMP protocol specification.
- [Wireshark](https://www.wireshark.org/) — Capture and analyze packets generated by hping3.
