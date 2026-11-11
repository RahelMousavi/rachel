# CEH Ethical Hacking Framework

## 1. Overview

The **CEH Ethical Hacking Framework** provides a structured approach to conducting ethical hacking and security assessments.
It introduces the main phases of ethical hacking, different security testing domains, commonly used tools, and techniques that attackers may use.
The framework consists of five main phases and several supporting components, including reconnaissance, vulnerability analysis, ethical hacking tools, domains, and TTPs.

## 2. Phases of Ethical Hacking

The framework consists of five main phases:

### 2.1 Phase 1: Reconnaissance

**Reconnaissance** is the process of collecting information about the target before conducting security tests.
The objective is to understand the target environment, identify potential entry points, and gather information about its systems and network infrastructure.

### 2.2 Phase 2: Vulnerability Scanning

**Vulnerability Scanning** involves examining systems and networks to identify potential security weaknesses.
This phase may include identifying:

- Open ports.
- Running services.
- Outdated software.
- Known vulnerabilities.
- Security misconfigurations.

### 2.3 Phase 3: Gaining Access

**Gaining Access** involves attempting to access target systems by exploiting identified vulnerabilities within the authorized scope of testing.
The objective is to evaluate whether security weaknesses can be exploited to gain unauthorized access.

### 2.4 Phase 4: Maintaining Access

**Maintaining Access** focuses on evaluating whether an attacker could maintain access to a compromised system.
This phase examines techniques that may allow an attacker to retain access or regain access after the initial compromise.

### 2.5 Phase 5: Clearing Tracks

**Clearing Tracks** refers to techniques attackers use to hide their activities and remove evidence of their presence.
This may involve manipulating or deleting logs and other traces of malicious activity.
During ethical hacking, these techniques should only be simulated and documented. Actual logs and evidence must be handled according to the agreed testing rules.

## 3. Ethical Hacking Process

An ethical hacking assessment generally involves the following activities:

### 3.1 Footprinting and Reconnaissance

Collecting information about the target organization, systems, network infrastructure, and potential attack surfaces.

### 3.2 Scanning and Enumeration

Identifying active hosts, open ports, running services, and additional information about target systems and networks.

### 3.3 Vulnerability Analysis

Analyzing collected information to identify potential vulnerabilities and evaluate their severity and impact.

## 4. Ethical Hacking Domains

Ethical hacking covers several domains, each focusing on a different area of technology.

- **System Hacking:** Testing the security of operating systems and servers.
- **Web Application Hacking:** Identifying vulnerabilities in web applications.
- **Network Hacking:** Assessing the security of networks and network devices.
- **Mobile Hacking:** Testing the security of mobile operating systems and applications.
- **Wireless Hacking:** Evaluating the security of wireless networks and communication protocols.
- **OT/IoT Hacking:** Assessing the security of Operational Technology (OT) systems and Internet of Things (IoT) devices.
- **Cloud Hacking:** Evaluating the security of cloud infrastructure and services.
- **Hacking AI:** Identifying security weaknesses and threats related to Artificial Intelligence systems.

## 5. Ethical Hacking Tools

Ethical hackers use different tools to perform security assessments.

- **Nmap:** A network scanning tool used to discover hosts, scan ports, and identify running services.
- **Wireshark:** A network protocol analyzer used to capture and inspect network traffic.
- **Burp Suite:** A platform used to test web application security and identify vulnerabilities.
- **Metasploit:** A penetration testing framework used to develop, test, and execute exploits.
- **SET (Social Engineering Toolkit):** A toolkit used to simulate and assess social engineering attacks.
- **AI (Artificial Intelligence):** AI-based technologies can assist with information analysis, pattern recognition, and various security activities.

## 6. Ethical Hacking TTPs

**TTP** stands for:

- **Tactics:** The objectives or goals an attacker wants to achieve.
- **Techniques:** The methods used to achieve those objectives.
- **Procedures:** The specific ways and steps used to perform those techniques.

Common techniques and activities include:

- **Password Cracking:** Recovering or discovering passwords using different techniques.
- **Malware:** Using malicious software to steal information, damage systems, or gain unauthorized access.
- **Social Engineering:** Manipulating or deceiving people into revealing sensitive information or providing access.
- **Brute Forcing:** Repeatedly trying different password combinations or possible values until the correct one is found.
- **DoS/DDoS:** Attacks designed to disrupt the availability of systems or services.
- **Privilege Escalation:** Gaining higher levels of access or permissions within a system.
- **SQL Injection:** Injecting malicious SQL statements into applications that do not properly validate user input.
- **Sniffing:** Capturing and analyzing network traffic to collect information.
- **AI:** Using artificial intelligence in attack-related activities or security assessments.
- **Session Hijacking:** Taking control of an active user session to gain unauthorized access.
- **Cryptanalysis:** Analyzing cryptographic algorithms and systems to identify weaknesses.

## 7. Summary

The CEH Ethical Hacking Framework provides a structured approach to understanding and performing security assessments.

Its five main phases are:

1. Reconnaissance
2. Vulnerability Scanning
3. Gaining Access
4. Maintaining Access
5. Clearing Tracks

The framework also introduces different ethical hacking domains, tools, and TTPs used to assess security weaknesses and understand attacker techniques.

Understanding this framework helps ethical hackers organize their testing activities and evaluate the security of different systems and environments.
