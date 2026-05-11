# groupquest-app
Dokumentation 
Mitglieder: Mona Auer, Zoe Auer, Amelie Gerhardt, Leni Biasi 

Srcummaster: Zoe Auer

Product owner: Leni Biasi

Entwicklungsteam: Mona, Amelie

Sprint 1 Ziel:
User können sich registrieren, einloggen und Challenges sehen
# Projektdokumentation — GroupQuest-App

# 1. Projektübersicht

## Projektname
GroupQuest-App

## Projektidee
Die GroupQuest-App ist eine motivierende Social-Challenge-App, bei der Nutzer:innen gemeinsam Challenges absolvieren können. Ziel der App ist es, Motivation, Fortschritt und Zusammenarbeit sichtbar zu machen.

Die Anwendung ermöglicht:
- Registrierung und Login
- Erstellen von Challenges
- Anzeigen aller Challenges
- Verwaltung von Nutzerkonten
- Zusammenarbeit über Gruppen und Social Features (geplant)

Die Entwicklung erfolgt mit:
- Python
- Streamlit
- SQLite
- GitHub
- SCRUM

---

# 2. Team & Rollen

| Rolle | Person |
|---|---|
| Scrum Master | Zoe Auer |
| Product Owner | Leni Biasi |
| Development Team | Mona Auer, Amelie Gerhardt |
| Dokumentation | gesamtes Team |

---

# 3. Verwendete Technologien

| Technologie | Zweck |
|---|---|
| Python | Backend-Logik |
| Streamlit | Frontend/Web-App |
| SQLite | Datenbank |
| GitHub | Versionsverwaltung |
| GitHub Projects | Scrum Board |
| Git | Zusammenarbeit im Team |

---

# 4. Projektorganisation mit SCRUM

Das Projekt wurde nach der SCRUM-Methode organisiert.

Dabei wurden:
- Features definiert
- User Stories erstellt
- Prioritäten vergeben
- Sprint-Planungen durchgeführt
- Sprint-Reviews durchgeführt
- Sprint-Retrospektiven durchgeführt

---

# 5. Product Backlog

## Features

### Feature 1 — Authentication
- Registrierung
- Login
- Logout
- Passwortschutz

### Feature 2 — Challenges
- Challenge erstellen
- Challenge anzeigen
- Challenge löschen
- Challenge Beschreibung

### Feature 3 — Gruppen
- Gruppen erstellen
- Gruppen beitreten

### Feature 4 — Fortschritt / Check-ins
- Fortschritt posten
- Text-Check-ins

### Feature 5 — Gamification
- Punkte
- Levels
- Badges

### Feature 6 — Social Feed
- Feed
- Kommentare
- Likes
- Leaderboard

---

# 6. GitHub Organisation

Für die Projektverwaltung wurden folgende GitHub-Elemente verwendet:

## Repository
groupquest-app

## GitHub Project Board
SCRUM Board mit:
- Todo
- In Progress
- Done

## Milestones
Features wurden als Milestones dokumentiert.

## Issues
Jede User Story wurde als eigenes Issue angelegt.

---

# 7. Sprint 1

## Sprint Planning

### Sprint Ziel
Erstellung einer ersten funktionierenden Streamlit-App mit:
- Registrierung
- Login
- SQLite Datenbank
- Challenges erstellen
- Challenges anzeigen

### Ausgewählte User Stories
- US-01 Registrierung erstellen
- US-02 Login erstellen
- US-05 Challenge erstellen
- US-09 Challenge Liste anzeigen

### Aufwandsschätzung
Die User Stories wurden mit T-Shirt-Größen bewertet:
- XS
- S
- M

### Priorisierung
- P0 → sehr wichtig
- P1 → wichtig
- P2 → optional

---

## Sprint Umsetzung

### Umgesetzte Funktionen
- Streamlit-App erstellt
- SQLite Datenbank integriert
- Login-System implementiert
- Registrierung implementiert
- Challenges speichern
- Challenges anzeigen

### Technische Umsetzung

#### Datenbank
SQLite wurde verwendet.

Erstellte Tabellen:
- users
- challenges

#### Frontend
Das Frontend wurde mit Streamlit umgesetzt.

#### Projektstruktur

groupquest-app/

├── app.py  
├── database.py  
├── requirements.txt  

├── pages/  
│   ├── login.py  
│   └── challenges.py  

└── data/

---

## Sprint Review

Im Sprint Review wurde die funktionierende Anwendung präsentiert.

### Präsentierte Funktionen
- Registrierung neuer User
- Login bestehender User
- Erstellung neuer Challenges
- Anzeige gespeicherter Challenges

### Ergebnis
Das Sprintziel wurde erfolgreich erreicht.

Die umgesetzten User Stories konnten demonstriert werden.

---

## Sprint Retrospektive

### Was gut funktioniert hat
- Erfolgreiche Zusammenarbeit im Team
- GitHub-Projekt erfolgreich eingerichtet
- Erste funktionierende Web-App erstellt
- Verwendung von Git und GitHub gelernt
- Scrum Board erfolgreich genutzt

### Herausforderungen
- Einstieg in GitHub war anfangs schwierig
- Verständnis von Milestones und Issues musste zuerst aufgebaut werden
- Git Push/Pull Konflikte mussten gelöst werden

### Verbesserungen für den nächsten Sprint
- Bessere Aufgabenaufteilung
- Häufigere Commits
- Frühzeitigeres Pushen auf GitHub
- Strukturiertere Kommunikation im Team

---

# 8. Sprint 2

## Sprint Planning

### Geplante Erweiterungen
- Logout-Funktion
- Gruppenfunktionen
- Challenge löschen
- Verbesserte Benutzeroberfläche
- Social Features

### Ziel
Die App soll erweitert und benutzerfreundlicher gestaltet werden.

---

# 9. Aktueller Stand des Projekts

Aktuell verfügt die App über:
- funktionierende Registrierung
- funktionierenden Login
- SQLite Datenbank
- Challenge-System
- GitHub Repository
- Scrum Board
- Dokumentation

Die Anwendung läuft lokal erfolgreich über Streamlit.

---

# 10. Fazit

Im bisherigen Projektverlauf konnte erfolgreich eine erste Version der GroupQuest-App entwickelt werden.

Besonders wichtig war:
- das Erlernen von GitHub
- die Arbeit mit SCRUM
- die Entwicklung einer echten Web-App
- Teamarbeit im Entwicklungsprozess

Das Projekt bildet eine solide Grundlage für die weiteren Sprintphasen und zukünftige Erweiterungen der Anwendung.
