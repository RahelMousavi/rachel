
# NetBIOS Enumeration

### What Is NetBIOS?

NetBIOS (Network Basic Input/Output System) is an API that allows applications on different computers to communicate over a local network.

NetBIOS names are 16-character strings used to identify network devices over TCP/IP.

### Characteristics of NetBIOS

- **16-Character Names:** NetBIOS names consist of 16 characters. The 16th character is commonly used to identify the service or resource associated with the name.
- **Flat Naming:** NetBIOS uses a flat naming system rather than a hierarchical naming structure.
- **Broadcast:** NetBIOS can use broadcast messages to identify computers on a network.
- **No Specific Naming Rules:** NetBIOS does not follow the same hierarchical naming rules as DNS.

### What Can Attackers Discover Through NetBIOS Enumeration?

Attackers may use NetBIOS enumeration to obtain:

- **Computer Lists:** Identifying computers within a domain or network.
- **Shared Information:** Discovering shared files, folders, and network resources.
- **Password Policies:** Gathering information about password policies configured on the target network.

---

## NetBIOS Enumeration Using `nbtstat`

### What Is nbtstat?

`nbtstat` is a Windows command-line utility used to retrieve NetBIOS information from local and remote computers.

It can display information such as NetBIOS name tables and cached NetBIOS name-to-IP address mappings.

### Important nbtstat Commands

#### 1. Display the Local NetBIOS Name Cache

```cmd
nbtstat -c
```

Displays the contents of the local NetBIOS name cache, including NetBIOS names and their resolved IP addresses.

#### 2. Display the Remote Machine's NetBIOS Name Table

```cmd
nbtstat -a <IP_ADDRESS>
```

Retrieves the NetBIOS name table of a remote computer using its IP address.

**Example:**

```cmd
nbtstat -a 192.168.1.10
```

This command attempts to retrieve NetBIOS information from the remote machine at `192.168.1.10`.

---

## NetBIOS Enumeration Tools

Several tools can be used to perform NetBIOS enumeration and discover information about network hosts.

### 1. Nmap

Nmap is a network scanning tool that supports NetBIOS enumeration through its NSE (Nmap Scripting Engine) scripts.

**Example:**

```bash
nmap -sV -v --script nbstat.nse <TARGET_IP>
```

- `-sV`: Detects service versions.
- `-v`: Enables verbose output.
- `--script nbstat.nse`: Runs the NetBIOS information-gathering script.

### 2. Net View

`net view` is a Windows command used to display shared resources on a computer or network.

**Example:**

```cmd
net view \\<TARGET_IP> /ALL
```

This command attempts to list all available shared resources on the remote computer.

### 3. SuperScan

SuperScan is a Windows-based network scanning and enumeration tool.

It provides several enumeration capabilities, including:

- NetBIOS name table enumeration.
- NULL session checks.
- MAC address discovery.
- Workstation and server information.
- User and group enumeration.
- Share discovery.
- Domain and trusted-domain information.
- Service and registry enumeration.

---

## Related Links

- [Microsoft Learn — nbtstat Command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nbtstat)
- [Microsoft Learn — net view Command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/net-view)
- [Nmap — NSE Documentation](https://nmap.org/book/nse.html)
- [Nmap — nbstat Script](https://nmap.org/nsedoc/scripts/nbstat.html)
- [RFC 1001 — NetBIOS over TCP/IP](https://www.rfc-editor.org/rfc/rfc1001)
- [RFC 1002 — NetBIOS over TCP/IP: Detailed Specifications](https://www.rfc-editor.org/rfc/rfc1002)
