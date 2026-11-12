
# PKI and Digital Security

## 1. Public Key Infrastructure (PKI)

Public Key Infrastructure (PKI) is a framework consisting of hardware, software, people, policies, and procedures used to manage digital certificates and public-key cryptography.

PKI provides mechanisms to:

- Create digital certificates.
- Manage and distribute certificates.
- Use and store certificates.
- Revoke digital certificates when necessary.

### 1.1 PKI Components

The main components involved in the certificate management process include:

- **Registration Authority (RA):** Reviews and approves certificate requests.
- **Certificate Authority (CA):** Issues digital certificates and manages certificate information.
- **Validation Authority (VA):** Checks the validity of digital certificates and provides validation results.

### 1.2 PKI Process

The certificate issuance and validation process can be described as follows:

1. A user requests a digital certificate.
2. The Registration Authority (RA) reviews and approves the request.
3. The approved request is forwarded to the Certificate Authority (CA).
4. The CA updates the certificate-related information and issues the certificate.
5. The user sends a digitally signed message along with a copy of their public key certificate.
6. The recipient's system or client queries the Validation Authority (VA) to check the certificate.
7. The VA returns the certificate validation result.

## 2. Digital Certificates

A digital certificate is an electronic document that associates an identity with a public key.

The module introduces two types of certificates:

- Signed Certificates
- Self-Signed Certificates

### 2.1 Signed Certificate

A signed certificate is obtained from a trusted Certificate Authority (CA).

It contains information such as:

- Certificate holder's name.
- Certificate serial number.
- Expiration date.
- A copy of the certificate holder's public key.
- The CA's digital signature.

#### Verification Process

1. The user signs a document using their private key.
2. The signed document is sent to the receiver.
3. The receiver can query the Validation Authority (VA) to verify the certificate.
4. The VA checks the certificate and confirms its validity.

### 2.2 Self-Signed Certificate

A self-signed certificate is created by the user using certificate creation tools rather than being issued by a trusted CA.

It contains:

- The user's name.
- The user's public key.
- The user's own digital signature.

#### Verification Process

1. The user creates their own certificate.
2. The user signs a document and sends it to the receiver.
3. The receiver can contact the certificate owner directly to verify the certificate.

Unlike a certificate issued by a trusted CA, a self-signed certificate does not rely on an external certificate authority to establish trust.

## 3. Digital Signatures

A Digital Signature uses asymmetric cryptography to provide security properties similar to a handwritten signature.

However, it is a cryptographic mechanism rather than an image or representation of a handwritten signature.

Digital signatures help provide:

- Authentication
- Integrity
- Non-repudiation

A digitally signed email can also be encrypted to provide additional confidentiality.

### 3.1 Digital Signature Process

The process described in the module involves the following steps:

#### Sender's Side

1. The sender generates a hash of the original message.
2. The sender signs the hash using their private key.
3. The message is encrypted using a one-time symmetric key.
4. The encrypted message and digital signature are prepared for transmission.

#### Receiver's Side

1. The receiver decrypts the message using the one-time symmetric key.
2. The receiver decrypts the one-time symmetric key using their private key.
3. The receiver verifies the signed hash using the sender's public key.
4. The receiver independently calculates the hash of the received message.
5. The receiver compares the calculated hash with the verified hash.

If both hashes match, the message integrity and signature verification are confirmed.

## Related Links

- [NIST — Public Key Infrastructure](https://csrc.nist.gov/projects/pki)
- [NIST — Digital Signatures](https://csrc.nist.gov/projects/digital-signatures)
- [RFC 5280 — Internet X.509 Public Key Infrastructure Certificate and CRL Profile](https://www.rfc-editor.org/rfc/rfc5280)

## Summary

This section introduced Public Key Infrastructure (PKI), its main components, and the process of issuing and validating digital certificates.

It also explained signed and self-signed certificates and described how digital signatures use asymmetric cryptography and hashing to verify message integrity and authenticity.
