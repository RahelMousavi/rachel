
# Introduction to Network Sniffing

## What Is Network Sniffing?

Network sniffing is the process of capturing and monitoring data packets traveling across a network.

A **sniffer** is a hardware or software tool that captures network traffic and allows it to be analyzed.

Sniffing has legitimate uses, such as:

- Network troubleshooting.
- Monitoring network performance.
- Detecting suspicious activities.
- Analyzing communication protocols.
- Identifying network problems.

However, attackers may use sniffing to intercept sensitive information, especially when communication is not encrypted.

## Network Sniffing Threats

Sniffing can expose sensitive information when network traffic is transmitted without proper encryption.

Potentially exposed information includes:

- Usernames and passwords.
- Session cookies and authentication tokens.
- Emails and messages.
- Confidential business information.
- Network configuration details.

Protocols that transmit information in plaintext are particularly vulnerable.

Examples include:

- HTTP
- FTP
- Telnet
- Older versions of POP3 and IMAP

Modern alternatives such as HTTPS, SFTP, and SSH use encryption to protect transmitted data.

**Important:** Encryption does not prevent packet capture. It protects the captured data from being easily understood by unauthorized parties.

## How Does a Sniffer Work?

A network sniffer uses a network interface card (NIC) to capture packets traveling through the network.

The captured packets can then be inspected to identify:

- Source and destination addresses.
- Communication protocols.
- Port numbers.
- Packet contents, when accessible.
- Communication patterns.

A NIC can operate in different modes. One important mode for packet capture is **Promiscuous Mode**.

## Promiscuous Mode

Promiscuous Mode is a setting that allows a network interface card to accept Ethernet frames that are not necessarily addressed to its own MAC address.

In normal operation, a NIC generally processes frames addressed to its MAC address, broadcast frames, and relevant multicast traffic.

In promiscuous mode, the NIC can also pass other frames it receives to the operating system for analysis.

However, enabling promiscuous mode does not automatically allow a device to capture all traffic on a switched network. The traffic must first be made visible to that interface, for example through a network TAP or a configured SPAN port.

## Related Links

- [Wireshark - About](https://www.wireshark.org/)
- [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
- [RFC 9110 - HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [RFC 8446 - TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446)

## Summary

Network sniffing involves capturing and analyzing packets transmitted across a network. It is useful for troubleshooting and security monitoring, but attackers can exploit it to collect sensitive information. Promiscuous mode allows a NIC to accept frames beyond those addressed directly to it, although it does not bypass network switching or encryption.
