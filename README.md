Home Network Traffic Analysis

Project 1 — Wireshark Network Capture
Analyst: Abudu Rudiyyah  
Date: 30 May 2026  
Tool: Wireshark on Kali Linux (VMware)  



## Objective

Capture and analyze live network traffic on a home network to identify active devices, observe protocol behavior, detect unencrypted traffic, and build foundational SOC analyst skills.

---

## Environment

| Component | Details |
|-----------|---------|
| OS | Kali Linux 2026.1 (VMware) |
| Hypervisor | VMware Workstation Pro |
| Network Mode | NAT |
| Analysis Tool | Wireshark |
| Scan Tool | Nmap |
| Capture Duration | ~5 minutes |



## Network Devices Found

Command used:
nmap -sn 192.168.146.0/24


Result: 4 hosts active out of 256 IPs scanned

| Host | IP Address | Role |
|------|-----------|------|
| 1 | 192.168.146.1 | Router / Gateway |
| 2 | 192.168.146.2 | Kali Linux VM (Analyst Machine) |
| 3 | 192.168.146.x | Windows Host Machine |
| 4 | 192.168.146.x | Additional Device |



## DNS Traffic

Filter used: dns

Domains observed in DNS queries:
- youtube.com
- fonts.googleapis.com
- models.com

Security note: DNS reveals every domain a machine attempts to contact. Malware uses DNS to reach command-and-control (C2) servers — unusual domain names in DNS traffic are a key indicator of compromise.



HTTP Traffic (Unencrypted)

Filter used: http

- 2 unencrypted HTTP packets found in the capture
- HTTP transmits data in plain text — credentials and session tokens are fully visible to anyone on the network
- Using Follow TCP Stream in Wireshark reveals the complete readable content of these sessions

Recommendation: All web traffic should use HTTPS. Unencrypted HTTP is a serious risk on any network.


## ICMP Traffic

Filter used: icmp

| ICMP Type | Direction | Meaning |
|-----------|-----------|---------|
| Echo Request (Type 8) | Kali → Windows | Ping sent |
| Echo Reply (Type 0) | Windows → Kali | Host is alive |

Security note: Thousands of ICMP packets per second to a single IP indicates a Ping Flood DDoS attack.


## ARP Traffic

Filter used: arp

- Multiple ARP broadcast packets observed (Source: VMware, Destination: Broadcast)
- ARP resolves IP addresses to MAC addresses on the local network
- ARP has no authentication — vulnerable to ARP Spoofing (Man-in-the-Middle attacks)



## Port Analysis

Via: Statistics → Endpoints → TCP tab

| Port | Protocol | Observation |
|------|----------|-------------|
| 443 | HTTPS/TLS | Most active — encrypted web traffic |
| 80 | HTTP | 2 unencrypted packets found |
| 53 | DNS | Domain name resolution |

---

## Suspicious Activity

No malicious traffic detected. Observations:
- 2 unencrypted HTTP packets — data exposure risk
- High ARP broadcast volume — normal but worth monitoring
- No unknown external IPs communicating with devices
- No suspicious ports detected (4444, 23, 8080)


## Key Learnings

- Wireshark filters allow rapid isolation of specific traffic types
- ARP operates at Layer 2 using broadcasts — vulnerable to spoofing
- DNS traffic reveals all domains a machine contacts — critical for threat detection
- Port 443 dominates modern traffic due to HTTPS
- Follow TCP Stream exposes full plaintext content of HTTP sessions
- Abnormal ICMP volumes indicate DDoS activity


## Files in this folder


home-network-capture.pcapng- Raw Wireshark capture file 
README.md- This analysis report 



