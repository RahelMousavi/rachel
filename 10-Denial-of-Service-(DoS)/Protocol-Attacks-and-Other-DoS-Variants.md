
# Protocol Attacks and Other DoS Variants

## Introduction

**Protocol attacks** consume resources within network infrastructure, such as firewalls and load balancers.

These attacks exploit the way network protocols and infrastructure components process packets and maintain connections.

### Measurement

The magnitude of protocol attacks is measured in:

- **PPS (Packets Per Second):** The number of packets transmitted per second.

## 1. SYN Flood Attack

A **SYN Flood** attack exploits the TCP three-way handshake process by creating a large number of incomplete TCP connections.

### How It Works

A normal TCP connection is established through three steps:

1. The client sends a `SYN` packet to the server.
2. The server responds with a `SYN/ACK` packet.
3. The client sends an `ACK` packet to complete the connection.

During a SYN Flood attack:

1. The attacker sends a large number of SYN requests to the target server.
2. The server responds to each request with SYN/ACK.
3. The attacker does not send the final ACK.
4. The server keeps the connections in a pending state.
5. These incomplete connections consume server resources and occupy the connection queue.

If the number of incomplete connections becomes too large, the server may be unable to accept legitimate connections.

## 2. TCP SACK Panic Attack

**TCP SACK Panic** is a remote attack that targets Linux systems.

It attempts to trigger a **Kernel Panic** by sending specially crafted TCP packets containing Selective Acknowledgment (SACK) information and an incorrect Maximum Segment Size (MSS).

### Technical Background

- **SACK (Selective Acknowledgment):** A TCP mechanism that allows a receiver to report which data segments have been successfully received.
- **MSS (Maximum Segment Size):** The maximum amount of TCP data carried in a single segment.
- **SKB (Socket Buffer):** A Linux kernel structure used to manage network packet data.
- **Integer Overflow:** An arithmetic condition in which a calculated value exceeds the range that can be represented by a data type.
- **Kernel Panic:** A critical error that causes the operating system kernel to stop functioning.

According to the course material, Linux uses a linked-list structure to manage data in the socket buffer. The presented example describes a buffer capable of storing up to 17 segments.

### Attack Concept

The course describes the following sequence:

1. Specially crafted SACK packets are sent to the target.
2. The MSS value is set to a very low value, such as 48 bytes.
3. The small MSS increases the number of segments that need to be handled.
4. The socket buffer may be forced to handle more than 17 segments.
5. An integer overflow occurs, potentially resulting in a Kernel Panic.

The course also notes that this vulnerability can affect virtual machines and containers.

## 3. Distributed Reflection DoS (DRDoS)

**Distributed Reflection DoS (DRDoS)**, also called a spoofed attack in the course, uses multiple intermediate systems called **reflectors** to direct malicious traffic toward a primary victim.

The attack uses spoofed source addresses so that the intermediate systems send their responses to the victim instead of the original sender.

### How It Works

The course describes the following process using TCP:

1. The attacker controls compromised systems, also called zombies.
2. These systems send TCP SYN packets to reflector machines.
3. The source IP address of the packets is set to the primary victim's IP address.
4. The reflectors believe that the victim initiated the connection.
5. The reflectors send SYN/ACK responses to the victim.
6. The victim receives responses for connections it did not initiate.
7. Because the victim does not send the expected ACK, the reflectors may retransmit their SYN/ACK responses until their timeout expires.

The large volume of responses can overwhelm the primary victim.

### Main Components

- **Attacker:** Coordinates the attack.
- **Zombies:** Compromised systems used to send spoofed requests.
- **Reflectors:** Intermediate systems that send responses to the spoofed source address.
- **Primary Victim:** The actual target of the attack.

## 4. Permanent Denial of Service (PDoS)

**Permanent Denial of Service (PDoS)**, also known as **phlashing**, is an attack that directly targets hardware and attempts to cause irreversible damage.

Unlike conventional DoS attacks, which generally disrupt system availability or performance, PDoS attacks can damage hardware to the point where replacement or reinstallation is required.

### How It Works

According to the course material:

1. The attacker exploits security weaknesses in a device to gain access to its hardware management interface.
2. The targeted devices may include printers, routers, and other network equipment.
3. The attacker prepares a fake or malicious hardware update.
4. The update is delivered through channels such as email, chat, IRC, social media, or video.
5. The victim clicks a link or pop-up and installs the fake update.
6. The malicious or incomplete firmware damages the device and may make it unusable.

## Techniques Listed but Not Detailed in the Course Slides

The basic attack-vector classification also lists the following protocol attack techniques:

- **Fragmentation Attack**
- **Spoofed Session Flood**

The slides provided for this section identify these techniques but do not explain their mechanisms in detail.

## Summary

- **SYN Flood:** Creates many incomplete TCP connections to consume server resources.
- **TCP SACK Panic:** Exploits a Linux kernel vulnerability involving TCP SACK processing and may cause a Kernel Panic.
- **DRDoS:** Uses reflector systems and spoofed source addresses to direct traffic toward a victim.
- **PDoS:** Attempts to cause permanent hardware damage, commonly through malicious firmware.

## Related Links

- [Cloudflare — SYN Flood DDoS Attack](https://www.cloudflare.com/learning/ddos/syn-flood-ddos-attack/)
- [RFC 2018 — TCP Selective Acknowledgment Options](https://www.rfc-editor.org/rfc/rfc2018)
- [CVE-2019-11477 — TCP SACK Panic](https://nvd.nist.gov/vuln/detail/CVE-2019-11477)
- [Cloudflare — DDoS Attack Types](https://www.cloudflare.com/learning/ddos/ddos-attack-types/)
