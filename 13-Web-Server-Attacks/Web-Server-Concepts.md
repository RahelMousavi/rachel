
# Web Server Concepts

## 1. Web Server Operations

A **Web Server** is a computer or software system that stores and processes web pages and delivers them to clients through the HTTP protocol.

When a client requests a web page, the web server processes the request and returns an appropriate HTTP response.

### Basic Web Server Architecture

A typical web server environment may contain the following components:

- **Web Client:** Sends HTTP requests to the web server and receives responses.
- **Web Server:** Processes client requests and serves static content.
- **Static Data Store:** Stores static resources such as HTML files, images, and CSS files.
- **Application Server:** Processes application-related requests and executes application logic.
- **Web Container:** Provides an environment for running web components.
- **Application Data Store:** Stores data used by web applications.

The web server may communicate with an application server when a request requires dynamic processing.

## 2. Components of a Web Server

### Document Root

The **Document Root** is the directory where files related to website pages are stored.

When a client requests a web resource, the web server retrieves the corresponding file from this directory and returns it to the client.

### Server Root

The **Server Root** contains important server-related files, including:

- Server configuration files
- Error messages
- Executable files
- Log files

### Virtual Document Tree

A **Virtual Document Tree** provides access to storage located on another machine or disk.

It can be used when the capacity of the primary disk is insufficient and additional storage is required.

### Virtual Hosting

**Virtual Hosting** is a technique that allows multiple domain names to be hosted on a single web server.

This makes it possible to host multiple websites using the same server infrastructure.

### Web Proxy

A **Web Proxy** acts as an intermediary between a web client and a web server.

Client requests are sent to the proxy, which forwards them to the destination server.

Web proxies can be used for purposes such as:

- Hiding the client's original IP address from the destination server.
- Managing and filtering web requests.
- Helping users access resources when direct access is restricted.

## 3. Why Are Web Servers Vulnerable?

Web servers may become vulnerable due to security weaknesses in their configuration, software, maintenance, and access controls.

Common reasons include:

### Lack of Security Policies

The absence of proper security policies, procedures, and maintenance operations can lead to unmanaged security risks.

### Improper Configuration

Incorrect server configuration, especially when default installation settings are left unchanged, may expose sensitive services and information.

### Software Vulnerabilities

Security weaknesses may exist in:

- Server software
- Operating systems
- Web applications

### Missing Security Patches

Failure to install security patches on time leaves known vulnerabilities unaddressed.

### Default Files and Configurations

Default files, sample applications, and configuration settings may reveal information or provide unnecessary access to attackers.

### Incorrect File and Directory Permissions

Improper permissions may allow unauthorized users to read, modify, or execute files and directories.

### Unnecessary Services

Running services that are not required increases the server's attack surface.

### Improper Authentication

Weak authentication mechanisms may allow unauthorized users to gain access to server resources.

### Default Accounts and Passwords

Using default accounts with default passwords or accounts without passwords creates opportunities for unauthorized access.

## 4. Apache Vulnerabilities

**Apache HTTP Server** is a widely used web server. The PDF presents several examples of vulnerabilities related to Apache and Apache-based components.

### HTTP Response Splitting

Occurs when improperly validated input allows an attacker to inject malicious headers into HTTP responses.

Potential consequences include:

- Cross-Site Scripting (XSS)
- Cache poisoning
- Sensitive information disclosure

### HTTP/2 DoS by Memory Exhaustion on Endless Continuation Frames

This vulnerability involves sending continuous HTTP/2 headers and excessive CONTINUATION frames.

It may cause excessive memory consumption and make the server unresponsive or crash.

### mod_macro Buffer Over-read

Occurs when the `mod_macro` module handles macro expansion improperly.

An attacker may exploit crafted requests to access sensitive adjacent memory.

### DoS in HTTP/2 with Initial Window Size 0

An attacker manipulates the HTTP/2 initial window size to zero.

This can block data transmission and potentially cause a denial-of-service condition.

### HTTP/2 Stream Memory Not Reclaimed Right Away on RST

Occurs when memory associated with an HTTP/2 stream is not released after a reset.

This may lead to memory exhaustion and denial of service.

### Insecure Default Configuration

Insecure default administrative credentials may allow attackers to gain access and potentially execute remote code.

### Improper Authorization

Improper authorization in Apache Submarine server components may allow attackers to exploit privilege checks and perform unauthorized actions.

### DNS Rebinding in Import Functionality

Insufficient input validation may allow attackers to manipulate DNS responses and access internal services.

### Path Traversal

