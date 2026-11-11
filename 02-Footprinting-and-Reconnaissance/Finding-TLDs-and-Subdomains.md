
# Finding TLDs and Subdomains

Finding TLDs and subdomains is an important part of the Footprinting phase.

It helps penetration testers identify domains and subdomains associated with a target organization and understand its external digital infrastructure.

## Key Concepts

- **TLD (Top-Level Domain):** The last part of a domain name, such as `.com`, `.org`, or `.net`.
- **Domain:** The registered name of a website, such as `microsoft.com`.
- **Subdomain:** A subdivision of a domain, such as `mail.microsoft.com` or `support.microsoft.com`.

## Subdomain Enumeration Techniques and Tools

### 1. Finding Domains Owned by an Organization

Identifying domains owned or used by a target organization helps reveal its online presence and external assets.

For example, Microsoft may use multiple domains and subdomains for different products, services, and regions.

### 2. Google Search Operators

Google search operators can help discover indexed pages and subdomains associated with a target.

Example:

```text
site:microsoft.com -inurl:www
```

- `site:microsoft.com` - Restricts results to pages indexed under the Microsoft domain.
- `-inurl:www` - Excludes results whose URLs contain `www`.

This query can help discover indexed pages hosted on other subdomains.

### 3. Sublist3r

[Sublist3r](https://github.com/aboul3la/Sublist3r) is an open-source Python tool designed to enumerate subdomains using OSINT techniques.

It collects information from multiple search engines and public sources to identify subdomains associated with a target domain.

**Example:**

```bash
sublist3r -d google.com
```

- `-d` - Specifies the target domain.
- `google.com` - The domain being investigated.

**Installation on Kali Linux:**

```bash
sudo apt install sublist3r
```

**Useful options:**

```bash
sublist3r -h
```

Displays available commands and options.

```bash
sublist3r -v -d google.com
```

Displays discovered subdomains in real time.

```bash
sublist3r -o subdomains.txt -d google.com
```

Saves discovered subdomains to a file.

### 4. Netcraft

[Netcraft](https://www.netcraft.com/) provides internet research tools that help identify information about websites, domains, hostnames, and web technologies.

Its DNS Search service can be used to discover hostnames associated with a particular domain.

**Useful Features:**

- Search for hostnames associated with a domain.
- Identify websites and related infrastructure.
- Gather information about web technologies and hosting environments.

**DNS Search:** https://searchdns.netcraft.com/

### 5. Pentest-Tools.com

[Pentest-Tools.com](https://pentest-tools.com/) provides online penetration testing and reconnaissance tools.

Its Subdomain Finder helps discover subdomains associated with a target domain.

**Main Features:**

- Discover subdomains using passive and active techniques.
- Identify DNS records and associated IP addresses.
- Check whether discovered subdomains are reachable.
- Help map an organization's external attack surface.

**Subdomain Finder:** https://pentest-tools.com/information-gathering/find-subdomains-of-domain

## Role in Footprinting

Finding domains and subdomains helps security researchers:

- Discover additional assets belonging to an organization.
- Identify forgotten or publicly exposed subdomains.
- Understand the target's external infrastructure.
- Identify potential entry points for further security assessments.
- Build a more complete map of the target's attack surface.

**Important:** Subdomain enumeration results may be incomplete or outdated. Always verify discovered assets and perform security testing only within an authorized scope.
