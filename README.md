# Cisco DevNet Network Automation Lab

Two ways to automate the same task: creating, verifying, and deleting loopback
interfaces on a Cisco Catalyst 8000v, using the DevNet Always-On sandbox.

## Why two methods
- **RESTCONF (API-based):** structured, machine-readable, good where an API exists.
- **Netmiko (CLI-based):** works on any SSH-reachable device, no API required.

Comparing them on the same task shows when to reach for each.

## Environment
- Device: Cisco Catalyst 8000v, DevNet "Catalyst 8000 Always-On" sandbox
- Access: RESTCONF over HTTPS (Basic Auth) and SSH (Netmiko)
- Credentials: pulled from environment variables, never hardcoded

## Part 1 — RESTCONF
Tested first in Postman, then automated in Python with `requests`.

| Action | Method | Screenshot |
|---|---|---|
| List interfaces | GET | `01-restconf-get-interfaces.png` |
| Create Loopback100 | POST → 201 Created | `02-restconf-create-loopback-201.png` |
| Verify it exists | GET | `03-restconf-verify-loopback.png` |
| Re-create (expected failure) | POST → 409 Conflict | `04-restconf-conflict-409.png` |
| Delete Loopback100 | DELETE → 204 No Content | `05-restconf-delete-204.png` |

Run:
```bash
pip install -r requirements.txt
export DEVNET_HOST=<sandbox-hostname>
export DEVNET_USER=<username>
export DEVNET_PASS=<password>

python restconf/get_interfaces.py
python restconf/create_loopback.py
python restconf/delete_loopback.py
```

## Part 2 — Netmiko (CLI automation)
Same idea, different transport: SSH + `send_config_set()`, scaled to 20 interfaces
in a single session instead of one.

| Script | What it does | Screenshot |
|---|---|---|
| `create_loopbacks.py` | Creates Loopback201–220 | `06-cli-create-loopbacks.png` |
| `show_loopbacks.py` | Verifies with `show ip interface brief` | `07-cli-show-loopbacks.png` |
| `delete_loopbacks.py` | Removes Loopback201–220 | `08-cli-delete-loopbacks.png` |

Run:
```bash
cd cli
cp device_info_example.py device_info.py   # fill in your own values, don't commit real creds
python create_loopbacks.py
python show_loopbacks.py
python delete_loopbacks.py
```

## What I learned
- RESTCONF gives structured JSON back and clear HTTP status codes (201, 204, 409),
  which makes error handling straightforward.
- A single Netmiko session for 20 interfaces is far faster than opening 20 sessions —
  connection setup is the expensive part.
- Basic Auth headers and `verify=False` are fine for a lab sandbox with a self-signed
  cert; never disable certificate verification against a real device.

## Limitations / next steps
- No YAML inventory yet — hardcoded single device for now.
- No Ansible yet — CLI and API methods are separate scripts, not idempotent modules.
- Both are next in the roadmap (Ansible, November).

## Security note
No credentials are committed. All scripts read `DEVNET_HOST`, `DEVNET_USER`,
`DEVNET_PASS` from environment variables.
