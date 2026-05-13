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

# Sprint 1 und 2 Retrospektive

## 1. Wo stehen wir mit unserem App-Projekt gerade?

Aktuell haben wir eine erste funktionierende Version unserer GroupQuest-App entwickelt.  
Die App läuft lokal mit Streamlit und besitzt bereits folgende Funktionen:

- Registrierung von Usern
- Login-System
- SQLite-Datenbank
- Challenges erstellen
- Challenges anzeigen
- GitHub Repository
- GitHub Scrum Board mit Issues und Milestones

Zusätzlich haben wir unsere Projektorganisation mit GitHub Projects erfolgreich eingerichtet und alle User Stories dokumentiert.

---

## 2. Wie hat uns SCRUM dabei unterstützt, den aktuellen Zwischenstand zu erreichen?

SCRUM hat uns geholfen, unsere Aufgaben besser zu strukturieren und den Überblick über das Projekt zu behalten.

Besonders hilfreich waren:
- Sprint Planning zur Planung der Aufgaben
- GitHub Issues für die User Stories
- Milestones zur Organisation der Features
- Scrum Board zur Übersicht über Todo, In Progress und Done
- Sprint Reviews zur Kontrolle unseres Fortschritts

Durch die kurzen Sprints konnten wir Schritt für Schritt an der App arbeiten und schnell erste Ergebnisse sehen.

---

## 3. Wo hat uns SCRUM behindert?

Teilweise war der Einstieg in SCRUM und GitHub anfangs kompliziert.

Schwierigkeiten:
- Verständnis von Milestones und Issues
- Umgang mit Git Push/Pull Konflikten
- Aufteilung der Aufgaben im Team
- Branching und Git-Kommandos waren neu für uns

Am Anfang benötigten organisatorische Aufgaben mehr Zeit als erwartet.

---

## 4. Welche SCRUM-Tools setzen wir aktuell ein und funktionieren diese für uns?

Wir verwenden:
- GitHub Repository
- GitHub Projects
- GitHub Issues
- GitHub Milestones
- Git für Versionierung

Diese Tools funktionieren grundsätzlich gut für unser Team.  
Besonders hilfreich ist das Scrum Board, weil wir dort direkt sehen können:
- welche Aufgaben offen sind
- woran gerade gearbeitet wird
- welche Aufgaben abgeschlossen sind

Auch die Dokumentation der User Stories über Issues funktioniert gut.

---

## 5. Was ändern wir im nächsten Sprint, um effizienter arbeiten zu können?

Im nächsten Sprint möchten wir:
- Aufgaben klarer aufteilen
- häufiger Commits machen
- regelmäßiger auf GitHub pushen
- besser kommunizieren
- Branches strukturierter verwenden

Außerdem möchten wir früher testen, ob neue Funktionen korrekt funktionieren.

---

# Sprint 3 und 4 Retrospektive

## 1. Wo stehen wir mit unserem App-Projekt gerade?

Unsere App besitzt mittlerweile eine stabile Grundstruktur.

Aktuell vorhanden:
- funktionierendes Login-System
- Registrierung
- SQLite Datenbank
- Challenge-Erstellung
- Challenge-Anzeige
- GitHub Organisation
- Scrum Board
- Dokumentation

Die Anwendung läuft erfolgreich mit Streamlit im Browser.

Zusätzlich konnten wir unsere Zusammenarbeit im Team deutlich verbessern.

---

## 2. Wie einfach war es, das Feedback aus der ersten Retrospektive in unsere Abläufe zu integrieren?

Das Feedback aus der ersten Retrospektive konnten wir relativ gut umsetzen.

Verbesserungen:
- bessere Aufgabenverteilung
- häufigere Git-Commits
- klarere Kommunikation im Team
- strukturierteres Arbeiten mit GitHub

Dadurch konnten wir Konflikte und Probleme schneller lösen.

---

## 3. Wie gehen wir als Team mit Komplexität um? Nutzen wir Branches?

Ja, wir verwenden Git und arbeiten teilweise mit Branches.

Was gut funktioniert:
- paralleles Arbeiten im Team
- bessere Versionsverwaltung
- Nachvollziehbarkeit von Änderungen

Was schwierig war:
- Merge-Konflikte
- Push/Pull Fehler
- Verständnis der Git-Befehle

Zur Lösung:
- häufigere Synchronisation mit GitHub
- bessere Kommunikation
- kleinere Änderungen pro Commit

Dadurch konnten wir die Komplexität besser kontrollieren.

---

# Sprint Planning — Sprint 3

## Sprint Ziel
Erweiterung der bestehenden App und Verbesserung der Benutzeroberfläche.

## Geplante User Stories
- US-03 Logout Funktion
- US-06 Challenge Beschreibung hinzufügen
- US-07 Challenge Dauer festlegen
- US-10 Gruppe erstellen

## Priorisierte Aufgaben
P0 und P1 User Stories wurden zuerst bearbeitet.

---

# Sprint Review — Sprint 3

## Präsentierte Ergebnisse
- Verbesserte Challenge-Funktionen
- Erweiterte Datenbank
- Optimierte Streamlit Oberfläche
- Verbesserte GitHub Organisation

## Ergebnis
Die geplanten Funktionen konnten größtenteils umgesetzt werden.

---

# Sprint Retrospektive — Sprint 3

## Was gut funktioniert hat
- bessere Zusammenarbeit
- strukturierteres Arbeiten
- schnellere Problemlösung

## Was verbessert werden soll
- noch häufigere Tests
- sauberere Branch-Struktur
- bessere Zeitplanung

---

# Sprint Planning — Sprint 4

## Sprint Ziel
Vorbereitung der finalen Präsentation und Stabilisierung der App.

## Geplante Aufgaben
- Fehlerbehebung
- Verbesserung des Designs
- README fertigstellen
- Dokumentation abschließen
- Präsentation vorbereiten

---

# Sprint Review — Sprint 4

## Ergebnisse
- funktionierende Streamlit-App
- vollständige Dokumentation
- GitHub Repository organisiert
- Scrum Board gepflegt
- User Stories dokumentiert

## Ergebnis
Die App ist bereit für die finale Präsentation.

---

# Sprint Retrospektive — Sprint 4

## Positives
- Teamarbeit hat sich verbessert
- GitHub wird sicherer verwendet
- SCRUM-Prozess funktioniert besser

## Herausforderungen
- Zeitmanagement
- Git-Konflikte
- technische Probleme

## Learnings
- kleine Commits helfen
- klare Kommunikation ist wichtig
- frühes Testen spart Zeit

---

# Finale Präsentation — Vorbereitung

## 1. Wie schaut eure finale App aus?

Unsere finale App ist eine Streamlit-Webanwendung mit:
- Login-System
- Registrierung
- Challenge-System
- SQLite Datenbank
- GitHub Scrum Organisation

Die App läuft lokal im Browser über Streamlit.

---

## 2. Die 3 wichtigsten Lessons Learned

1. Git und GitHub richtig verwenden  
2. Arbeiten mit SCRUM und Sprintplanung  
3. Zusammenarbeit im Entwicklerteam

---

## 3. Was würden wir beim nächsten Projekt anders machen?

- früher mit Branches arbeiten
- Aufgaben klarer verteilen
- regelmäßiger testen
- früher mit der Dokumentation beginnen

---

## 4. Wie können wir die Lessons Learned im nächsten Semester nutzen?

Die Erfahrungen helfen uns:
- besser im Team zu arbeiten
- GitHub sicherer zu verwenden
- Projekte strukturierter zu planen
- SCRUM effizienter einzusetzen
- schneller Webanwendungen zu entwickeln
