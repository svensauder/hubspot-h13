# Arbeitsregeln für das HubSpot-Projekt

Dieses Repo dokumentiert die HubSpot-Konfiguration von Hangar-13
(Portal 2368160, Starter Customer Platform, ein Nutzer).

## Feste Regeln

- **Keine Kundendaten.** Claude liest und schreibt nur Metadaten: Felder,
  Feldgruppen, Pipelines, Phasen, Workflow-Definitionen. Kein Aufruf von
  Endpunkten unter `/crm/v3/objects/`, keine Listenmitglieder, keine
  Formular-Einsendungen, keine E-Mails, keine Nachrichten. Zeigt ein Aufruf
  doch personenbezogene Daten, abbrechen und dem Nutzer Bescheid geben.
- Erlaubt ist zusätzlich der Bereich `content`: Blog-Beiträge und Seiten der
  Website lesen, Blog-Beiträge als Entwurf anlegen und ändern.
- Den Zugriff nicht erweitern und nicht um Erweiterung bitten, außer der
  Nutzer verlangt es.
- Starter ausreizen. Keine Vorschläge, die ein Upgrade oder kostenpflichtige
  Zusatztools voraussetzen, ohne das ausdrücklich zu sagen.
- Nichts löschen und keinen Workflow abschalten ohne ausdrückliche Zustimmung.
  Aufräum-Kandidaten stehen in `docs/INVENTAR.md`.
- Nichts versenden und nichts veröffentlichen. Blog-Artikel entstehen als
  Datei unter `content/blog/` und gehen mit `./scripts/blog_draft.py` als
  Entwurf nach HubSpot; veröffentlicht wird vom Nutzer. Veröffentlichte
  Artikel und Seiten nicht ändern, außer der Nutzer verlangt es.
- Zugangsdaten nie ausgeben.

## Zu Beginn jeder Session

1. `./scripts/snapshot.py` ausführen und `git status` prüfen. Geänderte
   Dateien unter `metadata/` sind Änderungen, die jemand in HubSpot von Hand
   gemacht hat. Erst mit dem Nutzer klären und committen, dann Neues bauen.

## Branches

- Änderungen gehen direkt auf `main`, damit das Repo dem Stand in HubSpot
  entspricht. Einen Pull Request nur öffnen, wenn der Nutzer es verlangt.

## Ablauf pro Änderung

1. Vor dem Anlegen eines Feldes prüfen, ob es ein Feld mit demselben Zweck
   schon gibt, auch unter den Standardfeldern von HubSpot.
2. Änderung per API ausführen.
3. `./scripts/snapshot.py` ausführen, Ergebnis committen.
4. In `docs/` festhalten: was sich ändert, wie man es prüft, wie man es
   zurücknimmt, und welche Schritte in der Oberfläche von Hand nötig sind.

## Konventionen

- Interne Feldnamen englisch in `snake_case`, Beschriftungen deutsch.
- Jedes Feld bekommt eine Beschreibung, die den Zweck erklärt.
- Interne Werte von Auswahllisten englisch, Beschriftungen deutsch.
- Die Deal-Pipeline `default` hat die Phasen Qualification, Pain & Impact
  Comm., Auftragsklärung, ClosedWon, Abgeschlossen und verloren. Sie passt
  und wird nicht umgebaut.
- Qualifizierung läuft über die vorhandenen Gruppen „SPICED Framework“ und
  „Qualification“ am Deal. Keine weiteren Qualifizierungsfelder anlegen.
- Nächster Schritt am Deal: Standardfelder `hs_next_step` und
  `notes_next_activity_date` nutzen.

## Inhalte für die Website

- Die Website wird zunehmend von KI-Agenten statt von Menschen gelesen. Jeder
  Inhalt folgt den Regeln in `docs/AGENTEN-TAUGLICHKEIT.md`.
- Tonfall: Ich-Perspektive, kurze Sätze, Anrede „du“ oder „ihr“, nie „Sie“.
- Keine erfundenen Zahlen, Kunden oder Erlebnisse. Fakten zum Angebot nur von
  der Startseite übernehmen. Wo ein Praxisbeispiel fehlt, eine Lücke markieren.
- LinkedIn bespielt der Nutzer selbst. Claude unterstützt nur bei Blog-Artikeln.

## Was die API nicht kann

Dashboards, Berichte, gespeicherte Ansichten, Vertriebs-Vorlagen und
Textbausteine lassen sich nur in der Oberfläche anlegen. Die Anleitung dafür
steht in `docs/HANDARBEIT.md` und wird bei Änderungen mit angepasst.
