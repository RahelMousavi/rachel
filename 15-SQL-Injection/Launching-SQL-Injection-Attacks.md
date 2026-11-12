
# Launching SQL Injection Attacks

## Introduction

After gathering information and identifying potential SQL Injection vulnerabilities, the next step is to examine how the vulnerability can be exploited.

The course covers several attack techniques, including UNION-based SQL Injection, authentication bypass, and Blind SQL Injection.

The examples below are based on the course material and should only be tested in authorized lab environments.

## 1. UNION-Based SQL Injection

UNION-based SQL Injection uses the SQL UNION operator to combine the results of an injected SELECT statement with the results of the original query.

The course demonstrates the following steps using MySQL.

### Step 1: Identify the Injection Point

A single quotation mark can be added to an input parameter to observe whether the application produces an SQL error.

This may indicate that the parameter interacts with an SQL query.

### Step 2: Determine the Number of Columns

The `ORDER BY` clause can be used to determine the number of columns returned by the original query.

Example from the course:

```sql
ORDER BY 5
```

### Step 3: Test UNION Compatibility

After determining the number of columns, a UNION SELECT statement can be tested.

Example:

```sql
UNION SELECT 1,2,3,4,5
```

The number of selected values should correspond to the number of columns in the original query.

### Step 4: Enumerate Database Tables

The course demonstrates using the `information_schema.tables` metadata table and the `database()` function to retrieve table information.

Example:

```sql
SELECT group_concat(table_name)
FROM information_schema.tables
WHERE table_schema = database()
```

### Step 5: Enumerate Database Columns

After identifying tables, column information can be retrieved from `information_schema.columns`.

This helps identify the structure of the selected database tables.

### Step 6: Retrieve Column Data

Once the required tables and columns have been identified, their data can be queried.

The course also includes identifying an administrator page as part of this attack process.

## 2. SQL Injection in Microsoft SQL Server

The course also presents UNION-based SQL Injection examples for Microsoft SQL Server.

The examples use SQL Server-specific functions and system objects.

### Retrieving SQL Server Information

```sql
SELECT @@VERSION
```

### Identifying the Current Database

```sql
SELECT DB_NAME()
```

### Enumerating Databases

The course demonstrates querying:

```sql
master..sysdatabases
```

### Enumerating Database Objects

The following system objects are included in the examples:

- `sysobjects`
- `syscolumns`

The course also demonstrates retrieving information from a table named `products`.

**Note:** These examples use Microsoft SQL Server syntax and should not be treated as interchangeable with the MySQL examples above.

## 3. Bypassing Website Logins

Authentication bypass is one of the methods used to test SQL Injection vulnerabilities.

Attackers may try different inputs in application fields, especially username and password fields, to determine whether the application improperly handles SQL input.

If the application's authentication query is vulnerable, manipulated input may change the query's logic and allow access without valid credentials.

## 4. Blind SQL Injection

Blind SQL Injection is used when the application does not directly display the results of injected queries.

Instead, information is inferred from changes in application behavior or response time.

The course demonstrates several techniques.

### Boolean-Based Testing

Conditional expressions can be used to determine whether specific statements are true or false.

Examples from the course include:

```sql
LENGTH(database())
```

```sql
ASCII(SUBSTR(...))
```

These expressions can be used to test database name length and character values.

The course also demonstrates testing the number and names of database tables through conditional queries.

### Time-Based Testing

Time delays can be used to infer the result of a condition.

MySQL example:

```sql
SLEEP(5)
```

A conditional expression can also be used to trigger a delay only when a particular condition is true.

### Microsoft SQL Server Time-Based Testing

The course demonstrates using `WAITFOR DELAY` with SQL Server.

Examples include:

```sql
WAITFOR DELAY '0:0:5'
```

It also demonstrates using:

- `LEN(DB_NAME())`
- `ASCII(SUBSTRING(...))`

These expressions can be combined with conditional delays to infer information from the database.

## Related Links

- [PortSwigger - UNION SQL Injection](https://portswigger.net/web-security/sql-injection/union-attacks)
- [PortSwigger - Blind SQL Injection](https://portswigger.net/web-security/sql-injection/blind)
- [MySQL - INFORMATION_SCHEMA](https://dev.mysql.com/doc/refman/8.4/en/information-schema.html)
- [Microsoft - SQL Server System Catalog Views](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql)

## Summary

SQL Injection exploitation follows information gathering and vulnerability detection.

The course demonstrates UNION-based attacks for MySQL and Microsoft SQL Server, authentication bypass techniques, and Blind SQL Injection using Boolean conditions and time delays.

The examples illustrate how database information can be enumerated and how vulnerable application behavior can be analyzed during authorized security testing.
