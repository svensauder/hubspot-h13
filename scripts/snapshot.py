#!/usr/bin/env python3
"""Liest die HubSpot-Konfiguration (nur Metadaten) und schreibt sie nach metadata/.

Abgerufen werden ausschliesslich Definitionen: eigene Felder, Feldgruppen,
Pipelines und Workflows. Das Skript ruft keinen Endpunkt unter
/crm/v3/objects/ auf und liest damit keine Kunden-, Kontakt- oder Deal-Daten.

Aufruf:  ./scripts/snapshot.py
Zugang:  In Claude-Cloud-Sessions setzt der Proxy die Anmeldung selbst.
         Lokal die Variable HUBSPOT_TOKEN setzen (Private-App-Token).
"""
import json, os, pathlib, sys, urllib.request

BASE = "https://api.hubapi.com/"
OUT = pathlib.Path(__file__).resolve().parent.parent / "metadata"
OBJECTS = ["contacts", "companies", "deals", "tickets"]
# Felder, die sich bei jedem Abruf aendern oder nichts aussagen
DROP = {"updatedAt", "createdUserId", "updatedUserId", "modificationMetadata"}


def get(path):
    if "/crm/v3/objects/" in path:
        sys.exit("Abbruch: Dieses Skript liest keine Datensaetze.")
    req = urllib.request.Request(BASE + path)
    token = os.environ.get("HUBSPOT_TOKEN")
    if token:
        req.add_header("Authorization", "Bearer " + token)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def write(name, data):
    path = OUT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def clean(d):
    return {k: v for k, v in d.items() if k not in DROP}


def main():
    for obj in OBJECTS:
        props = get(f"crm/v3/properties/{obj}")["results"]
        custom = sorted((clean(p) for p in props if not p.get("hubspotDefined")), key=lambda p: p["name"])
        write(f"properties/{obj}.json", custom)
        groups = get(f"crm/v3/properties/{obj}/groups")["results"]
        write(f"property-groups/{obj}.json", sorted(groups, key=lambda g: g["name"]))
        print(f"{obj}: {len(custom)} eigene Felder von {len(props)}")
    for obj in ["deals", "tickets"]:
        pipes = get(f"crm/v3/pipelines/{obj}")["results"]
        write(f"pipelines/{obj}.json", sorted((clean(p) for p in pipes), key=lambda p: p["id"]))
        print(f"{obj}: {len(pipes)} Pipelines")
    flows, after = [], None
    while True:
        page = get("automation/v4/flows?limit=100" + (f"&after={after}" if after else ""))
        flows += page["results"]
        after = page.get("paging", {}).get("next", {}).get("after")
        if not after:
            break
    for old in (OUT / "workflows").glob("*.json"):
        old.unlink()
    for f in flows:
        write(f"workflows/{f['id']}.json", clean(get(f"automation/v4/flows/{f['id']}")))
    print(f"{len(flows)} Workflows")


if __name__ == "__main__":
    main()
