
# Web Application Threats - Part 1

## 1. Introduction to Web Application Threats

Web applications are exposed to different security threats because they interact with users, process input, communicate with databases, and provide access to application resources.

Attackers may exploit weaknesses in application code, authentication mechanisms, access controls, and input validation to access sensitive information or manipulate application behavior.

Common web application threats include:

- Injection attacks
- Broken Authentication
- XML External Entity (XXE)
- XML Injection
- Broken Access Control

## 2. OWASP Top 10

The OWASP Top 10 is a list of the most critical security risks affecting web applications. It helps developers and security professionals understand common vulnerabilities and improve application security.

The OWASP Top 10 list presented in this module includes:

1. **Broken Access Control:** Failures in enforcing restrictions on what authenticated users are allowed to do.
2. **Cryptographic Failures:** Weaknesses related to the protection of sensitive information through cryptography.
3. **Injection:** Untrusted data is interpreted as part of a command or query.
4. **Insecure Design:** Security weaknesses caused by missing or ineffective security controls in application design.
5. **Security Misconfiguration:** Incorrect or insecure configuration of application components.
6. **Vulnerable and Outdated Components:** Using components that contain known security vulnerabilities or are no longer maintained.
7. **Identification and Authentication Failures:** Weaknesses in identifying users and verifying their identities.
8. **Software and Data Integrity Failures:** Failures to ensure the integrity of software updates, critical data, and application components.
9. **Security Logging and Monitoring Failures:** Insufficient logging and monitoring that makes attacks difficult to detect.
10. **Server-Side Request Forgery (SSRF):** A vulnerability that allows an attacker to cause a server-side application to make requests to unintended locations.

## 3. Injection Attacks

Injection attacks occur when an application processes untrusted input without properly validating or handling it. An attacker can provide malicious input that is interpreted as part of a query or command.

The module discusses three common types of injection attacks:

- SQL Injection
- Command Injection
- LDAP Injection

### 3.1 SQL Injection

SQL Injection is an attack in which an attacker inserts malicious SQL statements into application input fields to manipulate database queries.

If the application does not properly handle user input, an attacker may be able to interact with the database in unintended ways.

**Common input locations include:**

- Web forms
- URL parameters
- Application input fields
- Search fields

SQL Injection may allow attackers to retrieve, modify, or manipulate database information.

### 3.2 Command Injection

Command Injection occurs when an attacker injects malicious commands through a vulnerable web application.

If an application passes untrusted input to operating system commands without proper validation, an attacker may be able to execute unintended commands.

The module describes the following forms:

- **Shell Injection:** Exploiting application functions or APIs that execute system commands, such as `system`, `StartProcess`, and `java.lang.Runtime.exec()`.
- **HTML Embedding:** Injecting HTML content into application input.
- **File Injection:** Injecting or manipulating file-related input to affect application behavior.

### 3.3 LDAP Injection

LDAP Injection occurs when an application uses untrusted input to construct LDAP queries without proper validation.

LDAP (Lightweight Directory Access Protocol) is used to access and manage directory information. Directory data is generally organized in a hierarchical structure.

An attacker may exploit LDAP Injection to manipulate directory queries, access unauthorized information, or modify directory content.

## 4. Broken Authentication

Broken Authentication refers to weaknesses in authentication and session management mechanisms.

These weaknesses may allow attackers to compromise user accounts, impersonate legitimate users, or gain unauthorized access.

The module identifies several areas that may contain authentication weaknesses:

- Session ID management
- Logout functionality
- Password management
- Session timeout
- Security questions

**Examples of authentication weaknesses include:**

- Session IDs exposed in URLs.
- Weak password hashes that can be exploited.
- Improper session timeout configuration.

## 5. XML External Entity (XXE)

XML External Entity (XXE) is listed in the module as a web application security threat.

The source material identifies XXE but does not provide further explanation of its operation in this section.

## 6. XML Injection

XML Injection occurs when an attacker inserts malicious XML content into application input.

If the application does not properly validate XML input, an attacker may be able to add or modify XML elements and influence application behavior.

For example, an attacker may manipulate an XML quantity field by adding additional elements to change the information processed by the application, potentially affecting product prices.

## 7. Broken Access Control

Broken Access Control occurs when an application does not properly enforce access restrictions.

An attacker may exploit these weaknesses to:

- Access restricted application resources.
- Perform functions that should not be available to their account.
- Bypass authorization mechanisms.
- Gain access to higher-level privileges.
- Impersonate users with greater permissions.

Access control mechanisms should ensure that users can only access the resources and functions they are authorized to use.

## Related Links

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Injection](https://owasp.org/www-community/Injection_Flaws)
- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [PortSwigger - SQL Injection](https://portswigger.net/web-security/sql-injection)
- [PortSwigger - LDAP Injection](https://portswigger.net/kb/issues/00100500_ldap-injection)
- [OWASP XML Security](https://owasp.org/www-community/vulnerabilities/XML_External_Entity_(XXE)_Processing)

## Summary

This file covered several common web application threats, including injection attacks, broken authentication, XML-related vulnerabilities, and broken access control.

These vulnerabilities may allow attackers to manipulate application input, access sensitive information, compromise user accounts, or bypass authorization mechanisms.
