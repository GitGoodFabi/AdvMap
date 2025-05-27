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