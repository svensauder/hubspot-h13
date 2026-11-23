# Website für KI-Agenten

Ausgangslage: Immer weniger Menschen besuchen die Website, immer mehr
KI-Agenten. Ein Agent liest im Auftrag eines Menschen, der zum Beispiel fragt:
„Wer hilft einem B2B-Scale-up mit 60 Leuten, dessen CRM niemand pflegt, und
was kostet das?“ Der Agent liest ohne JavaScript, überfliegt nicht, zitiert
wörtlich und empfiehlt nur, was er belegen kann.

## Prüfung von hangar-13.com am 23.11.2026

Geprüft wurde der Quelltext, so wie ihn ein Agent ohne Browser bekommt.

| Punkt | Befund | Wertung |
|---|---|---|
| `robots.txt` | Erlaubt alles Öffentliche, sperrt keine KI-Crawler | gut |
| `sitemap.xml` | 198 Adressen, davon 184 Blog-Artikel | gut |
| Startseite: Text ohne JavaScript lesbar | Ja, auch Preise und FAQ | gut |
| Blog-Artikel: strukturierte Daten | `BlogPosting` mit Autor und Datum vorhanden | gut |
| `llms.txt` | fehlt (404) | **Lücke** |
| Startseite: strukturierte Daten | keine | **Lücke** |
| Startseite: Meta-Beschreibung | nur „CRM & RevOps Consulting“ | **Lücke** |
| `/probe-session` | 354 Zeichen Text. Der Kalender lädt per JavaScript. Ein Agent sieht nicht, wie man bucht. | **Lücke** |
| `/blog` Übersicht | keine Hauptüberschrift, keine Beschreibung, keine kanonische Adresse | Lücke |
| `/podcasts`, `/sven-sauder-hubspot-kostenrechner` | Beschreibung „Let's fix xou CRM!“ mit Tippfehler; Inhalt nur per JavaScript | Lücke |
| `/lexikon` | Guter Stoff für Agenten, aber ohne Beschreibung und nicht in der Navigation | Lücke |
| Angebot als eigene Seite | Preise und Ablauf stehen nur auf der Startseite, zwischen Werbetext | Lücke |
| Markdown-Fassung der Seiten | wird nicht angeboten | Kür |
| Anrede | Startseite „ihr“, Blog „du“, linqi-Seite „Sie“ | Kleinigkeit |

## Was zu tun ist, nach Wirkung

1. **`llms.txt` veröffentlichen.** Entwurf: `content/llms.txt`. In HubSpot die
   Datei unter Dateien hochladen und unter Einstellungen → Website →
   Domains & URLs → URL-Weiterleitungen `/llms.txt` auf die Datei-Adresse
   leiten. Ob Starter Weiterleitungen auf Dateien zulässt, zeigt sich beim
   Anlegen. Sonst als Seite mit reinem Text anlegen.
2. **Faktenseite zum Angebot.** Entwurf:
   `content/blog/2026-11-crm-revops-sparring-preise-ablauf.md`. Eine Seite,
   die ohne Werbesprache sagt: was, für wen, Ablauf, Preis, Laufzeit, Buchung.
3. **`/probe-session` mit Text füllen.** Über dem Kalender in Klartext: Dauer
   30 Minuten, kostenlos, kein Verkaufsgespräch, was man vorbereitet, und der
   direkte Buchungslink `https://hangar-13.com/meetings/s-sauder` als normaler
   Link.
4. **Strukturierte Daten auf der Startseite.** Vorlage unten. Einfügen unter
   Einstellungen → Website → Seiten → Vorlagen → HTML im Kopfbereich, oder im
   Kopfbereich der Startseite.
5. **Meta-Beschreibungen** für Startseite, `/blog`, `/podcasts`, `/lexikon`
   und den Kostenrechner. Vorschläge unten.
6. **FAQ-Daten.** Die FAQ der Startseite zusätzlich als `FAQPage` auszeichnen.
7. **Messen.** Im Dashboard den Bericht nach „Original Traffic Source“ mit dem
   Wert „AI Referrals“ beobachten und bei neuen Kontakten den Lead-Kanal
   „KI-Assistent / Agent“ setzen.

## Regeln für jeden neuen Inhalt

1. **Antwort zuerst.** Unter der Überschrift steht ein Absatz „Kurz gesagt“
   mit zwei bis vier Sätzen, der für sich allein stimmt und zitierbar ist.
