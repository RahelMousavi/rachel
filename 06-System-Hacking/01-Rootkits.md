
# Rootkits

## Introduction to Rootkits

A **Rootkit** is a type of malicious software designed to hide the presence of an attacker, malicious programs, or unauthorized activities on a compromised system.

Rootkits may modify operating system components or interfere with normal system functions to make malicious activities difficult to detect.

A rootkit may contain or work alongside:

- Backdoors
- DDoS tools
- Packet sniffers
- Log-removal utilities
- Other malicious programs

Some rootkits modify system files, kernel components, drivers, or system calls to hide malicious processes and files.

## How Rootkits Infect Systems

Attackers may introduce rootkits into a system through different methods:

- **Bundling with legitimate-looking software:** Hiding malicious components inside software packages, games, or other downloads.
- **Social Engineering:** Convincing users to install or execute malicious software.
- **Zero-Day Exploitation:** Exploiting previously unknown vulnerabilities to compromise a system and install malicious components.

Other possible infection methods include compromised software updates, malicious attachments, and exploitation of existing system vulnerabilities.

## Objectives of Rootkits

Rootkits may be used to achieve several objectives:

### 1. Gain Persistent or Privileged Access

Some rootkits help attackers maintain access to a compromised system, potentially with elevated privileges.

### 2. Hide Malicious Activities

Rootkits can hide:

- Malicious files
- Running processes
- Network connections
- Registry entries
- Other traces of unauthorized activity

### 3. Collect Sensitive Information

Some rootkits work with other malware to collect sensitive information, monitor network traffic, or access data on the compromised system.

### 4. Support Other Malicious Activities

A compromised system may be used to host additional malware or participate in attacks such as Distributed Denial of Service (DDoS).

## Types of Rootkits

Rootkits can be classified according to the system component or execution level they target.

### 1. Hypervisor-Level Rootkit

A **Hypervisor-Level Rootkit** operates at the virtualization layer.

It may attempt to place the original operating system inside a virtualized environment controlled by the malicious hypervisor.

This can allow the rootkit to monitor or manipulate the operating system from a lower level.

### 2. Kernel-Level Rootkit

A **Kernel-Level Rootkit** operates within the operating system kernel.

It may modify kernel code, kernel data structures, or device drivers to hide malicious activities.

Kernel-level rootkits are particularly dangerous because the kernel has extensive control over system operations.

### 3. Application-Level Rootkit

An **Application-Level Rootkit** targets applications and user-level components.

It may replace legitimate application files, modify application behavior, or inject malicious code into running processes.

### 4. Hardware/Firmware Rootkit

A **Hardware/Firmware Rootkit** targets firmware or hardware-related components.

It may modify firmware stored in devices such as network adapters, storage controllers, or system firmware.

Because firmware operates below the operating system, these rootkits can be difficult to detect using ordinary security software.

### 5. Bootloader-Level Rootkit

A **Bootloader-Level Rootkit** modifies or replaces components involved in the system boot process.

It may execute before the operating system fully loads, allowing malicious code to operate early in the startup process.

### 6. Library-Level Rootkit

A **Library-Level Rootkit** targets system libraries or shared functions.

It may replace or modify legitimate library functions to hide information about malicious files, processes, or activities.

## Examples of Rootkits

The course introduces the following rootkit examples:

- **LoJax:** A UEFI firmware rootkit discovered in the wild. It demonstrated how attackers could maintain persistence by modifying system firmware.
- **Necurs:** A malware family associated with a large botnet and rootkit-like capabilities.
- **Scranos:** A malware family known for spreading through malicious software and using rootkit-related techniques.
- **Horse Pill:** A rootkit-related name included in the course material; its technical details and classification should be independently verified.

These examples illustrate that rootkit-related threats can target different layers of a computer system.

## Summary

A rootkit is designed to hide malicious activities and maintain unauthorized access to a compromised system.

Rootkits may target different system layers:

- **Hypervisor-Level:** Operates at the virtualization layer.
- **Kernel-Level:** Modifies kernel components or drivers.
- **Application-Level:** Modifies applications or user-level components.
- **Hardware/Firmware:** Targets firmware or hardware-related components.
- **Bootloader-Level:** Modifies the system boot process.
- **Library-Level:** Alters system libraries or their functions.

Because rootkits can operate at low levels of a system, they may be difficult to detect and remove.

## Related Links

- [MITRE ATT&CK - Rootkit (T1014)](https://attack.mitre.org/techniques/T1014/)
- [MITRE ATT&CK - Boot or Logon Autostart Execution](https://attack.mitre.org/techniques/T1547/)
- [ESET - LoJax UEFI Rootkit](https://www.welivesecurity.com/2018/09/27/lojax-first-uefi-rootkit-found-wild/)
- [Microsoft Security](https://www.microsoft.com/en-us/security)
