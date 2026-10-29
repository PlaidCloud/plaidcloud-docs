---
title: Stripe-REST-Konnektor
description: Konfigurieren Sie in PlaidCloud eine Stripe-REST-API-Verbindung, um Zahlungsabwicklungs- und Finanzdaten in Ihre Workflows zu integrieren.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/stripe.md
---

## API-Dokumentation
Die [API-Referenz des Herstellers](https://docs.stripe.com/api) behandelt die Endpunkte dieses Konnektors.

## Konfiguration

Diese Felder werden angezeigt, wenn Sie diese Verbindung erstellen oder bearbeiten. Ob ein Feld erforderlich oder optional ist, hängt von den aktivierten Authentifizierungsoptionen ab.

### Identifikation

| Feld | Typ | Beschreibung |
|---|---|---|
| Name | Text | Anzeigename für diese Verbindung. |
| Alias | Text (mehrzeilig) | Optionaler Alias oder Notizen zur Verbindung. |
| Ist aktiv | Schalter | Gibt an, ob die Verbindung aktiviert ist. Deaktivieren Sie sie, um sie zu pausieren, ohne sie zu löschen. |

### Sonstiges

| Feld | Typ | Beschreibung |
|---|---|---|
| Host | Text | — |
| Authentifizierungstyp | Auswahl | — |
| SSL-Zertifikatsprüfung aktivieren | Schalter | — |
| Weiterleitungen automatisch folgen | Schalter | — |
| Ursprüngliche HTTP-Methode beibehalten | Schalter | — |
| Authorization-Header beibehalten | Schalter | — |
| Referer-Header bei Weiterleitung entfernen | Schalter | — |
| Strikten HTTP-Parser aktivieren | Schalter | — |
| URL automatisch codieren | Schalter | URL-Endpunkt. |
| Cookie-Speicher deaktivieren | Schalter | — |
| Cipher-Suite des Servers beim Handshake verwenden | Schalter | — |
| Maximale Anzahl an Weiterleitungen | Zahl | — |
| Test-Endpunkt | Text | — |
| Testmethode | Auswahl | — |
