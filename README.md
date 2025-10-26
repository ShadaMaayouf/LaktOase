# LaktOase

## 🧩 Projektidee: Stillraum-Finder für Düsseldorf

### 🔍 Ziel
Eine interaktive Web-App, die alle öffentlich zugänglichen Stillräume in Düsseldorf nach Postleitzahl filterbar darstellt — inklusive Adresse und ggf. Zusatzinfos wie Öffnungszeiten oder Ausstattung.

### 🛠️ Technologiestack
- **Frontend & Web-Framework**: [Streamlit](https://streamlit.io/) (einfach, schnell, ideal für Prototypen)
- **Backend-Datenstruktur**: pandas DataFrame
- **Datenquelle**: Manuell gepflegte CSV oder JSON-Datei mit Stillraum-Daten (später erweiterbar durch Webscraping oder API)

### 📦 Beispiel-Datenstruktur (CSV oder JSON)
```csv
Name,Adresse,PLZ,Stadtteil,Öffnungszeiten,Bemerkung
Düsseldorf Arcaden Stillraum,Friedrichstraße 133,40217,Friedrichstadt,"Mo-Sa 10-20 Uhr","Neben Kundentoiletten im UG & OG"
...
```

### 🧭 Nächste Schritte
1. **Datenbasis aufbauen**: z. B. mit Orten wie Düsseldorf Arcaden.
2. **PLZ-Zuordnung prüfen**: z. B. über [meinestadt.de](https://home.meinestadt.de/duesseldorf/postleitzahlen) oder [onlinestreet.de](https://onlinestreet.de/plz/D%C3%BCsseldorf.html).
3. **Design verfeinern**: z. B. mit Kartenansicht (Folium oder Mapbox) oder Icons für Ausstattung.


Wenn du magst, helfe ich dir beim Aufbau der CSV-Datei oder erweitere die App mit Features wie Favoriten, Hebammen-Tipps oder Wickelmöglichkeiten. Bereit für den nächsten Schritt?
