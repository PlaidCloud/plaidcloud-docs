---
title: Business-Central-Schritte
description: Workflow-Schritte, die über Ihre Business-Central-Verbindung aus Microsoft Dynamics 365 Business Central lesen und dorthin schreiben – OData-Entitäten importieren und Sachkonten-Journalzeilen buchen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/business-central/index.md
---

Workflow-Schritte, die über Ihre [Business-Central-Verbindung](/de/guides/connections/business-central/) aus Business Central lesen und dorthin schreiben. Der Importschritt ruft die Standard-OData-v2.0-Entitäten von Business Central ab, ohne dass Sie eine Abfrage schreiben müssen; der Buchungsschritt bucht Sachkonten-Journalzeilen über die gemeinsame ERP-Schreibpipeline von PlaidCloud.

## Schritte

- [Import Business Central Entity](/de/reference/workflow-steps/business-central/import-business-central-entity/) – Konten, Hauptbucheinträge, Debitoren, Kreditoren, Artikel und Journale, mit serverseitigen Filtern.
- [Business Central: Post General Journal Lines](/de/reference/workflow-steps/business-central/business-central-post/) – Zeilen in einen vorhandenen Journalstapel buchen und den Stapel buchen.

## Verwandte Themen

- [Business Central REST Connector](/de/reference/connectors/rest/business-central/)
- [Mit Business Central verbinden](/de/guides/connections/business-central/)
- [ERP-Buchungsverlauf prüfen](/de/guides/connections/erp-post-history/)
