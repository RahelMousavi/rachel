
# Linux Enumeration

## What Is Linux Enumeration?

Linux Enumeration is the process of gathering information about users, active sessions, and other system details on Linux and Unix-based systems.

One important part of this process is examining user accounts and identifying who is currently logged into the system.

## Information Obtained Through Linux Enumeration

By examining user sessions and system information, an attacker may discover:

- Usernames
- Hostnames
- Active login sessions
- Date and time of each session's start

This information can help an attacker understand system usage and identify potential targets for further attacks.

## Linux Enumeration Commands

After gaining access to a Linux or Unix system, several commands can be used to retrieve information about users and sessions.

### 1. rwho

`rwho` displays information about users currently logged into machines on the local network.

```bash
rwho
```

It can display usernames, hostnames, and login information.

### 2. rusers

`rusers` displays information about users logged into remote systems.

```bash
rusers -l <HOSTNAME>
```

The `-l` option provides detailed information about logged-in users.

### 3. finger

`finger` retrieves information about local or remote user accounts.

```bash
finger
```

To query a specific user:

```bash
finger <USERNAME>
```

It may display information such as:

- Username
- Login name
- Login time
- Idle time
- User details

## Services Required for Remote Enumeration

Remote enumeration using these commands depends on specific services being enabled on the target system:

- **rwhod:** Collects and distributes information about users and system status across a network.
- **fingerd:** Provides remote access to user information through the Finger protocol.
- **rusersd:** Provides information about users currently logged into a system.

If these services are enabled and accessible, remote users may be able to retrieve information about the target system.

---

## Related Links

- [Linux Manual — rwho](https://man7.org/linux/man-pages/man1/rwho.1.html)
- [Linux Manual — rusers](https://man7.org/linux/man-pages/man1/rusers.1.html)
- [Linux Manual — finger](https://man7.org/linux/man-pages/man1/finger.1.html)
- [RFC 1288 — The Finger User Information Protocol](https://www.rfc-editor.org/rfc/rfc1288)
- [Linux Manual — rwhod](https://man7.org/linux/man-pages/man8/rwhod.8.html)
