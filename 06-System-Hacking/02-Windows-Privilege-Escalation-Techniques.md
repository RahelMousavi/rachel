
# Windows Privilege Escalation Techniques

Windows systems contain several mechanisms for communication, service management, and automated installation. Incorrect configurations in these mechanisms may create opportunities for privilege escalation.

## 1. Named Pipe Impersonation

### What Are Named Pipes?

**Named Pipes** are a Windows mechanism that allows communication between processes, either on the same computer or across a network.

A named pipe provides a communication channel through which processes can exchange data.

Two main roles are involved:

- **Pipe Server:** Creates the named pipe and waits for connections.
- **Pipe Client:** Connects to the named pipe to communicate with the server.

### How Can Named Pipe Impersonation Lead to Privilege Escalation?

Windows supports a mechanism called **Impersonation**, which allows a server process to temporarily operate using the security context of a connected client.

If a privileged client connects to a pipe server and the server is able to impersonate that client, the server may obtain access to the client's security token.

An attacker may attempt to abuse this behavior by:

1. Creating or controlling a named pipe server.
2. Waiting for a process running with higher privileges to connect.
3. Attempting to impersonate the connected client.
4. Abusing an improperly configured impersonation mechanism to obtain elevated access.

Successful exploitation depends on token privileges, impersonation levels, and the security configuration of the application.

**Important:** Simply creating a named pipe does not automatically grant elevated privileges. Specific security conditions must be satisfied.

## 2. Unquoted Service Paths

Windows services are configured with executable paths that specify which program should run when a service starts.

These paths should be enclosed in quotation marks when they contain spaces.

### How Does the Vulnerability Occur?

Consider the following service executable path:

`C:\Program Files\My Service\service.exe`

If this path is configured without quotation marks, Windows may interpret the executable path ambiguously when attempting to launch it.

Depending on the way the service is started and the path is parsed, Windows may attempt to locate executable files at intermediate locations.

For example, possible candidate paths may include:

- `C:\Program.exe`
- `C:\Program Files\My.exe`

If an attacker can write a malicious executable to an appropriate candidate location, it may be executed with the privileges of the service.

### Conditions for Exploitation

This issue does not automatically result in privilege escalation.

An exploitable situation generally requires:

- An unquoted service path containing spaces.
- A candidate directory that is writable by the attacker.
- A service that runs with higher privileges.
- An opportunity for the service to restart or execute the affected path.

### Prevention

- Enclose service executable paths containing spaces in quotation marks.
- Restrict write permissions on service directories.
- Review service configurations regularly.
- Run services with the minimum privileges required.

## 3. Service Object Permissions

Windows services have security permissions that control which users can interact with or modify them.

Incorrectly configured service permissions may allow a low-privileged user to modify service settings.

For example, an attacker may be able to:

- Modify the service configuration.
- Change the executable path.
- Change the service startup settings.
- Replace or modify files used by the service.

If the modified service runs with elevated privileges, this weakness may lead to privilege escalation.

### Prevention

- Restrict service configuration permissions.
- Allow only authorized administrators to modify critical services.
- Review service access-control settings.
- Protect service executable files and directories against unauthorized modification.

## 4. Unattended Installation

**Unattended Installation** is a Windows installation method that allows administrators to deploy the operating system automatically without manually answering installation prompts.

Installation settings are commonly stored in configuration files such as:

`Unattend.xml`

These files may contain information about the installation process, including:

- System configuration settings.
- User account information.
- Installation options.
- Passwords or other sensitive values, depending on the configuration.

### How Can It Lead to Privilege Escalation?

If sensitive credentials are stored in an unattended installation file and the file is accessible to an unauthorized user, an attacker may recover those credentials.

If the recovered credentials belong to a privileged account, they may be used to obtain elevated access.

Potential locations mentioned in the course include:

- `C:\Windows\Panther\`
- `C:\Windows\Panther\Unattend\`
- `C:\Windows\System32\`
- `C:\Windows\Panther\Sysprep\`

These are locations worth checking during an authorized security assessment; the file is not guaranteed to exist in every directory or on every Windows installation.

### Prevention

- Avoid storing plaintext passwords in unattended installation files.
- Restrict access to installation configuration files.
- Remove temporary installation files when they are no longer needed.
- Use secure deployment methods for handling credentials.
- Review systems after automated deployment.

## Summary

Several Windows configuration weaknesses can create opportunities for privilege escalation.

- **Named Pipe Impersonation:** May allow a process to use the security context of a connected client under specific conditions.
- **Unquoted Service Paths:** Ambiguous executable paths may allow unauthorized executable placement when writable candidate directories exist.
- **Service Object Permissions:** Weak service permissions may allow unauthorized modification of service configurations.
- **Unattended Installation:** Exposed installation files may reveal sensitive credentials.

Proper permission management, secure service configuration, and protection of sensitive installation files help reduce these risks.

## Related Links

- [Microsoft Learn - Named Pipes](https://learn.microsoft.com/en-us/windows/win32/ipc/named-pipes)
- [Microsoft Learn - Impersonation](https://learn.microsoft.com/en-us/windows/win32/secauthz/impersonation)
- [Microsoft Learn - Windows Services](https://learn.microsoft.com/en-us/windows/win32/services/services)
- [Microsoft Learn - Unattended Windows Setup](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/automate-windows-setup)
- [MITRE ATT&CK - Abuse Elevation Control Mechanism](https://attack.mitre.org/techniques/T1548/)

