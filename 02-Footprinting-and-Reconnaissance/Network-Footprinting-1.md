
# Network Footprinting

Network Footprinting is the process of collecting information about a target's network infrastructure, IP address ranges, and geographical location.

It helps security researchers understand the target's network structure and identify the route between a source and a destination.

## Traceroute

Traceroute is a network diagnostic technique used to identify the routers (hops) between a source device and a destination.

It uses the **TTL (Time To Live)** field in IP packets to discover the intermediate routers along a network path.

### How Traceroute Works

1. The source sends a packet with a low TTL value.
2. Each router that forwards the packet decreases its TTL by one.
3. When the TTL reaches zero, the router discards the packet.
4. The router usually sends an ICMP Time Exceeded message back to the source.
5. The source increases the TTL and sends another packet to discover the next router.
6. This process continues until the destination is reached or the maximum hop limit is reached.

### TTL (Time To Live)

TTL is an IP header field that limits the lifetime of a packet and prevents packets from circulating indefinitely in routing loops.

Each router decreases the TTL value by one before forwarding the packet.

If the TTL reaches zero, the packet is discarded.

### Common Initial TTL Values

The course material mentions these typical initial TTL values:

- **Windows:** 128
- **Cisco devices and many internet systems:** 255
- **Linux:** 64

**Note:** These are common initial values, not universal rules. The actual TTL observed by a remote system decreases as the packet travels through routers, so it cannot reliably identify an operating system by itself.

## Role in Network Footprinting

Traceroute can help security researchers:

- Identify intermediate routers.
- Understand network paths.
- Estimate the number of network hops.
- Identify possible routing or connectivity problems.
- Collect information about network infrastructure.

## Summary

Network Footprinting involves collecting information about a target's network infrastructure.

Traceroute uses TTL values to identify intermediate routers and understand the path between a source and destination.
