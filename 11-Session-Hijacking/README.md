
# Module 11 — Session Hijacking

## Overview

Session Hijacking is a security attack in which an attacker takes control of an active session between a client and a server.

By obtaining a valid session identifier or interfering with an active communication, an attacker may impersonate a legitimate user and gain unauthorized access to information or services.

This module covers the concepts, techniques, tools, detection methods, and countermeasures related to Session Hijacking.

## Learning Objectives

By completing this module, you will understand:

- The concept and process of Session Hijacking.
- The differences between Passive and Active Session Hijacking.
- Application-Level and Network-Level Session Hijacking.
- Different techniques used to compromise session identifiers.
- Common Session Hijacking tools.
- Methods and tools for detecting session hijacking attempts.
- Security mechanisms and countermeasures for protecting sessions.

## Module Contents

### 01. Session Hijacking Concepts

- Introduction to Session Hijacking
- Why Session Hijacking Attacks Are Successful
- Session Hijacking Process
- Passive and Active Attacks
- Session Hijacking in the OSI Model
- Session Hijacking vs. Spoofing

### 02. Application-Level Session Hijacking

- Application-Level Session Hijacking
- Session ID Stealing, Guessing, and Brute Forcing
- Session Hijacking Using Sniffing
- Predictable Session IDs
- Man-in-the-Browser Attacks
- Client-Side Attacks
- Session Fixation
- CRIME Attack

### 03. Network-Level Session Hijacking

- Network-Level Hijacking
- TCP Three-Way Handshake
- TCP/IP Hijacking
- RST Hijacking
- Blind Hijacking
- Man-in-the-Middle (Packet Sniffing)
- UDP Hijacking
- PetitPotam Hijacking

### 04. Session Hijacking Tools

- Caido
- Burp Suite
- JHijack
- Surf Jack
- Ettercap
- Bettercap
- Per Jack
- WhatsUp Gold Engineer's Toolkit
- Cookie Cadger
- Firesheep
- Cookie Catcher
- T-sight
- SSLstrip

### 05. Session Hijacking Detection

- Session Hijacking Detection Methods
- Session Hijacking Detection Tools:
  - Wireshark
  - USM Anywhere
  - Quantum IPS
  - SolarWinds Security Event Manager
  - IBM Security Network Intrusion Prevention System
  - LogRhythm

### 06. Session Hijacking Countermeasures

- Session Hijacking Solutions for Protocols
- HTTP Strict Transport Security (HSTS)
- Token Binding
- DNS over HTTPS (DoH)
- General Countermeasures
- Recommendations for Web Developers
- Recommendations for Web Users

## Summary

Session Hijacking exploits weaknesses in session management and communication security to compromise active user sessions.

Understanding application-level and network-level attacks, recognizing suspicious activity, and implementing secure session management practices are essential for protecting users and services.

## Disclaimer

All practical security testing and experiments should be performed only in authorized and isolated lab environments.
