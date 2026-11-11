
# OS Discovery

OS Discovery is a network scanning technique used to identify the operating system running on a target host.

Knowing the target's operating system helps security professionals understand the environment, identify potential vulnerabilities, and choose appropriate assessment techniques.

Nmap provides different methods for gathering operating system information.

## 1. OS Detection with Nmap

Nmap uses the `-O` option to perform Operating System Detection.

```bash
nmap -O 10.10.10.16
```

### Command Breakdown

- `nmap`: Runs the Nmap network scanner.
- `-O`: Enables operating system detection.
- `10.10.10.16`: Specifies the target IP address.

### Example Output

```text
Device type: general purpose
Running: Microsoft Windows 2016
OS CPE: cpe:/o:microsoft:windows_server_2016
OS details: Microsoft Windows Server 2016
Network Distance: 1 hop
```

### Understanding the Output

- **Device type:** Indicates the general type of device, such as a general-purpose computer or router.
- **Running:** Shows the operating system family that Nmap believes is running.
- **OS CPE:** Provides a standardized identifier for the detected operating system.
- **OS details:** Displays more specific operating system information when Nmap can identify it.
- **Network Distance:** Indicates the estimated number of network hops between the scanner and the target.

## 2. OS Discovery Using SMB

Nmap also provides an NSE script called `smb-os-discovery` to gather operating system and system information from SMB services.

SMB (Server Message Block) is a network protocol commonly used by Windows systems for file and printer sharing.

### Nmap Command

```bash
nmap --script smb-os-discovery.nse 10.10.10.10
```

### Command Breakdown

- `nmap`: Runs the Nmap network scanner.
- `--script`: Executes an Nmap Scripting Engine (NSE) script.
- `smb-os-discovery.nse`: Specifies the SMB OS discovery script.
- `10.10.10.10`: Specifies the target IP address.

### Information That Can Be Discovered

Depending on the target's SMB configuration and available information, the script may identify:

- Operating system name and version.
- Computer name.
- NetBIOS computer name.
- Domain name.
- Workgroup name.
- System time.

### Example Output

```text
Host script results:
| smb-os-discovery:
|   OS: Windows 10 Enterprise 17763
|   Computer name: DESKTOP-EXAMPLE
|   NetBIOS computer name: DESKTOP-EXAMPLE
|   Workgroup: WORKGROUP
|   System time: 2026-11-11T08:00:00+03:30
```

The values above are illustrative examples, not actual scan results.

## 3. Difference Between `-O` and `smb-os-discovery`

Both methods can provide operating system information, but they work differently.

### Nmap OS Detection (`-O`)

- Uses TCP/IP stack fingerprinting.
- Analyzes how the target responds to specially crafted network probes.
- Attempts to identify the operating system and device type.
- Does not specifically depend on SMB.

### SMB OS Discovery (`smb-os-discovery`)

- Uses the SMB protocol to gather information.
- Can reveal system details such as computer name, workgroup, and domain.
- Requires an accessible SMB service and sufficient information from the target.

## 4. Combining OS Detection with Other Options

Nmap allows OS detection to be combined with other scanning options.

### OS and Service Version Detection

```bash
nmap -O -sV 10.10.10.10
```

This command attempts to identify both the operating system and the versions of running services.

### Aggressive Scan

```bash
nmap -A 10.10.10.10
```

The `-A` option enables several advanced features, including:

- OS Detection
- Service Version Detection
- Script Scanning
- Traceroute

## Important Notes

- OS detection is more effective when at least one open and one closed TCP port are available.
- Firewalls and network filtering can affect OS detection accuracy.
- Nmap may return several possible operating system matches instead of one exact result.
- SMB-based discovery requires the target's SMB service to be accessible.
- Neither method guarantees accurate identification in every environment.

## Summary

OS Discovery helps identify the operating system and gather system information about a target host.

Two useful Nmap methods are:

**OS Detection:**

```bash
nmap -O 10.10.10.10
```

**SMB OS Discovery:**

```bash
nmap --script smb-os-discovery.nse 10.10.10.10
```

The first method analyzes TCP/IP responses, while the second gathers information through SMB.

---

## Related Links

- [Nmap OS Detection](https://nmap.org/book/man-os-detection.html) — Official documentation for Nmap operating system detection.
- [Nmap OS Detection Techniques](https://nmap.org/book/osdetect.html) — Explains how Nmap identifies operating systems through TCP/IP fingerprinting.
- [Nmap SMB OS Discovery Script](https://nmap.org/nsedoc/scripts/smb-os-discovery.html) — Official documentation for the `smb-os-discovery` NSE script.
- [Nmap Scripting Engine (NSE)](https://nmap.org/book/nse.html) — Introduction to Nmap's scripting capabilities.
- [Nmap Reference Guide](https://nmap.org/book/man.html) — Complete documentation of Nmap commands and options.
- [Wireshark](https://www.wireshark.org/) — Network protocol analyzer for examining network traffic.
- [CPE Dictionary](https://nvd.nist.gov/products/cpe) — Information about the Common Platform Enumeration (CPE) naming system.
