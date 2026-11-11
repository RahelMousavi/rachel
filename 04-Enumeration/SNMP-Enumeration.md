
## Working of SNMP

### How Does SNMP Work?

SNMP (Simple Network Management Protocol) uses two main components:

- **SNMP Manager:** The system responsible for monitoring and managing network devices.
- **SNMP Agent:** Software running on network devices or operating systems that collects and provides information to the manager.

The SNMP Agent starts running when the device is powered on and listens for requests from the SNMP Manager on **UDP port 161**.

### SNMP Operations

The SNMP Manager communicates with agents using different operations:

- **Get:** Retrieves the value of a specific variable from an SNMP agent.
- **GetNext:** Retrieves the next variable in the Management Information Base (MIB).
- **Set:** Changes the value of a variable on the SNMP agent.
- **GetBulk:** Retrieves multiple variables in a single request.

### SNMP Notifications

SNMP agents can also send messages to the manager without waiting for a request.

Two important notification types are:

- **Trap:** An unsolicited message sent by an agent to notify the manager about an event.
- **Inform:** A notification message that requires acknowledgment from the receiver.

### SNMP Communication Process

The general communication process involves:

1. **Agent Initialization:** The SNMP agent starts when the network device is powered on.
2. **Discovery:** The manager identifies SNMP agents available on the network.
3. **Information Exchange:** The manager sends requests such as Get, GetNext, Set, and GetBulk.
4. **Notifications:** Agents can send Trap or Inform messages to report events.

---

## SNMP Enumeration Tools

Several tools are available for gathering information from devices and systems running SNMP.

### 1. OpUtils

A network management and monitoring tool that provides information about network devices and their resources.

### 2. Engineers Toolset

A collection of network administration and troubleshooting tools used to monitor and analyze network infrastructure.

### 3. SNMP Scanner

A tool used to scan networks and identify devices running SNMP.

### 4. Getif

An SNMP-based network monitoring tool used to retrieve information from network devices.

### 5. OiDViEW SNMP MIB Browser

An SNMP MIB browser used to explore MIB objects and retrieve information from SNMP-enabled devices.

### 6. PRTG

A network monitoring solution that uses SNMP to monitor network devices and collect performance information.

### 7. snmp-check

A command-line tool used to enumerate information from SNMP-enabled devices.

### 8. SNScan

A tool used to scan networks for devices running SNMP.

### 9. SoftPerfect Network Scanner

A network scanning tool that can discover network devices and gather information about them.

### 10. SNMP Informant

A Windows-based SNMP extension that provides additional system information through SNMP.

### 11. Net-SNMP

A collection of command-line tools and utilities for working with SNMP, including querying and managing SNMP-enabled devices.

### 12. Nsauditor Network Security Auditor

A network security auditing tool that provides various network discovery and security assessment capabilities.

### 13. Spiceworks

A network inventory and monitoring platform used to discover and manage network devices.

---

## Related Links

- [RFC 3411 — SNMP Architecture](https://www.rfc-editor.org/rfc/rfc3411)
- [RFC 3416 — SNMP Protocol Operations](https://www.rfc-editor.org/rfc/rfc3416)
- [Net-SNMP Official Website](https://www.net-snmp.org/)
- [PRTG Network Monitor](https://www.paessler.com/prtg)
- [ManageEngine OpUtils](https://www.manageengine.com/products/oputils/)
- [Getif — SNMP MIB Browser](https://www.wtcs.org/snmp4tpc/getif.htm)
