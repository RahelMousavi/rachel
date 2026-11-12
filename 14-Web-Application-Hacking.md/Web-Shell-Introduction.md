
# Web Shell

## 1. Introduction to Web Shells

A Web Shell is a malicious script installed on a web server that provides an attacker with remote access to the server.

It allows attackers to interact with the compromised server through a web interface and perform different operations.

Web shells can be written in various server-side scripting languages, including:

- Ruby
- Perl
- ASP
- PHP
- Python

## 2. Web Shell Capabilities

Once installed on a vulnerable web server, a Web Shell may provide attackers with the ability to:

- Remotely access and manage the server.
- Interact with the server's file system.
- Execute operations on the compromised server.
- Access or manipulate files and directories.

Web shells are dangerous because they may allow attackers to maintain access to a compromised web server through ordinary web requests.

## 3. Web Shell Installation

A Web Shell must be placed on the target web server before it can be accessed.

A vulnerable application may provide an opportunity for an attacker to upload or otherwise place a malicious server-side script on the server.

If the server executes the uploaded script, the attacker may be able to interact with it remotely.

## Related Links

- [MITRE ATT&CK - Web Shell](https://attack.mitre.org/techniques/T1505/003/)
- [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
- [Microsoft Security - Web Shell Threats](https://www.microsoft.com/en-us/security/blog/)

## Summary

A Web Shell is a malicious server-side script that provides remote access to a compromised web server.

It may allow attackers to execute operations and interact with the server's file system. Web shells can be developed using different server-side scripting languages, such as PHP, ASP, Python, Perl, and Ruby.
