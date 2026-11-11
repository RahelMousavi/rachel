
# How Password Hashes Are Stored in Windows SAM

Windows stores local account information and password hashes in the Security Account Manager (SAM) database.

The SAM database is located at:

```text
C:\Windows\System32\config\SAM
```

## Structure of a SAM Entry

A SAM account entry contains several fields:

- **Username:** The name associated with the local Windows account.
- **User ID (RID):** A Relative Identifier that uniquely identifies the account within its security domain.
- **LM Hash:** A hash generated using the legacy LAN Manager hashing algorithm.
- **NTLM Hash:** A hash generated using the NT password hashing algorithm.

### LM Hash

LM (LAN Manager) is an outdated password hashing method with several security weaknesses.

It is disabled by default in Windows Vista and later versions. Therefore, the LM hash field is generally empty unless LM hash storage has been explicitly enabled.

### NTLM Hash

The NT hash is generated using the NT password hashing algorithm and is associated with Windows NTLM authentication.

Unlike LM, it does not split passwords into two separate seven-character sections.

## Summary

The Windows SAM database stores local account information and password hashes.

A typical account entry contains:

- **Username:** Account name.
- **RID:** Account identifier.
- **LM Hash:** Legacy password hash, generally disabled by default in modern Windows.
- **NTLM Hash:** Password hash used by the NTLM authentication mechanism.

**Key Point:** LM and NTLM hashes are different. LM is an older and weaker hashing method, while the NT hash is used in NTLM authentication. Neither should be confused with plain-text passwords.

## Related Links

- [Microsoft – Security Account Manager](https://learn.microsoft.com/en-us/windows/win32/secmgmt/security-account-manager)
- [Microsoft – SAM Database](https://learn.microsoft.com/en-us/windows/win32/secmgmt/sam-database)
- [Microsoft – NTLM Overview](https://learn.microsoft.com/en-us/windows-server/security/kerberos/ntlm-overview)
- [Microsoft – Relative Identifier (RID)](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-identifiers)