2. **Überschriften als Fragen**, so wie jemand einen Assistenten fragt.
3. **Jeder Abschnitt steht für sich.** Kein „wie oben erwähnt“. Agenten
   lesen oft nur einen Ausschnitt.
4. **Namen statt Fürwörter.** „Sven Sauder“, „Sparring“, „HubSpot“ ausschreiben,
   wo ein Absatz sonst ohne Zusammenhang unverständlich wäre.
5. **Fakten als Tabelle oder Liste:** Preise, Dauer, Zielgruppe, Voraussetzungen.
6. **Zahlen mit Einheit und Stand.** „3.100 € pro Monat zzgl. USt., Stand
   November 2026“.
7. **Für wen es nicht passt.** Agenten suchen Ausschlusskriterien. Wer sie
   nennt, wird bei den passenden Anfragen eher empfohlen.
8. **Abgrenzung benennen:** Sparring gegenüber Agentur, Implementierungspartner,
   Freelancer-Admin.
9. **Handlung als normaler Link** mit voller Adresse, nicht nur als Knopf oder
   eingebettetes Fenster.
10. **Alles Wichtige im HTML-Text.** Nichts nur in Bildern, Videos, Rechnern
    oder Ausklapp-Elementen, die JavaScript brauchen.
11. **Datum und Autor sichtbar**, bei Überarbeitung „Aktualisiert am“.
12. **FAQ am Ende** mit drei bis sechs echten Fragen, jede Antwort höchstens
    drei Sätze.
13. **Keine erfundenen Belege.** Agenten gleichen ab. Eine falsche Zahl
    entwertet die ganze Quelle.

## Vorlage: strukturierte Daten für die Startseite

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Sven Sauder – CRM & RevOps Consulting",
  "url": "https://hangar-13.com",
  "description": "Sparring für Marketing, Sales und Customer Success in B2B-Unternehmen mit HubSpot oder Salesforce. Gemeinsam die eigentliche Ursache finden, dann baut das Team die Lösung mit Bestandstools und KI selbst.",
  "founder": {
    "@type": "Person",
    "name": "Sven Sauder",
    "sameAs": "https://www.linkedin.com/in/sven-sauder/"
  },
  "areaServed": "DE",
  "knowsAbout": ["CRM", "Revenue Operations", "HubSpot", "Salesforce", "Sales-Prozesse"],
  "makesOffer": [
    {
      "@type": "Offer",
      "name": "Sparring Early Stage (bis 20 Mitarbeiter)",
      "price": "3100",
      "priceCurrency": "EUR",
      "description": "Pro Monat zzgl. USt. Weekly 30 Minuten, asynchroner Austausch, spontane Meetings bei Bedarf. Keine Mindestlaufzeit."
    },
    {
      "@type": "Offer",
      "name": "Sparring Growth Stage (21 bis 100 Mitarbeiter)",
      "price": "4100",
      "priceCurrency": "EUR",
      "description": "Pro Monat zzgl. USt. Weekly 30 Minuten, asynchroner Austausch, spontane Meetings bei Bedarf. Keine Mindestlaufzeit."
    }
  ],
  "potentialAction": {
    "@type": "ReserveAction",
    "name": "Probe-Session vereinbaren (30 Minuten, kostenlos)",
    "target": "https://hangar-13.com/probe-session"
  }
}
</script>
```

Vor dem Einbau prüfen: Impressumsangaben, ob „DE“ als Einzugsgebiet stimmt,
und ob die Preise noch gelten.

## Vorschläge für Meta-Beschreibungen

| Seite | Beschreibung |
|---|---|
| Startseite | Sparring für Marketing, Sales und Customer Success in B2B-Unternehmen mit HubSpot oder Salesforce. Ursache finden, mit KI selbst umsetzen. Ab 3.100 € pro Monat, keine Mindestlaufzeit. |
| `/blog` | Artikel von Sven Sauder zu CRM, RevOps, Sales-Prozessen und KI im Vertrieb, aus über 90 Projekten mit HubSpot und Salesforce. |
| `/probe-session` | 30 Minuten, kostenlos, kein Sales-Pitch: Du erzählst, woran ihr arbeitet, Sven Sauder sagt ehrlich, was er von außen sieht. Termin direkt buchen. |
| `/lexikon` | Sales- und CRM-Lexikon: verständliche Erklärungen von AE über GTM bis Win Rate. |
| `/podcasts` | Podcast-Folgen mit Sven Sauder zu CRM und RevOps. |
| Kostenrechner | Rechner für das Seats-und-Credits-Preismodell von HubSpot bei Neuverträgen. |
