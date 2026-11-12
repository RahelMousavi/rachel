
# ARP and MAC-Based Attacks

## ARP Protocol

**Address Resolution Protocol (ARP)** is used in IPv4 local networks to discover the MAC address associated with a known IPv4 address.

For example, when a device wants to communicate with another device on the same local network, it needs the destination device's MAC address.

The basic process is:

1. The sender checks its ARP cache.
2. If the required mapping is unavailable, it broadcasts an ARP Request.
3. The device with the matching IP address responds with an ARP Reply.
4. The sender stores the IP-to-MAC mapping in its ARP cache.

ARP operates between the Network and Data Link Layer functions of IPv4 communication.

## ARP Spoofing and ARP Poisoning

**ARP Spoofing** occurs when an attacker sends forged ARP messages to associate an IP address with an incorrect MAC address.

**ARP Poisoning** refers to the process of corrupting a device's ARP cache with false IP-to-MAC mappings.

These terms are closely related and are often used interchangeably.

### How ARP Poisoning Works

An attacker may send forged ARP messages to both a victim and the default gateway.

The victim may then associate the gateway's IP address with the attacker's MAC address.

Similarly, the gateway may associate the victim's IP address with the attacker's MAC address.

This can place the attacker between the two devices and enable a Man-in-the-Middle (MITM) attack.

### ARP Poisoning Threats

ARP poisoning can lead to:

- Packet interception.
- VoIP communication interception.
- Session hijacking.
- Credential theft when sensitive information is exposed.
- Connection manipulation or interruption.
- Denial-of-Service (DoS) attacks.

Encrypted protocols such as HTTPS reduce the attacker's ability to read intercepted application data.

### ARP Poisoning Tools

Tools mentioned in CEH include:

- Ettercap
- Ufasoft Snif
- Win ARP Attacker
- Cain & Abel

Some of these tools are outdated. Ettercap remains a known tool for network traffic analysis and MITM demonstrations.

### ARP Poisoning Countermeasures

**Dynamic ARP Inspection (DAI)** is a switch security feature that validates ARP packets against trusted IP-to-MAC bindings.

DAI commonly uses the DHCP Snooping Binding database to identify legitimate address mappings.

Other measures include:

- DHCP Snooping.
- Static ARP entries in limited environments.
- Network segmentation.
- Monitoring unexpected ARP changes.
- Using encrypted communication protocols.

**XArp** is a host-based tool historically used to detect suspicious ARP activity.

## MAC Spoofing / Duplication

MAC Spoofing is the process of changing or impersonating the MAC address of a network interface.

An attacker may use another device's MAC address to impersonate it on a local network.

Potential consequences include:

- Unauthorized network access when MAC-based restrictions are used.
- Network communication disruption.
- MAC address conflicts.
- Impersonation of another device.

MAC spoofing alone does not guarantee that an attacker will receive all traffic intended for the legitimate device. The result depends on switch behavior and network configuration.

### Countermeasures

- Enable DHCP Snooping.
- Configure Dynamic ARP Inspection.
- Enable IP Source Guard.
- Use Port Security and MAC address limits.
- Monitor duplicate MAC addresses and unexpected changes.

## IRDP Spoofing

**ICMP Router Discovery Protocol (IRDP)** allows hosts to discover available routers on their local subnet.

Hosts can listen for Router Advertisement messages to identify potential default routers.

In an IRDP Spoofing attack, an attacker sends forged Router Advertisement messages to influence a host's router selection.

If a victim accepts the malicious advertisement, some of its traffic may be directed through an attacker-controlled system.

This can enable:

- Man-in-the-Middle attacks.
- Traffic interception.
- Denial-of-Service attacks.

IRDP is a legacy mechanism and is uncommon in many modern networks.

## Related Links

- [RFC 826 - Address Resolution Protocol](https://www.rfc-editor.org/rfc/rfc826)
- [RFC 1256 - ICMP Router Discovery Messages](https://www.rfc-editor.org/rfc/rfc1256)
- [Cisco - Dynamic ARP Inspection](https://www.cisco.com/c/en/us/support/docs/security/dynamic-arp-inspection/118630-technote-dai-00.html)
- [Ettercap Project](https://www.ettercap-project.org/)
- [XArp](https://www.xarp.net/)

## Summary

ARP poisoning manipulates IP-to-MAC mappings to redirect or intercept local network traffic. MAC spoofing impersonates another device's hardware address, while IRDP spoofing uses forged router advertisements to influence routing decisions. DHCP Snooping, Dynamic ARP Inspection, IP Source Guard, and network monitoring help reduce these risks.
