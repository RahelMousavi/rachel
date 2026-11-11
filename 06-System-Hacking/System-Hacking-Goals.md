
# System Hacking Goals

System Hacking involves several stages, each with a specific objective. Attackers use different techniques and exploits to gain access to a system, increase their privileges, maintain access, hide malicious activities, and conceal evidence of compromise.

The following are the five main stages presented in the course material.

## 1. Gaining Access

**Goal:** Bypass access controls to gain access to the target system.

Attackers attempt to obtain initial access by exploiting weaknesses in authentication mechanisms or system security.

**Techniques / Exploits Used:**
- Password Cracking
- Vulnerability Exploitation
- Social Engineering

## 2. Escalating Privileges

**Goal:** Acquire the rights and permissions of another user or an administrator.

After gaining initial access, an attacker may attempt to obtain higher privileges to access restricted resources and perform actions that are not permitted to a normal user.

**Techniques / Exploits Used:**
- Exploiting Known System Vulnerabilities

## 3. Executing Applications

**Goal:** Create and maintain remote access to the system.

Attackers may execute malicious applications or programs to establish remote access and perform unauthorized operations.

**Techniques / Exploits Used:**
- Trojans
- Spyware
- Backdoors
- Keyloggers

## 4. Hiding Files

**Goal:** Hide attackers' malicious activities and steal data.

Attackers may conceal malicious files, tools, or other traces of their activities to make detection more difficult.

**Techniques / Exploits Used:**
- Rootkits
- Steganography

## 5. Covering Tracks

**Goal:** Hide the evidence of system compromise.

After performing malicious activities, attackers may attempt to remove or modify traces of their actions to avoid detection and make forensic investigations more difficult.

**Techniques / Exploits Used:**
- Clearing Logs

---

## Summary

System Hacking consists of five main stages, each serving a different purpose:

1. **Gaining Access:** Bypassing access controls using password cracking, vulnerability exploitation, or social engineering.
2. **Escalating Privileges:** Obtaining higher permissions by exploiting known system vulnerabilities.
3. **Executing Applications:** Establishing or maintaining remote access using Trojans, spyware, backdoors, and keyloggers.
4. **Hiding Files:** Concealing malicious activities and files using rootkits and steganography.
5. **Covering Tracks:** Hiding evidence of compromise by clearing logs.

**Key Point:** Remember the difference between the last three stages:
- Executing Applications focuses on creating and maintaining access.
- Hiding Files focuses on concealing malicious activities and files.
- Covering Tracks focuses on removing evidence of compromise.

## Related Links

### Gaining Access
- [MITRE ATT&CK – Credential Access](https://attack.mitre.org/tactics/TA0006/)
- [MITRE ATT&CK – Phishing](https://attack.mitre.org/techniques/T1566/)
- [OWASP – Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

### Privilege Escalation
- [MITRE ATT&CK – Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)
- [MITRE ATT&CK – Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068/)

### Malicious Applications
- [MITRE ATT&CK – Execution](https://attack.mitre.org/tactics/TA0002/)
- [MITRE ATT&CK – Persistence](https://attack.mitre.org/tactics/TA0003/)
- [MITRE ATT&CK – Remote Access Software](https://attack.mitre.org/techniques/T1219/)

### Hiding Files and Covering Tracks
- [MITRE ATT&CK – Rootkit](https://attack.mitre.org/techniques/T1014/)
- [MITRE ATT&CK – Steganography](https://attack.mitre.org/techniques/T1027/003/)
- [MITRE ATT&CK – Indicator Removal](https://attack.mitre.org/techniques/T1070/)
