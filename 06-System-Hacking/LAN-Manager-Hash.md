
# LAN Manager (LM) Hash

## What is LM Hash?

LAN Manager (LM) Hash is an old password hashing method developed by Microsoft for storing Windows passwords.

It was designed to support passwords with a maximum length of 14 characters. However, its hashing process contains several weaknesses that make it vulnerable to password-cracking attacks.

## How LM Hash Works

Before generating an LM hash, the password goes through several processing steps:

### 1. Convert Characters to Uppercase

All lowercase letters in the password are converted to uppercase.

For example:

```text
Original Password:  password123
After Conversion:   PASSWORD123
```

This makes the hashing process case-insensitive, reducing the number of possible password combinations.

### 2. Pad the Password to 14 Characters

If the password contains fewer than 14 characters, it is padded with null characters (`0x00`) until it reaches 14 characters.

### 3. Split the Password into Two Parts

The 14-character password is divided into two separate blocks, each containing 7 characters.

For example:

```text
Password: 123456QWERTY

First Part:  123456Q
Second Part: WERTY__
```

Each part is processed independently to generate its own hash.

### 4. Generate Two Separate Hashes

Each 7-character block is independently processed using the LM hashing algorithm.

The resulting hashes are then combined to form the final LM hash.

For example, the course slide shows:

```text
Original Password: 123456QWERTY

First Part:
123456Q = 6BF11E04AFAB197F

Second Part:
WERTY__ = F1E9FFDCC75575B15
```

The final LM hash is formed by combining the two resulting hash values.

### Important Note: Passwords Shorter Than 7 Characters

If the original password contains fewer than 7 characters, the second part is empty.

In this case, the second hash always has the following value:

```text
AAD3B435B51404EE
```

This predictable value can help attackers identify passwords that are shorter than 8 characters when analyzing LM hashes.

## Why Is LM Hash Insecure?

LM Hash has several security weaknesses:

- **Case Insensitivity:** Converting all characters to uppercase reduces password complexity.
- **Password Splitting:** Dividing the password into two independent 7-character blocks makes cracking easier because each block can be attacked separately.
- **Limited Password Length:** LM supports passwords of up to 14 characters.
- **Weak Hashing Algorithm:** LM uses DES-based hashing, which is considered cryptographically weak by modern standards.
- **Predictable Empty Block:** Passwords shorter than 8 characters produce a predictable hash for the second block.

Because of these weaknesses, LM Hash should not be used for modern password storage.

---

## Summary

LM Hash is a legacy Microsoft password hashing method with a maximum password length of 14 characters.

Its process consists of four main steps:

1. Convert all password characters to uppercase.
2. Pad the password with null characters until it reaches 14 characters.
3. Divide the password into two 7-character blocks.
4. Hash each block separately and combine the results.

The main weakness of LM Hash is that its password-splitting mechanism allows attackers to crack each half independently, making password recovery significantly easier.

**Key Point:** LM Hash is considered insecure and is disabled by default in Windows Vista and later versions. Modern Windows environments should avoid storing LM hashes.

## Related Links

- [Microsoft – LAN Manager Authentication](https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-do-not-store-lan-manager-hash-value-on-next-password-change)
- [Microsoft – LAN Manager Authentication Level](https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-lan-manager-authentication-level)
- [Microsoft – NTLM Overview](https://learn.microsoft.com/en-us/windows-server/security/kerberos/ntlm-overview)
- [Hashcat – LM Hash Mode (3000)](https://hashcat.net/wiki/doku.php?id=example_hashes)
- [NIST – Digital Identity Guidelines](https://pages.nist.gov/800-63-4/)
