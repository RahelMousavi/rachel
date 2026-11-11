
# Password Cracking Tools and Countermeasures

## Password Cracking Tools

Password-cracking tools are software applications used to recover passwords, analyze password hashes, and evaluate password security.

They are commonly used in authorized penetration tests and security assessments to identify weak credentials.

The course introduces several password-cracking tools.

### Tools Listed in the Course

| Tool | Description |
|---|---|
| Pwdump | Extracts password hashes from Windows systems. |
| FGdump | A Windows password-hash extraction utility. |
| L0phtCrack | A password auditing and recovery tool for Windows. |
| Ophcrack | Uses Rainbow Tables to recover Windows passwords from hashes. |
| Cain & Abel | A legacy Windows password recovery and network analysis tool. |
| RainbowCrack | Uses Rainbow Tables for password hash cracking. |
| John the Ripper | A password security auditing and recovery tool. |
| Proactive System Password Recovery | A legacy Windows password recovery utility. |
| Recover Keys | Recovers product keys and certain stored credentials. |
| WinPassword | A Windows password recovery utility. |
| Windows Password Reset Professional | A Windows password reset and recovery product. |
| Windows Password Cracker | A legacy password recovery tool. |
| LCP | A Windows password auditing tool. |
| PasswordsPro | A password recovery and auditing utility. |
| LSASecretsView | Displays secrets stored in the Windows LSA area. |
| RockXP | A legacy Windows password and product-key recovery utility. |
| Windows Password Unlocker | A Windows password reset utility. |
| KrbGuess | A tool name listed in the course material; verify its current availability and documentation before use. |
| Password Kit Enterprise | A password recovery product. |
| FlexiSPY Password Grabber | A credential collection product associated with surveillance software. |

### Modern Password Auditing Tools

Some tools listed in the course are outdated or no longer maintained. The following tools are more relevant for learning and authorized security assessments:

#### 1. John the Ripper

John the Ripper is an open-source password security auditing tool.

It supports multiple password hash formats and provides different cracking methods, including:

- Wordlist attacks.
- Incremental (brute-force-style) attacks.
- Rule-based password candidate generation.

Website: [https://www.openwall.com/john/](https://www.openwall.com/john/)

#### 2. Hashcat

Hashcat is an advanced password recovery tool that supports CPU and GPU-based password cracking.

It supports several attack modes, including:

- Straight (Dictionary) Attack.
- Combination Attack.
- Brute-Force Attack.
- Hybrid Attack.
- Rule-Based Attack.

Website: [https://hashcat.net/hashcat/](https://hashcat.net/hashcat/)

#### 3. Ophcrack

Ophcrack is a Windows password recovery tool based on Rainbow Tables.

It was designed primarily for recovering Windows passwords from password hashes.

Website: [https://ophcrack.sourceforge.io/](https://ophcrack.sourceforge.io/)

**Note:** Ophcrack and several other tools in the original course list are legacy tools. Their suitability depends on the operating system and hash format being tested.

## How to Defend Against LLMNR/NBT-NS Poisoning

LLMNR and NBT-NS Poisoning attacks exploit local name-resolution mechanisms to capture authentication-related information.

The following defensive measures help reduce the risk:

### 1. Disable LLMNR

LLMNR can be disabled through Windows Group Policy.

The policy is located at:

```text
Computer Configuration
  → Administrative Templates
    → Network
      → DNS Client
        → Turn off multicast name resolution
```

Enabling this policy disables LLMNR on supported Windows systems.

### 2. Disable NBT-NS

If NetBIOS over TCP/IP is not required, it can be disabled through the network adapter's TCP/IP settings.

This reduces the possibility of attacks abusing NetBIOS name resolution.

### 3. Use Secure Name Resolution

Ensure that DNS is properly configured and that systems rely on trusted name-resolution services.

### 4. Restrict NTLM Authentication

Where possible, reduce or disable NTLM authentication and prefer stronger authentication mechanisms such as Kerberos.

### 5. Monitor Network Traffic

Monitor network activity for unusual LLMNR and NBT-NS responses, unexpected authentication requests, and suspicious NTLM challenge-response traffic.

## Countermeasures Against Password Cracking

The following security practices help protect systems against password-cracking attacks.

### 1. Use Strong Passwords

Use long, unique, and unpredictable passwords.

Avoid:
- Common dictionary words.
- Names and birthdays.
- Sequential numbers.
- Repeated characters.
- Passwords based on personal information.

### 2. Use Password Policies

Organizations should establish password policies that encourage strong passwords and prevent the reuse of compromised credentials.

Modern guidance generally favors longer passwords, password blocklists, and changing passwords when compromise is suspected rather than requiring arbitrary frequent changes.

### 3. Monitor Authentication Logs

Monitor authentication logs and security events to detect suspicious login activity.

Pay attention to:
- Repeated failed login attempts.
- Unusual login locations.
- Attempts against multiple accounts.
- Unusual authentication patterns.

### 4. Implement Account Lockout and Rate Limiting

Limit repeated authentication attempts to reduce the effectiveness of online brute-force attacks.

Use carefully configured lockout policies or progressive delays to reduce automated guessing while avoiding unnecessary denial-of-service risks.

### 5. Avoid Default Passwords

Always change default credentials after installing or configuring devices and applications.

### 6. Avoid Sharing Passwords

Passwords should remain confidential and should not be shared between users.

Use individual accounts and appropriate access permissions.

### 7. Use Secure Authentication Protocols

Avoid transmitting credentials through clear-text protocols or protocols that use weak encryption.

Use secure alternatives such as HTTPS, SSH, and other appropriately configured encrypted authentication protocols.

### 8. Use Password Salting

Password storage systems should use a unique salt for each password.

Salting makes precomputed hash attacks, such as Rainbow Table attacks, significantly less effective.

Modern password storage should use dedicated password-hashing algorithms such as Argon2id, bcrypt, or scrypt.

### 9. Enable Multi-Factor Authentication (MFA)

MFA adds an additional authentication factor beyond the password.

Even if an attacker obtains a password, the additional factor can prevent unauthorized access.

---

## Summary

Password-cracking tools are used to audit password security, recover passwords, and analyze stored password hashes.

The course introduces several legacy tools, including Pwdump, FGdump, L0phtCrack, Ophcrack, Cain & Abel, and RainbowCrack. Modern tools such as John the Ripper and Hashcat remain useful for authorized password-security assessments.

Defending against password attacks requires multiple security measures:

- Disable unnecessary LLMNR and NBT-NS services.
- Use strong and unique passwords.
- Monitor authentication logs.
- Implement rate limiting and appropriate account lockout policies.
- Change default credentials.
- Use secure authentication protocols.
- Store passwords using salted, dedicated password-hashing algorithms.
- Enable Multi-Factor Authentication.

**Key Point:** Password security is not achieved by password complexity alone. Secure storage, strong authentication mechanisms, network configuration, monitoring, and user awareness must work together.

## Related Links

- [John the Ripper](https://www.openwall.com/john/)
- [Hashcat](https://hashcat.net/hashcat/)
- [Ophcrack](https://ophcrack.sourceforge.io/)
- [OWASP – Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [OWASP – Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [NIST – Digital Identity Guidelines](https://pages.nist.gov/800-63-4/)
- [Microsoft – Disable LLMNR](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/disable-link-local-multicast-name-resolution)
- [MITRE ATT&CK – Credential Access](https://attack.mitre.org/tactics/TA0006/)
