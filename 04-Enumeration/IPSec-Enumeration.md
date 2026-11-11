
# IPSec Enumeration

## What Is IPSec?

IPSec (Internet Protocol Security) is a suite of protocols used to secure communication over IP networks.

It provides security for data transmitted between networks or individual endpoints, commonly in VPN connections.

### Main IPSec Components

IPSec uses three important protocols and mechanisms:

- **Authentication Header (AH):**
  - Provides data integrity and authentication.
  - Helps verify that packets have not been modified during transmission.
  - Does not provide encryption or confidentiality.

- **Encapsulating Security Payload (ESP):**
  - Provides confidentiality through encryption.
  - Can also provide data integrity, authentication, and anti-replay protection.

- **Internet Key Exchange (IKE):**
  - Establishes Security Associations (SAs).
  - Negotiates encryption algorithms, authentication methods, and cryptographic keys.

### ISAKMP

ISAKMP (Internet Security Association and Key Management Protocol) defines a framework for establishing, negotiating, modifying, and deleting Security Associations.

IPSec commonly uses ISAKMP together with IKE for key management and security association negotiation.

### IPSec Enumeration

IPSec Enumeration is the process of identifying IPSec-enabled devices and gathering information about their VPN configurations.

An attacker may attempt to discover:

- Encryption algorithms
- Hash algorithms
- Authentication methods
- IKE versions and configurations
- VPN endpoints and supported security parameters

### IPSec Ports

- **UDP 500:** Used by IKE for key exchange and negotiation.
- **UDP 4500:** Used by IPsec NAT Traversal (NAT-T).
- **IP Protocol 50:** Used by ESP.
- **IP Protocol 51:** Used by AH.

### IPSec Enumeration Using Nmap

Nmap can be used to identify systems with IKE services exposed on UDP port 500.

```bash
nmap -sU -p 500 <TARGET_IP>
```

- `-sU`: Performs a UDP scan.
- `-p 500`: Scans UDP port 500.

### IPSec Enumeration Using ike-scan

`ike-scan` is a tool used to discover IKE-enabled VPN servers and identify their supported parameters.

**Example:**

```bash
ike-scan <TARGET_IP>
```

It can help identify information such as:

- IKE response behavior
- Supported encryption algorithms
- Hash algorithms
- Authentication methods
- Diffie-Hellman groups

---

## Related Links

- [RFC 4301 — Security Architecture for IP](https://www.rfc-editor.org/rfc/rfc4301)
- [RFC 4302 — IP Authentication Header](https://www.rfc-editor.org/rfc/rfc4302)
- [RFC 4303 — IP Encapsulating Security Payload (ESP)](https://www.rfc-editor.org/rfc/rfc4303)
- [RFC 7296 — Internet Key Exchange Protocol Version 2 (IKEv2)](https://www.rfc-editor.org/rfc/rfc7296)
- [RFC 3947 — Negotiation of NAT-Traversal in the IKE](https://www.rfc-editor.org/rfc/rfc3947)
- [ike-scan — Official Website](https://github.com/royhills/ike-scan)
- [Nmap Reference Guide](https://nmap.org/book/man.html)
