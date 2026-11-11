
# VoIP Enumeration

## What Is VoIP?

VoIP (Voice over Internet Protocol) is a technology that allows voice and video communication over IP networks instead of traditional telephone networks.

VoIP systems commonly use SIP (Session Initiation Protocol) to establish, manage, and terminate communication sessions.

## SIP (Session Initiation Protocol)

SIP is a signaling protocol used to initiate, modify, and terminate multimedia communication sessions, including voice and video calls.

It helps VoIP devices locate users and establish communication between endpoints.

### Common SIP Ports

- **UDP/TCP 5060:** Commonly used for SIP signaling without TLS encryption.
- **TCP 5061:** Commonly used for SIP signaling over TLS.

The course material also lists ports `2000`, `2001`, and `5050` as VoIP-related ports. However, these are not universal default SIP ports and may be used by specific VoIP applications or implementations.

## VoIP Enumeration

VoIP Enumeration is the process of gathering information about VoIP infrastructure and its components.

An attacker may attempt to identify:

- **IP-PBX Systems:** Private Branch Exchange systems used to manage internal telephone communications.
- **VoIP Gateways:** Devices that connect VoIP networks to traditional telephone networks.
- **VoIP Software:** Applications and platforms used for voice and video communication.
- **VoIP Users:** User accounts and extensions registered in the VoIP system.

## Why Is VoIP Enumeration Important?

Information gathered through VoIP Enumeration can help identify potential weaknesses in communication infrastructure.

It may also reveal exposed services, user extensions, and VoIP components that could become targets for further security assessments.

## Related Links

- [RFC 3261 — SIP: Session Initiation Protocol](https://www.rfc-editor.org/rfc/rfc3261)
- [RFC 3263 — SIP: Locating SIP Servers](https://www.rfc-editor.org/rfc/rfc3263)
- [RFC 5630 — SIP over TLS](https://www.rfc-editor.org/rfc/rfc5630)
- [Wireshark — VoIP Analysis](https://www.wireshark.org/docs/wsug_html_chunked/ChTelVoIP.html)
