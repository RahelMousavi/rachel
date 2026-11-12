
# MAC Addresses and CAM Tables

## MAC Addresses

A **MAC (Media Access Control) Address** is a hardware-level identifier assigned to a network interface.

It operates at the Data Link Layer (Layer 2) of the OSI model and is used for communication within a local network.

A traditional MAC address is 48 bits long and is usually represented in hexadecimal format.

Example:

```text
00:1A:2B:3C:4D:5E
```

Switches use MAC addresses to determine where Ethernet frames should be forwarded.

## CAM Tables

A **CAM (Content Addressable Memory) Table** is a table maintained by a network switch.

It stores information about learned MAC addresses and the switch ports associated with them.

For example, a switch may maintain entries such as:

```text
MAC Address          Switch Port
00:1A:2B:3C:4D:5E    FastEthernet0/1
00:1A:2B:3C:4D:6F    FastEthernet0/2
00:1A:2B:3C:4D:7A    FastEthernet0/3
```

When a switch receives an Ethernet frame, it examines the destination MAC address and uses its CAM table to determine the appropriate outgoing port.

If the destination MAC address is unknown, the switch generally floods the frame within the relevant VLAN, excluding the incoming port.

## CAM Table Exhaustion

Switches have limited memory for storing MAC address entries.

If an attacker sends a large number of Ethernet frames containing forged source MAC addresses, the switch may run out of available CAM table entries.

This technique is known as **MAC Flooding**.

When the CAM table becomes full, a switch may be unable to learn additional MAC addresses. Depending on the switch implementation and configuration, unknown unicast traffic may then be flooded to multiple ports within the VLAN.

This behavior can potentially expose traffic to unauthorized devices connected to the same network segment.

**Important:** A full CAM table does not necessarily make every switch behave exactly like a hub. Modern switches may use additional protections and different forwarding behaviors.

## MAC Flooding Tool: macof

`macof` is a Linux-based tool included in the `dsniff` suite.

It can generate Ethernet frames with randomized source MAC addresses and is commonly associated with MAC flooding demonstrations.

It is useful for understanding how CAM table exhaustion can affect switch behavior.

**Lab Safety:** Only test MAC flooding in an isolated virtual lab or on network equipment you own or have explicit permission to test.

## Countermeasures

Several measures can help protect switches against MAC flooding:

- Enable Port Security on access ports.
- Limit the number of MAC addresses learned on each port.
- Use sticky MAC addresses where appropriate.
- Configure violation actions such as restrict or shutdown.
- Monitor unusual MAC address learning activity.
- Use network segmentation to limit the impact of attacks.

## Related Links

- [Cisco - Port Security Configuration Guide](https://www.cisco.com/c/en/us/support/docs/lan-switching/port-security/12013-5.html)
- [Cisco - Understanding MAC Address Tables](https://www.cisco.com/)
- [dsniff Project](https://github.com/dugsong/dsniff)

## Summary

Switches use CAM tables to associate MAC addresses with physical ports and forward Ethernet frames efficiently. MAC flooding attempts to exhaust the table by generating frames with forged source MAC addresses. Port Security, MAC address limits, and network monitoring help reduce the risk of this attack.
