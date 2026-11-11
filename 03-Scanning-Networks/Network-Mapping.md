
# Network Mapping

Network Mapping is the process of identifying and visually representing the structure and architecture of a computer network.

A network map provides valuable information about the target network by showing its physical and logical structure.

It helps network administrators and security professionals understand how devices are connected and how information flows within the network.

## 1. Types of Network Maps

Network maps generally represent two aspects of a network:

### 1. Physical Network Map

A Physical Network Map represents the physical components and connections of a network.

It may include:

- Routers
- Switches
- Servers
- Workstations
- Network cables
- Firewalls
- Physical network connections

**Example:** A diagram showing how computers are connected to switches and how switches connect to routers.

### 2. Logical Network Map

A Logical Network Map represents how a network is organized logically, regardless of its physical layout.

It may include:

- IP address ranges
- Subnets
- VLANs
- Network segments
- Routing relationships
- Logical connections between devices
- DMZ and Intranet zones

**Example:** A diagram showing how an organization's internal network, DMZ, and external network communicate with each other.

## 2. Importance of Network Mapping in Ethical Hacking

Network mapping helps an ethical hacker understand the architecture of a target network before performing further security assessments.

It provides information about:

- Network devices and their roles.
- Connections between different systems.
- Internal and external network segments.
- Servers and other important resources.
- Security boundaries such as firewalls and DMZs.
- Potential entry points and exposed services.

A network map can help identify the network's attack surface and support further reconnaissance and vulnerability assessment.

## 3. Example of a Network Map

A typical enterprise network may contain three main areas:

### Intranet

An Intranet is a private internal network used by an organization.

It may contain:

- Employee workstations
- File servers
- Application servers
- Database servers
- Internal switches and routers

### DMZ (Demilitarized Zone)

A DMZ is a separate network segment that hosts services accessible from external networks while isolating them from the internal network.

It may contain:

- Web servers
- Email servers
- Public-facing application servers

### Internet

The Internet represents the external network through which users and external systems communicate with public-facing services.

Firewalls and routers are commonly used to control communication between the Internet, DMZ, and Intranet.

---

# Network Mapping Tools

Several tools can help administrators discover network devices, visualize connections, and create network topology diagrams.

The following tools are listed in the course material.

## 1. Network Topology Mapper

Network Topology Mapper is a network mapping tool that automatically discovers network devices and creates visual representations of network topology.

It can help identify:

- Routers and switches.
- Servers and workstations.
- Network connections.
- Device relationships.

## 2. LANState

LANState is a network monitoring and mapping tool designed to visualize LAN devices and monitor their availability.

It can help administrators maintain an overview of devices within a local network.

## 3. OpManager

ManageEngine OpManager is a network monitoring and management solution.

It provides network topology maps and helps administrators monitor devices such as routers, switches, and servers.

## 4. Network View

NetworkView is a network discovery and mapping utility used to identify devices and display network information.

It can help create a visual overview of network infrastructure.

## 5. What's Connected

What's Connected is a network discovery utility that identifies devices connected to a local network.

It can help administrators discover computers and other network-connected devices.

## 6. Insightix Visibility

Insightix Visibility was a network visibility and discovery solution designed to provide information about network-connected devices and infrastructure.

It is a legacy product name in the course material.

## 7. InterMapper

InterMapper is a network monitoring and mapping solution.

It provides visual network maps and helps administrators monitor network devices, connections, and performance.

## 8. Friendly Pinger

Friendly Pinger is a network monitoring and diagnostic utility that can help discover devices and monitor their availability.

## 9. IPsonar

IPsonar is a network discovery and security visibility solution associated with identifying network assets and understanding network exposure.

## 10. NetMapper

NetMapper is a network mapping tool name listed in the course material for visualizing network infrastructure.

## 11. Switch Center Enterprise

Switch Center Enterprise is a network management tool focused on monitoring and managing network switches and related infrastructure.

## 12. NetBrain Enterprise Suite

NetBrain Enterprise Suite is a network automation and visualization platform.

It helps organizations discover, visualize, and document network infrastructure.

## 13. HP OpenView Network Node Manager

HP OpenView Network Node Manager was an enterprise network management solution used to discover, monitor, and visualize network devices.

It is a legacy product name associated with HP's network management portfolio.

## Summary

Network Mapping provides a visual representation of network architecture and helps security professionals understand the target environment.

Two important types of network maps are:

- **Physical Network Map:** Represents physical devices and connections.
- **Logical Network Map:** Represents logical network organization, segmentation, and communication paths.

Some network mapping tools mentioned in the course include:

- Network Topology Mapper
- LANState
- OpManager
- InterMapper
- NetBrain Enterprise Suite
- HP OpenView Network Node Manager

**Key Concept:** Network Mapping helps identify network devices, understand their relationships, and visualize the physical and logical architecture of a target network.

---

## Related Links

### Network Mapping Tools

- [SolarWinds Network Topology Mapper](https://www.solarwinds.com/network-topology-mapper) — Automated network discovery and topology mapping.
- [ManageEngine OpManager](https://www.manageengine.com/network-monitoring/network-topology-mapper.html) — Network monitoring and automated topology mapping.
- [InterMapper](https://www.intermapper.com/) — Network mapping and real-time monitoring.
- [NetBrain](https://www.netbraintech.com/) — Network automation, discovery, and visualization.
- [10-Strike LANState](https://www.10-strike.com/lanstate/) — LAN monitoring and network visualization.
- [NirSoft — Network Utilities](https://www.nirsoft.net/network_tools.html) — Collection of network discovery and diagnostic utilities.

### Network Diagramming

- [diagrams.net (draw.io)](https://www.diagrams.net/) — Free tool for creating physical and logical network diagrams.
- [Microsoft Visio](https://www.microsoft.com/en-us/microsoft-365/visio/flowchart-software) — Diagramming tool with network diagram templates.

### Network Discovery and Documentation

- [Nmap Official Documentation](https://nmap.org/docs.html) — Network discovery and host scanning.
- [Nmap Host Discovery](https://nmap.org/book/man-host-discovery.html) — Techniques for identifying active hosts.
- [RFC 1918 — Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918.html) — Private IPv4 address ranges commonly used in Intranets.
