import streamlit as st
import sqlite3

st.title("🏆 Challenges")

conn = sqlite3.connect("data/groupquest.db")
cursor = conn.cursor()

# CHALLENGE ERSTELLEN
st.subheader("Neue Challenge erstellen")

challenge_title = st.text_input("Challenge Titel")
challenge_description = st.text_area("Beschreibung")

if st.button("Challenge speichern"):

    cursor.execute(
        "INSERT INTO challenges (title, description) VALUES (?, ?)",
        (challenge_title, challenge_description)
    )

    conn.commit()

    st.success("Challenge erstellt!")

# CHALLENGES ANZEIGEN
st.subheader("Alle Challenges")

cursor.execute("SELECT * FROM challenges")

challenges = cursor.fetchall()

for challenge in challenges:

    st.write(f"### {challenge[1]}")
    st.write(challenge[2])
    st.write("---")

conn.close()
