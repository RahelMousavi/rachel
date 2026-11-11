# Footprinting

Footprinting is one of the initial phases of Ethical Hacking. It involves collecting information about a target to understand its infrastructure, network, systems, and potential vulnerabilities.

The main goal is to gather relevant information about the target before starting the scanning and exploitation phases.

Footprinting techniques are divided into two main categories:

## 1. Passive Footprinting

Passive Footprinting is the process of collecting information about a target **without directly interacting with its systems or infrastructure**.

In this method, publicly available information and external sources are used. Since there is no direct interaction with the target, detecting the information-gathering activity is generally more difficult.

### Examples
- Search Engines (Google, Bing)
- Social Media Platforms
- WHOIS Lookup
- Public DNS Records
- Public Websites
- Job Portals
- Public Documents and Metadata

**Example:** Checking a company's website, its employees' LinkedIn profiles, or publicly available domain registration information.

## 2. Active Footprinting

Active Footprinting involves collecting information through **direct interaction with the target's infrastructure**.

In this method, requests are sent to target systems or services to gather technical information. Therefore, the activity is more likely to be detected by security systems.

### Examples
- Ping Sweeping
- Traceroute
- Port Scanning
- DNS Queries
- Banner Grabbing
- Network Enumeration

**Example:** Sending requests to a server to identify open ports or discover the versions of running services.

## Key Differences

### Passive Footprinting
- Does not directly interact with the target.
- Relies on publicly available information.
- Is generally harder to detect.
- Usually provides externally available information.

### Active Footprinting
- Directly interacts with the target.
- Sends requests to target systems and services.
- Is more likely to be detected.
- Can provide more detailed technical information.

## Summary

- **Passive Footprinting:** Collecting information without directly interacting with the target.
- **Active Footprinting:** Collecting information by directly interacting with the target.

Both techniques must be performed within the authorized scope of an ethical hacking engagement.
