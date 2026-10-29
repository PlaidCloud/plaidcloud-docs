---
title: Google-BigQuery-Konnektor
description: Konfigurieren Sie in PlaidCloud eine Google-BigQuery-Verbindung, um analytische Abfragen auszuführen und große Datenmengen in Workflows zu integrieren.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/google/big-query.md
---

## Verbindungsdokumentation
[Die Google-BigQuery-Dokumentation](https://docs.cloud.google.com/bigquery/docs).

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

### BigQuery-Verbindung

| Feld | Erforderlich | Beschreibung |
|---|---|---|
| Projekt | Ja | Das Google-Cloud-Projekt, das das Dataset enthält. |
| Dataset | Ja | Das BigQuery-Dataset, aus dem gelesen und in das geschrieben wird. |
| Tabelle | Ja | Eine Tabelle im Dataset. |

### Authentifizierungsdaten

| Feld | Erforderlich | Beschreibung |
|---|---|---|
| Dienstkontoschlüssel (JSON) | Ja | Fügen Sie die gesamte JSON-Schlüsseldatei eines Google-Dienstkontos ein, das das Dataset lesen kann. Gewähren Sie Schreibzugriff nur, wenn Sie in das Dataset schreiben möchten. Der Schlüssel ist nur schreibbar: Lassen Sie das Feld beim Bearbeiten leer, um den gespeicherten Schlüssel beizubehalten. |

Die Verbindung authentifiziert sich ausschließlich mit dem Dienstkontoschlüssel, den Sie angeben. [Import SQL](/de/reference/workflow-steps/import/import-sql/) liest BigQuery über diese Verbindung, und [Export External Database Tables](/de/reference/workflow-steps/export/export-external-tables/) schreibt mit einem BigQuery-Ladejob dorthin.
