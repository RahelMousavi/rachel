
# Countermeasures Against LDAP Enumeration

LDAP Enumeration can expose sensitive directory information, including usernames, email addresses, groups, and computer accounts.

The following countermeasures can help protect LDAP services against unauthorized information gathering.

## 1. Encrypt LDAP Traffic

LDAP traffic is not encrypted by default when using standard LDAP communication.

Use secure LDAP connections to protect information exchanged between clients and LDAP servers.

Two common methods are:

- **LDAPS:** Uses SSL/TLS encryption, commonly over TCP port `636`.
- **StartTLS:** Upgrades an existing LDAP connection to an encrypted TLS connection, commonly over TCP port `389`.

Encryption helps prevent attackers from intercepting sensitive directory information.

## 2. Use Different Usernames and Email Addresses

Avoid using usernames that are identical to users' email addresses.

Using different usernames and email addresses can make it more difficult for attackers to identify valid accounts through email-based information gathering.

## 3. Enable Account Lockout Policies

Configure Account Lockout policies to protect accounts against repeated failed authentication attempts.

An account can be temporarily locked after a specified number of unsuccessful login attempts.

This helps reduce the risk of password-guessing and brute-force attacks.

## 4. Restrict LDAP Access

Additional security measures include:

- Require authentication for sensitive directory queries.
- Apply appropriate access control permissions.
- Restrict anonymous LDAP binds where they are not required.
- Grant users only the minimum directory permissions necessary.
- Monitor LDAP queries for suspicious enumeration activity.

## Related Links

- [RFC 4511 — Lightweight Directory Access Protocol (LDAP)](https://www.rfc-editor.org/rfc/rfc4511)
- [RFC 4513 — LDAP Authentication Methods and Security Mechanisms](https://www.rfc-editor.org/rfc/rfc4513)
- [RFC 4511 — StartTLS Operation](https://www.rfc-editor.org/rfc/rfc4511)
- [Microsoft Learn — LDAP Signing and Channel Binding](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/ldap-signing)
- [Microsoft Learn — Account Lockout Policy](https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/account-lockout-policy)
