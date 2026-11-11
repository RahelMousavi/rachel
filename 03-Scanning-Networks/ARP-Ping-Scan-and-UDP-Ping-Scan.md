
# ARP Ping Scan / UDP Ping Scan

Host Discovery is the process of identifying active systems within a network before performing further scanning activities.

Two techniques used for host discovery are ARP Ping Scan and UDP Ping Scan.

## 1. ARP Ping Scan

ARP (Address Resolution Protocol) Ping Scan is a host discovery technique used to identify active devices on a local network.

It sends an ARP Request to the target IP address and waits for an ARP Reply.

### How It Works

1. The scanner sends an ARP Request asking which device owns the target IP address.
2. If the target is active on the local network, it responds with an ARP Reply containing its MAC address.
3. The scanner identifies the host as active.

### Nmap Command

```bash
nmap -sn -PR 10.10.10.10
```

- `-sn`: Performs host discovery without a port scan.
- `-PR`: Uses ARP requests for host discovery.
- `10.10.10.10`: Target IP address.

### Characteristics

- Mainly used on local Ethernet networks.
- Identifies active hosts through ARP responses.
- Can reveal the target's MAC address.
- Generally fast and reliable for local network discovery.

## 2. UDP Ping Scan

UDP Ping Scan is a host discovery technique that sends UDP packets to a target to determine whether it is active.

It analyzes the responses received from the target or intermediate network devices.

### How It Works

1. The scanner sends a UDP packet to a selected port on the target.
2. If the target responds, the scanner can identify it as active.
3. If the target port is closed, it may return an ICMP Port Unreachable message, indicating that the host is reachable.
4. If no response is received, the host's status may remain uncertain.

### Nmap Command

```bash
nmap -sn -PU 10.10.10.10
```

- `-sn`: Performs host discovery without a port scan.
- `-PU`: Uses UDP probes for host discovery.
- `10.10.10.10`: Target IP address.

### Characteristics

- Uses UDP packets instead of ARP requests.
- Can be used to discover hosts beyond the local network.
- May work when certain TCP or ICMP probes are filtered.
- Results can be affected by firewalls and packet filtering.

## ARP Ping Scan vs. UDP Ping Scan

### ARP Ping Scan

- Uses ARP Requests and Replies.
- Mainly works on local networks.
- Can identify the target's MAC address.
- Generally reliable for local host discovery.

### UDP Ping Scan

- Uses UDP packets.
- Can be used across routed networks.
- An ICMP Port Unreachable response can indicate that the target is active.
- Results may be affected by firewalls and network filtering.

## Summary

ARP Ping Scan and UDP Ping Scan are two techniques used to discover active hosts.

- **ARP Ping Scan (`-PR`):** Uses ARP requests to identify active devices on a local network.
- **UDP Ping Scan (`-PU`):** Sends UDP probes and analyzes responses to determine whether a host is reachable.

Both techniques help identify live systems before performing port scanning.

**Important:** A missing response does not necessarily mean that a host is inactive. Firewalls, filtering rules, and network configurations can prevent responses.

## Related Links

- [Nmap Host Discovery Documentation](https://nmap.org/book/man-host-discovery.html) — Official documentation for host discovery options, including `-PR` and `-PU`.
- [Nmap Host Discovery Techniques](https://nmap.org/book/host-discovery-techniques.html) — Explains how Nmap uses ARP, UDP, and other probes to discover active hosts.
- [Nmap Reference Guide](https://nmap.org/docs.html) — Complete Nmap documentation.
- [RFC 826 — Address Resolution Protocol](https://www.rfc-editor.org/rfc/rfc826) — Technical specification of ARP.
- [RFC 768 — User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768) — Technical specification of UDP.
- [Zenmap](https://nmap.org/zenmap/) — Official graphical interface for Nmap.
