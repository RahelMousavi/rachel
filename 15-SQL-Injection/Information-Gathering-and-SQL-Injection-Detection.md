
# Information Gathering and SQL Injection Detection

## Introduction

Information Gathering is an important step in SQL Injection testing.

The purpose of this phase is to identify how a web application communicates with its database, discover user input points, and collect information that may help identify SQL Injection vulnerabilities.

## 1. Monitoring Web Application and Database Communication

During information gathering, the communication between the web application and the database is examined.

The objective is to understand how submitted information is processed and how the application accesses database records.

Monitoring and analyzing this communication can help identify potential injection points.

## 2. Identifying Input Fields

All user input fields should be identified and examined.

These fields may include:

- Login forms
- Search fields
- Registration forms
- Other data entry fields

It is also important to identify the HTTP requests used to submit information.

Both GET and POST requests should be analyzed to discover all possible data entry points.

## 3. Analyzing GET and POST Requests

GET and POST requests may contain parameters that are processed by the web application.

An attacker or penetration tester can examine these parameters to identify potential SQL Injection entry points.

Tools such as Burp Suite can be used to intercept and manipulate HTTP requests during authorized testing.

## 4. Extracting Information Through Errors

Database error messages can reveal useful information about the underlying database and application.

Depending on the error, the disclosed information may include:

- Operating system information
- Database type
- Database version
- Details about the executed query

These errors can help determine which testing techniques may be appropriate.

### Generating Database Errors

During authorized testing, input parameters can be modified to observe how the application responds.

The course mentions the following examples:

**Testing with a single quotation mark:**

```sql
'
```

A single quotation mark may cause an error if the input is directly incorporated into an SQL query.

**Testing Boolean conditions:**

```sql
AND 1=1
```

```sql
AND 1=2
```

The responses can be compared to determine whether the application behaves differently when the condition is true or false.

These tests may help identify parameters that are potentially vulnerable to SQL Injection.

## 5. Preparing a List of Input Parameters

After gathering information and identifying input fields, prepare a list of all discovered inputs.

Each parameter should be tested for possible SQL Injection vulnerabilities.

This helps ensure that the testing process covers the application's different data entry points.

## 6. Source Code Analysis

Source code analysis is another method for identifying SQL Injection vulnerabilities.

By examining the application's source code, developers and security testers can identify sections where user input may be improperly incorporated into SQL queries.

This analysis can be performed manually or with specialized tools.

The course mentions the following tools:

- Veracode
- RIPS
- PVS-Studio
- Coverity Scan
- Parasoft Jtest
- CAST Application Intelligence Platform
- Klocwork

## Related Links

- [Burp Suite Documentation](https://portswigger.net/burp/documentation)
- [OWASP - SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [OWASP - Code Review Guide](https://owasp.org/www-project-code-review-guide/)

## Summary

Information gathering and vulnerability detection involve identifying input fields, analyzing GET and POST requests, examining database errors, and testing application parameters.

Source code analysis can also help locate vulnerable sections before an SQL Injection attack is attempted.
