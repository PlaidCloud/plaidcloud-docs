---
title: Workday-REST-Connector
description: Konfigurieren Sie in PlaidCloud eine Workday-REST-API-Verbindung, um HR-, Finanz- und Planungsdaten in Ihre Workflows zu integrieren.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/workday.md
---

## API-Dokumentation
Die [API-Referenz des Herstellers](https://community.workday.com/sites/default/files/file-hosting/restapi/) behandelt die Endpunkte dieses Connectors.

## Konfiguration

Diese Felder erscheinen beim Erstellen oder Bearbeiten dieser Verbindung. Ob sie erforderlich oder optional sind, hängt von den aktivierten Authentifizierungsoptionen ab.

### Identifikation

| Feld | Typ | Beschreibung |
|---|---|---|
| Name | Text | Anzeigename dieser Verbindung. |
| Alias | Text (mehrzeilig) | Optionaler Alias oder Notizen zur Verbindung. |
| Ist aktiv | Umschalter | Gibt an, ob die Verbindung aktiviert ist. Deaktivieren Sie sie, um sie zu pausieren, ohne sie zu löschen. |
| Datenbank schreibgeschützt | Umschalter | Beschränkt die Verbindung auf Lesevorgänge. |
| Zugriffstyp | Auswahl | Zugriffsebene dieser Verbindung: nur lesend, nur schreibend oder lesend und schreibend. |

### Sonstiges

| Feld | Typ | Beschreibung |
|---|---|---|
| OAuth2-Client-ID | Text | — |
| OAuth2-Client-Secret | Text | Geheime Zugangsdaten – werden verschlüsselt gespeichert. |
| Workday-URL | Text | URL-Endpunkt. |
| OAuth2-Refresh-Token | Text | — |
