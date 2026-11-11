
# TCP SYN Ping Scan

TCP SYN Ping Scan is a host discovery technique that uses TCP SYN packets to determine whether a target host is active.

Unlike ICMP Ping Scan, this method uses TCP packets to probe the target.

## How TCP SYN Ping Scan Works

1. The scanner sends a TCP SYN packet to a target host.
2. The target host responds depending on the state of the destination port:
   - **SYN/ACK:** Indicates that the port is open and the host is reachable.
   - **RST:** Indicates that the port is closed, but the host is reachable.
3. The scanner uses the response to determine whether the host is active.

A response is not necessarily proof that a particular service is available; it indicates that the target system responded to the TCP probe.

## Nmap Command

```bash
nmap -sn -PS 10.10.10.10
```

### Command Breakdown

- `nmap`: Runs the Nmap network scanner.
- `-sn`: Performs host discovery without port scanning.
- `-PS`: Sends TCP SYN packets as host discovery probes.
- `10.10.10.10`: Specifies the target IP address.

You can also specify a port after `-PS`:

```bash
nmap -sn -PS80,443 10.10.10.10
```

This sends TCP SYN probes to ports 80 and 443.

## Characteristics

- Uses TCP SYN packets for host discovery.
- Can work when ICMP Echo Requests are blocked.
- Can identify hosts even when the probed ports are closed, provided the host responds with a TCP RST.
- Firewall rules may block or filter these probes.

---

# TCP ACK Ping Scan

TCP ACK Ping Scan is a host discovery technique that sends TCP ACK packets to a target to determine whether it is active.

It is useful for discovering hosts when other probing methods, such as ICMP Echo requests, are filtered.

## How TCP ACK Ping Scan Works

1. The scanner sends a TCP ACK packet to the target host.
2. The target host receives the packet.
3. Since the ACK packet does not belong to an established TCP connection, the target typically responds with a TCP RST packet.
4. The scanner interprets the response as evidence that the host is active.

### Important Note

A TCP RST response indicates that the target is reachable, even if the destination port is closed.

If there is no response, the host may be down, or a firewall may be filtering the packet. Therefore, the absence of a response does not necessarily mean the host is inactive.

## Nmap Command

```bash
nmap -sn -PA 10.10.10.10
```

### Command Breakdown

- `nmap`: Runs the Nmap network scanner.
- `-sn`: Performs host discovery without port scanning.
- `-PA`: Sends TCP ACK packets as host discovery probes.
- `10.10.10.10`: Specifies the target IP address.

You can also specify destination ports:

```bash
nmap -sn -PA80,443 10.10.10.10
```

This sends TCP ACK probes to ports 80 and 443.

## Characteristics

- Uses TCP ACK packets for host discovery.
- Typically receives TCP RST responses from reachable hosts.
- Can be useful when ICMP-based discovery is blocked.
- Firewall configurations can affect the results.

---

# TCP SYN Ping Scan vs. TCP ACK Ping Scan

## TCP SYN Ping Scan

- Sends TCP SYN packets.
- An open port typically responds with SYN/ACK.
- A closed port typically responds with RST.
- Uses the `-PS` option in Nmap.

## TCP ACK Ping Scan

- Sends TCP ACK packets.
- A reachable host typically responds with RST.
- Uses the `-PA` option in Nmap.

## Summary

Both TCP SYN Ping Scan and TCP ACK Ping Scan are TCP-based host discovery techniques.

They are useful alternatives to ICMP-based discovery when ICMP traffic is filtered or blocked.

The main difference is the type of TCP packet sent:

- **SYN Ping:** Sends TCP SYN packets.
- **ACK Ping:** Sends TCP ACK packets.

---

## Related Links

- [Nmap Host Discovery Documentation](https://nmap.org/book/man-host-discovery.html) — Official documentation for TCP SYN and TCP ACK discovery options.
- [Nmap Host Discovery Techniques](https://nmap.org/book/host-discovery-techniques.html) — Explains how Nmap uses different probes to identify active hosts.
- [Nmap Reference Guide](https://nmap.org/docs.html) — Complete Nmap documentation.
- [RFC 9293 — Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293.html) — TCP protocol specification, including TCP flags and connection behavior.
- [Wireshark](https://www.wireshark.org/) — A network protocol analyzer that can help you inspect SYN, ACK, SYN/ACK, and RST packets.
