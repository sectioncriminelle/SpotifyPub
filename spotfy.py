import os
import ctypes

def chekadmin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

textprblock = """

# Spotify
127.0.0.1 ads-fa.spotify.com
127.0.0.1 analytics.spotify.com
127.0.0.1 adclick.g.doubleclick.net
127.0.0.1 pagead46.l.doubleclick.net
127.0.0.1 googleads.g.doubleclick.net
127.0.0.1 pubads.g.doubleclick.net
127.0.0.1 audio-ads.spotify.com
127.0.0.1 ads.spotify.com
127.0.0.1 tracking.spotify.com
127.0.0.1 ap-gew1.spotify.com
127.0.0.1 gew1-dealer-ssl.spotify.com
"""

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

def added():
    try:
        with open(hosts_path, "a", encoding="utf-8") as file:
            file.write("\n" + textprblock.strip() + "\n")
        print("✅ Blocage ajouté ")
    except PermissionError:
        print("❌ Merci de lancer en Admin")
    except Exception as e:
        print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    if chekadmin():
        added()
    else:
        print("❌ Merci de lancer en Admin")
