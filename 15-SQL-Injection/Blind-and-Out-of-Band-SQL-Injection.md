
# Blind and Out-of-Band SQL Injection

## Blind / Inferential SQL Injection

Blind SQL Injection, also known as Inferential SQL Injection, occurs when the application does not directly display the results of an injected SQL query.

Instead of returning useful database errors or query results, the application may display a customized response.

The attacker must infer information from indirect changes in the application's behavior.

This technique can be time-consuming because multiple requests may be required to discover individual characters or pieces of information.

The course identifies the following techniques:

## 1. Boolean-Based SQL Injection

Boolean-Based SQL Injection uses conditions that evaluate to TRUE or FALSE.

An attacker submits different conditions and observes how the application's response changes.

For example, the application may return different pages or responses depending on whether the injected condition is true or false.

By comparing these responses, an attacker can infer information about the database.

## 2. Time-Based SQL Injection

Time-Based SQL Injection relies on delays in the database response.

An attacker introduces a condition that causes the database to wait for a specified period when the condition is true.

By measuring the response time, the attacker can infer whether the condition was evaluated as true or false.

This approach is useful when the application does not provide visible differences in its responses.

## 3. Heavy Query Exploitation

Heavy Query Exploitation is also listed in the course's classification of Blind / Inferential SQL Injection.

The course does not provide a separate detailed explanation of this technique in the classification slide.

## Out-of-Band SQL Injection

Out-of-Band SQL Injection is a technique in which the attacker does not receive the results directly through the application's normal response.

Instead, the attacker uses another communication channel to obtain information.

For example, an injected query may trigger:

- A DNS request to an attacker-controlled domain.
- A ping or ICMP request.
- An HTTP connection.

The attacker can monitor these external requests to identify information about the database or determine whether the injected query was executed.

The term **Out-of-Band** refers to using a separate communication channel to discover or exploit a SQL Injection vulnerability.

## Comparison of SQL Injection Types

### In-Band SQL Injection

- Uses the same channel to send the attack and receive results.
- May return database errors or query results directly.
- Includes Error-Based and UNION SQL Injection.

### Blind / Inferential SQL Injection

- Does not directly display the injected query's results.
- Relies on indirect information from application behavior.
- Includes Boolean-Based and Time-Based techniques.

### Out-of-Band SQL Injection

- Uses a separate communication channel.
- May rely on DNS, ICMP, or HTTP requests.
- Does not require direct output in the application's response.

## Related Links

- [PortSwigger - Blind SQL Injection](https://portswigger.net/web-security/sql-injection/blind)
- [PortSwigger - Out-of-Band SQL Injection](https://portswigger.net/web-security/sql-injection/blind#exploiting-blind-sql-injection-by-triggering-conditional-responses)
- [OWASP - SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)

## Summary

SQL Injection attacks can be classified according to how the attacker receives information.

In-Band SQL Injection returns information through the normal application response. Blind SQL Injection relies on indirect observations, such as Boolean responses or time delays. Out-of-Band SQL Injection uses a separate communication channel to obtain information.
