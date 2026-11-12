
# 01 — Session Hijacking Concepts

## 1. What Is Session Hijacking?

**Session Hijacking** is an attack in which an attacker takes advantage of an active session between two systems and redirects or takes control of that session.

In a TCP session, authentication usually takes place at the beginning of the communication. Therefore, an attacker who obtains a valid session identifier may be able to take over an established session without knowing the user's username and password.

By hijacking an active session, an attacker may:

- Sniff traffic exchanged during the session.
- Steal the user's identity.
- Access sensitive information.
- Perform unauthorized actions.
- Impersonate an authenticated user.

A valid **Session ID** can allow an attacker to authenticate to a server as the legitimate user.

## 2. Why Are Session Hijacking Attacks Successful?

According to the course, several weaknesses can make Session Hijacking attacks successful.

### 2.1 Lack of Account Lockout

If a website does not implement an account lockout mechanism for invalid session identifiers, an attacker may attempt multiple connections using different Session IDs through a valid URL.

### 2.2 Weak Session ID Generation Algorithms

Some websites use weak or predictable algorithms to generate session identifiers.

For example, identifiers generated using predictable values such as timestamps or IP addresses may be easier to guess.

Short Session IDs also reduce the number of possible combinations.

### 2.3 Insecure Session ID Management

An attacker may obtain stored session information by tricking a user's browser into visiting another website.

The course mentions techniques such as:

- Cross-Site Scripting (XSS)
- DNS Poisoning
- Browser Vulnerabilities

### 2.4 Sessions Without Expiration

Some sessions do not have a defined expiration time.

This allows an attacker to continue guessing or using a session identifier for an extended period.

### 2.5 TCP/IP Protocol Vulnerabilities

The course identifies weaknesses in the design of TCP/IP protocols as another factor that may make systems vulnerable to session hijacking.

### 2.6 Lack of Encryption

If communication is not properly encrypted, session identifiers transmitted between the client and server may be captured through network sniffing.

## 3. Session Hijacking Process

Session Hijacking involves taking control of an existing communication session between a legitimate client and a server.

The attacker attempts to obtain or compromise the information required to take over the session, such as a valid Session ID or session-related network information.

Once the session is compromised, the attacker may impersonate the legitimate user and access resources available through that session.

**Note:** The course presents a process diagram on this topic but does not provide a detailed textual explanation of each stage.

## 4. Types of Session Hijacking

Session Hijacking attacks are classified into two main types:

### 4.1 Passive Session Hijacking

In a **Passive Session Hijacking** attack, the attacker takes control of or monitors a session without actively changing the communication.

The attacker mainly observes the information exchanged between the communicating systems.

### 4.2 Active Session Hijacking

In an **Active Session Hijacking** attack, the attacker identifies and takes over an active session.

The legitimate connection may be interrupted, allowing the attacker to communicate with the server instead of the original user.

## 5. Session Hijacking in the OSI Model

Session Hijacking can occur at two different levels:

### 5.1 Network-Level Session Hijacking

In Network-Level Hijacking, an attacker targets packets being exchanged between a client and a server.

According to the course, this type of attack can involve communication at the TCP and UDP levels.

### 5.2 Application-Level Session Hijacking

In Application-Level Hijacking, an attacker obtains or compromises a user's HTTP session identifier.

The attacker can then use the stolen or compromised Session ID to gain unauthorized access to a web server.

## 6. Session Hijacking vs. Spoofing

Session Hijacking and Spoofing are different techniques, although both can be used to impersonate another system or user.

### Spoofing

In a **Spoofing** attack:

- The attacker pretends to be another user or machine to gain unauthorized access.
- The attacker does not take over an existing active session.
- Instead, the attacker establishes a new session using stolen credentials or forged identity information.

### Session Hijacking

In a **Session Hijacking** attack:

- The attacker takes control of an already established session.
- The attacker relies on a legitimate user's existing connection and authentication.
- The objective is to take over the active communication rather than simply create a new session.

### Key Difference

The main difference is that **Spoofing involves impersonation to establish a connection, whereas Session Hijacking involves taking control of an existing active session.**

## Summary

Session Hijacking is an attack that allows an attacker to take control of an active communication session and impersonate a legitimate user.

The main concepts covered in this section are:

- **Session Hijacking:** Taking control of an active session.
- **Passive Hijacking:** Observing session communication.
- **Active Hijacking:** Taking over an active connection.
- **Network-Level Hijacking:** Targeting TCP or UDP communication.
- **Application-Level Hijacking:** Compromising HTTP session identifiers.
- **Spoofing:** Impersonating another user or machine to establish a new connection.

Weak Session ID generation, insecure session management, missing expiration mechanisms, and unencrypted communication can increase the risk of Session Hijacking.

## Related Links

- [OWASP — Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
- [MDN — Session Management](https://developer.mozilla.org/en-US/docs/Web/Security/Authentication/Session_management)
- [OWASP — Cross-Site Scripting (XSS)](https://owasp.org/www-community/attacks/xss/)

