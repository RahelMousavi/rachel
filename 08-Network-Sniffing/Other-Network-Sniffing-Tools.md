
# Other Network Sniffing Tools

Wireshark is not the only tool available for capturing and analyzing network traffic. Different tools provide different capabilities, including command-line packet capture, network monitoring, wireless analysis, and traffic inspection.

## Command-Line Packet Analysis Tools

### tcpdump

**tcpdump** is a command-line packet analyzer used to capture and inspect network traffic.

It is commonly available on Linux and Unix-like systems.

Example:

```bash
sudo tcpdump -i eth0
```

Captures traffic on the `eth0` interface.

Capture traffic involving a specific host:

```bash
sudo tcpdump host 192.168.1.10
```

Save captured packets to a file:

```bash
sudo tcpdump -i eth0 -w capture.pcap
```

Read a previously saved capture:

```bash
tcpdump -r capture.pcap
```

### WinDump

WinDump is the Windows version of tcpdump. It provides command-line packet capture and analysis capabilities on Windows systems.

## Network Monitoring and Analysis Tools

### ntopng

**ntopng** is a network traffic monitoring tool that provides information about network usage, hosts, protocols, and traffic patterns.

It offers a web-based interface for monitoring network activity.

Website: [ntopng](https://www.ntop.org/)

### Zeek

**Zeek** is an open-source network security monitoring platform.

It analyzes network traffic and generates structured logs that help security teams investigate network activity and detect suspicious behavior.

Website: [Zeek](https://zeek.org/)

### Kismet

**Kismet** is a wireless network detector, packet sniffer, and intrusion detection system.

It is primarily used for monitoring wireless networks and identifying wireless devices and activity.

Website: [Kismet](https://www.kismetwireless.net/)

### EtherApe

EtherApe is a graphical network monitoring tool that visualizes network activity and communication between hosts.

It can help users understand traffic patterns through a graphical representation.

Project: [EtherApe](https://etherape.sourceforge.io/)

## MITM and Network Security Testing Tools

### Ettercap

**Ettercap** is a tool for network traffic analysis and Man-in-the-Middle (MITM) testing.

It supports different network analysis techniques and can be used to study ARP poisoning in authorized lab environments.

Website: [Ettercap](https://www.ettercap-project.org/)

### dsniff

**dsniff** is a collection of tools designed for network auditing and traffic analysis.

It includes utilities such as:

- `macof` — generates frames with randomized source MAC addresses.
- `arpspoof` — performs ARP spoofing.
- `dnsspoof` — performs DNS spoofing.
- `dsniff` — analyzes network traffic for certain credentials and protocols.

Project: [dsniff on GitHub](https://github.com/dugsong/dsniff)

## Other Tools Mentioned in CEH

The course also introduces several other tools:

- **SteelCentral Packet Analyzer:** Network packet analysis and troubleshooting.
- **OmniPeek:** Network protocol analysis and monitoring.
- **Observer:** Network performance and protocol analysis.
- **Colasoft Packet Builder:** Creates and sends custom network packets.
- **RSA NetWitness Investigator:** Network traffic investigation and security analysis.
- **SmartSniff:** Windows-based packet monitoring utility.
- **CommView:** Network traffic monitoring and analysis.
- **Network Probe:** Network monitoring and traffic analysis.

Some of these products are legacy or have changed availability over time. Check their current status before using them.

## Mobile Sniffing Tools

The course mentions two mobile sniffing applications:

- **Wi.cap.Network Sniffer Pro:** A mobile network traffic capture and analysis application.
- **FaceNiff:** A legacy Android application associated with session hijacking on certain wireless networks.

These are historical examples and should not be assumed to work on modern Android devices or networks.

## Choosing the Right Tool

Different tools are suitable for different tasks:

- **Wireshark:** Detailed graphical packet analysis.
- **tcpdump:** Lightweight command-line packet capture.
- **ntopng:** Network traffic monitoring and visualization.
- **Zeek:** Network security monitoring and traffic analysis.
- **Kismet:** Wireless network monitoring.
- **Ettercap:** Authorized MITM and ARP spoofing demonstrations.
- **dsniff:** Network auditing and protocol-specific testing.

## Related Links

- [tcpdump Official Website](https://www.tcpdump.org/)
- [ntopng Official Website](https://www.ntop.org/)
- [Zeek Official Website](https://zeek.org/)
- [Kismet Official Website](https://www.kismetwireless.net/)
- [Ettercap Official Website](https://www.ettercap-project.org/)
- [dsniff GitHub Repository](https://github.com/dugsong/dsniff)
- [Wireshark Official Website](https://www.wireshark.org/)

## Summary

Several tools are available for network sniffing and traffic analysis. Wireshark and tcpdump are widely used for packet inspection, while ntopng and Zeek focus on network monitoring and security analysis. Kismet specializes in wireless networks, and Ettercap and dsniff provide tools for authorized network security testing.
