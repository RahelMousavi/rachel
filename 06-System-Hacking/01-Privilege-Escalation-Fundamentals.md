
# Privilege Escalation Fundamentals

## Introduction to Privilege Escalation

**Privilege Escalation** is the process of gaining higher levels of access or permissions than those originally assigned to a user or process.

An attacker may initially gain access to a system through a standard user account. After obtaining this initial access, the attacker may attempt to increase their privileges to gain greater control over the system.

Higher privileges may allow an attacker to:

- Access sensitive information.
- Modify or delete protected files.
- Install or execute malicious software.
- Change system configurations.
- Create or modify user accounts.
- Access resources restricted to administrators.

Privilege escalation is an important stage in many attacks because initial access does not necessarily provide complete control over a system.

## Types of Privilege Escalation

Privilege escalation is generally divided into two main categories:

### 1. Horizontal Privilege Escalation

**Horizontal Privilege Escalation** occurs when a user gains unauthorized access to the resources or permissions of another user at the same privilege level.

For example:

- User A has access to their own account and files.
- User A exploits an access-control weakness to access User B's files.
- Both accounts have the same general privilege level, but User A has accessed resources belonging to another user.

This type of escalation involves moving between accounts with similar privilege levels rather than gaining administrative permissions.

### 2. Vertical Privilege Escalation

**Vertical Privilege Escalation** occurs when a user gains access to permissions or resources belonging to a higher-privileged account.

For example:

- An attacker gains access to a system using a standard user account.
- The attacker exploits a vulnerability or misconfiguration.
- The attacker obtains administrator or root privileges.

Vertical privilege escalation can provide significantly greater control over the target system.

## Privilege Escalation by Exploiting Vulnerabilities

One common way to escalate privileges is by exploiting vulnerabilities in an operating system, application, or service.

If a vulnerability allows code to execute with higher privileges than the attacker's current account, it may be possible to gain elevated access.

A typical assessment process involves:

1. Identifying the operating system and its version.
2. Enumerating installed software, services, and configurations.
3. Identifying potential vulnerabilities.
4. Checking whether a vulnerability can be exploited in the current environment.
5. Evaluating the resulting privilege level.

### Exploit Database

The **Exploit Database (Exploit-DB)** is a public archive of exploit code and security-related research.

Security professionals can use it to research known vulnerabilities and identify publicly available proof-of-concept exploits.

Before using an exploit, it is important to verify:

- The affected software and version.
- The operating system and architecture.
- The vulnerability's conditions and limitations.
- Whether the exploit is reliable and applicable to the target environment.

A publicly available exploit does not automatically mean that the target system is vulnerable.

## Spectre and Meltdown Vulnerabilities

**Spectre** and **Meltdown** are hardware-related security vulnerabilities publicly disclosed in 2018. They are associated with speculative execution, a performance optimization technique used by modern processors.

These vulnerabilities demonstrated that sensitive information could potentially be exposed through side-channel techniques involving processor behavior.

### Meltdown

**Meltdown (CVE-2017-5754)** is a vulnerability that can allow an attacker to bypass certain memory isolation protections and potentially access sensitive data from memory.

The original vulnerability primarily affected certain Intel processors.

### Spectre

**Spectre** refers to a family of vulnerabilities associated with speculative execution.

Two important identifiers are:

- **CVE-2017-5753**
- **CVE-2017-5715**

Spectre can potentially allow information from memory used by other applications to be exposed through side-channel attacks.

The affected processor families included Intel, AMD, and ARM, although the impact depends on the specific processor and implementation.

### Why Are They Important?

Spectre and Meltdown demonstrated that security boundaries enforced by software and hardware can be affected by processor-level design issues.

They are important examples of vulnerabilities that may expose sensitive information even when traditional access controls are in place.

## Summary

Privilege escalation occurs when an attacker gains permissions beyond their original access level.

There are two main types:

- **Horizontal Privilege Escalation:** Gaining unauthorized access to another user's resources at a similar privilege level.
- **Vertical Privilege Escalation:** Gaining access to a higher privilege level, such as administrator or root.

Attackers may exploit operating system vulnerabilities, application weaknesses, or misconfigurations to escalate privileges.

Spectre and Meltdown are examples of hardware-related vulnerabilities that can expose sensitive information through speculative execution side channels.

## Related Links

- [Exploit Database](https://www.exploit-db.com/)
- [MITRE CVE - CVE-2017-5754](https://www.cve.org/CVERecord?id=CVE-2017-5754)
- [MITRE CVE - CVE-2017-5753](https://www.cve.org/CVERecord?id=CVE-2017-5753)
- [MITRE CVE - CVE-2017-5715](https://www.cve.org/CVERecord?id=CVE-2017-5715)
- [Google Project Zero - Reading Privileged Memory with a Side-Channel](https://googleprojectzero.blogspot.com/2018/01/reading-privileged-memory-with-side.html)
