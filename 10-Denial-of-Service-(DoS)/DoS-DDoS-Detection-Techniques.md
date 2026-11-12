
# DoS/DDoS Detection Techniques

## Introduction

DoS/DDoS detection techniques aim to identify abnormal increases in network traffic and distinguish malicious traffic from legitimate traffic spikes, also known as **Flash Events**.

These techniques generally identify an attack as an unusual deviation from the normal network traffic threshold.

## 1. Activity Profiling

**Activity Profiling** is based on measuring the average packet rate within a network flow.

Network traffic profiles are created by monitoring packet headers.

An attack may be detected when the activity level across network flow clusters increases beyond its normal behavior.

## 2. Sequential Change-Point Detection

**Sequential Change-Point Detection** uses algorithms to identify sudden changes in network traffic statistics.

The general process includes:

1. Filtering traffic based on IP addresses, ports, or protocols.
2. Storing the filtered traffic as a time series.
3. Analyzing changes in traffic patterns.
4. Using the **CUSUM** algorithm to identify and locate potential DoS attacks.

### CUSUM

**CUSUM (Cumulative Sum)** is a statistical algorithm used to detect sudden changes in data patterns or averages.

In network security, CUSUM helps identify significant deviations from normal traffic behavior.

#### How It Works

1. Network traffic is continuously recorded as a time series.
2. The algorithm calculates the difference between current values and expected average values.
3. These differences are accumulated over time.
4. Significant deviations can indicate abnormal network activity or a potential attack.

## 3. Wavelet-Based Signal Analysis

**Wavelet-Based Signal Analysis** examines incoming traffic signals by decomposing them into spectral components.

The energy of each spectral window is analyzed to identify possible anomalies.

Abnormal signals are then distinguished from background noise.

This technique helps detect unusual patterns in network traffic.

## Summary

- **Activity Profiling:** Monitors average packet rates within network flows to identify unusual increases in activity.
- **Sequential Change-Point Detection:** Identifies sudden changes in traffic statistics.
- **CUSUM:** Uses cumulative statistical changes to detect deviations from normal traffic behavior.
- **Wavelet-Based Signal Analysis:** Examines spectral components and identifies abnormal traffic patterns.

## Related Links

- [NIST — Guide to Intrusion Detection and Prevention Systems](https://csrc.nist.gov/pubs/sp/800/94/final)
- [NIST — DDoS Attack Prevention and Response](https://www.nist.gov/)
- [Wikipedia — CUSUM](https://en.wikipedia.org/wiki/CUSUM)
- [MathWorks — Wavelet Analysis](https://www.mathworks.com/help/wavelet/)
