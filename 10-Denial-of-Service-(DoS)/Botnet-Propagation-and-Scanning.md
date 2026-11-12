
# Botnet Propagation and Scanning

## 1. Identifying Vulnerable Systems

To expand a botnet, infected machines may search for additional vulnerable systems.

The course introduces five scanning methods used to identify potentially vulnerable machines.

### 1.1 Random Scanning

In **Random Scanning**, an infected machine randomly checks IP addresses within a target network range to identify vulnerable systems.

### 1.2 Hit-list Scanning

In **Hit-list Scanning**, the attacker first collects a list of potentially vulnerable machines.

The machines on this list are then scanned to identify vulnerable systems.

### 1.3 Topological Scanning

In **Topological Scanning**, information obtained from an already infected machine is used to identify new vulnerable machines.

### 1.4 Local Subnet Scanning

In **Local Subnet Scanning**, an infected machine searches for vulnerable systems within its own local network.

### 1.5 Permutation Scanning

In **Permutation Scanning**, a pseudo-random ordered list of IP addresses is used to search for additional vulnerable machines.

## 2. Malicious Code Propagation

The course introduces three methods for distributing malicious code to newly discovered vulnerable systems.

### 2.1 Central Source Propagation

In **Central Source Propagation**, the attacker places an attack toolkit on a central source.

The general process is:

1. The attacker identifies and compromises a vulnerable system.
2. The compromised system connects to the central source.
3. A copy of the malicious toolkit is transferred from the central source to the compromised system.
4. The process is repeated for other vulnerable systems.

### 2.2 Back-chaining Propagation

In **Back-chaining Propagation**, the attacker keeps the attack toolkit on their own system.

After compromising a machine, the attacker transfers the malicious code directly from their system to the newly compromised machine.

The process is repeated for additional systems.

### 2.3 Autonomous Propagation

In **Autonomous Propagation**, the infected system transfers the malicious code to another vulnerable system during the infection process.

The newly infected system can then continue the same process and infect additional machines.

## Summary

### Scanning Methods

- **Random Scanning:** Randomly checks IP addresses within a target range.
- **Hit-list Scanning:** Uses a previously collected list of potentially vulnerable systems.
- **Topological Scanning:** Uses information from an infected machine to identify new targets.
- **Local Subnet Scanning:** Searches for vulnerable systems within the infected machine's local network.
- **Permutation Scanning:** Uses a pseudo-random ordered list of IP addresses.

### Propagation Methods

- **Central Source Propagation:** Malicious code is distributed from a central source.
- **Back-chaining Propagation:** The attacker transfers malicious code directly to newly compromised systems.
- **Autonomous Propagation:** An infected system transfers malicious code to the next vulnerable system.

## Related Links

- [MITRE ATT&CK — Active Scanning](https://attack.mitre.org/techniques/T1595/)
- [MITRE ATT&CK — Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)
- [CISA — Malware](https://www.cisa.gov/topics/cyber-threats-and-advisories/malware)
