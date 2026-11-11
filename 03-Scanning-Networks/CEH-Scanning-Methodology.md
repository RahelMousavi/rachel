
# CEH Scanning Methodology

The CEH Scanning Methodology consists of several activities used to discover live systems, identify open ports and services, gather service information, and detect potential vulnerabilities in a target network.

These activities help security professionals build a better understanding of the target network and its attack surface.

## Main Steps of Scanning Methodology

### 1. Check for Live Systems

Identify active hosts within the target network to determine which systems are reachable.

### 2. Check for Open Ports

Identify open ports on live systems to discover accessible network services and potential entry points.

### 3. Banner Grabbing

Collect information from service banners to identify running services, software versions, and sometimes operating systems.

### 4. Scan for Vulnerabilities

Examine target systems and services to identify known vulnerabilities, outdated software, and potential security weaknesses.

### 5. Draw Network Diagram

Create a visual representation of the discovered network infrastructure, including hosts, devices, IP addresses, and network connections.

### 6. Prepare Proxies

Prepare proxy servers to route network traffic through intermediary systems when required for an authorized security assessment.

A proxy acts as an intermediary between a client and a destination server.

## Summary

The CEH Scanning Methodology includes six main activities:

- **Check for Live Systems:** Discover active hosts.
- **Check for Open Ports:** Identify accessible network ports.
- **Banner Grabbing:** Collect service and version information.
- **Scan for Vulnerabilities:** Identify potential security weaknesses.
- **Draw Network Diagram:** Map the discovered network infrastructure.
- **Prepare Proxies:** Configure intermediary systems when required.

These activities help security professionals understand the target network, identify exposed services, and discover potential security weaknesses.

## Related Links

- [Nmap Official Documentation](https://nmap.org/docs.html) — Documentation for host discovery, port scanning, and service detection.
- [Nmap Host Discovery](https://nmap.org/book/man-host-discovery.html) — Techniques for identifying active hosts.
- [Nmap Service and Version Detection](https://nmap.org/book/man-version-detection.html) — Explains how to identify running services and their versions.
- [NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final) — Technical guide to information security testing and assessment, including vulnerability scanning.
- [OWASP Attack Surface Analysis](https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html) — Guidance on understanding and assessing an application's attack surface.

