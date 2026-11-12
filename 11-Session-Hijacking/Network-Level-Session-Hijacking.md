
# 03 — Network-Level Session Hijacking

## 1. Introduction

**Network-Level Session Hijacking** is a technique designed to compromise communication at the network and transport protocol levels.

Through these attacks, an attacker attempts to collect sensitive information or take control of communication between systems.

The course introduces the following types of Network-Level Session Hijacking:

- TCP/IP Hijacking
- RST Hijacking
- Blind Hijacking
- Man-in-the-Middle (Packet Sniffing)
- UDP Hijacking
- PetitPotam Hijacking

## 2. TCP Three-Way Handshake

Before understanding TCP session hijacking, it is important to understand how a TCP connection is established.

TCP uses a process called the **Three-Way Handshake** to establish a connection between a client and a server.

The process consists of three steps:

### Step 1: SYN

The client sends a SYN packet to the server to request a connection.

### Step 2: SYN-ACK

The server responds with a SYN-ACK packet, acknowledging the client's request and providing its own initial sequence number.

### Step 3: ACK

The client sends an ACK packet to acknowledge the server's response.

After these three steps, the TCP connection is established.

### Sequence Numbers and Session Hijacking

TCP uses sequence numbers and acknowledgment numbers to keep track of transmitted data.

According to the course, if an attacker can predict the next sequence number and the number of ACKs sent by a legitimate client, the attacker may spoof the client's address and attempt to communicate with the server.

## 3. TCP/IP Hijacking

**TCP/IP Hijacking** is a technique in which an attacker uses forged packets to take control of communication between a victim and a host machine.

In this attack:

- The victim's connection is suspended.
- The attacker attempts to communicate with the host instead of the victim.
- The attacker sends packets that appear to belong to the legitimate communication.

According to the course, the attacker must be on the same network as the victim to perform this type of TCP/IP session hijacking.

## 4. RST Hijacking

**RST Hijacking** involves injecting a forged TCP Reset (RST) packet into an existing communication.

The attack follows these general stages:

1. The attacker sniffs the communication between the source and the victim.
2. The attacker collects connection information, such as source and destination IP addresses and sequence-related information.
3. The attacker forges the source address and attempts to predict the appropriate ACK number.
4. The attacker injects an RST packet into the communication.

If the ACK number is accepted, the victim's system may believe that the original source sent the reset packet and terminate the connection.

The main objective of this attack is to reset an established connection.

## 5. Blind Hijacking

**Blind Hijacking** is a technique in which an attacker injects malicious data or commands into an existing TCP session without being able to observe the server's responses.

To perform this attack, the attacker must correctly predict the **Initial Sequence Number (ISN)**.

After predicting the required sequence information, the attacker may attempt to inject data into the session.

The course gives examples of injected data such as:

- Commands to change a password.
- Commands intended to obtain remote access to a system.

### Main Limitation

The attacker cannot directly observe the server's response.

This makes Blind Hijacking more difficult because the attacker does not know whether the injected data was successfully processed.

## 6. Man-in-the-Middle: Packet Sniffing

**Man-in-the-Middle (MitM)** is a type of attack in which an attacker positions themselves between two communicating systems.

The attacker may intercept and inspect packets exchanged between the two parties.

In the context of session hijacking, packet sniffing can be used to obtain sensitive session information.

The course lists Man-in-the-Middle packet sniffing as one of the Network-Level Session Hijacking techniques.

## 7. UDP Hijacking

**UDP Hijacking** targets communication that uses the User Datagram Protocol (UDP).

Unlike TCP, UDP:

- Does not establish a connection before sending data.
- Does not use TCP-style sequence numbers and acknowledgment-based synchronization.
- Does not guarantee packet delivery or ordering.

Because UDP is connectionless, session manipulation can be easier in some scenarios.

According to the course, an attacker may sniff network traffic and forge a response to a client's UDP request before the legitimate server responds.

If the client accepts the forged response, the attacker may gain control over the communication.

## 8. PetitPotam Hijacking

**PetitPotam** is an attack technique that can force a Domain Controller (DC) to initiate NTLM authentication with an attacker-controlled server.

The course describes the use of the **MS-EFSRPC** protocol to trigger this authentication process.

### How PetitPotam Works

According to the course, the attack involves the following stages:

1. The attacker has valid credentials belonging to a network member.
2. The attacker uses MS-EFSRPC to trigger an authentication request from the Domain Controller.
3. The attacker configures an SMB server to receive the authentication attempt.
4. The Domain Controller initiates NTLM authentication with the attacker's server.
5. The attacker captures the NTLM authentication material.
6. The captured material may be relayed to Active Directory Certificate Services (AD CS).
7. Under vulnerable configurations, the attacker may obtain a certificate and use it to gain administrative access to the Domain Controller.

### Important Components

- **NTLM:** A Microsoft authentication protocol.
- **MS-EFSRPC:** A Microsoft protocol related to the Encrypting File System.
- **SMB:** A network protocol used for file and resource sharing.
- **Domain Controller (DC):** A server responsible for authentication and directory services in an Active Directory environment.
- **Active Directory Certificate Services (AD CS):** A Windows Server role used to issue and manage digital certificates.

PetitPotam is particularly relevant to Windows Active Directory environments where NTLM relay and certificate service configurations are vulnerable.

## Summary

Network-Level Session Hijacking targets communication at the network and transport layers.

The main techniques covered in this section are:

- **TCP Three-Way Handshake:** Establishes TCP connections using SYN, SYN-ACK, and ACK packets.
- **TCP/IP Hijacking:** Uses forged packets to take control of an existing connection.
- **RST Hijacking:** Injects forged TCP Reset packets to terminate a connection.
- **Blind Hijacking:** Injects data into a TCP session without observing server responses.
- **Man-in-the-Middle:** Intercepts communication between two systems.
- **UDP Hijacking:** Uses forged UDP responses to interfere with client-server communication.
- **PetitPotam:** Abuses authentication mechanisms in vulnerable Windows environments to trigger NTLM authentication and potentially enable relay attacks.

## Related Links

- [RFC 9293 — Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293)
- [Wireshark — User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
- [Microsoft — MS-EFSRPC Protocol Specification](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-efsrpc/)
- [Microsoft — Active Directory Certificate Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-cs/active-directory-certificate-services-overview)
- [MITRE ATT&CK — Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557/)
