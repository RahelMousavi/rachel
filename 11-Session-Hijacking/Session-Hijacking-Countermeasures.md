
# 06 — Session Hijacking Countermeasures

## 1. Introduction

**Session Hijacking Countermeasures** are security mechanisms and practices designed to prevent attackers from stealing, predicting, or taking control of active user sessions.

These countermeasures focus on protecting session identifiers, securing communication channels, and reducing opportunities for unauthorized access.

## 2. Session Hijacking Solutions for Protocols

The course introduces three security mechanisms related to protecting network and web communication.

### 2.1 HTTP Strict Transport Security (HSTS)

**HTTP Strict Transport Security (HSTS)** is a web security policy that helps protect HTTPS websites against Man-in-the-Middle (MITM) attacks and protocol downgrade attacks.

HSTS allows a web server to instruct browsers to communicate with the website only through HTTPS instead of insecure HTTP.

#### How HSTS Works

1. A browser connects to a website.
2. The server sends an HTTP response containing the `Strict-Transport-Security` header over HTTPS.
3. The browser stores the HSTS policy.
4. Future requests to that domain are automatically upgraded to HTTPS.
5. The browser refuses insecure HTTP connections to that domain while the policy is active.

**Important:** HSTS protection is established after the browser receives the policy over HTTPS. During a user's first visit, protection against an initial HTTP downgrade requires mechanisms such as HSTS Preloading.

### 2.2 Token Binding

**Token Binding** is a security mechanism designed to cryptographically bind authentication tokens to a specific client.

The course describes the following process:

1. The client generates a public/private key pair.
2. When connecting to the server, the client creates a signature using its private key.
3. The client sends the signature and its public key to the server.
4. The server verifies the signature using the client's public key.
5. This process helps ensure that the token is associated with the client possessing the corresponding private key.

The main purpose is to make stolen tokens more difficult to reuse from another client.

**Note:** Token Binding is a historical protocol proposal and is not a generally supported modern browser security mechanism. It is useful to understand as a course concept, but should not be treated as a current deployment recommendation.

### 2.3 DNS over HTTPS (DoH)

**DNS over HTTPS (DoH)** is a protocol that sends DNS queries through an encrypted HTTPS connection.

Traditional DNS queries are commonly transmitted without encryption, allowing network observers to monitor DNS requests.

DoH protects DNS queries by sending them through HTTPS, typically over TCP port 443.

#### Benefits of DoH

- Encrypts DNS communication between the client and DNS resolver.
- Makes DNS queries more difficult for network observers to inspect.
- Helps protect DNS requests against certain forms of interception and manipulation.
- Improves DNS query privacy.

**Important:** DoH protects DNS communication, not the entire web session. It does not replace HTTPS, secure session cookies, or proper session management.

## 3. General Session Hijacking Countermeasures

The course introduces the following general countermeasures:

### 3.1 Use SSH for Secure Communication

Use **Secure Shell (SSH)** to establish encrypted remote administrative connections.

SSH helps protect administrative communication against eavesdropping and unauthorized interception.

### 3.2 Use HTTPS for Authentication Cookies

Authentication cookies should only be transmitted over secure HTTPS connections.

The `Secure` cookie attribute helps ensure that browsers send session cookies only through HTTPS.

### 3.3 Implement a Logout Mechanism

Web applications should provide a proper **Log out** function.

When a user logs out, the server must invalidate the associated session so that the session identifier can no longer be reused.

### 3.4 Generate Session IDs After Authentication

Generate a new session identifier after successful authentication.

The server should generate and validate session identifiers rather than accepting arbitrary identifiers supplied by clients.

This helps prevent Session Fixation attacks.

### 3.5 Encrypt Data in Transit

Ensure that data transmitted between clients and servers is encrypted.

Implement **Defense in Depth**, which combines multiple security mechanisms instead of relying on a single protective measure.

### 3.6 Use Long and Random Session Keys

