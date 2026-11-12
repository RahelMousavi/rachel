
# Web Shell Prevention and Detection

## 1. Web Shell Prevention

Preventing Web Shell installation requires securing the web server, application, and file-handling mechanisms.

The module recommends the following security measures:

### 1.1 Keep Systems Updated

- Regularly patch the host operating system.
- Keep web applications and their components updated.
- Perform regular vulnerability assessments.

### 1.2 Secure the Web Server

- Place public-facing web servers in a Demilitarized Zone (DMZ).
- Disable unnecessary ports and services.
- Use firewalls to restrict unwanted network traffic.
- Disable directory browsing.
- Review user accounts and permissions regularly.

### 1.3 Strengthen Authentication

- Use strong authentication mechanisms.
- Avoid default passwords.
- Restrict access to administrative functions.

### 1.4 Validate User Input

- Validate and sanitize user input.
- Secure file upload forms.
- Restrict permitted file extensions.
- Do not execute untrusted uploaded files.

### 1.5 Disable Unnecessary PHP Functions

The module recommends disabling potentially risky PHP functions when they are not required.

Examples include:

- `exec`
- `pcntl_exec`
- `shell_exec`
- `show_source`
- `proc_open`
- `passthru`

Disabling unnecessary functions can reduce the capabilities available to malicious scripts.

### 1.6 Avoid Untrusted Code

Avoid using untrusted code in web applications and ensure that application components come from reliable sources.

## 2. Web Shell Detection Tools

The module introduces the following tools for detecting and identifying Web Shells:

### 2.1 Web Shell Detector

A tool designed to help identify suspicious Web Shell files on web servers.

### 2.2 FireEye Network Security

A network security solution that can help detect malicious activity and threats associated with compromised systems.

### 2.3 NeoPI

A tool used to identify potentially malicious PHP scripts through static analysis.

### 2.4 AntiShell Web Shell Hunter

A tool designed to detect Web Shells on web servers.

### 2.5 Astra

A web security solution that provides security assessment and protection capabilities.

## Related Links

- [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
- [PHP Configuration - Disable Functions](https://www.php.net/manual/en/ini.core.php#ini.disable-functions)
- [MITRE ATT&CK - Web Shell](https://attack.mitre.org/techniques/T1505/003/)
- [NeoPI](https://github.com/Neohapsis/NeoPI)
- [Astra Security](https://www.getastra.com/)

## Summary

Web Shell prevention involves securing the server, keeping software updated, validating user input, restricting file uploads, and disabling unnecessary services and functions.

Detection tools such as Web Shell Detector, NeoPI, AntiShell Web Shell Hunter, and other security solutions can help identify potentially malicious scripts on web servers.
