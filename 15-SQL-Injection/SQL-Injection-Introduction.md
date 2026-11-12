
# SQL Injection Introduction

## What Is SQL Injection?

SQL Injection (SQLi) is a web application vulnerability that occurs when an application does not properly validate user input before including it in SQL queries.

Web applications often communicate with databases by sending SQL commands. When user input is directly included in these commands without proper validation, an attacker may manipulate the original query and execute unintended SQL statements.

SQL Injection is an unauthorized database access attack that may allow attackers to retrieve information from a database.

An important point is that the vulnerability exists in the **web application**, not in the database or web server itself.

## How SQL Injection Works

A typical web application receives user input through forms or other input fields. The application processes this input and may use it to construct an SQL query.

The query is then sent to the database server for execution.

If the application does not properly validate user input, an attacker may provide specially crafted input that changes the intended SQL query.

As a result, the database may execute a query that was not originally intended by the application developer.

The general process is:

1. A user submits input to a web application.
2. The application processes the submitted input.
3. The application sends an SQL query to the database.
4. The database executes the query.
5. The application receives the database response.

In a vulnerable application, manipulated input can change the behavior of the SQL query.

## Impact of SQL Injection

SQL Injection attacks may affect the confidentiality, integrity, and availability of a database and its associated systems.

### 1. Authentication Bypass

Attackers may bypass application authentication mechanisms without providing a valid username or password.

### 2. Information Disclosure

Attackers may retrieve sensitive information stored in the database, including information they are not authorized to access.

### 3. Compromising Data Integrity

Attackers may modify database information, deface websites, or inject malicious content into applications.

### 4. Compromising Availability

Attackers may delete database information, events, or other stored data, making it unavailable to legitimate users.

### 5. Remote Code Execution

In some cases, SQL Injection may lead to remote code execution and potentially allow attackers to gain control of the host operating system.

## Related Links

- [OWASP - SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [PortSwigger - SQL Injection](https://portswigger.net/web-security/sql-injection)

## Summary

SQL Injection is a vulnerability in web applications that allows attackers to manipulate SQL queries through improperly handled user input.

Depending on the vulnerability and the application's configuration, its consequences may include authentication bypass, information disclosure, data manipulation, data deletion, and potentially remote code execution.