Session identifiers should be sufficiently long and generated using cryptographically secure random values.

Unpredictable identifiers make guessing and brute-force attacks significantly more difficult.

### 3.7 Educate Employees and Restrict Remote Access

Security awareness training helps employees recognize suspicious links, malicious websites, and other threats.

Remote access should also be restricted to authorized users and secure channels.

### 3.8 Implement Session Timeouts

A session should expire after a defined period of inactivity.

Expired sessions must be invalidated on the server side.

### 3.9 Use Strong Authentication Mechanisms

Use secure authentication mechanisms such as:

- IPsec
- VPN
- Multi-Factor Authentication (MFA)

These mechanisms add security layers to network access and user authentication.

### 3.10 Use IDS and IPS

**Intrusion Detection Systems (IDS)** monitor network or system activity and generate alerts when suspicious behavior is detected.

**Intrusion Prevention Systems (IPS)** can detect and actively block malicious traffic.

Both can contribute to identifying and preventing suspicious session-related activity.

## 4. Recommendations for Web Developers

Web developers should implement secure session management practices to reduce the risk of Session Hijacking.

The course provides the following recommendations:

- Generate session identifiers using long and unpredictable random values.
- Generate a new Session ID after successful login to prevent Session Fixation.
- Encrypt session data and session identifiers transmitted between the client and server.
- Expire sessions immediately when users log out.
- Prevent network eavesdropping by securing communication channels.
- Reduce the lifetime of sessions and cookies.

### Additional Best Practices

Modern web applications should also consider the following practices:

- Set the `HttpOnly` attribute to prevent client-side scripts from reading session cookies.
- Set the `Secure` attribute to restrict cookie transmission to HTTPS.
- Use the `SameSite` attribute to reduce cross-site request risks.
- Implement both idle and absolute session timeouts.
- Regenerate session identifiers after authentication and privilege changes.
- Never expose session identifiers in URLs.

## 5. Recommendations for Web Users

The course also provides recommendations for users to reduce the risk of session compromise.

- Avoid clicking links received through email or chat when their source is unknown or untrusted.
- Use a firewall to help prevent unauthorized network access and malicious traffic.
- Use browser security settings to control cookie behavior.
- Verify that websites use valid digital certificates issued by trusted Certificate Authorities.
- Clear browser history, offline content, and cookies after sensitive transactions when appropriate.
- Prefer HTTPS when accessing websites and transmitting sensitive information.
- Always use the website's **Log out** function instead of simply closing the browser.

## Summary

Session Hijacking countermeasures protect active sessions by securing communication, managing session identifiers, and reducing opportunities for attackers.

The main concepts covered in this section are:

- **HSTS:** Enforces HTTPS connections for supported browsers.
- **Token Binding:** A historical mechanism designed to bind tokens to a specific client.
- **DNS over HTTPS:** Encrypts DNS queries between clients and resolvers.
- **HTTPS and SSH:** Protect communication against network interception.
- **Secure Session Management:** Uses unpredictable session IDs, regeneration, expiration, and proper logout.
- **IDS and IPS:** Help detect and prevent suspicious network activity.
- **Developer Recommendations:** Focus on secure session creation, cookie protection, and session lifecycle management.
- **User Recommendations:** Focus on safe browsing, trusted websites, and proper logout practices.

A secure session management system should combine strong authentication, encrypted communication, unpredictable session identifiers, and proper session expiration.

## Related Links

- [OWASP — Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
- [OWASP — HTTP Strict Transport Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html)
- [RFC 6797 — HTTP Strict Transport Security (HSTS)](https://www.rfc-editor.org/rfc/rfc6797)
- [RFC 8484 — DNS Queries over HTTPS (DoH)](https://www.rfc-editor.org/rfc/rfc8484)
- [RFC 8471 — The Token Binding Protocol Version 1.0](https://www.rfc-editor.org/rfc/rfc8471)
- [MDN — HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies)
- [OWASP — Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)
