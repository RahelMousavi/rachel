
# Service Version Discovery

Service Version Discovery is a network scanning technique used to identify the services running on open ports and determine their version information.

Knowing the service name and version helps security professionals identify outdated software, known vulnerabilities, and potential security risks.

For example, instead of simply identifying port 80 as open, service version detection may reveal that the target is running a specific version of an HTTP server.

## How Service Version Discovery Works

1. Nmap scans the target to identify open ports.
2. It sends specific probes to the open ports.
3. The running services respond to these probes.
4. Nmap analyzes the responses and service banners.
5. Nmap attempts to identify the service name, version, and sometimes additional details.

## Nmap Command

Nmap uses the `-sV` option to perform Service Version Detection.

```bash
nmap -sV 10.10.10.10
```

### Command Breakdown

- `nmap`: Runs the Nmap network scanner.
- `-sV`: Enables service and version detection.
- `10.10.10.10`: Specifies the target IP address.

## Example Output

```text
PORT     STATE  SERVICE       VERSION
135/tcp  open   msrpc         Microsoft Windows RPC
139/tcp  open   netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open   microsoft-ds  Microsoft Windows SMB
5357/tcp open   http          Microsoft HTTPAPI httpd 2.0
```

### Understanding the Output

- **PORT:** The port number and transport protocol.
- **STATE:** The state of the port, such as open or closed.
- **SERVICE:** The name of the service associated with the port.
- **VERSION:** Information about the detected service and its version.

For example:

```text
80/tcp open http Apache httpd 2.4.XX
```

This indicates that:
- Port 80 is open.
- The service is HTTP.
- The detected web server is Apache.
- The reported version is 2.4.XX.

## Scanning Specific Ports

To detect service versions on a specific port:

```bash
nmap -sV -p 80 10.10.10.10
```

To scan multiple ports:

```bash
nmap -sV -p 22,80,443 10.10.10.10
```

## Combining Service Version Detection with Other Scans

Nmap allows service version detection to be combined with other scanning options.

### SYN Scan with Version Detection

```bash
nmap -sS -sV 10.10.10.10
```

This command performs a TCP SYN Scan and attempts to identify service versions.

### Aggressive Scan

```bash
nmap -A 10.10.10.10
```

The `-A` option enables several advanced features, including:

- OS Detection
- Service Version Detection
- Script Scanning
- Traceroute

## Why Is Service Version Discovery Important?

Service Version Discovery helps security professionals:

- Identify applications running on target systems.
- Discover outdated software versions.
- Identify services that may contain known vulnerabilities.
- Understand the target's network attack surface.
- Plan further vulnerability assessments and penetration tests.

## Service Version Detection vs. Banner Grabbing

These techniques are related but not identical.

### Banner Grabbing

- Collects information exposed by a service through its banner.
- May reveal the service name and version.
- Can be performed manually or with automated tools.

### Service Version Detection

- Uses probes to identify running services.
- Analyzes responses and service-specific behavior.
- May identify services even when they do not provide an obvious banner.
- Nmap performs this process using `-sV`.

## Summary

Service Version Discovery identifies services running on open ports and attempts to determine their versions.

Nmap performs this operation using:

```bash
nmap -sV 10.10.10.10
```

The results provide useful information about the target's services and help identify potentially outdated or vulnerable software.

---

## Related Links

- [Nmap Service and Version Detection](https://nmap.org/book/man-version-detection.html) — Official documentation explaining how Nmap identifies services and their versions.
- [Nmap Version Detection Techniques](https://nmap.org/book/vscan.html) — Detailed explanation of probes, responses, and service identification.
- [Nmap Reference Guide](https://nmap.org/book/man.html) — Complete documentation of Nmap commands and options.
- [Nmap Service Probes Database](https://svn.nmap.org/nmap/nmap-service-probes) — Database of probes and matching rules used by Nmap for service detection.
- [Nmap NSE Documentation](https://nmap.org/book/nse.html) — Information about Nmap Scripting Engine and additional service analysis.
- [Common Vulnerabilities and Exposures (CVE)](https://www.cve.org/) — Database of publicly disclosed cybersecurity vulnerabilities.
- [National Vulnerability Database (NVD)](https://nvd.nist.gov/) — Vulnerability information that can help assess identified software versions.
- [Wireshark](https://www.wireshark.org/) — Network protocol analyzer for examining service probes and responses.
