
# Password Cracking

## What is Password Cracking?

Password cracking is the process of recovering or discovering passwords used to access computer systems, applications, and accounts.

Attackers use different techniques to obtain passwords or authentication credentials and gain unauthorized access to vulnerable systems.

Password cracking is also an important part of authorized security assessments because it helps identify weak passwords and evaluate an organization's authentication security.

Most password-cracking attacks are successful because users choose passwords that are weak, predictable, or easy to guess.

## Types of Password Attacks

Password attacks are classified into four main categories based on how attackers obtain or exploit authentication information:

1. Passive Online Attacks
2. Active Online Attacks
3. Offline Attacks
4. Non-Electronic Attacks

## 1. Passive Online Attacks

Passive online attacks involve monitoring or capturing network communication to obtain authentication-related information.

The attacker generally observes communication without directly modifying the transmitted data.

### Wire Sniffing

Wire Sniffing involves capturing and analyzing network traffic to identify sensitive information, including authentication credentials.

On older hub-based networks, traffic could be visible to other connected devices. On modern switched networks, capturing another device's unicast traffic generally requires access to an appropriate capture point or additional techniques.

Network analysis tools such as Wireshark can be used to inspect captured traffic.

### Man-in-the-Middle (MITM)

A Man-in-the-Middle attack occurs when an attacker positions themselves between two communicating parties and intercepts their communication.

Depending on the circumstances, the attacker may be able to capture sensitive information, including authentication data, or manipulate transmitted messages.

### Replay Attack

In a Replay Attack, an attacker captures previously transmitted authentication data or network packets and retransmits them later to attempt to gain unauthorized access.

Protocols can defend against replay attacks through mechanisms such as:
- Nonces
- Timestamps
- Challenge-response authentication
- Session-specific tokens

## 2. Active Online Attacks

Active online attacks involve directly interacting with a target system or manipulating its authentication process.

Unlike passive attacks, these techniques may involve sending authentication requests, executing malicious software, or modifying network communication.

### Password Guessing

Password Guessing involves attempting to authenticate using passwords that are likely to be used by the target.

Attackers may use:
- Common passwords.
- Personal information.
- Birthdays and names.
- Predictable password patterns.
- Previously exposed credentials.

### Trojan, Spyware, and Keylogger

Attackers may use malicious software to collect credentials from compromised systems.

- **Trojan:** Malicious software disguised as legitimate software that can provide unauthorized access or perform harmful activities.
- **Spyware:** Software designed to secretly monitor user activities and collect information.
- **Keylogger:** A tool or program that records keystrokes, potentially capturing usernames and passwords.

### Hash Injection / Pass-the-Hash

Pass-the-Hash is an authentication attack in which an attacker uses a captured password hash instead of recovering the original plaintext password.

In certain Windows authentication environments, the attacker can use the hash to authenticate as the compromised user.

This technique is particularly associated with NTLM authentication.

### LLMNR/NBT-NS Poisoning

LLMNR (Link-Local Multicast Name Resolution) and NBT-NS (NetBIOS Name Service) are name-resolution mechanisms used in Windows networks.

An attacker may respond to name-resolution requests by impersonating the requested system or service.

This can cause clients to send authentication attempts to the attacker's machine, potentially exposing NetNTLM challenge-response data.

The captured data may then be used in offline password-cracking attempts or other credential attacks.

## 3. Offline Attacks

Offline attacks take place outside the target's live authentication process.

Instead of repeatedly communicating with the target system, attackers work with previously obtained password hashes or authentication data.

### Rainbow Table Attack

A Rainbow Table Attack uses precomputed tables containing password-hash relationships to help recover plaintext passwords from captured hashes.

Rainbow Tables are particularly effective against unsalted password hashes.

Password salting significantly reduces their effectiveness because each unique salt requires separate precomputation.

## 4. Non-Electronic Attacks

Non-Electronic Attacks do not primarily depend on exploiting computer systems or network protocols.

Instead, attackers use observation, deception, or physical access to obtain passwords and other sensitive information.

### Shoulder Surfing

Shoulder Surfing involves observing a user while they enter sensitive information, such as a password or PIN.

An attacker may physically stand nearby or use a camera to observe the victim's keyboard or screen.

### Social Engineering

Social Engineering manipulates people into revealing confidential information or performing actions that compromise security.

For example, an attacker may impersonate technical support and convince an employee to disclose their login credentials.

### Dumpster Diving

Dumpster Diving involves searching discarded documents, storage devices, or other waste for sensitive information.

Discarded papers may contain usernames, passwords, network information, or other confidential data.

---

## Summary

Password attacks are classified into four main categories:

- **Passive Online Attacks:** Capture or observe network communication. Examples include Wire Sniffing, MITM, and Replay Attacks.
- **Active Online Attacks:** Directly interact with or manipulate systems and authentication processes. Examples include Password Guessing, Pass-the-Hash, and LLMNR/NBT-NS Poisoning.
- **Offline Attacks:** Use previously obtained hashes or authentication data without interacting with the target's live authentication service. Rainbow Table Attacks are one example.
- **Non-Electronic Attacks:** Obtain credentials through physical observation, deception, or discarded information. Examples include Shoulder Surfing, Social Engineering, and Dumpster Diving.

**Key Point:** Password attacks are not limited to cracking password hashes. Credentials can also be captured from network traffic, obtained through malware, or collected by manipulating people.

## Related Links

- [MITRE ATT&CK – Credential Access](https://attack.mitre.org/tactics/TA0006/)
- [MITRE ATT&CK – Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557/)
- [MITRE ATT&CK – Brute Force](https://attack.mitre.org/techniques/T1110/)
- [MITRE ATT&CK – Input Capture](https://attack.mitre.org/techniques/T1056/)
- [Wireshark](https://www.wireshark.org/)
- [OWASP – Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
