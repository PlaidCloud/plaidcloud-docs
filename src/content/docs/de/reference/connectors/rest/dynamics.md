---
title: Microsoft-Dynamics-365-REST-Konnektor
description: Konfigurieren Sie in PlaidCloud eine Verbindung zur Microsoft-Dynamics-REST-API, um ERP- und CRM-Daten in Ihre Analyse-Workflows zu integrieren.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/dynamics.md
---

## API-Dokumentation
Die [API-Referenz des Herstellers](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/) behandelt die Endpunkte dieses Konnektors.

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
| Dynamics-Mandant | Text | — |
| OAuth2-Client-ID | Text | — |
| OAuth2-Client-Secret | Text | Geheime Zugangsdaten – werden verschlüsselt gespeichert. |
| Dynamics CRM | Text | — |
