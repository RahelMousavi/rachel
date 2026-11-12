
# Wireshark Protocol Analyzer

## What Is Wireshark?

**Wireshark** is a free and open-source network protocol analyzer used to capture and inspect network packets.

It was previously known as **Ethereal**.

Wireshark is widely used by network administrators, security professionals, and penetration testers for network troubleshooting and traffic analysis.

## Main Features

- Free and open-source.
- Provides a graphical user interface (GUI).
- Supports multiple operating systems.
- Captures live network traffic.
- Analyzes packets across different network protocol layers.
- Supports a wide range of network protocols.
- Provides powerful packet filtering capabilities.

## How Wireshark Works

Wireshark captures packets through a selected network interface and displays information about each packet.

The main steps are:

1. Select a network interface.
2. Start packet capture.
3. Generate or observe network traffic.
4. Stop the capture when needed.
5. Inspect packets and their protocol details.

## Wireshark Interface

The main interface contains three important sections:

### Packet List Pane

Displays captured packets, including information such as:

- Packet number.
- Timestamp.
- Source and destination.
- Protocol.
- Packet length.
- Brief information about the packet.

### Packet Details Pane

Displays the selected packet's protocol layers and fields.

For example, an Ethernet frame containing an IPv4 packet and a TCP segment can be expanded to inspect each layer.

### Packet Bytes Pane

Displays the raw packet data in hexadecimal and ASCII formats.

This is useful for examining the actual bytes transmitted over the network.

## Packet Capture vs. Packet Analysis

Wireshark supports both capturing and analyzing network traffic.

- **Packet Capture:** Collecting packets from a network interface.
- **Packet Analysis:** Examining captured packets to understand communication and identify suspicious behavior.

Wireshark can also open previously saved capture files, such as `.pcap` and `.pcapng`.

## Security Considerations

Wireshark should be kept updated because packet analysis software can contain vulnerabilities in protocol dissectors and other components.

Also, packet captures may contain sensitive information. Store and share capture files carefully.

## Related Links

- [Wireshark Official Website](https://www.wireshark.org/)
- [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
- [Wireshark Download](https://www.wireshark.org/download.html)
- [Wireshark Display Filter Reference](https://www.wireshark.org/docs/dfref/)

## Summary

Wireshark is a free, open-source network protocol analyzer used to capture and inspect network packets. Its packet list, packet details, and packet bytes panes help users understand network communication. Display filters make it easier to locate specific packets during analysis.
