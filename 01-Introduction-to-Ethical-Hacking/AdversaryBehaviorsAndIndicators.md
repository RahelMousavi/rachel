# Adversary Behavioral Identification

## 1. Overview

**Adversary Behavioral Identification** is the process of identifying and analyzing techniques, activities, and patterns used by attackers during cyberattacks.
By monitoring these behaviors, security professionals can recognize suspicious activities, detect potential threats, identify security incidents, and understand how attackers operate within an organization's network.

## 2. Common Adversary Behaviors and Indicators

### 2.1 Internal Reconnaissance

**Internal Reconnaissance** occurs when an attacker gathers information about an organization's internal network after gaining initial access.

The attacker may identify:

- Internal systems and servers.
- Network structure and connected devices.
- User accounts and access privileges.
- Available resources and services.

### 2.2 Use of Command-Line Interface

Attackers may use the **Command-Line Interface (CLI)** to execute commands, manage systems, collect information, and perform malicious activities.
Command-line tools provide direct access to system functions and can be abused to perform various operations.

### 2.3 Use of DNS Tunneling

**DNS Tunneling** is a technique that uses DNS queries and responses to transfer data or establish communication through DNS traffic.
Attackers may use this technique to communicate with external infrastructure, transfer stolen data, or bypass certain network security restrictions.

### 2.4 Use of PowerShell

**PowerShell** is a command-line shell and scripting language commonly used in Windows environments.
Attackers may abuse PowerShell to execute commands, run malicious scripts, gather information, and perform actions on compromised systems.

### 2.5 HTTP User-Agent

The **HTTP User-Agent** is a field in an HTTP request that provides information about the client making the request, such as its browser, operating system, or application.
Security professionals can analyze User-Agent values to identify unusual requests, automated tools, or suspicious activities.
Attackers may also modify or spoof User-Agent values to disguise their tools or activities.

### 2.6 Use of Web Shell

A **Web Shell** is a malicious script installed on a web server that allows an attacker to execute commands or remotely interact with the compromised server.
Web shells may provide attackers with persistent access and enable further malicious activities.

### 2.7 Unspecified Proxy Activities

Attackers may use proxy servers to route network traffic, hide their original IP addresses, or redirect communications.
Unusual, unauthorized, or suspicious proxy activities may indicate attempts to conceal malicious connections or evade security monitoring.

### 2.8 Command and Control (C2) Server

A **Command and Control (C2) Server** is an external server or infrastructure controlled by an attacker to communicate with compromised systems.
Through C2 communication, attackers may:

- Send commands to compromised devices.
- Remotely control infected systems.
- Receive information from compromised devices.
- Manage malicious activities.

### 2.9 Data Staging

**Data Staging** is the process of collecting and preparing data before transferring it outside a compromised network.
Attackers may gather, organize, compress, or store sensitive information in a specific location before performing data exfiltration.

## 3. Summary

Adversary Behavioral Identification helps security professionals understand attacker activities and recognize suspicious patterns within an organization's network.
The common behaviors and indicators introduced in this section include:

1. Internal Reconnaissance
2. Use of Command-Line Interface
3. Use of DNS Tunneling
4. Use of PowerShell
5. HTTP User-Agent
6. Use of Web Shell
7. Unspecified Proxy Activities
8. Command and Control (C2) Server
9. Data Staging

Monitoring these activities and indicators helps organizations detect malicious behavior, investigate security incidents, and improve their defensive capabilities.
