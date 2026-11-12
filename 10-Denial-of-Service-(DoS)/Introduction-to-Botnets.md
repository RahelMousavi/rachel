
# Introduction to Botnets

## 1. What Is a Botnet?

The term **Botnet** is derived from the words **Robot** and **Network**.

A botnet is a group of computers infected with malicious software that allows an attacker to control them remotely.

These infected computers are commonly called **Bots** or **Zombies**.

Botnets play an important role in cybercrime because they connect different types of malicious activities. An attacker can use infected systems as agents to perform unauthorized activities.

The bots may run hidden programs that help attackers identify vulnerabilities in other systems and expand the botnet.

## 2. Botnet Architecture

A typical botnet involves several components:

- **Attacker:** The person who controls the botnet and initiates malicious activities.
- **Bot:** An infected computer that executes instructions from the attacker.
- **Bot Command and Control (C&C) Server:** The infrastructure used to communicate with bots and distribute commands.
- **Zombies:** Compromised systems that are part of the botnet.
- **Target Server:** The system or service against which the botnet performs an attack.

### How a Botnet Operates

The diagram in the course illustrates the following general process:

1. The attacker establishes a Command and Control handler.
2. The attacker infects a computer.
3. The infected computer searches for other vulnerable systems and infects them.
4. The bots connect to the C&C handler and wait for instructions.
5. The attacker sends commands through the C&C infrastructure.
6. The bots execute the commands against the target server.

This structure allows an attacker to coordinate multiple compromised systems.

## Summary

- A botnet is a network of computers infected with malicious software.
- Infected computers are commonly called bots or zombies.
- The attacker coordinates botnet activities through Command and Control infrastructure.
- Botnets can be used to perform different malicious activities, including DDoS attacks.

## Related Links

- [Cloudflare — What Is a Botnet?](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-botnet/)
- [Microsoft — What Is a Botnet?](https://www.microsoft.com/en-us/security/business/security-101/what-is-a-botnet)
