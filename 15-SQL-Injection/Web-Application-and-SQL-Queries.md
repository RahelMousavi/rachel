
# Web Application and SQL Queries

## Web Application and Database Communication

Web applications commonly use databases to store and retrieve information.

When a user interacts with a web application, the browser sends a request to the web server. The application processes the request and communicates with the database when information needs to be stored or retrieved.

The database processes the SQL query and returns its result to the application.

The application can then use the returned information to generate a response for the user.

Understanding this communication process is important because SQL Injection occurs when user input is improperly included in database queries.

## HTTP POST Requests

HTTP POST is a method used to communicate with a web service and send information to a web server.

When a user fills in fields on a web page and clicks the Submit button, the browser sends a request to the web server.

For example, when a user submits a login form, the request contains the submitted username and password.

The web application receives the submitted information and may use it to communicate with the database.

POST requests are therefore important when examining web application input fields during SQL Injection testing.

## Normal and Malicious SQL Queries

Web applications use SQL queries to interact with databases.

A normal SQL query performs an operation intended by the application, such as retrieving information based on user input.

A maliciously manipulated query attempts to change the original query's intended behavior.

In SQL Injection, an attacker provides specially crafted input that may alter the SQL statement constructed by the application.

This can cause the database to perform unintended operations or return information that should not be accessible.

## SQL UPDATE Statement

The SQL UPDATE statement is used to modify existing records in a database.

In the context of SQL Injection, an improperly constructed UPDATE query may allow an attacker to manipulate the data modification operation.

This can compromise the integrity of database records.

## SQL INSERT Statement

The SQL INSERT statement is used to add new records to a database.

If user input is improperly handled when constructing an INSERT query, an attacker may be able to manipulate the data being inserted.

This may result in unauthorized or malicious content being added to the database.

## Related Links

- [MDN - HTTP Request Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods)
- [MySQL - UPDATE Statement](https://dev.mysql.com/doc/refman/8.4/en/update.html)
- [MySQL - INSERT Statement](https://dev.mysql.com/doc/refman/8.4/en/insert.html)

## Summary

Web applications communicate with databases through SQL queries. HTTP POST requests are commonly used to submit information from forms to web servers.

SQL Injection occurs when an application improperly incorporates user input into SQL queries, potentially changing their intended behavior.

The UPDATE and INSERT statements are examples of database operations that can be affected by improperly handled input.
