
# 01. Intrusion Detection and Prevention Systems

## 1. Intrusion Detection System (IDS)

An **Intrusion Detection System (IDS)** is a hardware or software security solution designed to monitor, detect, and protect networks or systems against malicious activities.

IDS continuously monitors incoming and outgoing network traffic and examines it for suspicious activities that may indicate a security violation.

When an intrusion is detected, the IDS generates an alert and notifies the responsible security personnel.

IDS can identify suspicious traffic by comparing it against known attack patterns and signatures.

### 1.1 IDS Deployment and Placement

One of the most common locations for deploying an IDS is near the firewall.

Depending on the traffic that needs to be monitored, an IDS can be placed:

- **Outside the Firewall:** To monitor suspicious traffic originating from external networks.
- **Inside the Firewall:** To monitor suspicious activities within the internal network.

A recommended approach is **Defense in Depth**, which involves deploying:

- One IDS before the firewall.
- Another IDS behind the firewall, inside the internal network.

This arrangement provides visibility into both external and internal network activities.

### 1.2 How IDS Works

The primary purpose of an IDS is to provide real-time monitoring and detect intrusions within a network.

Its general operation involves:

1. Monitoring network traffic or system activities.
2. Analyzing collected data.
3. Identifying suspicious patterns or known attack signatures.
4. Generating alerts when potential intrusions are detected.

Depending on its capabilities, an IDS may also support tracking, responding to, or preventing certain security incidents.

## 2. Intrusion Prevention System (IPS)

An **Intrusion Prevention System (IPS)** is also known as an active IDS because it can not only detect intrusions but also take action to prevent them.

IPS solutions continuously monitor network traffic and are generally deployed behind firewalls to provide an additional layer of protection.

Unlike a passive IDS, an IPS operates **inline** within the network, meaning it is placed directly in the communication path between the source and destination.

This allows it to analyze traffic and make automatic decisions about incoming network packets.

### 2.1 Types of IPS

Similar to IDS, IPS solutions are divided into two main categories:

- **Network-Based IPS (NIPS):** Monitors network traffic to detect and prevent malicious activities.
- **Host-Based IPS (HIPS):** Monitors activities on individual systems to detect and prevent suspicious behavior.

## 3. Intrusion Detection Methods

IDS uses different methods to identify suspicious activities and potential intrusions.

### 3.1 Signature Recognition

Signature Recognition identifies attacks by looking for known patterns or signatures associated with malicious activities.

The system compares observed events against a database of known attack signatures.

If a match is found, the IDS generates an alert.

**Limitation:** This method is generally less effective against previously unknown attacks that do not have known signatures.

### 3.2 Anomaly Detection

Anomaly Detection identifies intrusions by monitoring the normal behavior patterns of users and system components.

Any significant deviation from established behavior may indicate a potential intrusion.

**Example:** If a user normally accesses a system during business hours but suddenly performs unusual activities at midnight, the IDS may identify this behavior as suspicious.

### 3.3 Protocol Anomaly Detection

Protocol Anomaly Detection uses models based on specific network protocols, particularly TCP/IP, to identify unusual or unexpected protocol behavior.

The system compares observed protocol activities against expected protocol standards and behavior.

Deviations from these models may indicate malicious activity.

## 4. General Signs of Intrusion

Intrusions may produce different indicators depending on whether the attack targets a network or an individual system.

### 4.1 Network Intrusion Indicators

Common signs of suspicious network activity include:

- Sudden increases in network bandwidth consumption.
- Connections originating from unusual locations.
- Repeated remote login attempts.
- Unexpected changes in network configurations or firewall rules.
- Unusual or suspicious entries in log files.

### 4.2 System Intrusion Indicators

Common signs of suspicious activity on a system include:

- The presence of new and unauthorized files or programs.
- Unexpected changes in file permissions.
- Unexplained changes in file sizes or missing files.
- The presence of fake or unwanted files on the system.

These indicators should be investigated because they may suggest unauthorized access or malicious activity.

## 5. Types of IDS

Based on where monitoring takes place, IDS solutions can be classified into two main types.

### 5.1 Network-Based IDS (NIDS)

A **Network-Based Intrusion Detection System (NIDS)** monitors network traffic to identify suspicious activities and potential attacks.

NIDS commonly operates in **Promiscuous Mode**, allowing it to capture and inspect network packets passing through a monitored network segment.

It can help detect activities such as:

- Denial-of-Service (DoS) attacks.
- Port scanning.
- Attempts to compromise systems.

### 5.2 Host-Based IDS (HIDS)

A **Host-Based Intrusion Detection System (HIDS)** analyzes the behavior and activities of an individual system.

It can be installed on both client systems and servers.

HIDS focuses on local system changes and can be particularly effective in detecting unauthorized modifications to files.

Its monitoring mechanisms commonly include auditing events that occur on a specific host.

### NIDS vs. HIDS

- **NIDS:** Focuses on monitoring network traffic and identifying suspicious network activities.
- **HIDS:** Focuses on monitoring individual systems, including local activities and unauthorized file changes.

Using both approaches can provide broader visibility into security events.

## 6. IDS Alert Types

IDS alerts are classified according to whether an attack actually occurred and whether the system generated an alert.

There are four possible outcomes:

### 6.1 True Positive (Attack - Alert)

An actual attack occurs, and the IDS correctly detects it and generates an alert.

### 6.2 False Positive (No Attack - Alert)

No actual attack occurs, but the IDS incorrectly identifies normal activity as malicious and generates an alert.

### 6.3 False Negative (Attack - No Alert)

An actual attack occurs, but the IDS fails to detect it and does not generate an alert.

### 6.4 True Negative (No Attack - No Alert)

No attack occurs, and the IDS correctly identifies the activity as normal without generating an alert.

## Related Links

- [NIST SP 800-94 – Guide to Intrusion Detection and Prevention Systems](https://csrc.nist.gov/pubs/sp/800/94/final) – A technical guide covering IDS/IPS technologies, deployment, configuration, and maintenance.
- [Snort Documentation](https://docs.snort.org/) – Documentation for a network intrusion detection and prevention system.

## Summary

- **IDS** monitors network or system activities and generates alerts when suspicious behavior is detected.
- **IPS** can actively prevent detected threats and typically operates inline.
- The three detection methods covered in this section are Signature Recognition, Anomaly Detection, and Protocol Anomaly Detection.
- **NIDS** monitors network traffic, while **HIDS** monitors individual systems.
- IDS alerts are classified as True Positive, False Positive, False Negative, and True Negative.
- Deploying IDS solutions at different network locations can improve visibility and support Defense in Depth.
