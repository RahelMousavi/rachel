
# Module 08 — Network Sniffing

## Overview

Network sniffing is the process of capturing and analyzing network traffic to understand communication between devices. It can be used for legitimate network troubleshooting and monitoring, but attackers may also use it to intercept sensitive information.

This module covers network sniffing concepts, common sniffing techniques, tools used to capture and analyze packets, and methods for preventing and detecting sniffing activities.

## Learning Objectives

By the end of this module, you should be able to:

- Understand how network sniffing works.
- Distinguish between passive and active sniffing.
- Understand common network attacks related to sniffing.
- Identify tools used for packet capturing and network analysis.
- Apply security measures to reduce sniffing risks.
- Understand techniques used to detect sniffing activities.

## Module Contents

### 1. Sniffing Concept

- What Is Network Sniffing?
- Network Sniffing Threats
- How Does a Sniffer Work?
- Promiscuous Mode
- Hardware Protocol Analyzer
- MAC Addresses and CAM Tables
- SPAN Port

### 2. Sniffing Techniques

- Passive Sniffing
- Active Sniffing
- MAC Flooding
- DHCP Attacks
  - DHCP Message Types
  - DHCP Starvation
  - Rogue DHCP Server
- ARP Poisoning
  - ARP Protocol
  - ARP Spoofing
  - ARP Poisoning Threats
- MAC Spoofing / Duplication
- IRDP Spoofing
- VLAN Hopping
  - Switch Spoofing
  - Double Tagging
- DNS Poisoning
  - Intranet DNS Spoofing
  - Internet DNS Spoofing
  - Proxy Server DNS Spoofing
  - DNS Cache Poisoning

### 3. Sniffing Tools

- Wireshark Protocol Analyzer
- Wireshark Display Filters
  - IP Address Filters
  - TCP/UDP Port Filters
  - Protocol Filters
  - HTTP Request Filters
  - Logical Operators
  - MAC Address Filters
  - ARP Filters
- Other Network Sniffing Tools
- Mobile Sniffing Tools

### 4. Sniffing Countermeasures

- Physical Network Security
- Secure Communication Protocols
- Switching Instead of Hubs
- Encryption (IPsec and VPN)
- ARP and IP Protection
- Access Control and Network Hardening

### 5. Sniffing Detection Techniques

- Detecting Promiscuous Mode
- Monitoring MAC Address Changes
- Network Traffic Analysis
- Capsa Network Analyzer
- Promqry UI
- Nmap Sniffer Detection Script

## Lab Environment

Practical exercises can be performed in an isolated virtual lab using tools such as:

- **Kali Linux:** For network analysis and security testing.
- **Metasploitable:** As a deliberately vulnerable target.
- **Windows 10:** For observing network communication and testing defensive measures.
- **Wireshark:** For capturing and analyzing network packets.

> **Important:** Perform sniffing and network attack exercises only in systems and networks you own or have explicit permission to test.

## Related Links

- [Wireshark Official Website](https://www.wireshark.org/)
- [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
- [tcpdump Official Website](https://www.tcpdump.org/)
- [Nmap Official Documentation](https://nmap.org/book/man.html)
- [Nmap NSE Documentation](https://nmap.org/book/nse.html)
- [Cisco Networking Documentation](https://www.cisco.com/c/en/us/support/index.html)

## Summary

Module 08 focuses on understanding how network traffic can be captured and analyzed, how attackers exploit network protocols and configurations to intercept communications, and how organizations can prevent and detect sniffing activities. It also introduces practical tools such as Wireshark and Nmap for network analysis and security testing.
