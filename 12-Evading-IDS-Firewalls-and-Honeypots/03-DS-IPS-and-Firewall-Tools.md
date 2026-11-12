
# 03. IDS/IPS and Firewall Tools

## 1. IDS/IPS Tools

IDS/IPS tools are used to monitor network traffic or host activities, detect suspicious behavior, and identify potential security threats.

The course introduces several IDS/IPS tools.

### 1.1 Snort

**Snort** is an open-source network intrusion detection and prevention system.

It can be used for:

- Packet sniffing.
- Network traffic logging.
- Debugging and analyzing network traffic.
- Network Intrusion Detection (NIDS).

Snort performs detection based on predefined **Rules**.

These rules can specify:

- Source IP address.
- Destination IP address.
- Source port.
- Destination port.
- Protocol type.

Snort compares network packets against its rules and generates alerts when matching suspicious traffic is detected.

### 1.2 Other IDS/IPS Tools

The following tools are also introduced in the course:

- **Suricata**
- **Samhain HIDS**
- **IBM Security Network IPS**
- **Peek & Spy**
- **Zeek**
- **OSSEC**
- **Cisco Secure IPS**
- **McAfee HIPS**
- **SNARE**
- **Vanguard Enforcer**
- **FortiGate**
- **Secure IPS - NGIPS**
- **Palo Alto Advanced Threat Prevention**

## 2. Firewall Tools

Firewalls can be implemented at the network level or directly on individual hosts.

The course introduces the following examples.

### 2.1 Network-Based Firewalls

Network-based firewalls protect network segments by controlling traffic entering and leaving the network.

Examples:

- Cisco Secure Firewall ASA
- PA-7500
- FortiGate 7121F
- Check Point 28000 Quantum
- Juniper SRX

### 2.2 Host-Based Firewalls

Host-based firewalls are installed on individual systems to monitor and control their network connections.

Examples:

- Microsoft Defender Firewall
- ZoneAlarm Pro Firewall
- Comodo Firewall
- Norton Smart Firewall
- McAfee Firewall

## Related Links

### IDS/IPS

- [Snort](https://www.snort.org/) – Open-source network intrusion detection and prevention system.
- [Snort Documentation](https://docs.snort.org/) – Official documentation covering installation, configuration, and rules.
- [Suricata](https://suricata.io/) – Open-source network threat detection engine.
- [Suricata Documentation](https://suricata.io/documentation/) – Official documentation and user guides.
- [Zeek](https://zeek.org/) – Network security monitoring platform.
- [OSSEC](https://www.ossec.net/) – Open-source host-based intrusion detection system.
- [OSSEC Documentation](https://www.ossec.net/docs/) – Official documentation.

### Firewall

- [Cisco Secure Firewall](https://www.cisco.com/site/us/en/products/security/firewalls/index.html) – Cisco firewall solutions.
- [Fortinet FortiGate](https://www.fortinet.com/products/next-generation-firewall) – Next-generation firewall solutions.
- [Check Point Security](https://www.checkpoint.com/) – Network security and firewall solutions.
- [Juniper Security](https://www.juniper.net/us/en/products/security.html) – Network security products.

## Summary

- IDS/IPS tools monitor network traffic or host activities to detect and respond to security threats.
- **Snort** uses predefined rules to identify suspicious network packets.
- Other tools mentioned in the course include Suricata, Zeek, Samhain HIDS, and OSSEC.
- Firewalls are classified into Network-Based and Host-Based solutions.
- Examples of network-based firewalls include Cisco Secure Firewall, FortiGate, and Juniper SRX.
- Microsoft Defender Firewall and ZoneAlarm are examples of host-based firewalls.
