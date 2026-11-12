
# Sniffing Modes and Protocol Analyzers

## Types of Network Sniffing

Network sniffing is commonly divided into two categories:

- Passive Sniffing
- Active Sniffing

The main difference is whether the attacker only observes existing traffic or actively manipulates network communication to make additional traffic visible.

## Passive Sniffing

Passive sniffing involves monitoring network traffic without injecting additional packets or modifying network communication.

It is traditionally associated with hub-based networks.

A hub forwards incoming traffic to all connected ports. Therefore, devices connected to the same hub can receive traffic that was not specifically addressed to them.

An attacker connected to such a network may capture traffic using a packet analyzer.

**Characteristics:**

- Does not require injecting packets.
- Does not intentionally modify network traffic.
- Commonly associated with shared Ethernet networks and hubs.
- Can be difficult to detect because it does not necessarily generate additional network traffic.

Modern networks primarily use switches instead of hubs, making traditional passive sniffing less straightforward.

## Active Sniffing

Active sniffing involves injecting or manipulating network traffic to intercept communications.

It is commonly associated with switched networks, where normal switching limits the traffic visible to each device.

Some techniques associated with active sniffing include:

- MAC Flooding
- DHCP Attacks
- ARP Poisoning
- DNS Poisoning
- Spoofing Attacks

These techniques manipulate network behavior to redirect, expose, or interfere with communication.

We will cover each technique in detail in the next section.

## Hardware Protocol Analyzer

A Hardware Protocol Analyzer is a dedicated physical device used to capture, inspect, and analyze network traffic.

It receives network signals and examines the transmitted packets without intentionally modifying the original communication.

Hardware protocol analyzers can help administrators:

- Monitor network traffic.
- Troubleshoot communication problems.
- Analyze protocol behavior.
- Investigate suspicious network activities.
- Inspect packet contents and structures.

Unlike ordinary software sniffers, these devices are specialized hardware solutions designed for network monitoring and analysis.

## SPAN Port

**SPAN (Switched Port Analyzer)** is a feature available on many network switches.

It allows a switch to copy traffic from selected ports or VLANs to a designated monitoring port.

A monitoring device connected to that destination port can capture and analyze the copied traffic using tools such as Wireshark.

### How SPAN Works

1. An administrator selects the source ports or VLANs to monitor.
2. The switch copies the selected traffic.
3. The copied packets are forwarded to the SPAN destination port.
4. A monitoring device captures and analyzes the packets.

SPAN is useful for network troubleshooting, intrusion detection, and security monitoring.

**Security Note:** Unauthorized access to a SPAN destination port can expose sensitive network traffic. These ports should be protected and access-controlled.

## Related Links

- [Cisco - SPAN and RSPAN Configuration Guide](https://www.cisco.com/c/en/us/support/docs/switches/catalyst-9300-series-switches/217969-configure-span-and-rspan-on-catalyst.html)
- [Wireshark Official Website](https://www.wireshark.org/)
- [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/)

## Summary

Passive sniffing observes existing network traffic without injecting packets, while active sniffing manipulates network communication to expose additional traffic. Hardware protocol analyzers provide dedicated packet analysis capabilities, and SPAN ports allow switches to copy selected traffic to a monitoring device.
