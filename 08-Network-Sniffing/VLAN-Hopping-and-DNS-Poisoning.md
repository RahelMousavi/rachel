
# VLAN Hopping and DNS Poisoning

## VLAN Hopping

A **Virtual LAN (VLAN)** logically separates devices into different Layer 2 broadcast domains, even when they are connected to the same physical switch.

VLAN Hopping is an attack that attempts to gain access to traffic or resources belonging to another VLAN.

The two main techniques are:

- Switch Spoofing
- Double Tagging

## Switch Spoofing

Switch Spoofing occurs when an attacker attempts to make a switch port operate as a trunk port.

Trunk ports can carry traffic for multiple VLANs, while access ports normally belong to a single VLAN.

The attack may exploit automatic trunk negotiation, allowing an attacker's device to establish a trunk connection and potentially access traffic from multiple VLANs.

### Countermeasures

- Configure access ports explicitly as access ports.
- Disable unnecessary trunk negotiation.
- Configure trunk ports manually.
- Allow only required VLANs on trunk links.

Example Cisco configuration:

```text
switchport mode access
switchport nonegotiate
```

For a trunk port:

```text
switchport mode trunk
switchport nonegotiate
```

## Double Tagging

Double Tagging is a VLAN Hopping technique that exploits the handling of native VLAN traffic on certain trunk configurations.

An attacker creates an Ethernet frame containing two VLAN tags.

Under specific conditions:

1. The first switch processes and removes the outer tag associated with the native VLAN.
2. The remaining inner tag identifies another VLAN.
3. The next switch may forward the frame into that VLAN.

This technique generally relies on specific network conditions, including native VLAN behavior and the attacker's position on the network.

It is typically a one-way attack and does not automatically provide full communication with the target VLAN.

### Countermeasures

- Change the native VLAN to an unused VLAN.
- Avoid using the default VLAN as the native VLAN.
- Explicitly configure access and trunk ports.
- Restrict allowed VLANs on trunk links.
- Enable native VLAN tagging where supported.

Example Cisco commands:

```text
switchport trunk native vlan 999
```

```text
vlan dot1q tag native
```

VLAN 999 is only an example; choose an unused VLAN ID appropriate for the network.

## DNS Poisoning

**Domain Name System (DNS)** translates domain names into IP addresses.

For example, when a user visits a website, DNS helps resolve its domain name to the corresponding IP address.

DNS Poisoning involves providing or storing false DNS information so that users are directed to an incorrect destination.

Several forms of DNS spoofing and poisoning are described in CEH.

### Intranet DNS Spoofing

Intranet DNS Spoofing targets DNS communication within a local network.

An attacker may combine ARP poisoning with DNS manipulation to intercept or alter DNS responses.

As a result, users may be directed to an attacker-controlled IP address instead of the legitimate destination.

### Internet DNS Spoofing

The course describes a technique in which malware changes the victim's configured DNS server address to an attacker-controlled DNS server.

The malicious server can then return manipulated DNS responses.

Changing DNS settings is one possible method of redirecting DNS queries; it is not the only form of DNS spoofing.

### Proxy Server DNS Spoofing

In this technique, malware modifies a victim's browser proxy settings to use an attacker-controlled proxy server.

The attacker may then intercept or manipulate web requests.

The course describes Internet Explorer settings, but the general concept applies to proxy configuration in other environments as well.

### DNS Cache Poisoning

DNS Cache Poisoning occurs when false DNS records are inserted into a DNS resolver's cache.

When clients request a domain name, the resolver may return the malicious cached address instead of the legitimate one.

This can redirect users to fraudulent or attacker-controlled websites.

## DNS Poisoning Countermeasures

Several security measures can help protect DNS infrastructure.

### DNSSEC

**Domain Name System Security Extensions (DNSSEC)** use digital signatures to help validate the authenticity and integrity of DNS data.

DNSSEC helps resolvers detect forged DNS responses when validation is properly configured.

It does not encrypt DNS queries or provide confidentiality.

### Secure DNS Configuration

- Use trusted and properly maintained DNS resolvers.
- Restrict recursive DNS queries to authorized clients.
- Monitor unusual DNS responses and configuration changes.
- Keep DNS servers and internal systems updated.
- Use firewalls to restrict unauthorized DNS traffic.
- Randomize source ports and transaction IDs to make off-path DNS response spoofing harder.

### Encrypted Communication

Use HTTPS and other secure protocols to protect application data during transmission.

TLS helps protect communication confidentiality and integrity, but it does not replace DNSSEC.

### Important Clarifications

- SSL is obsolete; use modern TLS.
- Blocking all outbound UDP port 53 traffic can break DNS resolution. Instead, enforce the use of approved DNS resolvers.
- Static ARP entries do not directly prevent DNS cache poisoning.
- SSH secures remote administration; it is not a direct DNS poisoning countermeasure.
- NXDOMAIN rate limiting may help mitigate certain DNS abuse patterns, but it is not a general solution to DNS cache poisoning.

## Related Links

- [Cisco - VLAN Configuration and Trunking](https://www.cisco.com/c/en/us/support/docs/lan-switching/virtual-lans-vlans/10023-3.html)
- [RFC 4033 - DNS Security Introduction and Requirements](https://www.rfc-editor.org/rfc/rfc4033)
- [ICANN - DNSSEC](https://www.icann.org/resources/pages/dnssec-2012-02-25-en)
- [Cloudflare - What Is DNS Spoofing?](https://www.cloudflare.com/learning/dns/dns-spoofing/)
- [RFC 8446 - TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446)

## Summary

VLAN Hopping attempts to access traffic from other VLANs through switch spoofing or double tagging. DNS Poisoning manipulates DNS information to redirect users to incorrect destinations. Explicit switch port configuration, native VLAN security, trusted DNS resolvers, DNSSEC, and encrypted communication help protect networks against these attacks.
