
# Password Salting

## What is Password Salting?

Password salting is a security technique in which a random string of characters, called a **salt**, is added to a password before it is processed by a hashing algorithm.

The resulting hash is stored instead of the original password.

Salting makes password hashes more difficult to crack, especially when attackers use precomputed hash databases such as Rainbow Tables.

## How Password Salting Works

The process generally consists of three steps:

1. **Generate a Salt:** A unique random string is generated for each password.
2. **Combine with Password:** The salt is added to the original password.
3. **Generate the Hash:** The combined value is passed through a password-hashing algorithm, and the resulting hash is stored.

For example:

```text
Password: password123
Salt A:   x7k9
Salt B:   p2m5

Password + Salt A → Hash A
Password + Salt B → Hash B
```

Although the original passwords are identical, the resulting hashes are different because different salts are used.

## Advantages of Password Salting

### 1. Prevents Precomputed Hash Attacks

Salting makes precomputed hash databases, such as Rainbow Tables, much less effective because attackers cannot directly reuse precomputed values for different salts.

### 2. Produces Different Hashes

If two users choose the same password, their hashes will still be different when each account uses a unique salt.

### 3. Makes Password Cracking More Difficult

Attackers must perform separate calculations for each salt instead of efficiently reusing the same precomputed results across multiple accounts.

## Password Salting in Windows

According to the course material, Windows password hashes are not salted.

In particular, traditional LM and NT hashes do not use unique salts. This makes identical passwords produce identical hashes and can make offline password-cracking attacks easier.

Modern password storage systems should use unique salts with dedicated password-hashing algorithms such as Argon2id, bcrypt, or scrypt.

---

## Summary

Password salting is a technique that adds a unique random value to a password before hashing it.

Its main benefits are:

- **Protection Against Rainbow Tables:** Makes precomputed hash attacks less effective.
- **Unique Hashes:** Identical passwords produce different hashes when different salts are used.
- **Stronger Password Storage:** Makes large-scale offline password cracking more expensive.

**Key Point:** A salt is not a secret password. It is a unique random value stored alongside the password hash. Its purpose is to make password cracking more difficult.

The course material also emphasizes that Windows LM and NT password hashes are not salted.

## Related Links

- [OWASP – Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [NIST – Digital Identity Guidelines](https://pages.nist.gov/800-63-4/)
- [RFC 9106 – Argon2 Memory-Hard Function](https://www.rfc-editor.org/rfc/rfc9106)
- [OWASP – Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
- [Microsoft – Password Policy](https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-policy)
