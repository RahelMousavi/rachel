
# DoS/DDoS Countermeasures

## Introduction

DoS/DDoS countermeasures are security measures designed to prevent attacks, reduce their impact, and maintain the availability of systems and network services.

Protection can be implemented at different levels, including the network, operating system, application, and Internet Service Provider (ISP).

## 1. ISP-Level Protection

An ISP can help protect networks against large-scale DDoS attacks.

When attack traffic exceeds the capacity of the target network, the ISP can provide additional mitigation services.

### Traffic Redirection

In cloud-based protection, attack traffic is redirected to the ISP or a mitigation provider.

The malicious traffic is filtered, and legitimate traffic is forwarded to the protected network.

### Requesting Assistance from the ISP

Network administrators can request assistance from their ISP when their network is under attack.

According to the course, possible actions include:

- Asking the ISP to block the affected IP address.
- Moving the website to a new IP address.

## 2. General DoS/DDoS Countermeasures

The course introduces the following security measures:

### 2.1 Improve Routing Protocols

Improve and properly configure routing protocols to support reliable network operation and traffic handling.

### 2.2 Disable Unused and Insecure Services

Disable services that are unnecessary or insecure to reduce the system's exposure to potential attacks.

### 2.3 Keep Operating Systems Updated

Update operating systems to the latest available versions to address known vulnerabilities and security weaknesses.

### 2.4 Prevent IP Address Spoofing

ISPs should implement measures to prevent packets with forged or spoofed source IP addresses from entering or leaving their networks.

### 2.5 Configure Firewalls

Configure firewalls to restrict unwanted ICMP traffic and prevent unnecessary network requests from reaching protected systems.

### 2.6 Avoid Unsafe Programming Functions

Avoid unnecessary or unsafe programming functions such as:

- `strcpy()`
- `gets()`

Using safer alternatives helps prevent software vulnerabilities that may affect application stability and security.

### 2.7 Secure Remote Administrative Connections

Protect remote administrative and testing connections to prevent unauthorized access and misuse.

### 2.8 Perform Proper Input Validation

Validate user input carefully to prevent unexpected or malicious input from causing application errors or resource exhaustion.

### 2.9 Use Capable Network Interface Cards

Use better network interface cards (NICs) that can handle high packet volumes and support the required network performance.

## 3. Additional Protection Practices

The following practices provide additional protection against DoS/DDoS attacks:

- Monitor network traffic to identify unusual patterns.
- Apply traffic filtering and rate limiting where appropriate.
- Maintain network and application monitoring.
- Prepare an incident response plan.
- Coordinate with the ISP or DDoS mitigation provider during large-scale attacks.

## Summary

DoS/DDoS protection requires multiple layers of defense.

Important countermeasures include:

- Improving routing protocols.
- Disabling unused and insecure services.
- Updating operating systems.
- Preventing IP spoofing at the ISP level.
- Configuring firewalls to restrict unwanted traffic.
- Avoiding unsafe programming functions.
- Securing remote administrative connections.
- Performing proper input validation.
- Using network interfaces capable of handling high traffic volumes.
- Redirecting malicious traffic to cloud-based mitigation services.

## Related Links

- [CISA — Understanding and Responding to DDoS Attacks](https://www.cisa.gov/news-events/news/understanding-and-responding-distributed-denial-service-attacks)
- [Cloudflare — DDoS Protection](https://www.cloudflare.com/ddos/)
- [RFC 3704 — Ingress Filtering for Multihomed Networks](https://www.rfc-editor.org/rfc/rfc3704)
- [OWASP — Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
- [NIST — Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
