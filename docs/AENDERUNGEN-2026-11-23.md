# Änderungen vom 23.11.2026

Alles per API. Kundendaten wurden weder gelesen noch geschrieben.

## Neue Felder

| Objekt | Interner Name | Beschriftung | Typ | Gruppe |
|---|---|---|---|---|
| Kontakt | `lead_channel` | Lead-Kanal | Auswahl | Contact information |
| Kontakt | `lead_trigger_url` | Auslösender Inhalt (URL) | Text | Contact information |
| Deal | `lead_channel` | Lead-Kanal | Auswahl | Deal information |
| Unternehmen | `retainer_status` | Betreuungsstatus | Auswahl | Betreuung / Retainer (neu) |
| Unternehmen | `retainer_monthly_fee` | Monatliches Betreuungshonorar | Zahl (Währung) | Betreuung / Retainer |
| Unternehmen | `retainer_start_date` | Betreuung seit | Datum | Betreuung / Retainer |
| Unternehmen | `retainer_end_date` | Betreuung beendet am | Datum | Betreuung / Retainer |
| Unternehmen | `next_review_date` | Nächstes Kunden-Review | Datum | Betreuung / Retainer |

Werte von „Lead-Kanal“: LinkedIn-Beitrag, LinkedIn-Direktnachricht,
Blog-Artikel, Podcast, KI-Assistent / Agent, Empfehlung, Event, Sonstiges.
Der Wert „KI-Assistent / Agent“ ist für Kontakte gedacht, die über ChatGPT,
Claude, Perplexity oder einen anderen Agenten auf Hangar-13 gekommen sind.

Werte von „Betreuungsstatus“: Aktiv, Pausiert, Beendet, Keine laufende Betreuung.

## Neue Ticket-Pipeline „Kundenbetreuung“

Onboarding → Laufende Betreuung → Review fällig → Pausiert → Beendet (geschlossen).

Gedacht ist ein Ticket je betreutem Kunden. Es wandert bei jedem Review auf
„Review fällig“ und zurück.

## Aufgaben-Automatik in der Deal-Pipeline

| Phase | Workflow | Aufgabe |
|---|---|---|
| Qualification | 588310832 (unverändert) | Qualification |
| Pain & Impact Comm. | 1644155752 (war leer, befüllt) | Pain & Impact schärfen |
| Auftragsklärung | 5437084899 (neu) | Auftragsklärung: Entscheidung absichern |
| ClosedWon | 1606270030 (war leer, befüllt) | Übergabe in die Betreuung |
| Verloren | 588310840 (unverändert) | Closed Lost Deal nachhaken |

Jede Aufgabe wird Sven zugewiesen und hängt am Deal. Die Aufgabentexte stehen
in `metadata/workflows/<ID>.json`.

## Gelöschte Workflows

Mit Svens Zustimmung gelöscht. Alle drei taten nichts mehr. Die Definitionen
stehen in der Git-Historie unter `metadata/workflows/`.

| ID | Name | Grund |
|---|---|---|
| 600996770 | Dealphase „Angebot anpassen“ | Phase existiert nicht mehr, keine Aktion |
| 569765453 | Wenn ein Kontakt auf einen Link in der E-Mail klickt | abgeschaltet, nie fertig gebaut |
| 570225238 | Opportunity Reporting Mini Email Kurs Workflow | abgeschaltet, Kurs eingestellt |

Die fünf Marketing-Mails des Mini-Kurses liegen weiter in HubSpot.

## Abgeschaltete Workflows

Mit Svens Zustimmung abgeschaltet, nicht gelöscht. Wieder einschalten geht in
HubSpot unter Automatisierung → Workflows.

| ID | Name | Formular |
|---|---|---|
| 570748819 | Email Kurs Delivery | 0acbdd24-4bb0-4fd7-bb2d-3af5a5be2f48 |
| 571541570 | Follow-up nach Formular (Excel CRM) | c944c599-344d-4feb-9972-69242942cab9 |
| 576431900 | Follow-up nach Formular (OMR Messe Flow Templates) | d42e58ba-bb48-4ae8-b8e1-a2adfba6a57c |
| 579469705 | Follow-up nach Formular (Reporting-Inspo) | eb248979-b216-4af1-9e68-2d3d90c4f7f7 |
| 580872524 | Warteliste Anforderungsworkshop Training | 2a294ec8-800d-4f36-92e1-83529b4b517c |

Wer eines dieser Formulare jetzt ausfüllt, bekommt keine Mail mehr, und es
entsteht keine Aufgabe. Die Formulare selbst kann Claude nicht sehen. Bitte in
HubSpot unter Marketing → Formulare prüfen, ob sie noch auf einer Seite
eingebunden sind, und sie dort entfernen.

## Blog-Entwürfe in HubSpot

Nach Freigabe des Bereichs `content` als Entwurf angelegt, nicht veröffentlicht.

| Artikel | Entwurf in HubSpot | Offene Lücken |
|---|---|---|
| CRM- und RevOps-Sparring: Was es ist, was es kostet, für wen es passt | https://app-eu1.hubspot.com/blog/2368160/editor/522718516431/content | 2 |
| „Sales pflegt das CRM nicht“: Woran es wirklich liegt | https://app-eu1.hubspot.com/blog/2368160/editor/522741261522/content | 3 |

Lücken sind im Text gelb markiert. Beide Entwürfe tragen im Kopfbereich
strukturierte FAQ-Daten und haben noch kein Titelbild.

## Prüfen

1. Einen Test-Deal anlegen und durch die Phasen ziehen. In jeder Phase muss
   eine Aufgabe entstehen.
2. Einen Kontakt öffnen, „Alle Eigenschaften anzeigen“, nach „Lead-Kanal“ suchen.
3. Service → Tickets → Pipeline-Auswahl: „Kundenbetreuung“ muss erscheinen.

## Zurücknehmen

- Felder: Einstellungen → Eigenschaften → Feld archivieren.
- Pipeline: Einstellungen → Objekte → Tickets → Pipelines → löschen.
- Workflow 5437084899: löschen. In 1644155752 und 1606270030 die Aufgabe entfernen.

## Was nicht ging

| Vorhaben | Grund | Ersatz |
|---|---|---|
| Formulare um „Lead-Kanal“ ergänzen | Zugriff auf Formulare fehlt | Anleitung in `HANDARBEIT.md` |
| Dashboards, Ansichten, Vorlagen, Textbausteine | HubSpot bietet dafür keine API | Anleitung in `HANDARBEIT.md` |
| Langdock-Agent anlegen | In dieser Umgebung ist kein Langdock-API-Schlüssel hinterlegt | Fertige Vorlage unter `langdock/` |
