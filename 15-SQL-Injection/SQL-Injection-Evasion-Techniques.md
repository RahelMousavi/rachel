
# SQL Injection Evasion Techniques

## 1. Using SQL Comments

SQL comments can be inserted between SQL statements or keywords.

Attackers may use comments to modify the appearance of SQL input strings and attempt to bypass signature-based detection.

## 2. Using the CHAR() Function

The `CHAR()` function can represent characters using their numeric character codes.

Instead of writing a character directly, an attacker may use the function to represent it in another form.

This changes the representation of the input string.

## 3. Adding Whitespace

Whitespace can be added between SQL statements or keywords.

This modifies the structure and appearance of the submitted SQL input.

## 4. Using Mixed Letter Cases

SQL keywords can be written using a combination of uppercase and lowercase letters.

For example:

```sql
Union SelEcT
```

This changes the appearance of SQL keywords while retaining their recognizable structure.

## 5. Hexadecimal Encoding

Characters can be represented using hexadecimal values.

The course demonstrates hexadecimal representation using the `0x` prefix.

This technique changes how characters are represented in the input string.

## 6. Replacing Common SQL Conditions

Attackers may replace commonly used SQL conditions with alternative expressions that have equivalent logical results.

The course provides the following examples:

```sql
'Microsoft' = 'micro'+'soft'
```

```sql
'john' = 'john'
```

These expressions demonstrate how an attacker may replace a familiar condition with another expression.

## Related Links

- [PortSwigger - SQL Injection](https://portswigger.net/web-security/sql-injection)
- [OWASP - SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [OWASP - SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)

## Summary

SQL Injection evasion techniques modify the representation of SQL input strings.

The techniques covered in this section include SQL comments, the `CHAR()` function, whitespace manipulation, mixed letter cases, hexadecimal encoding, and replacing common SQL conditions.

These techniques demonstrate why relying only on signature-based detection is not sufficient for protecting web applications.
