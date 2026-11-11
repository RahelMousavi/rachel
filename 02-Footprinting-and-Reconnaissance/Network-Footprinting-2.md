
# Traceroute Commands

Traceroute functionality is available through different command-line utilities and protocols.

The commands differ depending on the operating system and the protocol used to send traceroute probes.

## 1. Tracert (Windows - ICMP)

`tracert` is the Windows command-line utility used to trace the route to a destination.

It uses ICMP Echo Requests and TTL values to identify intermediate routers.

### Usage

```cmd
tracert example.com
```

## 2. Traceroute (Linux - UDP)

`traceroute` is a Linux command-line utility that commonly uses UDP probes to discover the route to a destination.

### Usage

```bash
traceroute example.com
```

## 3. TCPTraceroute (Linux - TCP)

`tcptraceroute` is a traceroute utility that uses TCP packets instead of the traditional UDP probes.

It can be useful when ICMP or UDP traffic is filtered by firewalls.

### Usage

```bash
sudo tcptraceroute example.com
```

## Summary

Traceroute utilities identify the intermediate routers between a source and destination.

- **tracert:** Windows, commonly uses ICMP.
- **traceroute:** Linux, commonly uses UDP by default.
- **tcptraceroute:** Linux, uses TCP probes.

**Note:** Traceroute implementations may support multiple probe protocols and options.
