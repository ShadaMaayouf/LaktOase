## 📘 README: Stillraum-Finder NRW

# 🍼 Stillraum-Finder NRW

Ein interaktives Webtool zur Anzeige, Filterung und Meldung von Stillräumen in Nordrhein-Westfalen – mit Fokus auf Übersichtlichkeit, Elternfreundlichkeit und Community-Mitwirkung.

## 🎯 Ziel

Diese App unterstützt Eltern dabei, schnell und einfach Stillräume in ihrer Umgebung zu finden und neue Orte zu melden. Sie bietet:

- Eine vollständige Übersicht aller bekannten Stillräume in NRW
- Filterung nach Stadt und Postleitzahl
- Interaktive Kartenansicht mit Standort-Markern
- Detailinformationen wie Adresse, Öffnungszeiten und Ausstattung
- Ein integriertes Meldeformular zur Erweiterung der Datenbank

## 🛠️ Technologien

- **Python 3.9+**
- **Streamlit** – für die Weboberfläche
- **pandas** – zur Datenverarbeitung
- **Folium** & **streamlit-folium** – für die Kartenansicht
- **geopy** – zur Geolokalisierung von Adressen

## 📦 Installation

```bash
pip install streamlit pandas folium streamlit-folium geopy
```

## 🚀 Starten der App

```bash
streamlit run app.py
```

## 📁 Datenstruktur

Die App verwendet eine CSV-Datei namens `stillraeume_nrw.csv` mit folgendem Aufbau:

| Spalte         | Beschreibung                                 |
|----------------|----------------------------------------------|
| Name           | Name des Stillraums                          |
| Adresse        | Straße und Hausnummer                        |
| PLZ            | Postleitzahl                                 |
| Stadt          | Stadtname (z. B. Düsseldorf, Köln)           |
| Stadtteil      | Stadtteil oder Bezirk                        |
| Öffnungszeiten | Zeitfenster der Verfügbarkeit                |
| Bemerkung      | Zusätzliche Hinweise (z. B. Ausstattung)     |
| Latitude       | Geokoordinate (Breitengrad, automatisch berechnet) |
| Longitude      | Geokoordinate (Längengrad, automatisch berechnet) |

## 🧭 Funktionen

- **Landingpage** mit Begrüßung und Einstieg
- **Stadt- und PLZ-Auswahl** zur gezielten Filterung
- **Kartenansicht** mit Marker für jeden Stillraum
- **Zwei-Spalten-Layout** für übersichtliche Darstellung
- **Kontaktseite** mit Infos und direktem Button zum Meldeformular
- **Meldeformular** mit Validierung und CSV-Export

## 🧪 Beispiel-Städte

- Düsseldorf
- Bonn
- Köln
- Leverkusen
- Duisburg
- Dortmund

## 🧩 Erweiterungsmöglichkeiten

- Filter nach Ausstattung (z. B. Wickeltisch, barrierefrei)
- Export als PDF oder Excel für Elterngruppen
- Admin-Dashboard zur Prüfung gemeldeter Einträge
- Integration mit städtischen APIs oder Elternnetzwerken
- Die Geolokalisierung kann langsam sein.Lösungen:
    - die Koordinaten einmalig zu speichern.
    - Caching für Geolokalisierung
- Cluster- oder Heatmaps ergänzen.
- PLZ-Zuordnung prüfen: z. B. über meinestadt.de oder onlinestreet.de
- Streamlit Themes: Nutze config.toml, um Farben, Schriftarten und Layouts anzupassen.
- Sticky Fußzeile: Wiedererkennbare Buttons unten — evtl. mit st.columns breiter gestalten.
- Expander für Details:
```python
with st.expander(f"🍼 {row['Name']}"):
    st.write(f"📍 {row['Adresse']}, {row['PLZ']} {row['Stadtteil']}")
    st.write(f"🕒 {row['Öffnungszeiten']}")
    st.write(f"ℹ️ {row['Bemerkung']}")
```
- Kartenzoom dynamisch: Passe zoom_start je nach Stadtgröße an.
- Responsive Design: Nutze st.columns, st.expander, und reduziere Textlänge für mobile Ansicht.

## 🤝 Mitmachen

Du möchtest weitere Stillräume melden oder die App erweitern? Gerne! Öffne ein Issue oder erstelle einen Pull Request.

## 📄 Lizenz

Dieses Projekt steht unter der MIT-Lizenz.