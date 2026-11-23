# HubSpot-Konfiguration Hangar-13

Dieses Repository ist die Dokumentation und Versionierung der HubSpot-Konfiguration
(Portal 2368160, EU-Rechenzentrum, Starter Customer Platform).

## Inhalt

| Pfad | Was |
|---|---|
| `CLAUDE.md` | Arbeitsregeln für Claude in diesem Projekt |
| `scripts/snapshot.py` | Liest Felder, Feldgruppen, Pipelines und Workflows nach `metadata/` |
| `scripts/blog_draft.py` | Legt einen Artikel aus `content/blog/` als Entwurf im HubSpot-Blog ab |
| `metadata/` | Aktueller Stand der Konfiguration als JSON (keine Kundendaten) |
| `docs/INVENTAR.md` | Bestandsaufnahme und Aufräum-Vorschläge |
| `docs/AENDERUNGEN-2026-11-23.md` | Was am 23.11.2026 angelegt wurde und wie man es zurücknimmt |
| `docs/HANDARBEIT.md` | Schritte, die nur in der HubSpot-Oberfläche gehen |
| `docs/AGENTEN-TAUGLICHKEIT.md` | Prüfung der Website aus Sicht von KI-Agenten, Regeln für Inhalte |
| `content/llms.txt` | Entwurf der Datei, die Agenten die Website erklärt |
| `content/blog/` | Redaktionsplan und Artikel-Entwürfe |
| `content/vorlagen/` | Textvorlagen fürs Nachfassen |
| `langdock/` | Vorlage für den Langdock-Agenten |

## Stand nach einer Änderung festhalten

```bash
./scripts/snapshot.py
```

Danach zeigt `git diff`, was sich in HubSpot geändert hat.

## Blog-Artikel als Entwurf ablegen

```bash
pip install markdown
```

```bash
./scripts/blog_draft.py content/blog/<datei>.md
```

Das Skript veröffentlicht nie. Veröffentlicht wird in HubSpot von Hand.
