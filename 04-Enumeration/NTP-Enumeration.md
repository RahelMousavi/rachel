
# NTP Enumeration

### What Is NTP?

NTP (Network Time Protocol) is a protocol used to synchronize the clocks of computers and other devices across a network.

It allows systems to maintain accurate and consistent time.

### NTP Port

- **UDP 123:** Default port used by NTP.

### NTP Enumeration

NTP Enumeration is the process of sending queries to an NTP server to gather information about the systems communicating with it.

An attacker may use NTP requests to collect information such as:

- **Connected Hosts:** A list of hosts connected to the NTP server.
- **Client IP Addresses:** IP addresses of systems using the NTP server.
- **System Names:** Names of systems communicating with the server.
- **Operating System Details:** Information that may help identify the operating systems of connected hosts.

### NTP Time Accuracy

According to the course material:

- NTP can provide time synchronization accuracy of approximately **10 milliseconds**.
- Under ideal conditions in internal networks, accuracy may reach approximately **200 microseconds**.

---

## NTP Enumeration Tools

Several command-line tools can be used to query NTP servers and retrieve information about their configuration and operation.

### 1. ntptrace

`ntptrace` traces the chain of NTP servers back to the primary time source.

It helps identify the upstream NTP servers responsible for providing time synchronization.

**Syntax:**

```bash
ntptrace [-vdn] [-r retries] [-t timeout] [server]
```

**Options:**

- `-v`: Enables verbose output.
- `-d`: Enables debugging information.
- `-n`: Displays addresses numerically.
- `-r`: Specifies the number of retries.
- `-t`: Specifies the timeout value.
- `server`: Specifies the NTP server to query.

**Example:**

```bash
ntptrace 192.168.1.10
```

### 2. ntpdc

`ntpdc` is a utility used to monitor and query the operation of the NTP daemon (`ntpd`).

It can retrieve information about the NTP server and its clients.

**Syntax:**

```bash
ntpdc [-n] [-v] host1 [IPaddress1 ...]
```

One query shown in the course material is:

```bash
ntpdc -c monlist <TARGET_IP>
```

The `monlist` query requests a list of clients recently communicating with the NTP server.

### 3. ntpq

`ntpq` is a utility used to monitor NTP daemon operations and examine its performance.

It can retrieve information about NTP peers, synchronization status, and server statistics.

**Syntax:**

```bash
ntpq [-inp] [-c command] [host] [...]
```

**Options:**

- `-i`: Enables interactive mode.
- `-n`: Displays IP addresses numerically.
- `-p`: Displays a list of configured NTP peers.
- `-c`: Executes a specified command.

**Example:**

```bash
ntpq -p <TARGET_IP>
```

This command displays information about the NTP peers known to the server.

---

## Related Links

- [RFC 5905 — Network Time Protocol Version 4](https://www.rfc-editor.org/rfc/rfc5905)
- [NTP Project — Official Website](https://www.ntp.org/)
- [NTP Documentation](https://www.ntp.org/documentation/)
- [ntptrace Manual](https://www.ntp.org/documentation/4.2.8-series/ntptrace/)
- [ntpq Manual](https://www.ntp.org/documentation/4.2.8-series/ntpq/)
- [ntpdc Manual](https://www.ntp.org/documentation/4.2.8-series/ntpdc/)
