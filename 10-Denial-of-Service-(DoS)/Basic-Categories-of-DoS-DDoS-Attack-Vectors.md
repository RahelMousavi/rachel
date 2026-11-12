
# Basic Categories of DoS/DDoS Attack Vectors

DoS and DDoS attacks can target different resources within a system or network.

According to the course, attack vectors are divided into three basic categories:

1. Volumetric Attacks
2. Protocol Attacks
3. Application Layer Attacks

## 1. Volumetric Attacks

The main objective of volumetric attacks is to consume the available bandwidth of a network or service.

These attacks generate large amounts of traffic to overwhelm the target's network capacity.

### Measurement

The magnitude of volumetric attacks is measured in:

- **BPS (Bits Per Second):** The number of bits transmitted per second.

### Attack Techniques

- UDP Flood
- ICMP Flood
- Ping of Death
- Smurf Attack

## 2. Protocol Attacks

Protocol attacks consume resources within network infrastructure, such as firewalls and load balancers.

These attacks affect the resources required to process and handle network traffic.

### Measurement

The magnitude of protocol attacks is measured in:

- **PPS (Packets Per Second):** The number of packets transmitted per second.

### Attack Techniques

- SYN Flood
- Fragmentation
- Ping of Death
- Spoofed Session Flood

## 3. Application Layer Attacks

Application Layer attacks consume the resources of an application or service, making the application unavailable to legitimate users.

These attacks target the resources required by an application to process incoming requests.

### Measurement

The magnitude of application layer attacks is measured in:

- **RPS (Requests Per Second):** The number of requests sent per second.

### Attack Techniques

- HTTP GET/POST
- Slowloris
- UDP App Layer Flood

## Summary

The three basic categories of DoS/DDoS attack vectors target different resources:

- **Volumetric Attacks:** Consume network or service bandwidth. Measured in BPS.
- **Protocol Attacks:** Consume network infrastructure resources. Measured in PPS.
- **Application Layer Attacks:** Consume application or service resources. Measured in RPS.

Each category includes different attack techniques that will be covered in the next section.

## Related Links

- [Cloudflare — Types of DDoS Attacks](https://www.cloudflare.com/learning/security/what-is-a-ddos-attack-test-page/)
- [Canadian Centre for Cyber Security — Defending Against DDoS Attacks](https://www.cyber.gc.ca/en/guidance/defending-against-distributed-denial-service-ddos-attacks-itsm80110)

