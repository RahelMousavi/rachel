# MITRE ATT&CK Framework

## 1. Overview

**MITRE ATT&CK** is a globally recognized cybersecurity framework that documents and categorizes the behaviors, techniques, and procedures used by attackers in real-world cyberattacks.

ATT&CK stands for:
**Adversarial Tactics, Techniques, and Common Knowledge**
The framework helps security professionals understand attacker behavior, analyze cyberattacks, identify potential threats, and improve defensive strategies.
Unlike the Cyber Kill Chain, which describes an attack as a sequence of stages, MITRE ATT&CK provides a structured knowledge base of attacker behaviors and does not require attacks to follow a fixed sequence.

## 2. Structure of MITRE ATT&CK

The framework is built around three main concepts:

### 2.1 Tactics

**Tactics** represent the attacker's goals or objectives. They explain why an attacker performs a particular action.

### 2.2 Techniques

**Techniques** describe the methods attackers use to achieve their tactical objectives. They explain how an attacker performs an action.

### 2.3 Procedures

**Procedures** describe how an attacker implements a specific technique in a real-world attack.

**Example:**

- **Tactic:** Initial Access
- **Technique:** Drive-by Compromise
- **Procedure:** Using a compromised website containing malicious content to compromise visitors' systems.

## 3. Enterprise ATT&CK Tactics

The Enterprise ATT&CK Matrix contains 14 tactics that represent the different objectives attackers may pursue during an attack.

1. **Reconnaissance:** Gathering information about a target before an attack.
2. **Resource Development:** Acquiring or creating resources needed to support an attack.
3. **Initial Access:** Gaining an initial entry point into a target system or network.
4. **Execution:** Running malicious code or commands on a target system.
5. **Persistence:** Maintaining access to a compromised system.
6. **Privilege Escalation:** Obtaining higher levels of access or permissions.
7. **Defense Evasion:** Avoiding or bypassing security mechanisms.
8. **Credential Access:** Obtaining account credentials, such as passwords.
9. **Discovery:** Gathering information about internal systems, networks, and resources.
10. **Lateral Movement:** Moving through a network to access other systems.
11. **Collection:** Gathering information and data of interest.
12. **Command and Control (C2):** Communicating with and controlling compromised systems remotely.
13. **Exfiltration:** Transferring collected data outside the target environment.
14. **Impact:** Disrupting, damaging, or manipulating systems and data.

## 4. PRE-ATT&CK and Enterprise ATT&CK

In older representations, MITRE ATT&CK was divided into two main sections:

### 4.1 PRE-ATT&CK

Covered activities performed before an attacker gained access to the target, such as:

- **Recon:** Gathering information about the target.
- **Weaponize:** Preparing malicious tools or payloads for an attack.

### 4.2 Enterprise ATT&CK

Focused on attacker behaviors and techniques used during attacks against enterprise environments.
**Note:** PRE-ATT&CK was integrated into the Enterprise ATT&CK framework in newer versions. Its activities are now represented through tactics such as Reconnaissance and Resource Development.

## 5. Understanding the ATT&CK Matrix

The MITRE ATT&CK Matrix organizes attacker behaviors into columns and techniques.

- **Columns:** Represent Tactics and describe the attacker's objectives.
- **Techniques:** Describe the methods used to achieve those objectives.
- **Procedures:** Describe how specific techniques are implemented in real-world attacks.

For example, **Drive-by Compromise** is a technique associated with the **Initial Access** tactic.

## 6. Summary

MITRE ATT&CK is a knowledge base used to understand, classify, and analyze adversary behavior.
Its three main components are:

- **Tactics:** Why an attacker performs an action.
- **Techniques:** How an attacker achieves an objective.
- **Procedures:** How a technique is implemented in a specific attack.

The framework helps security professionals analyze attacks, identify attacker techniques, improve threat detection, and develop effective defensive strategies.
