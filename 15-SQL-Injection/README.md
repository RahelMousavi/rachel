
# Module 15: SQL Injection

## Overview

SQL Injection (SQLi) is a web application vulnerability that occurs when user input is not properly validated or sanitized before being included in SQL queries.

It allows attackers to manipulate database queries through vulnerable web applications. Depending on the application's implementation and database permissions, SQL Injection may lead to unauthorized data access, authentication bypass, data manipulation, or even remote code execution.

This module covers SQL Injection concepts, attack types, exploitation methodology, tools, evasion techniques, and countermeasures.

## Learning Objectives

By completing this module, you will understand:

- How SQL Injection vulnerabilities occur.
- How web applications communicate with databases.
- Different types of SQL Injection attacks.
- How to identify potential SQL Injection vulnerabilities.
- How attackers exploit SQL Injection flaws.
- Tools used for SQL Injection testing.
- Techniques used to evade signature-based detection.
- Methods for preventing and mitigating SQL Injection attacks.

## Module Structure

### 01. SQL Injection Concepts

- Introduction to SQL Injection
- How SQL Injection Works
- Web Application and Database Communication
- HTTP POST Requests
- Normal and Malicious SQL Queries
- SQL UPDATE and INSERT Statements

### 02. Types of SQL Injection

- In-Band SQL Injection
  - Error-Based SQL Injection
  - System Stored Procedure
  - Illegal / Logically Incorrect Query
  - UNION SQL Injection
  - Tautology
  - End-of-Line Comment
  - Inline Comments
  - Piggybacked Query
- Blind / Inferential SQL Injection
  - Boolean-Based SQL Injection
  - Time-Based SQL Injection
- Out-of-Band SQL Injection

### 03. SQL Injection Methodology

- Information Gathering
- Identifying Input Fields and Data Entry Points
- Extracting Information Through Errors
- Detecting SQL Injection Vulnerabilities
- Source Code Analysis
- Launching SQL Injection Attacks
  - UNION-Based SQL Injection
  - Bypassing Website Logins
  - Blind SQL Injection

### 04. SQL Injection Tools

- SQL Injection Tools Overview
- SQLmap
- SQL Injection Tools for Mobile Devices
  - Droid SQLi
  - SQL Map Chik
- Checking SQL Injection with AI

### 05. SQL Injection Evasion Techniques

- Introduction to Signature-Based Detection
- Using SQL Comments
- Using the CHAR() Function
- Adding Whitespace
- Using Mixed Letter Cases
- Hexadecimal Encoding
- Replacing Common SQL Conditions

### 06. SQL Injection Countermeasures

- Input Validation
- Data Type and Length Restrictions
- Secure SQL Query Construction
- Stored Procedures
- Avoiding Dynamic SQL
- Secure Configuration Files
- Least Privilege for Database Accounts
- Intrusion Detection Systems
- Security Testing and Source Code Analysis

## Lab Environment

Practical SQL Injection testing should be performed only in authorized environments.

Suggested practice environments:

- [DVWA](https://github.com/digininja/DVWA)
- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security/sql-injection)

## Related Links

- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [PortSwigger - SQL Injection](https://portswigger.net/web-security/sql-injection)
- [SQLmap Documentation](https://sqlmap.org/)
- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)

## Summary

This module explores SQL Injection from both offensive and defensive perspectives.

It begins with the fundamental concepts and different types of SQL Injection, then covers information gathering, vulnerability detection, exploitation techniques, and testing tools.

Finally, it examines evasion techniques and security measures that help prevent SQL Injection vulnerabilities.
