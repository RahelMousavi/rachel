
# DNS Enumeration

### What Is DNS Enumeration?

DNS Enumeration is the process of gathering information about a target's Domain Name System (DNS) infrastructure.

It helps identify DNS servers and retrieve records associated with a domain.

### Information Obtained Through DNS Enumeration

An attacker may discover:

- DNS server names
- Hostnames
- Machine names
- User information
- IP addresses

This information can help an attacker understand the target's network infrastructure and identify potential targets for further attacks.

### DNS Enumeration Using nslookup

`nslookup` is a command-line tool used to query DNS servers and retrieve information about domain names and DNS records.

**Step 1 — Start nslookup**

```bash
nslookup
```

**Step 2 — Specify the DNS Server**

```bash
server <DNS_SERVER_IP>
```

This command specifies the DNS server that will handle subsequent queries.

**Step 3 — Query All Available Record Types**

```bash
set type=any
```

This sets the query type to `ANY`, requesting available information about the domain.

**Step 4 — Attempt a DNS Zone Transfer**

```bash
ls -d <DOMAIN>
```

This command attempts to list the DNS records associated with the specified domain.

A successful zone transfer may reveal a large amount of DNS information, including hostnames and IP addresses.

**Note:** DNS zone transfers are not normally permitted for arbitrary clients. A DNS server should restrict zone transfers to authorized secondary DNS servers.

---

## DNSSEC Zone Walking

### What Is DNSSEC Zone Walking?

DNSSEC Zone Walking is a DNS enumeration technique used to retrieve information about DNS records in a DNSSEC-enabled zone.

It takes advantage of the way certain DNSSEC record types expose information about other records in a DNS zone.

### How Does It Work?

DNSSEC uses cryptographic mechanisms to provide authenticity and integrity for DNS responses.

However, certain DNSSEC configurations may allow an attacker to enumerate domain records.

In particular, zones using **NSEC records** can expose the names of existing records and information about the ordering of names in the zone.

### Tools Used for DNSSEC Zone Walking

The course material mentions the following tools:

- **LDNS:** A library and collection of DNS-related utilities that can be used to work with DNS and DNSSEC.
- **dnsrecon:** A DNS reconnaissance tool that supports several DNS enumeration techniques.

### NSEC and NSEC3

- **NSEC:** Uses signed records to indicate which domain names exist and the intervals between them. This can make zone walking possible.
- **NSEC3:** Uses hashed owner names to make straightforward DNS zone enumeration more difficult.

**Important:** DNSSEC Zone Walking is not possible against every DNSSEC-enabled domain. Its feasibility depends on the DNSSEC record type and server configuration.

---

## DNS Enumeration Using OWASP Amass

### What Is OWASP Amass?

OWASP Amass is an open-source tool used for attack surface mapping and network reconnaissance.

It can gather information about an organization's external assets, including domains, subdomains, and associated DNS information.

### DNS Enumeration with Amass

Amass combines different reconnaissance techniques to discover information about a target's DNS infrastructure.

These techniques include:

- **Passive Reconnaissance:** Collecting information from publicly available sources without directly querying the target's infrastructure.
- **Active Reconnaissance:** Interacting directly with DNS infrastructure to discover additional information.

By combining active and passive techniques, Amass can help identify domains, subdomains, and other assets associated with a target.

### Example Commands

**1. Passive Enumeration**

```bash
amass enum -passive -d example.com
```

Performs passive enumeration for the specified domain.

**2. Active Enumeration**

```bash
amass enum -active -d example.com
```

Enables active reconnaissance techniques to discover additional information.

**3. Save Results to a File**

```bash
amass enum -passive -d example.com -o results.txt
```

Saves the discovered results in `results.txt`.

---

## Related Links

- [RFC 1035 — Domain Names](https://www.rfc-editor.org/rfc/rfc1035)
- [Microsoft Learn — nslookup](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup)
- [RFC 5936 — DNS Zone Transfer Protocol (AXFR)](https://www.rfc-editor.org/rfc/rfc5936)
- [RFC 4033 — DNS Security Introduction and Requirements](https://www.rfc-editor.org/rfc/rfc4033)
- [RFC 4034 — DNSSEC Resource Records](https://www.rfc-editor.org/rfc/rfc4034)
- [RFC 5155 — DNSSEC Hashed Authenticated Denial of Existence (NSEC3)](https://www.rfc-editor.org/rfc/rfc5155)
- [OWASP Amass — GitHub Repository](https://github.com/owasp-amass/amass)
- [OWASP Amass — Documentation](https://owasp-amass.github.io/docs/)
- [dnsrecon — GitHub Repository](https://github.com/darkoperator/dnsrecon)
- [NLnet Labs — LDNS](https://www.nlnetlabs.nl/projects/ldns/)
