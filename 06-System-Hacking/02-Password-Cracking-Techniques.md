
# Password Cracking Techniques

## Introduction

Password cracking techniques are methods used to discover passwords or recover plaintext passwords from stored hashes.

Different techniques use different approaches to generate and test password candidates.

The three main techniques covered in this section are:

1. Dictionary Attack
2. Brute-Force Attack
3. Rule-Based Attack

## 1. Dictionary Attack

A Dictionary Attack uses a predefined list of words and commonly used passwords to find the correct password.

This list is called a **Wordlist**.

Instead of testing every possible combination, the cracking tool checks password candidates from the prepared wordlist.

### Example

A wordlist may contain:

```text
password
123456
qwerty
admin123
welcome
```

The cracking tool tests each entry against the target password or hash.

### Advantages

- Faster than testing every possible combination.
- Effective against common and weak passwords.
- Can use publicly available or custom wordlists.

### Limitations

- May fail if the password is not included in the wordlist.
- Its effectiveness depends on the quality of the wordlist.

## 2. Brute-Force Attack

A Brute-Force Attack attempts all possible password combinations within a defined character set and length range until the correct password is found.

For example, if a password contains only lowercase letters and has three characters, the attack may test combinations such as:

```text
aaa
aab
aac
aad
...
zzz
```

### Advantages

- Does not depend on a predefined wordlist.
- Can eventually find a password if the entire search space is covered.

### Limitations

- Can require significant time and computational resources.
- Longer passwords increase the number of possible combinations.
- Modern authentication systems may limit repeated login attempts.

### Factors Affecting Brute-Force Attacks

The difficulty of a brute-force attack depends on:

- Password length.
- Character set size.
- Available computational power.
- Password-hashing algorithm.
- Rate limiting and account lockout mechanisms.

## 3. Rule-Based Attack

A Rule-Based Attack uses predefined rules to modify existing words or password candidates.

It is particularly useful when the attacker has some knowledge about the target's password patterns.

Common rules include:

- Capitalizing the first letter.
- Replacing letters with similar-looking numbers or symbols.
- Adding numbers at the end.
- Adding special characters.
- Combining common words with numeric patterns.

### Example

Starting word:

```text
password
```

Possible rule-based variations:

```text
Password
password123
P@ssw0rd
password!
```

### Advantages

- Generates many variations from a relatively small wordlist.
- Can be effective against predictable password patterns.
- Combines the benefits of dictionary-based and pattern-based approaches.

### Limitations

- Depends on the quality of the initial wordlist.
- Effectiveness depends on the selected rules.
- May not discover passwords that do not follow expected patterns.

## Comparison of Password Cracking Techniques

| Technique | Main Approach |
|---|---|
| Dictionary Attack | Tests passwords from a predefined wordlist |
| Brute-Force Attack | Tests possible character combinations |
| Rule-Based Attack | Modifies password candidates using predefined rules |

## LLMNR/NBT-NS Poisoning

### What are LLMNR and NBT-NS?

**LLMNR (Link-Local Multicast Name Resolution)** is a protocol that allows devices on a local network to resolve hostnames when traditional DNS resolution fails.

**NBT-NS (NetBIOS Name Service)** is a name-resolution mechanism used in Windows networks to identify devices and services through NetBIOS names.

Both mechanisms can be abused by attackers to capture authentication-related information.

### How LLMNR/NBT-NS Poisoning Works

LLMNR/NBT-NS Poisoning occurs when an attacker responds to a name-resolution request and falsely claims to be the requested device or service.

The general process is:

1. A user or application attempts to access a network resource using a hostname.
2. The requested hostname cannot be resolved through normal name resolution.
3. The client sends an LLMNR or NBT-NS request to identify the resource.
4. The attacker responds to the request and impersonates the requested host.
5. The victim may attempt to authenticate with the attacker's system.
6. The attacker captures the resulting authentication challenge-response data.

This information may be used in offline password-cracking attempts or other credential attacks.

### Why Is This Attack Dangerous?

