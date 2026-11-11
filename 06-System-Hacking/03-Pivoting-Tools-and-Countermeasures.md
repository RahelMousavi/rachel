
# Pivoting, Privilege Escalation Tools, and Countermeasures

## Pivoting

**Pivoting** is a technique used during penetration testing to access other systems or networks through a machine that has already been compromised.

An attacker may gain access to one computer but discover that other systems are not directly reachable from their original machine.

Instead of connecting to those systems directly, the attacker uses the compromised machine as an intermediate point to reach the internal network.

### How Pivoting Works

A typical pivoting scenario involves:

1. The penetration tester gains access to an initial target system.
2. The compromised system has access to another internal network.
3. The tester establishes a communication channel through the compromised system.
4. A route is configured to direct traffic for the internal network through that connection.
5. The tester can then perform authorized assessments against reachable internal systems.

### Pivoting with Metasploit

Metasploit supports pivoting through sessions such as Meterpreter.

The `route` command can be used to configure routes through an established session.

A simplified example:

```bash
route add <target_subnet> <netmask> <session_id>
```

Where:

- `<target_subnet>` is the network that should be reached.
- `<netmask>` defines the network range.
- `<session_id>` identifies the Meterpreter session used as the pivot.

For example:

```bash
route add 192.168.2.0 255.255.255.0 1
```

This configures Metasploit to route traffic for the specified subnet through session 1.

The exact connectivity depends on the compromised host's network access and the available routing and forwarding capabilities.

### Why Is Pivoting Important?

Pivoting is useful for evaluating internal network security.

It helps penetration testers understand:

- Which internal systems are reachable from a compromised host.
- Whether network segmentation is effective.
- Whether access to one system can expose other systems.
- How far an attacker could potentially move within an internal network.

**Important:** Pivoting is not the same as privilege escalation. Privilege escalation increases permissions on a system, while pivoting uses an existing system or session to reach other network resources.

## Privilege Escalation Tools

Privilege escalation assessment tools help identify weaknesses in operating system configurations, permissions, services, and installed software.

The course introduces the following tools:

### 1. BeRoot

**BeRoot** is a privilege escalation enumeration tool designed to identify potential privilege escalation paths on Windows and Linux systems.

It examines system configurations and looks for weaknesses that may allow a user to obtain higher privileges.

Its findings can help security professionals identify:

- Misconfigured services.
- Weak file and directory permissions.
- Potentially vulnerable configurations.
- Other privilege escalation opportunities.

### 2. linpostexp

The course also lists **linpostexp** as a Linux privilege escalation-related tool.

Tools in this category are used to inspect Linux system information and identify possible privilege escalation weaknesses.

The exact functionality and availability of older tools should be verified before use.

### Additional Tools

Two widely used tools for privilege escalation enumeration are:

- **LinPEAS:** Searches Linux systems for possible privilege escalation paths.
- **WinPEAS:** Searches Windows systems for possible privilege escalation paths.

These tools automate parts of the enumeration process, but their findings must be reviewed manually. A detected configuration or permission issue is not necessarily exploitable.

## Countermeasures Against Privilege Escalation

Organizations can reduce privilege escalation risks by applying proper security controls and maintaining secure system configurations.

Important countermeasures include:

### 1. Apply the Principle of Least Privilege

Users and applications should operate with only the permissions required to perform their tasks.

Avoid granting administrator or root privileges when they are not necessary.

### 2. Protect Sensitive Data

Use encryption to protect sensitive information, especially credentials and confidential files.

Restrict access to sensitive data based on user roles and permissions.

### 3. Restrict Access to Login Interfaces

Limit access to administrative login interfaces and management services.

Use appropriate authentication controls and avoid exposing administrative services unnecessarily.

### 4. Minimize Privileged Code Execution

Reduce the amount of code that runs with elevated privileges.

Applications and services should use restricted accounts whenever possible.

### 5. Implement Strong Authentication and Access Control

Use appropriate authentication mechanisms and define clear access-control policies.

Multi-factor authentication (MFA) can provide additional protection for privileged accounts.

### 6. Perform Debugging and Security Testing

Regularly test applications and systems to identify programming errors, configuration weaknesses, and security vulnerabilities.

Fix identified issues before they can be exploited.

### 7. Separate Privileges

Use different accounts and permission levels for administrative and everyday activities.

Apply security boundaries between applications, users, and system components.

### 8. Manage Patches and Updates

Keep operating systems, applications, and services updated.

Security patches help address known vulnerabilities that could otherwise be exploited to gain elevated privileges.

### 9. Configure Windows UAC Properly

**User Account Control (UAC)** helps prevent unauthorized changes to Windows by prompting for approval or administrator credentials when an operation requires elevated permissions.

For stronger protection, configure UAC to provide appropriate notification levels, including the **Always Notify** setting where suitable.

### 10. Use Fully Qualified Paths

Use fully qualified executable paths and properly quote paths containing spaces in Windows service configurations.

This helps prevent ambiguity when Windows locates executable files.

## Summary

Pivoting allows a penetration tester to use an already compromised system as an intermediate point to access other systems or internal networks.

Metasploit supports pivoting through established sessions and its routing functionality.

Privilege escalation enumeration tools such as BeRoot, LinPEAS, and WinPEAS help identify possible weaknesses in system configurations and permissions.

To prevent privilege escalation, organizations should apply the principle of least privilege, protect sensitive information, secure authentication mechanisms, regularly test systems, manage patches, and properly configure services and access controls.

## Related Links

- [Metasploit Documentation](https://docs.metasploit.com/)
- [Metasploit Framework - GitHub](https://github.com/rapid7/metasploit-framework)
- [BeRoot - GitHub](https://github.com/AlessandroZ/BeRoot)
- [PEASS-ng - LinPEAS and WinPEAS](https://github.com/peass-ng/PEASS-ng)
- [MITRE ATT&CK - Privilege Escalation](https://attack.mitre.org/tactics/TA0004/)
- [Microsoft Learn - User Account Control](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/)
