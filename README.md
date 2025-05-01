# 🛡️ Spotify Ads Blocker (Windows Hosts File Modifier)

A lightweight Python script that blocks **Spotify ads** on Windows by automatically adding ad-related domains to your system's `hosts` file.

> ⚠️ This script must be run as **administrator** to function correctly.

---

## 🚀 Features

- Blocks known Spotify ad servers via `hosts` file
- No external dependencies
- Simple, quick, and effective

---

## 🔒 Domains Blocked

The following ad/tracking domains are redirected to `127.0.0.1`:

```plaintext
127.0.0.1 ads-fa.spotify.com
127.0.0.1 analytics.spotify.com
127.0.0.1 adclick.g.doubleclick.net
127.0.0.1 pagead46.l.doubleclick.net
127.0.0.1 googleads.g.doubleclick.net
127.0.0.1 pubads.g.doubleclick.net
127.0.0.1 audio-ads.spotify.com
127.0.0.1 ads.spotify.com
127.0.0.1 tracking.spotify.com
🖥️ Requirements
Windows OS

Python 3.x installed

Administrator privileges

🛠️ How to Use
Open Command Prompt as Administrator

Run the script:

bash
Copier
Modifier
python spotify.py
You should see a success message:
✅ Block added

If not, make sure you are running the terminal as Administrator.

⚠️ Disclaimer
This tool is for educational purposes only.

Blocking ads may violate Spotify's terms of service.

Use responsibly, and consider supporting the platforms you enjoy.
