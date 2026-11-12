
# 02. Firewall Concepts and Technologies

## 1. Firewall Concepts

A **Firewall** is a hardware or software security system designed to prevent unauthorized access to a network.

Firewalls are generally deployed at the network perimeter, separating an internal network from an external network such as the Internet.

They inspect incoming and outgoing network traffic and apply security rules to determine whether traffic should be allowed or blocked.

Firewalls also provide control over network ports and connections.

## 2. Firewall Architecture

The course introduces three common firewall architecture concepts:

### 2.1 Bastion Host

A **Bastion Host** is a specially secured system exposed to potentially untrusted networks. It is designed to provide a controlled point of access to protected services.

### 2.2 Screened Subnet

A **Screened Subnet** is a network architecture that uses filtering devices to separate publicly accessible systems from the protected internal network.

### 2.3 Multi-homed Firewall

A **Multi-homed** firewall has multiple network interfaces connected to different network segments. This allows it to control traffic moving between those segments.

## 3. Demilitarized Zone (DMZ)

A **Demilitarized Zone (DMZ)** is a network segment that acts as a neutral zone between an organization's secure internal network and an untrusted external network, such as the Internet.

It may contain one or more computers or a small subnet.

### Purpose of a DMZ

The main purpose of a DMZ is to prevent external users from accessing the organization's private network directly.

It provides an intermediate layer between the internal network and the Internet, helping protect internal systems from direct external access.

Public-facing services, such as web servers, can be placed inside a DMZ.

## 4. Types of Firewalls

Firewalls are generally classified into two main categories.

### 4.1 Network-Based Firewall

A **Network-Based Firewall** protects an entire network by monitoring and controlling traffic entering or leaving that network.

It is commonly deployed at network boundaries to control communication between different network segments.

Examples:

- Cisco Secure Firewall ASA
- FortiGate
- Check Point Quantum
- Juniper SRX

### 4.2 Host-Based Firewall

A **Host-Based Firewall** is installed on an individual computer or server.

It monitors and controls network traffic entering or leaving that specific host.

Examples:

- Microsoft Defender Firewall
- ZoneAlarm Pro Firewall
- Comodo Firewall
- Norton Smart Firewall
- McAfee Firewall

## 5. Firewall Technologies

Different firewall technologies inspect network traffic using different methods.

### 5.1 Packet Filtering

A **Packet Filtering Firewall** examines each packet before allowing it to pass through the firewall.

Packets are compared against a set of predefined filtering criteria.

Common criteria include:

- Source and destination IP addresses
- Source and destination ports
- Protocol
- Route
- Network interface

**Advantages:**

- Low cost.
- Minimal impact on network performance.
- Supported by most routers.

### 5.2 Circuit-Level Gateways

A **Circuit-Level Gateway** monitors TCP connections and the establishment of sessions between networks.

It does not inspect the actual application data in the same way as an application-level gateway.

According to the course material:

- It monitors TCP handshaking to determine whether a session is legitimate.
- It allows traffic to pass through the gateway.
- Connections to remote computers may appear to originate from the firewall itself because the firewall's IP address is used.

### 5.3 Application-Level Gateways

An **Application-Level Gateway**, also known as a **Proxy Firewall**, filters packets at the application layer.

It can inspect application-specific traffic and apply filtering rules based on the type of application data.

For example, it can filter HTTP methods such as:

- HTTP GET
- HTTP POST

Application-level gateways can also identify certain web-based attacks, such as SQL Injection.

### 5.4 Stateful Multilayer Inspection Firewall

A **Stateful Multilayer Inspection Firewall** tracks the state of network connections while filtering packets.

When a packet is allowed through the firewall, a record of the connection is added to the **State Table**.

Subsequent packets associated with that connection can be checked against the stored state information.

The firewall can examine information such as:

- Source IP address
- Destination IP address
- TCP/UDP ports

This approach improves performance because the firewall does not need to perform the same level of inspection on every packet.

### 5.5 Next-Generation Firewalls (NGFWs)

**Next-Generation Firewalls (NGFWs)** are advanced security solutions that combine traditional firewall capabilities with additional security features.

Important capabilities include:

- **Deep Packet Inspection (DPI):** Examines packet contents beyond basic header information.
- **Application Awareness and Control:** Identifies applications and controls their network traffic.
- **Integrated IPS:** Combines firewall functionality with intrusion prevention.
- **Cloud-Based Threat Intelligence:** Uses threat information obtained from cloud-based services.

These capabilities help NGFWs identify more complex and dynamic threats and provide enhanced protection for modern networks.

## 6. Firewall Limitations

Although firewalls are an essential part of network security, they have several limitations:

- **Insider Threats:** Firewalls cannot prevent all attacks originating from inside a network, such as an employee collaborating with an external attacker.
- **Performance Bottlenecks:** If all network connections pass through a firewall, it may become a bottleneck.
- **Social Engineering:** Firewalls cannot fully protect users against social engineering or data-driven attacks, such as malicious links and emails.
- **Zero-Day Attacks:** Firewalls may not provide sufficient protection against unknown vulnerabilities and zero-day malware.
- **Antivirus Replacement:** A firewall is not a replacement for antivirus software.
- **Poor Network Design:** A firewall cannot compensate for a poorly designed or incorrectly configured network.
- **Tunneled Traffic:** A firewall may not be able to properly understand or inspect traffic hidden inside tunnels.

Therefore, firewalls should be used as part of a broader security strategy rather than as the only security mechanism.

## Related Links

- [NIST SP 800-41 Rev. 1 – Guidelines on Firewalls and Firewall Policy](https://csrc.nist.gov/pubs/sp/800/41/r1/final) – A detailed guide covering firewall technologies, policies, deployment, and management.
- [NIST Firewall Glossary](https://csrc.nist.gov/glossary/term/firewall) – A formal definition of a firewall and related terminology.

## Summary

- A **Firewall** controls network traffic according to predefined security rules.
- A **DMZ** separates publicly accessible services from the organization's protected internal network.
- Firewalls can be **Network-Based** or **Host-Based**.
- Major firewall technologies include Packet Filtering, Circuit-Level Gateways, Application-Level Gateways, Stateful Multilayer Inspection, and NGFWs.
- **NGFWs** provide advanced capabilities such as DPI, application awareness, integrated IPS, and threat intelligence.
- Firewalls have limitations and should be combined with other security controls.
