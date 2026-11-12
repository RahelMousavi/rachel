
# Web Server Attacks

## 1. Types of Web Server Attacks

Web servers can be targeted through different types of attacks that affect their availability, integrity, confidentiality, or security.

The PDF introduces the following types of web server attacks:

- **DoS/DDoS Attack:** Attempts to disrupt the availability of a web server by overwhelming its resources or network capacity.
- **DNS Server Hijacking:** Unauthorized modification or manipulation of DNS settings or records to redirect users to unintended destinations.
- **DNS Amplification:** A type of DDoS attack that exploits DNS servers to amplify traffic directed at a target.
- **Directory Traversal:** Exploits insufficient restrictions on file paths to access files outside the intended directory.
- **MITM Attack:** A Man-in-the-Middle attack in which an attacker intercepts or potentially modifies communication between two parties.
- **Phishing Attack:** Uses deceptive messages or websites to trick users into revealing sensitive information.
- **Website Defacement:** Unauthorized modification of a website's content or appearance.
- **Misconfiguration:** Exploits insecure or incorrect web server configuration settings.
- **Password Attack:** Attempts to discover or compromise user credentials.
- **Web Application Attack:** Targets vulnerabilities in web applications running on or communicating with the web server.

## 2. Website Defacement

**Website Defacement** is an attack in which an attacker gains unauthorized access to a website and modifies its content or appearance.

The attacker may replace the original website page with unauthorized content, messages, images, or other materials.

### Impact of Website Defacement

- Damage to the organization's reputation.
- Loss of user trust.
- Unauthorized modification of website content.
- Potential disclosure of sensitive information.
- Indication of a compromised web server or website.

## 3. Web Server Misconfiguration

**Web Server Misconfiguration** occurs when a web server or its related software is configured insecurely.

Improper configuration may expose sensitive information and provide attackers with useful details about the server.

The PDF presents two examples:

### Exposing the server-status Page

A configuration in the Apache `httpd.conf` file can make the `server-status` page accessible.

This page may contain useful information about the web server, including its operational status and activity.

If access is not properly restricted, unauthorized users may obtain information about the server.

### Displaying PHP Error Messages

The following settings are shown in the PDF as an example of PHP configuration:

```ini
display_errors = On
log_errors = On
error_log = syslog
ignore_repeated_errors = Off
```

Enabling `display_errors` may cause error messages to be displayed to users.

These messages can reveal useful technical information about the application or server, which may help attackers understand the environment.

**Security Consideration:**

Error messages should not expose sensitive technical details to public users. Errors should be logged securely, while detailed error display should be disabled in production environments.

## 4. Password Attacks

A **Password Attack** attempts to discover or compromise passwords used to access a system or service.

The PDF introduces three common password attack techniques.

### 4.1 Dictionary Attack

A **Dictionary Attack** uses a predefined word list containing possible passwords.

The attack checks candidate passwords from the list to identify a matching password.

Its effectiveness depends on the quality of the word list and whether the target uses a password included in it.

### 4.2 Brute Force Attack

A **Brute Force Attack** systematically tests possible character combinations until the correct password is found.

Unlike a dictionary attack, it does not depend only on predefined words.

The number of possible combinations increases significantly with password length and character-set complexity.

### 4.3 Hybrid Attack (Word Mangling)

A **Hybrid Attack** combines dictionary-based guessing with variations of words.

It modifies words from a word list by applying changes such as adding numbers, symbols, or character substitutions.

This approach combines characteristics of dictionary and brute force attacks.

### Password Attack Tools

The PDF lists the following tools:

- **Cain and Abel**
- **John the Ripper**
- **oclHashcat-plus**

These tools are associated with password auditing and password recovery activities.

## 5. HTTP/2 Continuation Flood Attack

The **HTTP/2 Continuation Flood Attack** exploits the way HTTP/2 handles CONTINUATION frames.

It can cause excessive resource consumption on the target Apache server and lead to a Denial of Service (DoS).

### Understanding HTTP/2 Headers

In HTTP/2, when headers are too large to fit into a single HEADERS frame, they can be divided into multiple frames.

- The initial part of the headers is sent in a **HEADERS** frame.
- The remaining parts are sent in **CONTINUATION** frames.

These frames are used to transmit the complete header block.

### How the Attack Works

An attacker abuses this mechanism by sending a large number of CONTINUATION frames without properly completing the header block.

The server allocates memory and other resources to process these frames.

Excessive CONTINUATION frames can consume server resources and potentially cause the Apache server to become unresponsive or crash.

### Impact

- Excessive memory consumption.
- Resource exhaustion.
- Server unresponsiveness.
- Denial of Service (DoS).

## Related Links

### Web Server Security

- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Directory Traversal](https://owasp.org/www-community/attacks/Path_Traversal)
- [OWASP Cross-Site Request Forgery and Web Security Resources](https://owasp.org/www-community/attacks/)

### Password Security

- [John the Ripper](https://www.openwall.com/john/)
- [Hashcat Documentation](https://hashcat.net/wiki/)
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

### HTTP/2

- [RFC 9113 - HTTP/2](https://www.rfc-editor.org/rfc/rfc9113)
- [Apache HTTP Server Documentation](https://httpd.apache.org/docs/)

## Summary

- Web servers can be targeted through attacks such as DoS/DDoS, DNS attacks, Directory Traversal, MITM, Phishing, and Web Application Attacks.
- Website Defacement involves unauthorized modification of website content or appearance.
- Web Server Misconfiguration can expose sensitive information through accessible status pages or publicly displayed error messages.
- Dictionary Attacks use word lists, while Brute Force Attacks test possible character combinations.
- Hybrid Attacks combine dictionary-based guessing with word modifications.
- Cain and Abel, John the Ripper, and oclHashcat-plus are tools listed for password attacks.
- HTTP/2 Continuation Flood exploits the handling of CONTINUATION frames to exhaust server resources and cause DoS.
