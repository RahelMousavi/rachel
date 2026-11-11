
# SMTP Enumeration

## What Is SMTP?

SMTP stands for **Simple Mail Transfer Protocol**.

It is a communication protocol used to send email messages between mail clients and mail servers, as well as between mail servers.

SMTP commonly uses TCP port **25** for server-to-server email transmission.

## SMTP Enumeration

SMTP Enumeration is the process of gathering information about users and email accounts from an SMTP server.

An attacker may attempt to identify valid usernames and email accounts by interacting with the SMTP service.

This information can be used in subsequent attacks, such as targeted phishing or password attacks.

## SMTP Enumeration Using Telnet

Telnet can be used to establish a direct connection to an SMTP server.

**Syntax:**

```bash
telnet <TARGET_IP> 25
```

After establishing a connection, SMTP commands can be used to interact with the server.

## SMTP Enumeration Using Nmap

Nmap provides an NSE script called `smtp-enum-users` that can be used to enumerate valid SMTP usernames.

**Command:**

```bash
nmap -p 25 --script=smtp-enum-users <TARGET_IP>
```

**Example:**

```bash
nmap -p 25 --script=smtp-enum-users 10.10.1.19
```

### Command Explanation

- `nmap`: Starts the Nmap scanner.
- `-p 25`: Scans TCP port 25.
- `--script=smtp-enum-users`: Runs the SMTP user enumeration script.
- `<TARGET_IP>`: Specifies the target SMTP server.

### Example Output

The slide demonstrates an example in which Nmap identifies possible usernames, including:

- root
- admin
- administrator
- webadmin
- sysadmin
- netadmin
- guest
- user
- web
- test

The results depend on the target server's configuration and the enumeration method.

---

## Related Links

- [RFC 5321 — Simple Mail Transfer Protocol](https://www.rfc-editor.org/rfc/rfc5321)
- [Nmap — smtp-enum-users NSE Script](https://nmap.org/nsedoc/scripts/smtp-enum-users.html)
- [Nmap — NSE Documentation](https://nmap.org/book/nse.html)
- [Microsoft Learn — SMTP Overview](https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/how-to-configure-a-relay-connector)

