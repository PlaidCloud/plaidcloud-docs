---
title: Ramp-REST-Konnektor
description: Richten Sie in PlaidCloud eine Ramp-REST-API-Verbindung ein, um Ausgaben- und Spesendaten von Firmenkarten in Ihre Workflows zu integrieren.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/ramp.md
---

## API-Dokumentation
Die [API-Referenz des Herstellers](https://docs.ramp.com/developer-api/v1) behandelt die Endpunkte dieses Konnektors.

## Konfiguration

Diese Felder werden angezeigt, wenn Sie diese Verbindung erstellen oder bearbeiten. Ob ein Feld erforderlich oder optional ist, hängt von den aktivierten Authentifizierungsoptionen ab.

### Identifikation

| Feld | Typ | Beschreibung |
|---|---|---|
| Name | Text | Anzeigename für diese Verbindung. |
| Alias | Text (mehrzeilig) | Optionaler Alias oder Notizen zur Verbindung. |
| Ist aktiv | Schalter | Gibt an, ob die Verbindung aktiviert ist. Deaktivieren Sie sie, um sie zu pausieren, ohne sie zu löschen. |
| Db schreibgeschützt | Schalter | Beschränkt die Verbindung auf Lesevorgänge. |
| Zugriffstyp | Auswahl | Zugriffsebene für diese Verbindung: schreibgeschützt, nur schreibend oder lesend und schreibend. |

### Sonstiges

| Feld | Typ | Beschreibung |
|---|---|---|
| OAuth2-Client-ID | Text | — |
| OAuth2-Client-Secret | Text | Geheime Zugangsdaten – werden verschlüsselt gespeichert. |
| Ramp-Scope | Text | — |
