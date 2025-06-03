import instaloader
import os

PROFILE_NAME = "pixels.of.fabi"

L = instaloader.Instaloader()

print("🔍 Versuche Session zu laden...")

try:
    L.load_session_from_file(PROFILE_NAME)
    print("✅ Session geladen!")
except FileNotFoundError:
    print("❌ Keine Session-Datei gefunden.")
except Exception as e:
    print(f"⚠️ Fehler beim Laden der Session: {e}")

# Pfad zur Session-Datei ausgeben
config_dir = os.path.join(os.path.expanduser("~"), ".config", "instaloader")
session_file = os.path.join(config_dir, f"{PROFILE_NAME}.session")
print(f"📁 Erwarteter Session-Dateipfad: {session_file}")

# Test: Bist du eingeloggt?
try:
    profile = instaloader.Profile.from_username(L.context, PROFILE_NAME)
    print(f"👤 Profil geladen: {profile.username}")
    print(f"🔐 Eingeloggt als: {L.test_login()}")
except Exception as e:
    print(f"❌ Fehler beim Zugriff auf Instagram-Profil: {e}")
