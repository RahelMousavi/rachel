
# Ports and Services Related to Enumeration

Enumeration often involves querying network services running on specific ports.

The following table lists important ports and their associated services.

## Enumeration-Related Ports

### DNS and Windows Networking

- **TCP/UDP 53 — DNS Zone Transfer**
  - Domain Name System (DNS)
  - Used for DNS queries and zone transfers.

- **TCP/UDP 135 — Microsoft RPC Endpoint Mapper**
  - Used by Microsoft Remote Procedure Call (RPC) services to identify available RPC endpoints.

- **UDP 137 — NetBIOS Name Service (NBNS)**
  - Used for NetBIOS name resolution.

- **TCP 139 — NetBIOS Session Service**
  - Supports SMB communication over NetBIOS.

- **TCP/UDP 445 — SMB over TCP (Direct Host)**
  - Used for direct Server Message Block (SMB) communication over TCP.

### Network Management and Directory Services

- **UDP 161 — Simple Network Management Protocol (SNMP)**
  - Used for SNMP queries and network device management.

- **TCP/UDP 389 — Lightweight Directory Access Protocol (LDAP)**
  - Used to access and query directory services.

- **TCP/UDP 162 — SNMP Trap**
  - Used to receive SNMP Trap messages from network devices.

### Other Services

- **TCP 2049 — Network File System (NFS)**
  - Used for sharing files across a network.

- **TCP 25 — Simple Mail Transfer Protocol (SMTP)**
  - Used for sending email between mail servers.

- **UDP 500 — ISAKMP / Internet Key Exchange (IKE)**
  - Used during the establishment of IPsec security associations.

- **TCP 22 — Secure Shell (SSH)**
  - Provides secure remote access to systems.

## Related Links

- [IANA — Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)
- [RFC 1035 — Domain Names](https://www.rfc-editor.org/rfc/rfc1035)
- [RFC 4511 — LDAP](https://www.rfc-editor.org/rfc/rfc4511)
- [RFC 3417 — SNMP Transport Mappings](https://www.rfc-editor.org/rfc/rfc3417)
- [Microsoft — SMB Protocol](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-overview)
- [RFC 4253 — SSH Transport Layer Protocol](https://www.rfc-editor.org/rfc/rfc4253)
