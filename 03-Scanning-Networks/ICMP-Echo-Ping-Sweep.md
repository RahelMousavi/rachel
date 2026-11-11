
# ICMP Echo Ping Sweep

ICMP Echo Ping Sweep is a host discovery technique used to identify multiple active hosts within a specified IP address range.

Instead of checking a single IP address, the scanner sends ICMP Echo Request packets to multiple IP addresses and analyzes their responses.

## How ICMP Echo Ping Sweep Works

1. The scanner selects a range of IP addresses.
2. It sends an ICMP Echo Request to each address.
3. Active hosts that allow ICMP requests respond with ICMP Echo Reply packets.
4. The scanner identifies the responding hosts as active.

## Nmap Command

Nmap can perform an ICMP Echo Ping Sweep using the `-sn` and `-PE` options.

```bash
nmap -sn -PE 10.10.10.5-15
```

### Command Breakdown

- `nmap`: Runs the Nmap network scanner.
- `-sn`: Performs host discovery without a port scan.
- `-PE`: Uses ICMP Echo Requests for host discovery.
- `10.10.10.5-15`: Specifies the target IP range from `10.10.10.5` to `10.10.10.15`.

## Understanding the Results

Nmap displays information about the discovered hosts.

- **Host is up:** Indicates that the host responded to the discovery probe or was otherwise determined to be active.
- **MAC Address:** Displays the MAC address when it can be discovered, typically on a local Ethernet network.
- **Host Discovery Report:** Provides information about the status of each scanned IP address.

## ICMP Echo Ping Scan vs. ICMP Echo Ping Sweep

### ICMP Echo Ping Scan

- Checks whether a single target host is reachable.
- Sends ICMP Echo Request packets to one IP address.

### ICMP Echo Ping Sweep

- Checks multiple hosts within an IP address range.
- Sends ICMP Echo Request packets to multiple IP addresses.
- Helps identify active systems across a network.

## Practical Example

To discover active hosts in your lab network, run:

```bash
nmap -sn -PE 192.168.100.1-50
```

Replace the example range with the actual subnet or IP range assigned to your lab.

## Summary

ICMP Echo Ping Sweep is a host discovery technique used to identify multiple active systems within a network.

Nmap uses the `-sn` and `-PE` options to perform this type of discovery.

It helps security professionals identify live hosts before proceeding with port scanning and service identification.

**Important:** Hosts may not respond to ICMP requests if firewalls or network policies block ICMP traffic. Therefore, no response does not always mean that a host is inactive.

## Related Links

- [Nmap Host Discovery Documentation](https://nmap.org/book/man-host-discovery.html) — Official documentation for Nmap host discovery options, including `-sn` and `-PE`.
- [Nmap Host Discovery Techniques](https://nmap.org/book/host-discovery-techniques.html) — Explains different methods Nmap uses to discover active hosts.
- [Nmap Reference Guide](https://nmap.org/docs.html) — Complete Nmap documentation.
- [Zenmap](https://nmap.org/zenmap/) — Official graphical interface for Nmap, useful for visualizing scan results.
- [RFC 792 — Internet Control Message Protocol](https://www.rfc-editor.org/rfc/rfc792) — Technical specification of ICMP.

