
# Botnet Defense Techniques

## Introduction

Botnet defense techniques aim to reduce the impact of distributed attacks by identifying malicious traffic, preventing IP spoofing, and filtering traffic originating from suspicious sources.

The course introduces several techniques for defending against botnets and DDoS attacks.

## 1. RFC 3704 Filtering

**RFC 3704 Filtering** is a network security technique used to reduce the impact of DDoS attacks involving spoofed IP addresses.

It helps prevent packets with invalid or forged source addresses from entering or leaving a network.

ISPs should filter traffic originating from reserved or unused IP address ranges before forwarding it to the Internet.

This makes it more difficult for attackers to use spoofed source addresses.

## 2. Cisco IPS Source IP Reputation Filtering

**Source IP Reputation Filtering** uses reputation information to determine whether an IP address or service is associated with malicious activity.

According to the course, Cisco IPS maintains and updates threat information related to:

- Botnets
- Malware
- Other known threats

This information can be used to identify and filter potentially malicious DoS traffic.

## 3. Black Hole Filtering

**Black Hole Filtering** is a network routing technique that discards incoming traffic without notifying the original sender.

A specific network destination, known as a black hole, is configured to receive unwanted traffic.

Packets directed to this destination are dropped at the routing level.

This technique can help mitigate attacks by preventing malicious traffic from reaching the intended target.

However, incorrectly applied black hole routing may also discard legitimate traffic.

## 4. DDoS Prevention Services from ISPs

Organizations can use DDoS prevention services offered by their Internet Service Providers.

These services help detect and filter malicious traffic before it reaches the organization's network.

The course also mentions the use of Cisco **IP Source Guard** or similar features.

### IP Source Guard

IP Source Guard is a Cisco network security feature that filters traffic based on IP-to-MAC address bindings maintained through DHCP Snooping.

It helps prevent devices from sending packets with unauthorized or spoofed IP addresses.

## 5. ISP-Level DDoS Protection

ISPs play an important role in protecting networks against large-scale DDoS attacks.

The course introduces several ISP-level protection methods.

### 5.1 Blocking All Requests

During a DDoS attack, some ISPs may block all incoming requests to protect their infrastructure.

However, this approach can also prevent legitimate traffic from reaching the service.

### 5.2 In-the-Cloud Protection

Some ISPs provide cloud-based DDoS protection services.

These services help protect Internet links from becoming saturated by malicious traffic.

### 5.3 Malicious Traffic Redirection

In cloud-based protection, attack traffic is redirected to the ISP or a mitigation provider.

The traffic is filtered, and legitimate requests are forwarded to the protected network.

### 5.4 Requesting Assistance from the ISP

Network administrators can contact their ISP during an attack and request actions such as:

- Blocking the affected IP address.
- Moving the website to a new IP address.

## Summary

The main botnet defense techniques covered in this section are:

- **RFC 3704 Filtering:** Filters traffic with spoofed or invalid source IP addresses.
- **Cisco IPS Source IP Reputation Filtering:** Uses threat reputation information to identify malicious sources.
- **Black Hole Filtering:** Discards unwanted traffic at the routing level.
- **IP Source Guard:** Filters traffic based on trusted IP-to-MAC bindings.
- **ISP DDoS Services:** Provide additional traffic filtering and mitigation.
- **In-the-Cloud Protection:** Redirects attack traffic to external infrastructure for filtering.

## Related Links

- [RFC 3704 — Ingress Filtering for Multihomed Networks](https://www.rfc-editor.org/rfc/rfc3704)
- [Cisco — IP Source Guard](https://www.cisco.com/c/en/us/support/docs/security/identity-services-engine/118978-technote-ip-source-00.html)
- [Cloudflare — What Is a DDoS Attack?](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/)
- [Akamai — DDoS Protection](https://www.akamai.com/solutions/ddos-protection)
- [Fortinet — FortiDDoS](https://www.fortinet.com/products/ddos/fortiddos)
