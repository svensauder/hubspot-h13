#!/usr/bin/env python3
"""Legt einen Artikel aus content/blog/ als ENTWURF im HubSpot-Blog ab.

Das Skript veroeffentlicht nie. Es legt einen Entwurf an oder aktualisiert
ihn, wenn im Kopf der Datei schon eine hubspot-id steht. Einen bereits
veroeffentlichten Artikel fasst es nicht an.

Aufruf:   ./scripts/blog_draft.py content/blog/<datei>.md
Braucht:  pip install markdown
Zugang:   wie snapshot.py (Proxy in Claude-Sessions, sonst HUBSPOT_TOKEN)
"""
import json, os, re, sys, urllib.request, urllib.error
import markdown

BASE = "https://api.hubapi.com/cms/v3/blogs/posts"
BLOG_ID = "162597420079"      # Blog unter hangar-13.com/blog
AUTHOR_ID = "162642814896"    # Sven Sauder


def call(method, url, body=None):
    req = urllib.request.Request(url, method=method, data=json.dumps(body).encode() if body is not None else None)
    req.add_header("Content-Type", "application/json")
    if os.environ.get("HUBSPOT_TOKEN"):
        req.add_header("Authorization", "Bearer " + os.environ["HUBSPOT_TOKEN"])
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"HubSpot antwortet {e.code}: {e.read().decode()[:500]}")


def faq_jsonld(md_text):
    """Baut aus dem Abschnitt 'Haeufige Fragen' strukturierte Daten (FAQPage)."""
    m = re.search(r"^## Häufige Fragen\s*\n(.*?)(?=^## |\Z)", md_text, flags=re.S | re.M)
    if not m:
        return ""
    items = []
    for q, a in re.findall(r"\*\*(.+?)\*\*\s*\n(.+?)(?=\n\s*\n|\Z)", m.group(1), flags=re.S):
        a = re.sub(r"\s+", " ", a).strip()
        if "[LÜCKE" in a:
            continue
        items.append({"@type": "Question", "name": q.strip(), "acceptedAnswer": {"@type": "Answer", "text": a}})
    if not items:
        return ""
    data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def main(path):
    raw = open(path, encoding="utf-8").read()
    head, body = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, flags=re.S).groups()
    meta = dict((k.strip(), v.strip().strip('"')) for k, v in (l.split(":", 1) for l in head.splitlines() if ":" in l))
    body = re.sub(r"^# .*\n", "", body.lstrip(), count=1)              # Titel steht im eigenen Feld
    html = markdown.markdown(body, extensions=["tables"])
    html = re.sub(r"(\[LÜCKE:.*?\])", r'<mark>\1</mark>', html, flags=re.S)   # Luecken im Editor sichtbar
    html = html.replace("</p>", "</p>\n<!--more-->", 1)                # erster Absatz = Zusammenfassung
    post = {
        "name": meta["titel"],
        "htmlTitle": meta["titel"],
        "slug": meta["url-vorschlag"].lstrip("/"),
        "metaDescription": meta.get("meta-beschreibung", ""),
        "contentGroupId": BLOG_ID,
        "blogAuthorId": AUTHOR_ID,
        "language": "de",
        "postBody": html,
        "headHtml": faq_jsonld(body),
        "useFeaturedImage": False,
    }
    post_id = meta.get("hubspot-id")
    if post_id:
        current = call("GET", f"{BASE}/{post_id}")
        if current.get("currentlyPublished"):
            sys.exit("Abbruch: Der Artikel ist veröffentlicht. Änderungen bitte in HubSpot.")
        res = call("PATCH", f"{BASE}/{post_id}/draft", post)
        print("Entwurf aktualisiert:", res["id"])
    else:
        post["state"] = "DRAFT"
        res = call("POST", BASE, post)
        raw = raw.replace("---\n", f"---\nhubspot-id: {res['id']}\n", 1)
        open(path, "w", encoding="utf-8").write(raw)
        print("Entwurf angelegt:", res["id"])
    print(f"Bearbeiten: https://app-eu1.hubspot.com/blog/2368160/editor/{res['id']}/content")


if __name__ == "__main__":
    main(sys.argv[1])
