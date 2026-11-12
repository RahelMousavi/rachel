
# Volumetric Attacks

## Introduction

**Volumetric attacks** are a category of DoS/DDoS attacks that aim to consume the available bandwidth of a network or service.

The attacker generates a large volume of traffic toward the target, attempting to exhaust its network capacity and prevent legitimate traffic from reaching the destination.

### Measurement

The magnitude of volumetric attacks is measured in:

- **BPS (Bits Per Second):** The number of bits transmitted per second.

## 1. UDP Flood Attack

A **UDP Flood** attack sends large numbers of fake UDP packets at a high rate to random ports on a remote target.

When the target receives these packets, it repeatedly checks whether an application is listening on the destination ports.

If no application is available, the target may respond with an ICMP error message:

- **ICMP Destination Unreachable:** Indicates that the destination or service cannot be reached.

This process consumes network resources and available bandwidth. A sufficiently large volume of traffic can overwhelm the target network.

## 2. ICMP Flood Attack

Network administrators commonly use the **Internet Control Message Protocol (ICMP)** for IP operations, troubleshooting, and reporting errors related to undeliverable packets.

In an ICMP Flood attack, the attacker sends a large volume of ICMP Echo Request packets (ping requests) directly to the victim or through reflector networks.

The victim is forced to process and respond to these requests.

As a result:

- A large volume of traffic is generated.
- The victim's network bandwidth may become saturated.
- The system may become unable to respond to legitimate TCP/IP requests.

## 3. Ping of Death

A **Ping of Death** attack attempts to disrupt a target system or service by sending malformed or oversized packets.

The attack exploits problems that may occur when the target system reassembles and processes an oversized IP packet.

According to the course material:

- The maximum IP packet size defined in RFC 791 is 65,535 bytes.
- An example of an oversized packet is 65,538 bytes.
- Processing and reassembling such a packet may cause the target system to crash, freeze, or become unstable.

## 4. Smurf Attack

A **Smurf Attack** uses ICMP requests and network broadcast addresses to generate a large volume of traffic toward a victim.

The general process is:

1. The attacker sends an ICMP Echo Request to a network broadcast address.
2. The source IP address in the request is spoofed to appear as the victim's IP address.
3. Multiple machines on the network receive the request.
4. Those machines send their ICMP responses to the victim.
5. The victim receives a large volume of responses and may become overwhelmed.

This attack uses multiple responding machines to amplify the traffic directed at the victim.

## 5. Pulse Wave DDoS Attack

In a typical DDoS attack, traffic may follow a relatively continuous pattern.

A **Pulse Wave DDoS** attack uses repeated periods of extremely high traffic instead.

According to the course material:

- The attacker sends repeated bursts, or pulses, of heavy traffic.
- Each pulse can consume a large portion of the target's available bandwidth.
- The traffic intensity rises sharply and then decreases.
- The process repeats periodically.

The course illustrates pulses occurring every 10 minutes, with traffic approaching 400 Gbps.

The repeated bursts make it difficult for the target system or network to recover between attack periods.

## Summary

- **UDP Flood:** Sends large numbers of UDP packets to random ports, consuming network resources and bandwidth.
- **ICMP Flood:** Overwhelms the target with ICMP Echo Requests and their resulting traffic.
- **Ping of Death:** Uses oversized or malformed packets that may cause system instability or crashes.
- **Smurf Attack:** Uses spoofed ICMP requests and broadcast addresses to direct multiple responses toward a victim.
- **Pulse Wave DDoS:** Generates repeated bursts of high-volume traffic.

## Related Links

- [Cloudflare — UDP Flood Attack](https://www.cloudflare.com/learning/ddos/udp-flood-ddos-attack/)
- [Cloudflare — ICMP Flood Attack](https://www.cloudflare.com/learning/ddos/ping-icmp-flood-ddos-attack/)
- [RFC 791 — Internet Protocol](https://www.rfc-editor.org/rfc/rfc791)
- [Cloudflare — What Is a DDoS Attack?](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/)
