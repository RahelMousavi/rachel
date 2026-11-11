
# ICMP Echo Ping Scan

ICMP Echo Ping Scan is a host discovery technique used to determine whether a target system is active by sending ICMP Echo Request packets and waiting for ICMP Echo Reply packets.

It is commonly associated with the `ping` command.

## How ICMP Echo Ping Scan Works

1. The source sends an ICMP Echo Request packet to the destination.
2. The destination receives the request.
3. If the destination is active and allows ICMP Echo Requests, it sends an ICMP Echo Reply.
4. The source receives the reply and identifies the destination as reachable.

### ICMP Echo Request

An ICMP message sent by the source to check whether a destination is reachable.

### ICMP Echo Reply

An ICMP message returned by the destination in response to an Echo Request.

## Nmap Command

Nmap supports ICMP Echo Ping Scan using the `-PE` option.

```bash
nmap -sn -PE 10.10.10.10
```

- `-sn`: Performs host discovery without a port scan.
- `-PE`: Uses ICMP Echo Requests for host discovery.
- `10.10.10.10`: Target IP address.

## Using the Ping Command

You can also use the standard Linux `ping` command to test connectivity:

```bash
ping 10.10.10.10
```

To send a specific number of packets:

```bash
ping -c 4 10.10.10.10
```

- `-c 4`: Sends four ICMP Echo Requests.

## Characteristics of ICMP Echo Ping Scan

- Uses ICMP Echo Request and Echo Reply messages.
- Helps identify reachable hosts.
- Does not require checking TCP or UDP ports.
- Can be blocked or filtered by firewalls.
- A missing reply does not necessarily mean the target is inactive.

## Role in Network Scanning

ICMP Echo Ping Scan helps security professionals:

- Identify reachable hosts.
- Check basic network connectivity.
- Discover active systems before port scanning.
- Examine whether ICMP traffic is allowed by network security devices.

## Summary

ICMP Echo Ping Scan is a host discovery technique that uses ICMP Echo Request and Echo Reply messages to determine whether a target is reachable.

In Nmap, the `-PE` option enables ICMP Echo Request discovery.

**Important:** A host may be active even if it does not respond to ICMP Echo Requests because firewalls or network policies may block ICMP traffic.

## Related Links

- [Nmap Host Discovery Documentation](https://nmap.org/book/man-host-discovery.html) — Official documentation for Nmap host discovery options, including `-PE`.
- [Nmap Host Discovery Techniques](https://nmap.org/book/host-discovery-techniques.html) — Explains how Nmap uses different probes to identify active hosts.
- [Nmap Reference Guide](https://nmap.org/docs.html) — Complete Nmap documentation.
- [RFC 792 — Internet Control Message Protocol](https://www.rfc-editor.org/rfc/rfc792) — Technical specification of ICMP.
- [Zenmap](https://nmap.org/zenmap/) — Official graphical interface for Nmap.

