
# In-Band SQL Injection

## Introduction

In-Band SQL Injection is a type of SQL Injection in which an attacker uses the same communication channel to launch the attack and retrieve its results.

The attacker sends malicious SQL input through the web application and receives the database response through the application's normal response channel.

The following techniques are covered in this category.

## 1. Error-Based SQL Injection

Error-Based SQL Injection involves submitting abnormal input to generate database errors.

These errors may reveal useful information about the database, its structure, and the queries being executed.

An attacker can analyze the error messages and use the information they disclose to develop further SQL Injection attacks.

## 2. System Stored Procedure

Stored procedures are database routines that can be executed by an application.

If a web application does not properly sanitize user input before using it in stored procedures, attackers may be able to manipulate the queries.

For example, the course demonstrates an input such as:

```sql
anyuser OR 1=1
```

This type of condition may allow authentication to succeed without providing a valid password, depending on how the application constructs and executes the query.

## 3. Illegal / Logically Incorrect Query

In this technique, an attacker submits invalid input to generate database errors.

The resulting errors may help reveal information about the application's query structure, including table or column names.

For example, submitting a username containing an unmatched single quotation mark may cause a database error.

The attacker can analyze the error to understand how the application processes the input.

## 4. UNION SQL Injection

UNION SQL Injection uses the SQL UNION operator to combine the results of two or more SELECT statements.

An attacker may exploit this behavior to retrieve information from other database tables through a vulnerable query.

The technique can be used to obtain information that the application does not normally display.

## 5. Tautology

A tautology is a condition that always evaluates to TRUE.

In SQL Injection, attackers may use OR expressions to create conditions that are always true.

This may change the logic of the original query and potentially allow unauthorized access or information extraction.

## 6. End-of-Line Comment

SQL comments can be used to make the database ignore the remaining part of a query.

In this technique, an attacker places a comment marker at the end of an input to remove the rest of the developer's SQL statement from execution.

For example, this may allow an attacker to bypass a password condition in a vulnerable login query.

## 7. Inline Comments

Inline comments are comments placed within an SQL statement.

They may be used to separate or hide parts of SQL commands and parameters.

Attackers can use inline comments to bypass certain restrictions or modify how SQL statements are interpreted.

## 8. Piggybacked Query

Piggybacked Query attacks involve appending an additional SQL query to the original query.

A statement separator, such as a semicolon, may be used to separate the original query from the injected query.

If the database executes both statements, the additional query may perform unauthorized operations.

Depending on the database and application configuration, attackers may use statements such as:

- `DROP`
- `UPDATE`
- `INSERT`
- `DELETE`

These operations can be used to modify or delete database information.

## Related Links

- [OWASP - SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [PortSwigger - SQL Injection](https://portswigger.net/web-security/sql-injection/union-attacks)
- [MySQL - UNION Clause](https://dev.mysql.com/doc/refman/8.4/en/union.html)

## Summary

In-Band SQL Injection uses the same communication channel to send malicious input and receive database results.

Its techniques include Error-Based SQL Injection, System Stored Procedure, Illegal / Logically Incorrect Query, UNION SQL Injection, Tautology, End-of-Line Comment, Inline Comments, and Piggybacked Query.
