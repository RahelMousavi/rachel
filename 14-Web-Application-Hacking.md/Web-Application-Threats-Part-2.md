
# Web Application Threats - Part 2

## 1. Cross-Site Scripting (XSS)

Cross-Site Scripting (XSS) is a vulnerability that allows attackers to inject malicious scripts into a web application.

When a victim accesses the affected page, the browser executes the injected script.

Unlike attacks that directly target the web server, XSS primarily targets the application's users and their browsers.

Depending on how the application handles sensitive information, XSS may expose session-related data, such as cookies.

## 2. Components with Known Vulnerabilities

Web applications often use third-party components, libraries, plugins, and frameworks.

Using outdated or vulnerable components may introduce security weaknesses into an application.

Attackers can exploit known vulnerabilities in these components to compromise the application or gain unauthorized access.

Keeping application components updated is an important part of web application security.

## 3. Insufficient Logging and Monitoring

Insufficient Logging and Monitoring occurs when an application does not adequately record or monitor security-related activities.

Without proper logging and monitoring:

- Suspicious activities may remain undetected.
- Attack attempts may not be identified.
- Security incidents may be difficult to investigate.
- Detecting unauthorized access becomes more challenging.

## 4. Unvalidated Redirects and Forwards

Unvalidated Redirects and Forwards occur when an application redirects or forwards users without properly validating the destination.

An attacker may manipulate redirect parameters to send users to attacker-controlled websites.

This may be used for:

- Phishing attacks.
- Credential theft.
- Redirecting users to malicious websites.
- Distributing malware.

Unsafe forwards may also allow attackers to bypass access control mechanisms.

## 5. Directory Traversal

Directory Traversal is an attack that attempts to access files and directories outside the intended web application directory.

An attacker may manipulate file paths to access sensitive resources, including:

- Application source code.
- Configuration files.
- System files.
- Other restricted files and directories.

The vulnerability occurs when an application does not properly validate or restrict file path input.

## 6. Parameter Tampering

Parameter Tampering occurs when an attacker modifies parameters exchanged between a client and a server.

These parameters may contain information such as:

- User information.
- Product prices.
- Account-related values.
- Application settings.

If the server trusts modified client-side parameters without proper validation, an attacker may manipulate application behavior or gain unauthorized access.

Parameter tampering may also be used as part of other attacks, including injection attacks.

## 7. Improper Error Handling

Improper Error Handling occurs when an application reveals sensitive technical information through error messages.

Detailed error messages may expose information such as:

- Default account information.
- Database details.
- System functions.
- Internal file paths.
- Network information.

Attackers can use this information to understand the application's internal structure and identify potential weaknesses.

Applications should avoid exposing unnecessary technical details in error messages shown to users.

## 8. Cross-Site Request Forgery (CSRF)

Cross-Site Request Forgery (CSRF) is an attack that tricks an authenticated user's browser into sending an unauthorized request to a web application.

The attack takes advantage of the application's trust in the user's authenticated session.

When a user is logged in, the browser may automatically include existing session cookies with requests sent to the application.

An attacker may exploit this behavior to make the victim perform actions without their knowledge or consent.

## Related Links

- [OWASP Cross-Site Scripting (XSS)](https://owasp.org/www-community/attacks/xss/)
- [PortSwigger - Cross-Site Scripting](https://portswigger.net/web-security/cross-site-scripting)
- [OWASP Directory Traversal](https://owasp.org/www-community/attacks/Path_Traversal)
- [OWASP CSRF](https://owasp.org/www-community/attacks/csrf)
- [PortSwigger - CSRF](https://portswigger.net/web-security/csrf)
- [OWASP Error Handling](https://owasp.org/www-community/Improper_Error_Handling)

## Summary

This file covered additional web application threats, including XSS, vulnerable components, insufficient logging and monitoring, unvalidated redirects, directory traversal, parameter tampering, improper error handling, and CSRF.

These vulnerabilities can expose sensitive information, compromise user sessions, manipulate application behavior, and allow unauthorized actions.