- It can expose NetNTLM challenge-response data.
- It may allow attackers to obtain information useful for password cracking.
- It can be exploited in poorly configured Windows networks.
- It may lead to further attacks if captured credentials are weak or reusable.

### How to Defend Against LLMNR/NBT-NS Poisoning

Recommended defensive measures include:

- Disable LLMNR through Group Policy when it is not required.
- Disable NBT-NS where it is not needed.
- Use DNS correctly across the network.
- Restrict or disable NTLM authentication where feasible.
- Monitor network traffic for suspicious name-resolution responses.
- Use strong authentication and appropriate network segmentation.

## Default Passwords

Default passwords are predefined credentials supplied by manufacturers or vendors for devices, applications, and services.

Examples include default credentials used by:

- Routers.
- Network switches.
- Printers.
- Security cameras.
- Servers.
- Other network-connected devices.

If administrators do not change these credentials after installation, attackers may use publicly known default passwords to gain unauthorized access.

### Why Are Default Passwords a Security Risk?

- They may be publicly documented.
- Attackers can search for vendor-specific default credentials.
- The same credentials may be used across multiple devices.
- Unchanged credentials can provide an easy entry point into a network.

### Security Recommendations

- Change default credentials immediately after installation.
- Use unique passwords for different devices.
- Disable unused accounts.
- Restrict administrative interfaces to trusted networks.
- Keep device firmware updated.

### Reference Resources

The course lists the following websites as default-password databases:

- [Default Password](http://default-password.info)
- [Default Password US](http://www.defaultpassword.us)
- [Passwords Database](http://www.passwordsdatabase.co)
- [Router Passwords](https://www.routerpasswords.com)

**Note:** These are references listed in the course material. Their current availability and reliability should be verified before use. Prefer official vendor documentation when checking default credentials.

## Password Complexity

Password complexity refers to the characteristics that make a password difficult to guess or crack.

A strong password should avoid common words, predictable patterns, and easily discoverable personal information.

The course slide illustrates different password examples, including:

```text
HIJKLMNO
4455852097
ax1500g
m@roon$
@$47$
E1n@84_4#
```

These examples demonstrate different combinations of letters, numbers, and special characters. However, using multiple character types alone does not guarantee password strength.

### Characteristics of Strong Passwords

- **Length:** Longer passwords generally provide a larger search space.
- **Uniqueness:** Each account should have its own password.
- **Unpredictability:** Avoid common words and predictable patterns.
- **Complexity:** Use a combination of character types when appropriate.
- **No Personal Information:** Avoid names, birthdays, and other easily discoverable details.

Using a password manager can help generate and store strong, unique passwords.

---

## Summary

This section covers three major password-cracking techniques and several related security concepts.

- **Dictionary Attack:** Uses a predefined wordlist to test likely passwords.
- **Brute-Force Attack:** Tests possible character combinations.
- **Rule-Based Attack:** Modifies existing password candidates using predefined rules.

LLMNR/NBT-NS Poisoning abuses Windows name-resolution mechanisms to capture authentication-related data. Default passwords create security risks when they are not changed after installation.

Password complexity is another important security factor. Long, unique, and unpredictable passwords make password attacks more difficult.

**Key Point:** Password security depends not only on password complexity but also on secure authentication protocols, proper network configuration, and the prevention of credential exposure.

## Related Links

- [Hashcat – Advanced Password Recovery](https://hashcat.net/hashcat/)
- [John the Ripper](https://www.openwall.com/john/)
- [MITRE ATT&CK – Brute Force](https://attack.mitre.org/techniques/T1110/)
- [MITRE ATT&CK – LLMNR/NBT-NS Poisoning and SMB Relay](https://attack.mitre.org/techniques/T1557/001/)
- [Microsoft – Disable LLMNR](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/disable-link-local-multicast-name-resolution)
- [Microsoft – NetBIOS over TCP/IP](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/disable-netbios-tcp-ip)
- [OWASP – Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [NIST – Digital Identity Guidelines](https://pages.nist.gov/800-63-4/)
