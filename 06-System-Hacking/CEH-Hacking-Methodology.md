
# CEH Hacking Methodology (CHM)

The CEH Hacking Methodology (CHM) describes the different phases of an ethical hacking process, from gathering information about a target to gaining access and covering tracks.

The methodology shown in the diagram consists of the following phases:

## 1. Footprinting

Footprinting is the process of collecting information about a target system or organization.

It helps identify potential targets, network information, and other details that may be useful during later stages of an assessment.

## 2. Scanning

Scanning involves examining the target's network and systems to discover active hosts, open ports, running services, and potential weaknesses.

The information collected helps identify possible entry points.

## 3. Enumeration

Enumeration is the process of extracting additional information from target systems and services.

It may reveal details such as usernames, network resources, system information, and available services.

## 4. Vulnerability Analysis

Vulnerability Analysis involves identifying and evaluating security weaknesses discovered during previous phases.

The results help determine which vulnerabilities may be exploited during the next stage.

## 5. System Hacking

System Hacking is the phase in which an attacker attempts to gain access to a target system, increase privileges, maintain access, and cover their activities.

According to the diagram, this phase contains four main stages:

### 5.1 Gaining Access

The attacker attempts to obtain initial access to the target system by exploiting identified weaknesses.

The diagram highlights two activities:

- **Cracking Passwords:** Attempting to discover or recover passwords to gain unauthorized access.
- **Vulnerability Exploitation:** Taking advantage of security vulnerabilities to access a system or execute unauthorized actions.

### 5.2 Escalating Privileges

After gaining access, an attacker attempts to obtain higher privileges within the target system.

The objective is to move from a limited account to an account with greater permissions, potentially administrator or root access.

### 5.3 Maintaining Access

After obtaining access, an attacker may attempt to retain access to the compromised system.

The diagram identifies two activities:

- **Executing Applications:** Running applications or programs on the target system.
- **Hiding Files:** Concealing files to make malicious activities or tools less noticeable.

### 5.4 Clearing Logs

This stage involves attempting to remove or alter evidence of activities performed on the target system.

The diagram identifies:

- **Covering Tracks:** Hiding traces of unauthorized activities to make detection and investigation more difficult.

---

## Summary

The CEH Hacking Methodology describes the major phases of an ethical hacking process:

1. **Footprinting:** Collecting information about the target.
2. **Scanning:** Discovering active systems, ports, and services.
3. **Enumeration:** Extracting detailed information from target systems.
4. **Vulnerability Analysis:** Identifying and evaluating security weaknesses.
5. **System Hacking:** Attempting to gain access, escalate privileges, maintain access, and cover tracks.

System Hacking consists of four main stages:

- **Gaining Access:** Through password cracking and vulnerability exploitation.
- **Escalating Privileges:** Obtaining higher access permissions.
- **Maintaining Access:** Executing applications and hiding files.
- **Clearing Logs:** Covering tracks to conceal activities.

**Key Point:** System Hacking follows the initial information-gathering and vulnerability analysis phases. In ethical hacking, these activities must be performed within an authorized and controlled scope.

## Related Links

- [EC-Council – Certified Ethical Hacker (CEH)](https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/)
- [MITRE ATT&CK – Credential Access](https://attack.mitre.org/tactics/TA0006/)
- [MITRE ATT&CK – Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)
- [MITRE ATT&CK – Persistence](https://attack.mitre.org/tactics/TA0003/)
- [MITRE ATT&CK – Defense Evasion](https://attack.mitre.org/tactics/TA0005/)
- [MITRE ATT&CK – Indicator Removal](https://attack.mitre.org/techniques/T1070/)
- [NIST – Technical Guide to Information Security Testing and Assessment](https://csrc.nist.gov/pubs/sp/800/115/final)
