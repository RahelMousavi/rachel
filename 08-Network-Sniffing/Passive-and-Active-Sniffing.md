
# Passive and Active Sniffing

## Types of Network Sniffing

Network sniffing is generally classified into two types:

- Passive Sniffing
- Active Sniffing

The main difference is whether the attacker only observes existing traffic or actively manipulates network communication.

## Passive Sniffing

Passive sniffing involves monitoring network traffic without injecting additional packets or modifying communication.

It is traditionally associated with hub-based networks.

A hub forwards incoming traffic to all connected ports. Therefore, devices connected to the same hub can receive traffic that was not specifically addressed to them.

An attacker connected to such a network may capture traffic using a packet analyzer.

**Characteristics:**

- Does not require injecting packets.
- Does not intentionally modify network traffic.
- Commonly associated with shared Ethernet networks.
- Can be difficult to detect because it does not necessarily generate additional traffic.

Modern networks primarily use switches instead of hubs, making traditional passive sniffing less straightforward.

## Active Sniffing

Active sniffing involves injecting or manipulating network traffic to expose communications that would not normally be visible to the attacker.

It is commonly associated with switched networks.

Common techniques include:

- MAC Flooding
- DHCP Attacks
- ARP Poisoning
- DNS Poisoning
- Spoofing Attacks

These techniques attempt to manipulate network behavior, redirect traffic, or interfere with communication.

## MAC Flooding

MAC Flooding is an attack that attempts to exhaust a switch's CAM table by sending a large number of Ethernet frames with forged source MAC addresses.

When the table becomes full, the switch may flood unknown unicast traffic within the affected VLAN.

This can expose traffic to devices that would not normally receive it.

### MAC Flooding Tool: macof

`macof` is a Linux-based tool included in the `dsniff` suite.

It generates Ethernet frames with randomized source MAC addresses and can be used to demonstrate CAM table exhaustion.

**Lab Safety:** Test this technique only in an isolated lab or on networks you are authorized to assess.

## DHCP Attacks

### What Is DHCP?

**Dynamic Host Configuration Protocol (DHCP)** automatically provides network configuration to client devices.

A DHCP server can assign:

- IP addresses.
- Subnet masks.
- Default gateways.
- DNS server addresses.
- Other network configuration parameters.

### DHCP Message Types

The following are important DHCP messages:

- **DHCP Discover:** A client searches for available DHCP servers.
- **DHCP Offer:** A server offers an IP address and configuration.
- **DHCP Request:** A client requests the offered configuration.
- **DHCP ACK:** The server confirms the configuration.
- **DHCP NACK:** The server rejects the client's request.
- **DHCP Release:** A client releases its assigned IP address.
- **DHCP Inform:** A client requests additional configuration parameters without requesting an IP address.
- **DHCP Decline:** A client informs the server that an offered address appears to be already in use.

The first four messages form the common DORA process:

**Discover → Offer → Request → Acknowledgment**

### DHCP Starvation Attack

DHCP Starvation is a Denial-of-Service (DoS) attack in which an attacker attempts to exhaust the available IP address pool.

The attacker generates numerous DHCP requests, often using forged MAC addresses, causing the server to allocate or reserve many addresses.

As a result, legitimate clients may be unable to obtain an IP address.

**Tools mentioned in CEH:**

- Yersinia
- DHCP Starv

### Rogue DHCP Server

A Rogue DHCP Server is an unauthorized DHCP server operating on a network.

It responds to client requests and may provide malicious network configuration, such as:

- A malicious default gateway.
- An attacker-controlled DNS server.
- Incorrect network settings.

This can redirect traffic, enable man-in-the-middle attacks, or disrupt network communication.

Rogue DHCP servers may be introduced alongside DHCP starvation attacks, but the two techniques are distinct.

### DHCP Attack Countermeasures

- Enable DHCP Snooping on managed switches.
- Mark trusted and untrusted switch ports correctly.
- Use Port Security where appropriate.
- Monitor unauthorized DHCP responses.
- Apply appropriate DHCP server protections.

DHCP Snooping allows a switch to distinguish trusted DHCP server connections from untrusted ports.

## Related Links

- [RFC 2131 - Dynamic Host Configuration Protocol](https://www.rfc-editor.org/rfc/rfc2131)
- [Cisco - DHCP Snooping](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/217371-configure-dhcp-snooping.html)
- [dsniff Project](https://github.com/dugsong/dsniff)
- [Yersinia Project](https://github.com/tomac/yersinia)

## Summary

Passive sniffing observes existing network traffic, while active sniffing manipulates network communication to expose additional traffic. MAC flooding targets switch CAM tables, whereas DHCP starvation exhausts available IP addresses and rogue DHCP servers provide unauthorized network configuration. DHCP Snooping and switch security features help defend against these attacks.
