# AdvMap 🗺️

**Your adventure mapping tool for climbers, riders and explorers.**

## 🚀 Features

- 🧗 Crag database with map integration (Leaflet + OpenStreetMap)
- 📝 Markdown-enabled blog for trip reports
- 📷 Image uploads and rich content support
- 🌍 Dynamic map markers with popups
- 🔗 Instagram integration

## 🛠 Built with

- [Django](https://www.djangoproject.com/)
- [Leaflet.js](https://leafletjs.com/)
- Markdown2 for content rendering

## 📦 Setup (local)

```bash
git clone https://github.com/dein-name/advmap.git
cd advmap
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Because the vibe coder crafting this page has the memory of a bird here is how to start the server in cmd:
C:\Users\Admin\Documents\AdvMap> venv\Scripts\activate
(venv) PS C:\Users\Admin\Documents\AdvMap> cd AdvMap
(venv) PS C:\Users\Admin\Documents\AdvMap\AdvMap> python manage.py runserver    

🌌 Git:
# 🚀 AdvMap auf neuem Gerät klonen & entwickeln

## ✅ Voraussetzungen (einmalig auf dem neuen Gerät)
- Python 3.x
- Git
- (Optional) VS Code

---

## 🔁 Projekt klonen

```bash
git clone https://github.com/GitGoodFabi/AdvMap.git
cd AdvMap
```

---

## 🧱 Virtuelle Umgebung einrichten

```bash
python -m venv venv
.env\Scriptsctivate     # Windows
# source venv/bin/activate  # Linux/macOS
```

---

## 📦 Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

Falls `requirements.txt` fehlt, auf dem Ursprungsgerät ausführen:

```bash
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add requirements.txt"
git push
```

---

## ⚙️ Django vorbereiten

```bash
python manage.py migrate
```

---

## 🚀 Server starten

```bash
python manage.py runserver
```

Dann im Browser öffnen: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔄 Änderungen sichern

```bash
git add .
git commit -m "Mein Update von unterwegs"
git push
```

Auf anderen Geräten mit `git pull` synchronisieren.

---

**Tipp:** Erstelle einen SSH-Key oder nutze GitHub Token für einfaches Pushen.
