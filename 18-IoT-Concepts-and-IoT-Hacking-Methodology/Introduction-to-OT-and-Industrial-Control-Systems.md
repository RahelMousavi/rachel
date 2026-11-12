
# Introduction to OT and Industrial Control Systems

## 1. What is Operational Technology (OT)?

Operational Technology (OT) refers to the combination of hardware and software used to monitor or control physical industrial operations.

OT systems interact directly with industrial devices and processes.

Examples of OT components include:

- Switches
- Pumps
- Lights
- Sensors
- Surveillance Cameras
- Elevators
- Robots
- Valves
- HVAC Systems

Any system that analyzes or processes operational data may be considered part of an OT environment. This can include technical components, electronics, communication systems, and computer systems.

## 2. Essential OT Terminology

### 2.1 Assets

Assets are the physical components used in OT environments.

Examples include:

- Sensors
- Actuators
- Servers
- Workstations
- Network Devices

### 2.2 Zones and Conduits

Zones and Conduits are network segmentation concepts used to isolate networks and assets.

They help organizations apply and maintain access controls between different parts of an OT environment.

### 2.3 OT Industrial and Business Network

An OT industrial and business network is a collection of interconnected automated control systems designed to achieve a specific business objective.

It is also referred to as an industrial network.

### 2.4 Industrial Protocols

OT environments use different industrial communication protocols.

These protocols can be classified into two categories:

**Proprietary Protocols:**
- SRTP
- CDA
- S7

**Non-Proprietary Protocols:**
- Modbus
- CIP
- DNP3
- OPC

Industrial protocols commonly use serial communication. However, they may also operate over standard Ethernet using IP with TCP or UDP.

## 3. Challenges of OT Security

OT systems play critical roles in environments such as:

- Power Plants
- Water Facilities
- Healthcare Facilities

However, securing these environments can be challenging.

The course identifies the following challenges:

1. Vulnerable communication protocols
2. Unpatched systems
3. Lack of security visibility and awareness
4. Fake devices
5. Lack of antivirus protection
6. Plaintext passwords
7. Poor remote management
8. Lack of security specialists
9. Complex networks
10. Old or obsolete software versions

## 4. What is an Industrial Control System (ICS)?

An Industrial Control System (ICS) is an essential part of industrial processes.

The term often refers to a collection of different control systems and related equipment working together to monitor and control industrial operations.

ICS environments may include:

- Basic Process Control Systems (BPCS)
- Distributed Control Systems (DCS)
- Supervisory Control and Data Acquisition (SCADA)
- Safety Instrumented Systems (SIS)
- Remote Terminal Units (RTU)
- Programmable Logic Controllers (PLC)
- Human-Machine Interfaces (HMI)

ICS components include sensors, controllers, and actuators.

Actuators may be mechanical, electrical, hydraulic, or pneumatic. These components work together to achieve an industrial objective.

## 5. Distributed Control System (DCS)

A Distributed Control System (DCS) is a large-scale engineered control system designed to perform specific industrial tasks.

DCS technology is used in several industries, including:

- Chemical Production
- Nuclear Plants
- Oil Refineries
- Water and Wastewater Treatment
- Power Generation
- Automotive Industry
- Pharmaceuticals

### DCS Architecture

A DCS typically uses a central supervisory control unit to manage multiple local controllers.

These controllers may manage thousands of Input/Output (I/O) points and other devices involved in industrial production processes.

## 6. Supervisory Control and Data Acquisition (SCADA)

SCADA is a centralized system that provides supervisory control and real-time data acquisition from distributed assets in industrial environments.

### Main Functions

SCADA systems:

- Collect information from devices.
- Send collected information to a central computer system.
- Automate complex industrial processes.
- Measure and monitor trends in real time.
- Detect and help correct operational problems.

## 7. Safety Instrumented System (SIS)

A Safety Instrumented System (SIS) is an automated control system designed to protect industrial production environments during hazardous incidents.

It monitors and executes specific control functions to:

- Shut down a monitored system.
- Bring a system into a predefined safe state.
- Reduce the potential consequences of hazardous events.

SIS is an essential part of an industrial risk management strategy.

## Related Links

- [NIST - Guide to Operational Technology Security (SP 800-82)](https://csrc.nist.gov/pubs/sp/800/82/r3/final)
- [CISA - Industrial Control Systems](https://www.cisa.gov/topics/industrial-control-systems)
- [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)
- [OPC Foundation](https://opcfoundation.org/)
- [Modbus Organization](https://www.modbus.org/)

## Summary

Operational Technology combines hardware and software to monitor and control physical industrial processes.

Important OT concepts include assets, zones, conduits, industrial networks, and industrial protocols.

Industrial Control Systems (ICS) consist of multiple control systems and components, including DCS, SCADA, SIS, RTUs, PLCs, and HMIs.

- **DCS:** Controls industrial processes through distributed local controllers.
- **SCADA:** Provides centralized supervisory control and real-time data acquisition.
- **SIS:** Protects industrial processes by bringing systems into safe states during hazardous events.
