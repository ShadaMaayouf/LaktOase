import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim

# -------------------------------
# 📁 Daten laden und vorbereiten
# -------------------------------
CSV_PATH = "stillraeume_nrw.csv"
df = pd.read_csv(CSV_PATH)
df["Volladresse"] = df["Adresse"] + ", " + df["PLZ"].astype(str) + " " + df["Stadt"]

# Geolokalisierung (einmalig ausführen, dann speichern)
geolocator = Nominatim(user_agent="stillraum_app")
def get_coords(adresse):
    try:
        location = geolocator.geocode(adresse)
        return pd.Series([location.latitude, location.longitude]) if location else pd.Series([None, None])
    except:
        return pd.Series([None, None])

if "Latitude" not in df.columns or "Longitude" not in df.columns:
    df[["Latitude", "Longitude"]] = df["Volladresse"].apply(get_coords)

# -------------------------------
# 🔗 Fußzeile mit Navigation
# -------------------------------
def footer_navigation():
    st.markdown("---")
    cols = st.columns([1, 1])
    with cols[0]:
        if st.button("🏠 Zur Landingpage"):
            st.session_state["page"] = "landing"
    with cols[1]:
        if st.button("📬 Kontakt"):
            st.session_state["page"] = "contact"

# -------------------------------
# 🧭 Seitensteuerung
# -------------------------------
if "page" not in st.session_state:
    st.session_state["page"] = "landing"

# -------------------------------
# 📬 Kontaktseite
# -------------------------------
if st.session_state["page"] == "contact":
    st.title("📬 Kontakt")
    st.markdown("""
    Du möchtest Feedback geben oder mit dem Projektteam in Kontakt treten?

    **E-Mail:** LaktOase@outlook.com  
    **Instagram:** [@stillraumfinder.nrw](https://instagram.com/LaktOase.nrw)  
    **GitHub:** [Projektseite](https://github.com/ShadaMaayouf/LaktOase)

    Wir freuen uns über jede Rückmeldung!
    """)

    if st.button("➕ Stillraum melden"):
        st.session_state["page"] = "melden"

    footer_navigation()
    st.stop()

# -------------------------------
# 📝 Meldeformular für Stillräume
# -------------------------------
if st.session_state["page"] == "melden":
    st.title("➕ Stillraum melden")

    with st.form("meldeformular"):
        name = st.text_input("Name des Stillraums")
        adresse = st.text_input("Straße und Hausnummer")
        plz = st.text_input("Postleitzahl")
        stadt = st.text_input("Stadt")
        stadtteil = st.text_input("Stadtteil")
        zeiten = st.text_input("Öffnungszeiten")
        bemerkung = st.text_area("Bemerkung oder Ausstattung")

        submitted = st.form_submit_button("Absenden")

        if submitted:
            if not name or not adresse or not plz or not stadt:
                st.error("Bitte fülle mindestens Name, Adresse, PLZ und Stadt aus.")
            elif not plz.isdigit():
                st.error("Die Postleitzahl muss eine Zahl sein.")
            else:
                new_entry = pd.DataFrame([{
                    "Name": name,
                    "Adresse": adresse,
                    "PLZ": int(plz),
                    "Stadt": stadt,
                    "Stadtteil": stadtteil,
                    "Öffnungszeiten": zeiten,
                    "Bemerkung": bemerkung
                }])
                new_entry["Volladresse"] = adresse + ", " + plz + " " + stadt
                new_entry[["Latitude", "Longitude"]] = new_entry["Volladresse"].apply(get_coords)
                new_entry.to_csv(CSV_PATH, mode="a", header=False, index=False)
                st.success("🎉 Vielen Dank! Der Stillraum wurde erfolgreich gemeldet. Du hilfst anderen Eltern, sich besser zurechtzufinden.")

    footer_navigation()
    st.stop()

# -------------------------------
# 🍼 Landingpage
# -------------------------------
if st.session_state["page"] == "landing":
    st.title("🍼 Willkommen bei der LaktOase – Der Stillraum-Finder für NRW")
    st.markdown("""
    Diese App hilft dir, Stillräume in deiner Nähe zu finden – übersichtlich, interaktiv und elternfreundlich.

    ✅ Filter nach Stadt und Postleitzahl  
    ✅ Kartenansicht mit Standort-Markern  
    ✅ Alle Details wie Adresse, Öffnungszeiten und Ausstattung  
    ✅ Möglichkeit zur Meldung neuer Stillräume

    ---
    """)
    if st.button("Los geht's"):
        st.session_state["page"] = "finder"
    footer_navigation()
    st.stop()

# -------------------------------
# 🔍 Hauptansicht: Finder-Modus
# -------------------------------
st.sidebar.title("🧭 Navigation")
selected_stadt = st.sidebar.selectbox("Wähle eine Stadt", sorted(df["Stadt"].unique()))
show_map = st.sidebar.checkbox("🗺️ Kartenansicht anzeigen")

stadt_df = df[df["Stadt"] == selected_stadt]
plz_list = sorted(stadt_df["PLZ"].unique())
selected_plz = st.sidebar.selectbox("Optional: Filtere nach PLZ", ["Alle anzeigen"] + [str(plz) for plz in plz_list])
filtered_df = stadt_df if selected_plz == "Alle anzeigen" else stadt_df[stadt_df["PLZ"] == int(selected_plz)]

st.title("🍼 Stillräume in Nordrhein-Westfalen")
st.subheader(f"📍 Stadt: {selected_stadt}" + (f", PLZ: {selected_plz}" if selected_plz != "Alle anzeigen" else ""))

if show_map:
    st.markdown("### 🗺️ Karte der Stillräume")
    m = folium.Map(location=[51.5, 7.0], zoom_start=10)
    for _, row in filtered_df.dropna(subset=["Latitude", "Longitude"]).iterrows():
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=f"{row['Name']} ({row['Stadtteil']})",
            tooltip=row["Adresse"]
        ).add_to(m)
    st_folium(m, width=700, height=500)

st.markdown("### 📋 Stillräume")
for i in range(0, len(filtered_df), 2):
    cols = st.columns(2)
    for j in range(2):
        if i + j < len(filtered_df):
            row = filtered_df.iloc[i + j]
            with cols[j]:
                st.markdown(f"#### 🍼 {row['Name']}")
                st.write(f"📍 **Adresse:** {row['Adresse']}, {row['PLZ']} {row['Stadtteil']}, {row['Stadt']}")
                st.write(f"🕒 **Öffnungszeiten:** {row['Öffnungszeiten']}")
                st.write(f"ℹ️ **Bemerkung:** {row['Bemerkung']}")
                st.markdown("—")

footer_navigation()
