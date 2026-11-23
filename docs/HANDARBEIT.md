# Handgriffe in der HubSpot-Oberfläche

Diese Schritte kann Claude nicht ausführen: Entweder bietet HubSpot dafür keine
API, oder es wären Kundendaten im Spiel. Reihenfolge nach Nutzen. Zeitbedarf
insgesamt etwa 90 Minuten.

Wie viele Dashboards und Berichte Starter erlaubt, zeigt HubSpot beim Anlegen
an. Reicht das Kontingent nicht, zuerst alte Dashboards löschen.

## 1. Neue Felder sichtbar machen (10 Minuten)

Neue Felder erscheinen nicht von selbst in der linken Spalte eines Datensatzes.

- Einstellungen → Objekte → Kontakte → Datensatz anpassen → linke Seitenleiste:
  „Lead-Kanal“ und „Auslösender Inhalt (URL)“ hinzufügen.
- Dasselbe für Deals: „Lead-Kanal“, „Next step“, „Next Activity Date“.
- Dasselbe für Unternehmen: eine Karte „Betreuung“ mit den fünf neuen Feldern
  und „Total Revenue“.

## 2. Ansichten fürs Nachfassen (15 Minuten)

CRM → Deals → Ansicht hinzufügen:

| Ansicht | Filter | Sortierung |
|---|---|---|
| Ohne nächsten Schritt | Pipeline = Pipeline, Deal offen, „Next Activity Date“ ist unbekannt | Betrag absteigend |
| Überfällig | Deal offen, „Next Activity Date“ liegt vor heute | Datum aufsteigend |
| Zu lange in der Phase | Deal offen, „Date entered current stage“ liegt mehr als 30 Tage zurück | Datum aufsteigend |

Die erste Ansicht als Standard anheften. Sie ist die Antwort auf „Was versandet
gerade?“. Bei ein bis drei neuen Deals im Monat und Laufzeiten bis sechs Monate
ist ein Deal ohne Termin das eigentliche Risiko.

CRM → Kontakte → Ansicht „Neue Kontakte ohne Lead-Kanal“: Erstellt in den
letzten 30 Tagen, „Lead-Kanal“ ist unbekannt.

CRM → Unternehmen → Ansicht „Review fällig“: „Betreuungsstatus“ = Aktiv,
„Nächstes Kunden-Review“ liegt in den nächsten 14 Tagen oder davor.

CRM → Unternehmen → Ansicht „Schlafende Kunden“: „Total Revenue“ größer 0,
„Betreuungsstatus“ ist nicht Aktiv, „Recent Deal Close Date“ liegt mehr als
12 Monate zurück.

## 3. Pflichtfelder je Phase (10 Minuten)

Einstellungen → Objekte → Deals → Pipelines → Pipeline → Spalte
„Bedingte Phaseneigenschaften“:

| Beim Wechsel nach | Abfragen |
|---|---|
| Pain & Impact Comm. | Pain, Impact, Lead-Kanal |
| Auftragsklärung | Decision, Critical Event, Betrag, Abschlussdatum, Next step |
| ClosedWon | Closed Won Reason |
| Abgeschlossen und verloren | Closed Lost Reason |

Sollte HubSpot Pflichtfelder in Starter nicht erzwingen, erscheinen sie
trotzdem als Abfrage beim Phasenwechsel.

## 4. Dashboard „Vertrieb“ (20 Minuten)

Berichte → Dashboards → Dashboard erstellen → leeres Dashboard. Berichte aus
der Bibliothek hinzufügen:

1. Deal-Betrag nach Phase (offene Pipeline)
2. Gewichtete Deal-Prognose nach Abschlussmonat
3. Gewonnene Deals nach Monat, letzte 12 Monate
4. Deals nach „Lead-Kanal“ (Anzahl und Betrag)
5. Neue Kontakte nach „Lead-Kanal“ und Monat
6. Neue Kontakte nach „Original Traffic Source“
7. Unternehmen nach „Total Revenue“, die oberen 20
8. Summe „Monatliches Betreuungshonorar“ bei Betreuungsstatus = Aktiv

Bericht 6 zeigt unter „AI Referrals“ Besucher, die von KI-Assistenten kommen.
Das ist die Kennzahl dafür, ob die Website bei Agenten ankommt.

## 5. Formulare (10 Minuten)

Marketing → Formulare. In jedem aktiven Formular:

- Feld „Wie bist du auf mich aufmerksam geworden?“ behalten.
- Verstecktes Feld „Lead-Kanal“ ergänzen und je Seite vorbelegen: auf
  Blog-Seiten „Blog-Artikel“, auf der Podcast-Seite „Podcast“.
- Verstecktes Feld „Auslösender Inhalt (URL)“ ergänzen. HubSpot füllt es mit
  der Seitenadresse, wenn in der Feldoption die Vorbelegung über einen
  URL-Parameter gewählt wird.

## 6. Vorlagen und Textbausteine (15 Minuten)

Die Texte stehen in `content/vorlagen/nachfass-mails.md`.

- Bibliothek → Vorlagen: die fünf Mails anlegen.
- Bibliothek → Textbausteine (Snippets): die Kurzbausteine anlegen.

## 7. Blog-Entwürfe fertigstellen (je Artikel 15 Minuten)

Marketing → Website → Blog → Entwürfe. Je Artikel: gelb markierte Lücken
füllen, Titelbild setzen, Vorschau prüfen, veröffentlichen. Die Links stehen
in `AENDERUNGEN-2026-11-23.md`.

## 8. Aufräumen

- Die fünf Formulare der abgeschalteten Lead-Magneten von den Seiten nehmen
  (IDs in `AENDERUNGEN-2026-11-23.md`).
- Die übrigen Entscheidungen aus `INVENTAR.md`, Abschnitt „Aufräum-Vorschläge“
  (Punkte 4 bis 7).
