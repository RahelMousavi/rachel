
# IP Address Spoofing

IP Address Spoofing is a technique in which an attacker changes the source IP address of network packets to make them appear as if they originated from another system.

Instead of using the attacker's real IP address, the attacker places a different IP address in the source address field of the packet.

This technique can be used to disguise the origin of network traffic, impersonate another system, or support certain network attacks.

## 1. How IP Address Spoofing Works

Every IP packet contains a source IP address and a destination IP address.

- **Source IP Address:** Identifies the apparent sender of the packet.
- **Destination IP Address:** Identifies the intended receiver.

During IP Address Spoofing, the attacker modifies the source IP address while keeping the destination address unchanged.

### Example

Consider the following systems:

- Attacker's real IP address: `7.7.7.7`
- Spoofed source IP address: `7.7.7.7` (as shown in the slide)
- Victim's IP address: `5.5.5.5`

The attacker sends a packet that contains a forged source address.

The victim receives the packet and sees the spoofed address instead of the actual network source.

**Note:** The diagram illustrates an attacker using `7.7.7.7` as the spoofed source address. The actual source address of the attacker is not necessarily the same as the forged address.

## 2. IP Address Spoofing with hping3

The slide demonstrates IP spoofing using hping3.

### Command

```bash
hping3 www.certifiedhacker.com -a 7.7.7.7
```

### Command Breakdown

- `hping3`: Runs the hping3 packet crafting tool.
- `www.certifiedhacker.com`: Specifies the destination hostname.
- `-a 7.7.7.7`: Sets the spoofed source IP address.

The command generates packets that appear to originate from `7.7.7.7`.

The `-a` option is used to specify a spoofed source address.

## 3. What Happens to the Responses?

One important characteristic of IP spoofing is that responses are normally sent to the forged source IP address.

For example:

1. The attacker sends a packet to the victim.
2. The packet contains a spoofed source IP address.
3. The victim receives the packet.
4. If the victim replies, the response is sent to the spoofed IP address.
5. The attacker may not receive the response.

This makes ordinary two-way communication difficult when using a forged source address.

## 4. Types and Uses of IP Address Spoofing

IP spoofing can be used in different network attacks and scenarios, including:

### 1. Denial of Service (DoS)

Attackers may use spoofed source addresses to make it harder to identify the actual origin of malicious traffic.

### 2. Distributed Denial of Service (DDoS)

Spoofed source addresses may be used in some DDoS attacks to disguise traffic origins or complicate filtering.

### 3. Reflection and Amplification Attacks

Attackers can send requests with forged source addresses to third-party servers. The servers may send their responses to the spoofed address, potentially overwhelming the victim with traffic.

### 4. Identity Impersonation

An attacker may attempt to make packets appear as if they originated from a trusted system.

However, changing the source IP address alone does not automatically provide access to the impersonated system or establish a trusted connection.

## 5. Limitations of IP Address Spoofing

- Responses are generally routed to the spoofed source address.
- Stateful protocols and applications may require a valid two-way communication channel.
- Firewalls and intrusion detection systems can identify suspicious traffic patterns.
- Network devices may filter packets with invalid or unexpected source addresses.
- IP spoofing does not bypass authentication or encryption by itself.

## 6. Countermeasures Against IP Address Spoofing

Organizations can reduce IP spoofing risks through:

- **Ingress Filtering:** Reject packets entering a network with source addresses that should not originate from outside.
- **Egress Filtering:** Prevent internal systems from sending packets with unauthorized source addresses.
- **Anti-Spoofing Rules:** Configure routers and firewalls to reject invalid source addresses.
- **Network Monitoring:** Monitor unusual traffic patterns and suspicious packet sources.
- **Secure Network Configuration:** Apply appropriate access controls and filtering policies.

## Summary

IP Address Spoofing is a technique used to forge the source IP address of network packets.

The hping3 option used in the slide is:

```bash
-a <spoofed-source-IP>
```

Example:

```bash
hping3 www.certifiedhacker.com -a 7.7.7.7
```

**Key Concept:** IP Address Spoofing changes the apparent source IP address of a packet. It does not change the actual physical or network origin of the packet.

---

## Related Links

- [hping3 Official Website](https://www.hping.org/) — Information about hping3 and its packet crafting capabilities.
- [hping3 Manual](https://manpages.debian.org/bookworm/hping3/hping3.8.en.html) — Command-line options, including source address spoofing with `-a`.
- [RFC 791 — Internet Protocol](https://www.rfc-editor.org/rfc/rfc791.html) — IPv4 packet structure and source/destination address fields.
- [RFC 2827 — Network Ingress Filtering](https://www.rfc-editor.org/rfc/rfc2827.html) — Recommendations for preventing IP address spoofing through ingress filtering.
- [RFC 3704 — Ingress Filtering for Multihomed Networks](https://www.rfc-editor.org/rfc/rfc3704.html) — Guidance on filtering traffic with forged source addresses.
- [CISA — Understanding Denial-of-Service Attacks](https://www.cisa.gov/news-events/news/understanding-denial-service-attacks) — Overview of DoS attacks and related techniques.
- [Wireshark](https://www.wireshark.org/) — Capture and inspect IP packets and their source and destination addresses.
