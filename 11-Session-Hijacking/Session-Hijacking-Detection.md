
# 05 — Session Hijacking Detection

## 1. Introduction

**Session Hijacking Detection** refers to identifying attempts to compromise or take control of active communication sessions.

The course divides Session Hijacking detection methods into two main categories:

- Manual Method
- Automatic Method

## 2. Manual Detection Method

The manual method involves inspecting network traffic using packet sniffing software.

### Packet Sniffing Software

**Packet Sniffing** is the process of capturing and analyzing network packets exchanged between systems.

Security analysts can use packet sniffing tools to inspect network communication and identify suspicious activity.

For example, they may examine:

- Source and destination IP addresses.
- Network protocols.
- TCP connections and session information.
- Unusual or unexpected network traffic.

The course identifies packet sniffing software as the main tool used in manual detection.

## 3. Automatic Detection Method

The automatic method uses security systems to monitor network activity and identify suspicious behavior.

The course introduces two types of security systems:

### 3.1 Intrusion Detection Systems (IDS)

An **Intrusion Detection System (IDS)** monitors network or system activity to identify suspicious behavior and potential security threats.

When suspicious activity is detected, an IDS generates alerts for security administrators.

Its primary purpose is detection and notification.

### 3.2 Intrusion Prevention Systems (IPS)

An **Intrusion Prevention System (IPS)** monitors network traffic and can take action to prevent detected threats.

Unlike an IDS, which primarily detects and reports suspicious activity, an IPS can actively block malicious traffic.

## 4. Session Hijacking Detection Tools

The course introduces the following tools for detecting Session Hijacking:

### 4.1 Wireshark

**Wireshark** is a network protocol analyzer used to capture and inspect network traffic.

It allows security analysts to examine packets and investigate suspicious communication.

### 4.2 USM Anywhere

**USM Anywhere** is a security monitoring platform developed by AT&T Cybersecurity (formerly AlienVault).

It provides security monitoring and threat detection capabilities.

### 4.3 Quantum IPS

**Quantum IPS** is listed in the course as an intrusion prevention solution.

The slides do not provide additional technical details about this product.

### 4.4 SolarWinds Security Event Manager

**SolarWinds Security Event Manager (SEM)** is a security information and event management solution.

It helps organizations collect, analyze, and monitor security events.

### 4.5 IBM Security Network Intrusion Prevention System

**IBM Security Network Intrusion Prevention System** is listed in the course as a network intrusion prevention solution.

The slides do not provide further technical details.

### 4.6 LogRhythm

**LogRhythm** provides security monitoring and analytics solutions used to identify suspicious activities and investigate security incidents.

## Summary

Session Hijacking detection methods are divided into two main categories:

- **Manual Detection:** Uses packet sniffing software to capture and inspect network traffic.
- **Automatic Detection:** Uses IDS and IPS solutions to identify and respond to suspicious activity.

The tools introduced in the course are:

- Wireshark
- USM Anywhere
- Quantum IPS
- SolarWinds Security Event Manager
- IBM Security Network Intrusion Prevention System
- LogRhythm

## Related Links

- [Wireshark — Official Website](https://www.wireshark.org/)
- [AT&T Cybersecurity — USM Anywhere](https://cybersecurity.att.com/products/usm-anywhere)
- [Check Point — Quantum Security](https://www.checkpoint.com/quantum/)
- [SolarWinds — Security Event Manager](https://www.solarwinds.com/security-event-manager)
- [IBM — Security Products](https://www.ibm.com/security)
- [LogRhythm — Security Operations](https://logrhythm.com/)
