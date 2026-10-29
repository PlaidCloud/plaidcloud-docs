---
title: QuickBooks-REST-Konnektor
description: Konfigurieren Sie in PlaidCloud eine QuickBooks-REST-API-Verbindung, um Buchhaltungs- und Finanzdaten in Ihre Analyse-Workflows zu integrieren.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/quickbooks.md
---

## API-Dokumentation
Die [API-Referenz des Herstellers](https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api) behandelt die Endpunkte dieses Konnektors.

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
