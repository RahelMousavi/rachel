
# Nmap Switches

Nmap provides different command-line switches to control how network scanning and host discovery are performed.

Each switch enables a specific scanning technique or changes the way Nmap interacts with target systems.

## 1. TCP Scan Techniques

These options specify different methods for scanning TCP ports.

### `-sT` — TCP Connect Scan

Performs a full TCP connection using the operating system's `connect()` system call.

```bash
nmap -sT 10.10.10.10
```

### `-sS` — SYN Scan

Performs a TCP SYN Scan without completing the full TCP three-way handshake.

```bash
nmap -sS 10.10.10.10
```

### `-sF` — FIN Scan

Sends TCP packets with only the FIN flag set.

```bash
nmap -sF 10.10.10.10
```

### `-sX` — Xmas Scan

Sends TCP packets with FIN, PSH, and URG flags set.

```bash
nmap -sX 10.10.10.10
```

### `-sN` — NULL Scan

Sends TCP packets without setting any TCP flags.

```bash
nmap -sN 10.10.10.10
```

### `-sA` — ACK Scan

Sends TCP packets with the ACK flag set. It is mainly used to examine firewall filtering behavior.

```bash
nmap -sA 10.10.10.10
```

### `-sW` — Window Scan

A variation of ACK Scan that examines the TCP Window field in RST responses.

```bash
nmap -sW 10.10.10.10
```

## 2. Other Scanning Techniques

### `-sU` — UDP Scan

Scans UDP ports to identify available UDP services.

```bash
nmap -sU 10.10.10.10
```

### `-sO` — IP Protocol Scan

Identifies which IP protocols are supported by the target host.

```bash
nmap -sO 10.10.10.10
```

### `-sI` — Idle Scan

Performs an indirect TCP port scan using a third-party host, known as a Zombie.

```bash
nmap -sI <zombie-host> 10.10.10.10
```

### `-sR` — RPC Scan

In older Nmap versions, this option was used to perform RPC scanning separately.

In modern Nmap versions, `-sR` is an alias for service and version detection (`-sV`).

### `-sL` — List Scan

Lists the specified targets without sending scanning packets to them. DNS resolution may be performed to obtain hostnames.

```bash
nmap -sL 192.168.1.0/24
```

## 3. Host Discovery Options

These switches control how Nmap determines whether target systems are online.

### `-sP` — Ping Scan

An older option for performing host discovery without a port scan.

The modern equivalent is `-sn`.

```bash
nmap -sn 192.168.1.0/24
```

### `-P0` — Don't Ping

An older option that tells Nmap to skip host discovery and treat targets as online.

The modern equivalent is `-Pn`.

```bash
nmap -Pn 10.10.10.10
```

### `-PT` — TCP Ping

An older host discovery option that used TCP probes.

Modern Nmap provides more specific options, such as `-PS` and `-PA`.

### `-PS` — TCP SYN Ping

Sends TCP SYN probes to determine whether a host is online.

```bash
nmap -sn -PS80,443 10.10.10.10
```

### `-PI` — ICMP Ping

An older option for ICMP Echo Request discovery.

The modern equivalent is `-PE`.

```bash
nmap -sn -PE 10.10.10.10
```

### `-PB` — TCP and ICMP Ping

An older option that combined TCP and ICMP host discovery probes.

This option is no longer part of the modern Nmap command-line interface.

### `-PP` — ICMP Timestamp Ping

Sends ICMP Timestamp Request packets to determine whether a target is online.

```bash
nmap -sn -PP 10.10.10.10
```

### `-PM` — ICMP Netmask Ping

Sends ICMP Address Mask Request packets for host discovery.

```bash
nmap -sn -PM 10.10.10.10
```

## 4. Modern vs. Older Nmap Options

Some options shown in the slide belong to older versions of Nmap. Their modern equivalents are important when using current Nmap installations.

- `-sP` → `-sn`
- `-P0` → `-Pn`
- `-PI` → `-PE`
- `-PT` → Use `-PS` or `-PA`, depending on the desired TCP probe.
- `-PB` → No direct modern equivalent; choose and combine the required discovery probes.
- `-sR` → Alias for `-sV` in modern Nmap.

**Important:** The options `-sT`, `-sS`, `-sF`, `-sX`, `-sN`, `-sU`, `-sO`, `-sI`, `-sA`, `-sW`, and `-sL` remain useful in modern Nmap.

## Summary

Nmap switches allow security professionals to customize network scanning based on their objectives.

The main categories include:

- **TCP Scanning:** `-sT`, `-sS`, `-sF`, `-sX`, `-sN`, `-sA`, `-sW`
- **Other Scanning Techniques:** `-sU`, `-sO`, `-sI`, `-sR`, `-sL`
- **Host Discovery:** `-sn`, `-Pn`, `-PS`, `-PE`, `-PP`, `-PM`

Understanding these options helps select the appropriate scanning technique for different network environments.

---

## Related Links

- [Nmap Options Summary](https://nmap.org/book/man-briefoptions.html) — Quick reference for Nmap command-line switches.
- [Nmap Reference Guide](https://nmap.org/book/man.html) — Complete documentation of Nmap options.
- [Nmap Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html) — Details about TCP, UDP, and other scanning techniques.
- [Nmap Host Discovery](https://nmap.org/book/man-host-discovery.html) — Documentation for host discovery options.
- [Nmap IP Protocol Scan](https://nmap.org/book/man-port-scanning-techniques.html) — Information about IP protocol scanning.
- [Nmap Idle Scan](https://nmap.org/book/idlescan.html) — Detailed explanation of the Idle Scan technique.
- [Nmap Service and Version Detection](https://nmap.org/book/man-version-detection.html) — Documentation about service detection and the modern behavior of `-sR`.
