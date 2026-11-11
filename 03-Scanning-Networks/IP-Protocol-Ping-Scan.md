
# IP Protocol Ping Scan

IP Protocol Ping Scan is a host discovery technique that uses different IP protocol packets to determine whether a target host is active.

Unlike TCP or ICMP Echo Ping scans, this technique sends probes using different IP protocols, such as:

- ICMP (Internet Control Message Protocol)
- IGMP (Internet Group Management Protocol)
- TCP (Transmission Control Protocol)
- UDP (User Datagram Protocol)

The scanner analyzes the responses received from the target to determine whether it is reachable.

## How IP Protocol Ping Scan Works

1. The scanner sends packets using different IP protocols to the target host.
2. The target host receives the probes.
3. If the host is reachable, it may respond to one or more probes.
4. The scanner considers any valid response as evidence that the host is active.

## Nmap Command

Nmap uses the `-PO` option to perform IP Protocol Ping Scan.

```bash
nmap -sn -PO 10.10.10.10
```

### Command Breakdown

- `nmap`: Runs the Nmap network scanner.
- `-sn`: Performs host discovery without port scanning.
- `-PO`: Uses IP protocol probes for host discovery.
- `10.10.10.10`: Specifies the target IP address.

You can also specify particular IP protocol numbers:

```bash
nmap -sn -PO1,2,6,17 10.10.10.10
```

Protocol numbers in this example:

- `1`: ICMP
- `2`: IGMP
- `6`: TCP
- `17`: UDP

## Characteristics

- Uses different IP protocols to discover active hosts.
- Does not rely exclusively on ICMP Echo Requests.
- Can identify hosts that respond to supported protocol probes.
- The results depend on firewall rules and the protocols supported by the target.
- A lack of response does not necessarily mean that the host is inactive.

## IP Protocol Ping Scan vs. Other Ping Scans

- **ICMP Echo Ping Scan:** Uses ICMP Echo Request packets.
- **TCP SYN Ping Scan:** Uses TCP SYN packets.
- **TCP ACK Ping Scan:** Uses TCP ACK packets.
- **IP Protocol Ping Scan:** Uses probes based on different IP protocol numbers.

## Summary

IP Protocol Ping Scan is a host discovery method that sends packets using different IP protocols, including ICMP, IGMP, TCP, and UDP.

Nmap uses the `-PO` option to perform this type of scan.

It provides an alternative approach to discovering active hosts when other discovery techniques may not receive responses.

---

## Related Links

- [Nmap Host Discovery Documentation](https://nmap.org/book/man-host-discovery.html) — Official documentation for Nmap host discovery options, including IP protocol ping.
- [Nmap Host Discovery Techniques](https://nmap.org/book/host-discovery-techniques.html) — Explains different host discovery methods.
- [Nmap Reference Guide](https://nmap.org/docs.html) — Complete Nmap documentation.
- [IANA Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) — Official registry of IP protocol numbers.
- [RFC 791 — Internet Protocol](https://www.rfc-editor.org/rfc/rfc791) — Defines the IPv4 protocol and its header structure.
- [Wireshark](https://www.wireshark.org/) — Network protocol analyzer for inspecting IP packets and their protocol fields.
