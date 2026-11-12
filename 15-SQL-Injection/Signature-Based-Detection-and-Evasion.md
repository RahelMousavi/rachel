
# Signature-Based Detection and Evasion

## Introduction

Attackers use evasion techniques to hide malicious input strings from Intrusion Detection Systems (IDS).

One of the detection approaches used by security systems is signature-based detection.

## Signature-Based Detection

Signature-based detection works by comparing incoming input strings against a database of known attack signatures.

When an input matches a known signature, the security system may identify it as malicious and detect or block the attack.

However, attackers may modify the appearance of SQL statements to make them less recognizable to signature-based detection systems.

These modifications are known as SQL Injection evasion techniques.

## SQL Injection Evasion Techniques

The course introduces several techniques that attackers may use to modify SQL input strings.

The following techniques are covered:

- Using SQL comments
- Using the `CHAR()` function
- Adding whitespace
- Using mixed letter cases
- Hexadecimal encoding
- Replacing common SQL conditions

## Related Links

- [OWASP - SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [OWASP - Web Application Firewall](https://owasp.org/www-community/Web_Application_Firewall)
- [PortSwigger - SQL Injection](https://portswigger.net/web-security/sql-injection)

## Summary

Signature-based detection identifies potentially malicious input by comparing it against known attack signatures.

SQL Injection evasion techniques attempt to modify the representation of SQL statements so that they may avoid detection by signature-based security systems.
