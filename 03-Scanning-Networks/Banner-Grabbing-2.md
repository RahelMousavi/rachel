
# Countermeasures Against Banner Grabbing

Banner Grabbing allows attackers to collect information about services, software versions, and server configurations.

Organizations can reduce the amount of information exposed by their systems through proper server configuration and security practices.

## 1. Disable Unnecessary Services

Disable services that are not required for normal system operation.

Every unnecessary running service may expose additional information about the system and increase its attack surface.

Disabling unused services helps:

- Reduce exposed network services.
- Limit information disclosure.
- Reduce potential attack vectors.
- Improve overall system security.

## 2. Modify or Hide Server Banners

Web servers may disclose their software name and version through HTTP response headers.

For example:

```http
HTTP/1.1 200 OK
Server: Apache/2.4.XX
X-Powered-By: PHP/8.X
```

Administrators can configure servers to reduce or remove unnecessary version information.

The slide also mentions displaying misleading banners to confuse attackers.

However, deliberately presenting false information is not a substitute for properly securing and updating the server.

## 3. Use Server Security Tools

The slide introduces several tools for modifying or limiting server information:

- **IIS Lockdown:** A legacy Microsoft utility designed to improve the security configuration of IIS servers.
- **URLScan:** A legacy IIS security tool that filters HTTP requests according to configured rules.
- **ServerMask:** A tool historically used to modify server-identification information in HTTP responses.

**Note:** These tools are mentioned for understanding the course material. IIS Lockdown and URLScan are legacy tools and should not be treated as modern security recommendations. Prefer supported IIS security features and maintained server configurations.

## 4. Configure Apache Server Signature

Apache can expose server information through generated error pages and directory listings.

The slide recommends changing the following directive in the Apache configuration file:

```apache
ServerSignature On
```

to:

```apache
ServerSignature Off
```

### What Does ServerSignature Do?

`ServerSignature` controls whether Apache adds a footer containing server information to server-generated documents, such as error pages and directory listings.

- `On`: Displays the server signature.
- `Off`: Hides the server signature.
- `EMail`: Displays the server signature with a mail link.

**Important:** `ServerSignature Off` does not by itself remove the HTTP `Server` response header. That is controlled separately by `ServerTokens`.

## 5. Configure Apache ServerTokens

The slide recommends changing:

```apache
ServerTokens OS
```

to:

```apache
ServerTokens ProductOnly
```

### What Does ServerTokens Do?

`ServerTokens` controls how much information Apache reveals in the HTTP `Server` response header.

For example:

With detailed information:

```http
Server: Apache/2.4.XX (Unix)
```

With `ServerTokens ProductOnly`:

```http
Server: Apache
```

This reduces the amount of information exposed through the response header.

### Recommended Configuration

In the Apache configuration file (`httpd.conf`), use:

```apache
ServerSignature Off
ServerTokens Prod
```

`Prod` is the abbreviated form of `ProductOnly`.

**Note:** The slide refers to the configuration file as `http.conf`, but the commonly used Apache configuration filename is `httpd.conf`.

## 6. Disable PHP Version Exposure

PHP may reveal its presence and version through the `X-Powered-By` HTTP response header.

For example:

```http
X-Powered-By: PHP/8.2.XX
```

The slide recommends disabling the `expose_php` setting in the `php.ini` configuration file.

Change:

```ini
expose_php = On
```

to:

```ini
expose_php = Off
```

This prevents PHP from advertising its presence through the PHP-generated HTTP header.

## 7. Manage Web Page Extensions

The slide introduces two approaches for managing web page extensions on Apache and IIS.

### Apache — mod_negotiation

Apache's `mod_negotiation` module provides content negotiation.

One of its features is MultiViews, which can select a suitable resource based on a requested URL and available file variants.

Administrators should understand and configure this behavior carefully to avoid unintentionally exposing resources or alternative file representations.

### IIS — PageXchanger

PageXchanger is mentioned in the slide as a tool for managing web page extensions on IIS.

It is a legacy tool and should be treated as a historical example rather than a current security recommendation.

---

## Important Security Notes

- Hiding server banners reduces information disclosure but does not eliminate vulnerabilities.
- Attackers may identify software through other methods, even when version headers are hidden.
- Always keep web servers, applications, and operating systems updated.
- Disable unnecessary services and remove unused components.
- Avoid exposing detailed error messages and debugging information.
- Use supported security configurations instead of relying on outdated tools.

## Summary

The main countermeasures against Banner Grabbing include:

1. Disabling unnecessary services.
2. Reducing or removing server-identification information.
3. Using appropriate server security configurations.
4. Disabling Apache server signatures.
5. Limiting Apache version information with `ServerTokens`.
6. Disabling PHP version exposure with `expose_php = Off`.
7. Managing web server behavior and exposed file extensions.

### Important Configuration Commands

**Apache:**

```apache
ServerSignature Off
ServerTokens Prod
```

**PHP:**

```ini
expose_php = Off
```

These settings help reduce information disclosure, but they should be combined with proper patching, access control, and secure server configuration.

---

## Related Links

### Apache Configuration

- [Apache ServerTokens Directive](https://httpd.apache.org/docs/2.4/mod/core.html#servertokens) — Controls the information exposed in the HTTP Server response header.
- [Apache ServerSignature Directive](https://httpd.apache.org/docs/2.4/mod/core.html#serversignature) — Controls server signatures in generated error pages and directory listings.
- [Apache mod_negotiation](https://httpd.apache.org/docs/2.4/mod/mod_negotiation.html) — Documentation about content negotiation and MultiViews.

### PHP Configuration

- [PHP — Hiding PHP](https://www.php.net/manual/en/security.hiding.php) — Explains how to reduce PHP-related information disclosure.
- [PHP Core Configuration Directives](https://www.php.net/manual/en/ini.core.php) — Documentation for `expose_php` and other PHP configuration options.

### Microsoft IIS

- [IIS Request Filtering](https://learn.microsoft.com/en-us/iis/configuration/system.webserver/security/requestfiltering/) — Configure request filtering and other IIS security settings.
- [Configure Request Filtering in IIS](https://learn.microsoft.com/en-us/iis/manage/configuring-security/configure-request-filtering-in-iis) — Microsoft guidance for configuring request filtering.

### General Web Security

- [OWASP Secure Configuration Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Configuration_Cheat_Sheet.html) — Security configuration recommendations for applications and infrastructure.
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) — Security configuration recommendations for operating systems, servers, and applications.
