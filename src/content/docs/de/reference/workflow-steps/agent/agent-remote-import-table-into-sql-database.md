---
title: Agent Remote Import Table into SQL Database
description: Importieren Sie PlaidCloud-Tabellendaten über einen PlaidLink-Agent in Remote-SQL-Datenbanken, für sicheres Laden von Daten hinter Firewalls.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database.md
---

## Beschreibung



Überträgt eine PlaidCloud-Projekttabelle in eine Datenbank, die nur über einen PlaidLink-Agent erreichbar ist. Der Agent empfängt die Daten von PlaidCloud und führt das Laden lokal aus — nützlich, um eine lokale operative Datenbank mit den PlaidCloud-Analysen synchron zu halten.

Typische Verwendung: PlaidCloud erzeugt ein aktualisiertes Prognose- oder Umlageergebnis, und der Agent lädt es in das lokale ERP, das Data Mart oder die operative Berichtsdatenbank.


## Wie die Daten den Agent erreichen

Ein PlaidLink-Agent ab Version 1.2.33 erhält die Zeilen der Tabelle als eine einzelne Parquet-Datei. Zahlen, Datumswerte, Zeitstempel und Wahr/Falsch-Werte kommen als eigene Typen an. Andere Spalten, etwa Zeit-, Intervall- und JSON-Spalten, kommen als Text an. Ein leerer Textwert kommt leer an (NULL), wie schon immer.

Ein älterer Agent erhält die Zeilen wie bisher als gezippte, tabulatorgetrennte Datei. [Aktualisieren Sie den Agent](/de/reference/cli/plaidlink/upgrade/), um Parquet zu erhalten.

## Beispiele

Noch keine Beispiele ...
