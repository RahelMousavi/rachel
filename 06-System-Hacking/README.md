
# Module 06: System Hacking

## Overview

System Hacking is a phase of the Certified Ethical Hacker (CEH) methodology that focuses on understanding how attackers gain access to computer systems, obtain higher privileges, maintain access, and hide their activities.

After completing Footprinting, Scanning, Enumeration, and Vulnerability Analysis, an attacker may attempt to exploit identified weaknesses to compromise a target system.

This module explores common system hacking techniques, authentication mechanisms, password attacks, privilege escalation, malware, and methods used to hide evidence of system compromise.

## CEH Hacking Methodology

System Hacking is part of the CEH Hacking Methodology (CHM) and includes four major stages:

1. **Gaining Access:** Obtaining unauthorized access to a target system by exploiting vulnerabilities or cracking passwords.
2. **Escalating Privileges:** Increasing access privileges to gain the permissions of another user or an administrator.
3. **Maintaining Access:** Establishing ways to retain access to a compromised system.
4. **Covering Tracks:** Hiding evidence of malicious activities to avoid detection.

## Main Topics

### 1. System Hacking Goals

Understand the objectives of system hacking and the techniques attackers may use at different stages, including gaining access, escalating privileges, executing applications, hiding files, and covering tracks.

### 2. Microsoft Authentication

Explore how Microsoft Windows handles authentication and stores user credentials.

Topics include:

- Security Account Manager (SAM) Database
- LAN Manager (LM) Hash
- NTLM Authentication
- Kerberos Authentication
- Password Hash Storage
- Password Salting

### 3. Password Cracking

Learn about common password attacks and techniques used to obtain or recover passwords.

Topics include:

- Types of Password Attacks
- Passive Online Attacks
- Active Online Attacks
- Offline Attacks
- Non-Electronic Attacks
- Dictionary Attacks
- Brute Force Attacks
- Rule-Based Attacks
- Rainbow Table Attacks
- Password Cracking Tools

### 4. Privilege Escalation

Understand how attackers attempt to obtain higher permissions on a compromised system.

This stage focuses on exploiting weaknesses to gain additional privileges, potentially reaching administrator-level access.

### 5. Executing Applications

Explore how attackers may execute applications or malicious programs on compromised systems to maintain access or perform unauthorized activities.

Topics include malicious applications, Trojans, spyware, backdoors, and keyloggers.

### 6. Keyloggers and Spyware

Understand how malicious software can monitor user activities and collect sensitive information.

Topics include:

- Software and Hardware Keyloggers
- Types of Keyloggers
- Spyware
- Types of Spyware
- Spyware Distribution Methods
- Anti-Keylogger Techniques
- Spyware Detection and Prevention

### 7. Hiding Files

Explore techniques used to conceal malicious files and activities on compromised systems.

Topics include:

- Rootkits
- File Hiding Techniques
- Steganography
- Steganography Detection Tools

### 8. Covering Tracks

Learn how attackers attempt to remove or hide evidence of their activities after compromising a system.

Topics include:

- Clearing and Manipulating Logs
- Disabling Auditing
- Disabling Last Access Timestamps
- Disabling Windows Hibernation
- Windows Prefetch
- Covering Tracks on Linux
- Covering Tracks on Windows
- Covering Tracks Tools

## Learning Objectives

By completing this module, you should be able to:

- Understand the main stages and goals of system hacking.
- Explain Windows authentication mechanisms and password hash storage.
- Identify different types of password attacks.
- Understand common password cracking techniques and tools.
- Explain the purpose of privilege escalation.
- Recognize the role of Trojans, spyware, and keyloggers in system compromise.
- Understand rootkits and file-hiding techniques.
- Explain how steganography can be used to conceal information.
- Understand how system logs and auditing mechanisms help detect suspicious activities.
- Identify defensive techniques for protecting systems against system hacking.

## Summary

System Hacking explores the techniques used to compromise computer systems and the different stages involved in maintaining control over them.

The four main stages are:

- **Gaining Access:** Breaking through system security controls.
- **Escalating Privileges:** Obtaining higher-level permissions.
- **Maintaining Access:** Retaining access to a compromised system.
- **Covering Tracks:** Concealing evidence of unauthorized activities.

Understanding these techniques is essential for ethical hackers and security professionals because it helps them recognize attack methods, assess system security, and implement appropriate defensive measures.

## Related Links

### Windows Authentication and Security
- [Microsoft Security Documentation](https://learn.microsoft.com/en-us/windows/security/)
- [Microsoft Authentication Documentation](https://learn.microsoft.com/en-us/windows-server/security/windows-authentication/)
- [Microsoft Kerberos Authentication](https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview)

### Password Security and Cracking
- [John the Ripper](https://www.openwall.com/john/)
- [Ophcrack](https://ophcrack.sourceforge.io/)
- [Hashcat](https://hashcat.net/hashcat/)
- [RainbowCrack](https://project-rainbowcrack.com/)
- [Have I Been Pwned](https://haveibeenpwned.com/)

### Malware, Rootkits, and Keyloggers
- [MITRE ATT&CK](https://attack.mitre.org/)
- [MITRE ATT&CK – Credential Access](https://attack.mitre.org/tactics/TA0006/)
- [MITRE ATT&CK – Persistence](https://attack.mitre.org/tactics/TA0003/)
- [Microsoft Defender](https://www.microsoft.com/en-us/security/business/endpoint-security/microsoft-defender-endpoint)

### Steganography
- [Steghide](https://steghide.sourceforge.net/)
- [Stegseek](https://github.com/RickdeJager/stegseek)

### System Monitoring and Forensics
- [Windows Event Logging](https://learn.microsoft.com/en-us/windows/win32/eventlog/event-logging)
- [Sysinternals Suite](https://learn.microsoft.com/en-us/sysinternals/)
- [Autopsy Digital Forensics](https://www.autopsy.com/)
- [NIST Computer Forensics Resources](https://www.nist.gov/itl/ssd/software-quality-group/computer-forensics-tool-testing-program-cftt)
