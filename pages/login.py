import streamlit as st
import sqlite3

st.title("🔐 Login & Registrierung")

conn = sqlite3.connect("data/groupquest.db")
cursor = conn.cursor()

menu = st.selectbox(
    "Menü",
    ["Registrieren", "Login"]
)

# REGISTRIERUNG
if menu == "Registrieren":

    st.subheader("Neuen Account erstellen")

    username = st.text_input("Username")
    password = st.text_input("Passwort", type="password")

    if st.button("Registrieren"):

        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )

            conn.commit()
            st.success("Registrierung erfolgreich!")

        except:
            st.error("Username existiert bereits!")

# LOGIN
elif menu == "Login":

    st.subheader("Einloggen")

    username = st.text_input("Username")
    password = st.text_input("Passwort", type="password")

    if st.button("Login"):

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        if user:
            st.success(f"Willkommen {username}!")
        else:
            st.error("Falsche Login-Daten")

conn.close()

