
# SQL Injection Tools Overview

## Introduction

Various tools are available to help security professionals identify and test SQL Injection vulnerabilities.

These tools can assist with detecting injection points, analyzing database responses, and testing different SQL Injection techniques.

The course introduces the following tools:

- SQLmap
- BSQLHacker
- Marathon Tool
- SQL Power Injector
- Bsql
- NoSQLMap
- SQL Brute
- Fatcat-SQL-Injector
- SQL ninja
- SQL get
- Absinthe
- Blind SQL Injection Brute Forcer
- Dark Jumper
- Pangolin
- SQL PAT
- Automagic SQL Injector
- The Mole
- SQL Poizon

## SQLmap

SQLmap is an open-source penetration testing tool designed to detect and exploit SQL Injection vulnerabilities.

It automates several SQL Injection testing and database enumeration tasks.

According to the course, SQLmap can be used to:

- Identify SQL Injection vulnerabilities.
- Enumerate database names.
- Enumerate database tables.
- Retrieve column information.
- Extract data from database tables.

### Basic SQLmap Commands

The following commands are presented in the course.

**1. Enumerating databases**

```bash
sqlmap -u "http://site.com/listproducts.php?cat=1" --dbs --level
```

**2. Enumerating tables in a database**

```bash
sqlmap -u "http://site.com/listproducts.php?cat=1" -D <db_name> --tables
```

**3. Enumerating columns in a table**

```bash
sqlmap -u "http://site.com/listproducts.php?cat=1" -D <db_name> -T <table_name> --columns
```

**4. Extracting table data**

```bash
sqlmap -u "http://site.com/listproducts.php?cat=1" -D <db_name> -T <table_name> -C <column_name> --dump
```

### Understanding the Options

- `-u`: Specifies the target URL.
- `--dbs`: Retrieves database names.
- `-D`: Specifies a database.
- `--tables`: Retrieves table names.
- `-T`: Specifies a table.
- `--columns`: Retrieves column names.
- `-C`: Specifies a column.
- `--dump`: Retrieves data from the selected table or columns.
- `--level`: Controls the level of testing.

**Note:** The first command is reproduced as shown in the course. It does not specify a numeric value for `--level`.

## Related Links

- [SQLmap Official Website](https://sqlmap.org/)
- [SQLmap GitHub Repository](https://github.com/sqlmapproject/sqlmap)
- [SQLmap Usage Documentation](https://github.com/sqlmapproject/sqlmap/wiki/Usage)

## Summary

SQL Injection tools help security professionals identify and analyze SQL Injection vulnerabilities.

SQLmap is one of the tools introduced in this module. It automates vulnerability testing and provides options for database, table, and column enumeration, as well as data extraction.

All testing should be performed only against systems for which explicit authorization has been granted.
