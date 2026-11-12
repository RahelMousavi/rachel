
# Honeypots

## 1. Honeypot Concepts

A **Honeypot** is a system deployed within a network to attract and deceive attackers who attempt to gain unauthorized access.

Honeypots can:

- Record attempts to access network ports.
- Monitor an attacker's activities.
- Help security teams observe suspicious behavior.
- Collect information about potential threats and attack techniques.

## 2. Types of Honeypots

### Low-Interaction Honeypot

A Low-Interaction Honeypot provides a limited number of services for attackers to interact with.

- It simulates only a limited set of services.
- It is designed to reduce the risk of being fully compromised.
- It provides limited information about attacker activities.

**Examples:** SPECTER and KFSensor.

### High-Interaction Honeypot

A High-Interaction Honeypot simulates or provides access to a broader range of services and applications.

- Attackers can interact with a more realistic environment.
- It allows security professionals to observe more detailed attacker behavior.
- It has a higher risk of being fully compromised.

## 3. Honeypot Tools

The following tools are introduced in this section:

- KFSensor
- SPECTER
- LaBrea Trapit
- Patriot Box
- Kojoney
- Honey BOT
- Google Hack Honeypot
- Win Honeyd
- HIHAT
- Argos
- Glastopf

## Related Links

- [NIST SP 800-94 - Guide to Intrusion Detection and Prevention Systems](https://csrc.nist.gov/pubs/sp/800/94/final)
- [KFSensor Official Website](https://www.keyfocus.net/kfsensor/)
- [Honeyd Project](https://github.com/DataSoft/Honeyd)
- [Glastopf GitHub Repository](https://github.com/mushorg/glastopf)

## Summary

- A Honeypot is a decoy system designed to attract attackers and monitor their activities.
- It can record unauthorized access attempts and provide useful information for security analysis.
- **Low-Interaction Honeypots** simulate a limited number of services and are less likely to be fully compromised.
- **High-Interaction Honeypots** provide a more realistic environment but carry a higher risk of compromise.
- Several Honeypot tools are introduced in this section, including KFSensor, SPECTER, Kojoney, Honeyd, and Glastopf.
