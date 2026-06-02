# Python Packet Sniffer — Scapy

## Project 2 — Cybersecurity Portfolio
**Tool:** Python + Scapy on Kali Linux
**Date:** June 2026

## What it does
- Captures live TCP, UDP and ICMP traffic
- Timestamps every packet
- Flags suspicious ports (4444, 8080, 23, 1337, 9001)
- Logs all traffic to capture_log.txt

## How to run
sudo python3 sniffer.py

## What I found
- Google servers communicating on port 443 (HTTPS and QUIC/UDP)
- HTTP traffic on port 80 from Google
- QUIC protocol (UDP/443) used by YouTube for faster streaming
- No suspicious ports detected in capture

## Key learnings
- Scapy requires root (sudo) to capture raw packets
- UDP port 443 = QUIC protocol, not standard HTTPS
- Use whois or nslookup to identify unknown IPs
- Suspicious ports matter more than suspicious IPs

## Tools used
- Python 3
- Scapy 2.7.0
- Kali Linux