Improper directory path limitations may allow attackers to access files outside the intended directory.

This can expose sensitive information or potentially allow code execution.

### SQL Injection

Improper neutralization of SQL elements may allow attackers to execute unauthorized SQL queries and manipulate data.

## 5. IIS Vulnerabilities

**Internet Information Services (IIS)** is Microsoft's web server platform.

The PDF presents the following examples of vulnerabilities associated with IIS and related applications:

### Trust Boundary Violation

Inadequate privilege separation in Teleric Report Server may allow unauthenticated users to access and manipulate restricted functionality.

### Authentication Bypass

A weakness in the authentication process may allow attackers to access restricted functions and execute arbitrary code on the server.

### CRLF Cross-Site Scripting Vulnerability

Misconfiguration in the SiteMinder Web Agent for IIS may allow attackers to execute arbitrary JavaScript in a client's browser.

### C-CURE Passwords Exposed to Administrators

Improper handling and logging may expose sensitive information within an IIS Server hosting the C-CURE 9000 Web Server.

### Arbitrary File Path Access

An insecure default configuration in Aquaforest TIFF Server may allow attackers to access, enumerate, or traverse directories and files.

### Windows IIS Server Elevation of Privilege

Improper handling of user requests may allow attackers to gain unauthorized access and control over the system.

### File and Directory Permissions Vulnerability

Incorrect default permissions in Hitachi JP1/Performance Management may allow attackers to manipulate files and directories without authorization.

### TYPO3 Cross-Site Scripting (XSS)

Unfiltered use of the server environment variable `PATH_INFO` in the `GeneralUtility::getIndpEnv()` function may allow attackers to inject malicious HTML into uncached pages.

### MailEnable Vulnerability

Improper handling of file paths may allow authenticated mail users to add files containing unauthorized content to public folders.

### XSS in Password Manager

Improper neutralization of user-controllable input in the `isapi/PasswordManager.dll` component may allow unauthorized code injection and exposure of sensitive information.

## 6. Nginx Vulnerabilities

**Nginx** is a web server that can also be used as a reverse proxy and load balancer.

The PDF presents the following examples of vulnerabilities related to Nginx and associated components:

### NULL Pointer Dereference in HTTP/3

A NULL pointer dereference in Nginx's QUIC module may cause denial of service or potentially remote code execution.

### Server-Side Request Forgery (SSRF)

An SSRF vulnerability may allow attackers to make requests to internal or otherwise restricted resources through a vulnerable server-side application.

### Remote Code Execution

Exposed configuration settings in Nginx-UI may allow attackers to perform remote code execution, privilege escalation, or information disclosure.

### Improper Certificate Validation

Improper input validation in the Nginx-UI Import Certificate feature may allow attackers to perform unauthorized file writes.

### SQL Injection

Improper neutralization of SQL elements may allow attackers to execute arbitrary SQL queries, potentially resulting in unauthorized access or data breaches.

### Unauthenticated Private Keys Access

If private key files are accessible without authentication, attackers may be able to read sensitive cryptographic material.

### Excessive Memory Usage and CPU Consumption in HTTP/2

Improper memory handling and excessive CPU usage during HTTP/2 requests may allow attackers to disrupt server operations through resource exhaustion.

### OS Command Injection in NginxWebUI

Improper handling of file arguments in the upload feature may allow attackers to inject and execute operating system commands remotely.

### Default File Permissions Vulnerability

Insecure default file permissions in Nginx Management Suite may allow attackers to modify sensitive files.

## Related Links

### Web Server Documentation

- [Apache HTTP Server Documentation](https://httpd.apache.org/docs/)
- [Apache Security Reports](https://httpd.apache.org/security_report.html)
- [Microsoft IIS Documentation](https://learn.microsoft.com/en-us/iis/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Nginx Security Advisories](https://nginx.org/en/security_advisories.html)

### Web Security References

- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE - Common Weakness Enumeration](https://cwe.mitre.org/)

## Summary

- A web server stores and processes web resources and delivers them to clients through HTTP.
- Important web server components include Document Root, Server Root, Virtual Document Tree, Virtual Hosting, and Web Proxy.
- Web servers may be vulnerable because of improper configuration, outdated software, weak authentication, incorrect permissions, and unnecessary services.
- Apache, IIS, and Nginx may be affected by different vulnerability classes.
- Common vulnerability types include SQL Injection, XSS, Path Traversal, SSRF, Authentication Bypass, Remote Code Execution, and Denial of Service.
- Proper configuration, regular updates, secure authentication, and access control are essential for web server security.
