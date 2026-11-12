
# Cryptography Fundamentals

## 1. Introduction to Cryptography

Cryptography is the process of converting data into encrypted code to protect information during transmission over private or public networks.

It is used to protect confidential information such as:

- Email messages
- Chat messages
- Web transactions
- Personal information
- Corporate data
- E-commerce applications

Cryptography helps protect sensitive information from unauthorized access.

### 1.1 Goals of Cryptography

Cryptography has four main security goals:

- **Confidentiality:** Ensures that information is accessible only to authorized individuals.
- **Integrity:** Ensures that information has not been altered or modified without authorization.
- **Authentication:** Verifies the identity of communicating parties.
- **Non-repudiation:** Prevents a sender from denying that they sent a message or performed an action.

## 2. Government Access to Keys (GAK)

Government Access to Keys (GAK) refers to the legal obligation of individuals or organizations to disclose their encryption keys to government agencies.

Under this concept:

- Software companies may provide copies of encryption keys to government agencies.
- Law enforcement agencies can use these keys to monitor suspicious communications and collect evidence related to cybercrime.
- Governments may use this access for national security purposes.
- Governments promise to store the keys securely and use them only when authorized by a court order.

GAK is often compared to traditional wiretapping because both involve government access to private communications.

## 3. Ciphers

A cipher is an algorithm used to perform encryption and decryption.

- **Encryption:** Converts readable information into an encrypted form.
- **Decryption:** Converts encrypted information back into its original readable form.

Ciphers use specific algorithms and keys to transform information.

## 4. Substitution Ciphers

Substitution ciphers are encryption techniques in which characters or bytes in the original message are replaced with other characters or bytes.

Two substitution techniques covered in this section are Rotation Substitution and Arbitrary Substitution.

### 4.1 Rotation Substitution

Rotation Substitution is a symmetric encryption technique based on simple mathematics and the use of a single key.

Anything encrypted using a key can be decrypted using the same key.

In this method, each character in the original message is shifted forward by a specified number of positions in the character sequence.

#### Caesar Cipher

The Caesar cipher is a historical example of rotation substitution. It was used by Julius Caesar to encrypt messages sent to his generals.

For example:

- **ROT-3:** Each character is shifted three positions forward.
- **ROT-13:** Each character is shifted thirteen positions forward.

Rotation substitution techniques have a long history, dating back approximately 2,000 years, with early uses in places such as Egypt and China.

### 4.2 Arbitrary Substitution

Arbitrary Substitution is an encryption technique in which one character or byte is replaced with another according to a predefined mapping.

In simple substitution schemes:

- Each character is mapped to another character.
- Encryption replaces each original character with its corresponding mapped character.
- Decryption reverses the substitution process.
- The mapping function acts as the encryption key.

#### Example

Consider the following mapping:

```text
Plaintext:  A B C D E ...
Key:        W K M P D ...
```

Using this mapping:

```text
Plaintext:  C A B
Ciphertext: M W K
```

The original characters are replaced according to the defined mapping.

## Related Links

- [NIST — Cryptographic Standards and Guidelines](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines)
- [Caesar Cipher — Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)
- [Substitution Cipher — Wikipedia](https://en.wikipedia.org/wiki/Substitution_cipher)

## Summary

This section introduced the fundamentals of cryptography, its four main security goals, and Government Access to Keys (GAK).

It also explained ciphers and two substitution techniques: Rotation Substitution and Arbitrary Substitution. These techniques demonstrate how encryption transforms readable information into an encrypted form.
