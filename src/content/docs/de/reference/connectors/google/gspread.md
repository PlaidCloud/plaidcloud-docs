---
title: Google Sheets
description: Richten Sie in PlaidCloud eine Google-Sheets-Verbindung ein, um Tabellendaten in Ihren Workflows zu importieren, zu exportieren und zu synchronisieren.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/google/gspread.md
---

## Verbindungsdokumentation
Google Sheets richtet sich eher an Privatanwender. Technische Dokumentation finden Sie in der [Entwicklerdokumentation](https://developers.google.com/workspace/sheets).

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
