
# DNS Sites & Tools

DNS Footprinting can be performed using online services and command-line tools.

These tools help researchers collect DNS records, identify subdomains, examine DNS configurations, and investigate domain-related information.

## Online DNS Tools

### 1. DNSstuff

Provides DNS lookup and domain-related diagnostic services.

Website: https://www.dnsstuff.com/

### 2. SecurityTrails

A platform for DNS intelligence, domain research, historical DNS records, and subdomain discovery.

Website: https://securitytrails.com/

### 3. MXToolbox

Provides tools for checking MX records, DNS records, email configurations, and domain health.

Website: https://mxtoolbox.com/

### 4. BetterWhois

A WHOIS lookup service for retrieving domain registration information.

Website: https://www.betterwhois.com/

### 5. Ajax DNS

A DNS lookup service listed in the course material.

### 6. NetworkTools

Provides online network and DNS diagnostic utilities.

Website: https://www.networktools.com/

### 7. CheckDNS

Provides DNS-related checking and diagnostic services.

Website: https://www.checkdns.net/

## DNS Command-Line and Analysis Tools

### 1. DIG

`dig` (Domain Information Groper) is a command-line utility used to query DNS servers and retrieve DNS records.

Example:

```bash
dig example.com
```

To query a specific record:

```bash
dig example.com MX
```

### 2. Fierce

Fierce is a DNS reconnaissance tool used to identify subdomains and discover DNS-related information about a target domain.

Website: https://github.com/mschwager/fierce

### 3. DNSRecon

DNSRecon is a DNS enumeration tool used to gather information about DNS records, name servers, and subdomains.

Website: https://github.com/darkoperator/dnsrecon

### 4. DNSenum

DNSenum is a Perl-based DNS enumeration tool designed to collect domain-related information and identify subdomains.

Website: https://github.com/fwaeytens/dnsenum

### 5. DNS Watch

A DNS monitoring and lookup service listed in the course material.

### 6. My DNS Tools

A collection of DNS-related lookup and diagnostic utilities listed in the course material.

### 7. DNS Data View

A DNS information utility listed in the course material.

## Role in Footprinting

DNS tools can help security researchers:

- Retrieve DNS records.
- Identify name servers and mail servers.
- Discover subdomains.
- Examine DNS configurations.
- Identify IP addresses associated with domains.
- Map parts of a target's external infrastructure.

## Summary

DNS tools and online services are important resources during DNS Footprinting.

They help researchers analyze DNS records, discover subdomains, identify network services, and understand a target's domain infrastructure.

## Official Resources

- DNSstuff: https://www.dnsstuff.com/
- SecurityTrails: https://securitytrails.com/
- MXToolbox: https://mxtoolbox.com/
- NetworkTools: https://www.networktools.com/
- Fierce: https://github.com/mschwager/fierce
- DNSRecon: https://github.com/darkoperator/dnsrecon
- DNSenum: https://github.com/fwaeytens/dnsenum
