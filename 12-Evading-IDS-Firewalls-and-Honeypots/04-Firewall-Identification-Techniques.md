
# Firewall Identification Techniques

Firewall identification techniques are used to gather information about firewalls, their behavior, and the services they expose. The main techniques covered in this section are Port Scanning, Firewalking, and Banner Grabbing.

## 1. Port Scanning

Port Scanning is a technique used to identify open ports and the services running on a system.

Some firewalls listen on specific ports. By scanning these ports, it may be possible to identify the firewall product.

**Examples mentioned in the course:**

- **Check Point:** Listens on ports `256`, `257`, `258`, and `259`.
- **FortiGate:** During scanning, port `113` may appear closed, while ports `5060` and `2000` may appear open.

These port behaviors can provide clues about the firewall in use.

## 2. Firewalking

Firewalking is a technique used to identify network topology and determine the presence of a firewall by sending packets with specific TTL (Time to Live) values.

The response helps determine whether packets can pass through the firewall:

- **TTL Exceeded:** If the packet returns with a TTL Exceeded message, it indicates that the packet did not pass through the firewall.
- **Packet Reaches Destination:** If the packet reaches its destination, it indicates that the firewall allowed it to pass.

## 3. Banner Grabbing

Banner Grabbing is a technique used to identify the type of a service.

By collecting service banners, it may be possible to identify:

- The firewall vendor or manufacturer.
- The firewall firmware version.

This information can help determine which firewall product and version are being used.

## Related Links

- [Nmap Documentation](https://nmap.org/book/man.html)
- [Nmap Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html)
- [Nmap Service and Version Detection](https://nmap.org/book/man-version-detection.html)
- [Firewalking - Original Research Paper](https://www.packetfactory.net/firewalking/)

## Summary

Firewall identification techniques help discover information about firewalls and their configurations.

- **Port Scanning:** Identifies open ports and services.
- **Firewalking:** Uses TTL behavior to investigate network topology and firewall filtering.
- **Banner Grabbing:** Identifies service types and may reveal the firewall vendor and firmware version.
