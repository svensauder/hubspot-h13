# Inventar der HubSpot-Konfiguration

Stand: 23.11.2026, nach den Änderungen dieses Tages. Rohdaten unter `metadata/`.

## Überblick

| Objekt | Eigene Felder | Bemerkung |
|---|---|---|
| Kontakte | 9 | davon 5 von der Dubletten-App Koalify |
| Unternehmen | 14 | davon 5 von Koalify, 5 neu für die Betreuung |
| Deals | 30 | 22 Qualifizierungs-Kästchen, 5 SPICED-Felder |
| Tickets | 23 | Gruppen „Off Market“ und „Discord Signals“ |

- Deal-Pipelines: 3 (`Pipeline`, `Automated Sales Pipeline`, `HubSpot Shared Selling Pipeline`)
- Ticket-Pipelines: 3 (`Support Pipeline`, `TheSquad Pipeline`, neu `Kundenbetreuung`)
- Workflows: 14, davon 9 aktiv (am 23.11.2026 drei tote gelöscht, fünf Lead-Magneten von 2024 abgeschaltet)
- Eigene Objekte: keine

## Workflows

| ID | Name | Aktiv | Was er tut | Einschätzung |
|---|---|---|---|---|
| 588310832 | Dealphase „Target / Identifiziert“ | ja | Aufgabe „Qualification“ beim Eintritt in die Phase Qualification | Funktioniert. Nur der Name ist veraltet. |
| 1644155752 | Phase „Pain & Impact Comm.“ | ja | Aufgabe „Pain & Impact schärfen“ | Neu befüllt am 23.11.2026, war leer |
| 5437084899 | Phase „Auftragsklärung“ | ja | Aufgabe „Auftragsklärung: Entscheidung absichern“ | Neu am 23.11.2026 |
| 1606270030 | Dealphase „Closed!“ | ja | Aufgabe „Übergabe in die Betreuung“ bei Gewonnen | Neu befüllt am 23.11.2026, war leer |
| 588310840 | Dealphase „Closed Lost“ | ja | Aufgabe „Closed Lost Deal nachhaken“ | Behalten |
| 3218548975 | Ticketstatus „Neu“ (Support) | ja | Nichts, keine Aktion | Löschen oder befüllen |
| 1626266645 | CRM Prozessvorlage, Formular 96eab298 | ja | Mail, 30 Min. warten, Aufgabe, 4 Tage warten, Mail, Liste 94 | Behalten, Seite ist online |
| 1639801715 | CRM Prozessvorlage, Formular 9d6531cf | ja | Gleiche Mails, zusätzlich Listen 94 und 105 | Behalten. Zwei fast gleiche Workflows, zusammenlegen möglich |
| 1638982516 | Newsletter-Liste nach Formular | ja | Fügt zu Liste 105 hinzu | Behalten |
| 570748819 | Email Kurs Delivery | nein | 4 Mails, jeweils samstags 10 Uhr | Am 23.11.2026 abgeschaltet |
| 571541570 | Follow-up nach Formular (Excel CRM) | nein | Mail und Aufgabe „Nachfragen ob das Excel CRM was gebracht hat“ | Am 23.11.2026 abgeschaltet |
| 576431900 | Follow-up nach Formular (OMR Messe Flow Templates) | nein | Mail und Aufgabe | Am 23.11.2026 abgeschaltet |
| 579469705 | Follow-up nach Formular (Reporting-Inspo) | nein | Mail und Aufgabe | Am 23.11.2026 abgeschaltet |
| 580872524 | Warteliste Anforderungsworkshop Training | nein | Aufgabe und Liste 63 | Am 23.11.2026 abgeschaltet |

Welche Formulare zu den IDs gehören und ob sie noch auf einer Seite eingebunden
sind, kann Claude nicht sehen (kein Zugriff auf Formulare). In HubSpot unter
Marketing → Formulare zeigt jedes Formular seine Einsendungen der letzten Zeit.

## Aufräum-Vorschläge

Nichts davon ist ausgeführt. Jede Zeile braucht ein Ja von Sven.

1. ~~Löschen: Workflows 600996770, 569765453, 570225238.~~ Erledigt am 23.11.2026.
2. ~~Abschalten: „Email Kurs Delivery“ (570748819).~~ Erledigt am 23.11.2026.
3. ~~Abschalten: 571541570, 576431900, 579469705, 580872524.~~ Erledigt am
   23.11.2026. Offen: die zugehörigen Formulare von den Seiten nehmen oder
   löschen, sonst trägt sich jemand ein und bekommt nichts.
4. Zusammenlegen: die beiden „CRM Prozessvorlage“-Workflows zu einem mit zwei
   Formular-Auslösern.
5. Koalify-Felder (5 an Kontakten, 5 an Unternehmen): Wenn die App nicht mehr
   installiert ist, können die Felder weg. Das Löschen von Feldern vernichtet
   deren Werte.
6. Deal-Pipeline „Automated Sales Pipeline“ (Payment Succeeded → Rechnung
   versendet → Buchhaltung erledigt): Wird sie noch befüllt? Rechnungen
   entstehen laut Sven in der Buchhaltungssoftware.
7. Die 22 Qualifizierungs-Kästchen am Deal haben sehr lange interne Namen
   (bis 90 Zeichen). Sie funktionieren. Umbenennen geht nicht, nur neu anlegen.
   Empfehlung: so lassen.

## Was schon da war und deshalb nicht neu gebaut wurde

| Zweck | Vorhandenes Feld |
|---|---|
| Nächster Schritt am Deal | `hs_next_step` (Standard) |
| Datum der nächsten Aktivität | `notes_next_activity_date` (Standard, füllt sich aus Aufgaben und Terminen) |
| Qualifizierung | Gruppen „SPICED Framework“ und „Qualification“ am Deal |
| Verlustgrund, Gewinngrund | `closed_lost_reason`, `closed_won_reason` (Standard) |
| Kundenumsatz | `total_revenue`, `recent_deal_amount`, `recent_deal_close_date` am Unternehmen (Standard, aus gewonnenen Deals) |
| Lead-Quelle frei formuliert | `wie_bist_du_auf_mich_aufmerksam_geworden_` am Kontakt |
| Online-Herkunft | `hs_analytics_source` (Standard) |
| Lead-Status | `hs_lead_status` mit eigenen Werten |
| Lifecycle | `lifecyclestage` mit eigenen Werten bis „Ex-Kunde“ |
