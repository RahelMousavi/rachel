
# Microsoft Authentication

Microsoft Windows uses different authentication mechanisms to verify user identities and control access to systems and network resources.

The three main concepts covered in this section are SAM, NTLM, and Kerberos.

## 1. SAM Database (Security Account Manager)

SAM is a Windows database that stores local user account information and password hashes.

For domain accounts, authentication information is managed through Active Directory (AD).

- Passwords are not stored as plain text.
- Password hashes are used for authentication.
- SAM is primarily associated with local Windows accounts.

## 2. NTLM Authentication

NTLM (NT LAN Manager) is a Microsoft authentication protocol used to authenticate users in Windows environments.

It includes two password hashing methods:

- **LM (LAN Manager):** An older and insecure password hashing method.
- **NTLM Hash:** A stronger hashing method than LM, used in NTLM authentication.

These methods are associated with different ways of storing and processing password hashes.

## 3. Kerberos Authentication

Kerberos is a network authentication protocol used in Windows domain environments.

Microsoft adopted Kerberos as the default authentication protocol for domain authentication because it provides stronger security than NTLM.

Kerberos uses tickets to authenticate users and services without repeatedly transmitting passwords over the network.

---

## Summary

Windows authentication involves different mechanisms for storing credentials and verifying user identities.

- **SAM:** Stores local account information and password hashes.
- **NTLM:** A legacy Microsoft authentication protocol that includes LM and NTLM password hashing methods.
- **Kerberos:** A ticket-based authentication protocol used by default in modern Windows domain environments.

**Important Distinction:** SAM is a local account database, while NTLM and Kerberos are authentication protocols. Kerberos is generally preferred over NTLM in Windows domain environments.

## Related Links

- [Microsoft – Security Account Manager](https://learn.microsoft.com/en-us/windows/win32/secmgmt/security-account-manager)
- [Microsoft – NTLM Overview](https://learn.microsoft.com/en-us/windows-server/security/kerberos/ntlm-overview)
- [Microsoft – Kerberos Authentication Overview](https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview)
- [Microsoft – Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)
