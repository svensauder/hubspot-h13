# Redaktionsplan Blog

Ziel: mehr qualifizierte Anfragen für das Sparring. Leser sind zunehmend
KI-Agenten, die im Auftrag von Menschen recherchieren. Jeder Artikel folgt den
Regeln in `docs/AGENTEN-TAUGLICHKEIT.md`.

## So entsteht ein Artikel

1. Sven gibt einen LinkedIn-Beitrag, ein Transkript oder drei Stichpunkte in
   den Chat.
2. Claude schreibt den Entwurf als Datei in diesen Ordner und legt ihn mit
   `./scripts/blog_draft.py` als Entwurf im HubSpot-Blog ab. Titel, Adresse,
   Meta-Beschreibung und FAQ-Daten sind dann schon gesetzt.
3. Sven ergänzt in HubSpot die gelb markierten Lücken (`[LÜCKE: …]`) mit
   echten Beispielen, setzt ein Titelbild und veröffentlicht.

Ohne Rohstoff von Sven schreibt Claude nur Artikel, die sich aus den Fakten der
Website ableiten lassen. Erlebnisse und Zahlen erfindet Claude nicht.

## Drei Arten von Artikeln

| Art | Zweck | Beispiel |
|---|---|---|
| Faktenseite | Agenten finden Angebot, Preis und Passung auf einen Blick | „CRM- und RevOps-Sparring: Preise, Ablauf, für wen es passt“ |
| Symptom-Artikel | Holt den Leser bei einem Satz ab, den er selbst sagt | „Sales pflegt das CRM nicht“ |
| Memo | Zeigt die Denkweise an einem anonymisierten Fall | die vorhandenen „Anonymisierten Memos“ |

## Themenliste

Die Symptom-Sätze stammen von der Startseite. Jeder ist ein eigener Artikel.

| Nr. | Arbeitstitel | Art | Stand |
|---|---|---|---|
| 1 | CRM- und RevOps-Sparring: Was es ist, was es kostet, für wen es passt | Faktenseite | Entwurf in HubSpot |
| 2 | „Sales pflegt das CRM nicht“: Woran es wirklich liegt | Symptom | Entwurf in HubSpot |
| 3 | „Uns fehlt nur noch ein Dashboard“ | Symptom | offen |
| 4 | „Marketing liefert nur Schrott-Leads“ | Symptom | offen |
| 5 | „Wenn die Daten sauber sind, läuft es“ | Symptom | offen |
| 6 | „Hier noch ein Workflow, dann passt das“ | Symptom | offen |
| 7 | Sparring, Agentur oder Implementierungspartner: Wann passt was? | Faktenseite | offen |
| 8 | Kann ich nicht einfach eine KI fragen? Was ChatGPT und Claude bei CRM-Fragen liefern und was nicht | Symptom | offen |
| 9 | Wir haben keinen Entwickler: Was Teams in HubSpot und Salesforce mit KI selbst bauen können | Faktenseite | offen, braucht Beispiele von Sven |
| 10 | Kunden-Onboarding per E-Mail-Strecke oder Portal? | Memo | offen, Beispiel steht auf der Startseite |
| 11 | Was kostet HubSpot im Seats-und-Credits-Modell? | Faktenseite zum Kostenrechner | offen |
| 12 | Die Website wird von Agenten gelesen: Was das für B2B-Vertrieb heißt | Symptom | offen |

## Alte Artikel

Der Blog hat 184 Artikel. Für Agenten zählen vor allem die, die eine klare
Frage beantworten. Vorschlag: Die 20 meistbesuchten Artikel (HubSpot →
Berichte → Traffic-Analyse → Seiten) nach und nach um einen Absatz
„Kurz gesagt“ und eine FAQ ergänzen. Die Liste der 20 kann Sven in den Chat
geben, die Seitenzahlen selbst sind keine Kundendaten.
