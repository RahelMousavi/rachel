
# Web Application Attack Methodology

## 1. Attacking Authentication Mechanisms

This stage focuses on identifying and exploiting weaknesses in the design and implementation of authentication mechanisms.

The module introduces the following types of attacks:

- **Password Attacks:** Attempts to compromise user passwords.
- **User Enumeration:** Identifying valid usernames or user accounts.
- **Session-Based Attacks:** Exploiting weaknesses in session management.
- **Cookie-Based Attacks:** Targeting authentication or session information stored in cookies.
- **Authentication Bypass:** Attempting to bypass the application's authentication mechanisms.

## 2. Attacking Authorization Schemes

Authorization determines what an authenticated user is allowed to access or perform.

During security testing, an account with limited privileges may be used to check whether its access level can be increased.

The module identifies two techniques:

- HTTP parameter tampering.
- Cookie parameter tampering.

These techniques can help identify weaknesses in how the application handles authorization-related information.

## 3. Attacking Access Controls

Access controls are security mechanisms that restrict access to application resources and functions.

They are logically related to authentication and session management.

During testing, an attacker may examine the following areas:

- Access to specific subsets of application data.
- Different access levels, such as employees, administrators, and supervisors.
- Administrative configuration and monitoring capabilities.
- Features that may allow privilege escalation.

## 4. Attacking Session Management Mechanisms

Web applications exchange sensitive information between clients and servers during a session.

If session management is insecure, attackers may exploit these weaknesses to compromise web application sessions.

The module describes the following approaches:

- Obtaining and using session tokens.
- Predicting weak or guessable session tokens.
- Manipulating obtained session tokens.
- Using Man-in-the-Middle (MITM) attacks to obtain session tokens.
- Performing Session Hijacking.

## 5. Performing Injection Attacks

Injection attacks involve modifying input data to introduce malicious instructions into an application or its underlying systems.

The module identifies several types of injection attacks:

### 5.1 Web Script Injection

Web Script Injection occurs when user input is dynamically executed by a web application without proper control.

An attacker may modify input values to affect the behavior of the web application.

### 5.2 Operating System Command Injection

Operating System Command Injection involves injecting malicious commands through application input fields.

This can occur when a web application uses user-provided input in system commands without proper validation.

### 5.3 SMTP Injection

SMTP Injection involves injecting commands into SMTP-related functionality in a web application.

The module mentions that this type of attack may be used to generate a large number of emails.

### 5.4 SQL Injection

SQL Injection involves inserting malicious SQL statements into application input fields to interact with or manipulate a database.

### 5.5 LDAP Injection

LDAP Injection exploits insufficient input validation in applications that interact with LDAP services.

An attacker may use this weakness to bypass LDAP filters and access unauthorized information.

### 5.6 Buffer Overflow

A Buffer Overflow occurs when an application receives more data than an input buffer is designed to hold.

The module describes this attack as injecting an unusually large amount of data into input fields.

## 6. Attacking Application Logic Flaws

Web applications contain business logic and processing rules at different levels.

Many attackers focus on common vulnerabilities such as SQL Injection and XSS because these attacks may be detected by security systems.

However, application logic flaws are more difficult to identify because they are not necessarily associated with known attack signatures.

The module highlights two important points:

- Security systems may not detect application logic flaws through signature-based detection.
- Vulnerability scanners may also fail to identify these weaknesses.

Therefore, testing application logic often requires manual analysis.

## 7. Attacking Web Application Clients

Some vulnerabilities directly affect web servers and do not require user interaction.

Other vulnerabilities require a response or action from the user before the attack can be completed.

The module identifies the following client-side attacks:

- Cross-Site Scripting (XSS)
- Session Fixation
- Cross-Site Request Forgery (CSRF)

## 8. Attacking Web Services

Web applications often integrate web services to perform specific functions.

If an integrated web service contains vulnerabilities, the web application that depends on it may also become vulnerable.

Therefore, web services should be included in web application security assessments.

## 9. Web Services Probing Attacks

WSDL (Web Services Description Language) documents contain information about web services, including service ports and connections between machines.

Attackers may analyze WSDL documents to identify potential weaknesses in web services.

The module describes the following probing process:

1. **Identify and Analyze the WSDL Document:** Locate the WSDL document and analyze it to understand the application's purpose, entry points, and message types.
2. **Construct Valid Requests:** Create valid requests according to XML rules that can be sent to the web service.
3. **Analyze SOAP Requests and Errors:** Include test content in SOAP requests and analyze the resulting errors to gain a better understanding of potential security weaknesses.

## 10. SOAP Injection

SOAP is a lightweight XML-based protocol designed for exchanging structured and typed information over the web.

SOAP Injection involves inserting malicious query strings into SOAP requests.

The module mentions characters such as:

- Single quotes (`'`)
- Double quotes (`"`)
- Semicolons (`;`)

An attacker may inject malicious query strings to bypass web service authentication mechanisms or gain access to databases.

SOAP Injection operates similarly to SQL Injection.

## Related Links

- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
- [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
- [OWASP Business Logic Testing](https://owasp.org/www-project-web-security-testing-guide/)
- [WSDL - W3C](https://www.w3.org/TR/wsdl)
- [SOAP - W3C](https://www.w3.org/TR/soap/)

## Summary

This file covered the main attack stages in web application hacking methodology.

These stages include testing authentication, authorization, access controls, and session management; performing injection attacks; identifying application logic flaws; and assessing web application clients and integrated web services.

WSDL analysis and SOAP Injection are also important parts of web service security testing.
