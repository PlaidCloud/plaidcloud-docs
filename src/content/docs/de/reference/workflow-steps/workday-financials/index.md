---
title: Workday-Financials-Schritte
description: Workflow-Schritte, die über Ihre Workday-Financials-Verbindung aus Workday Financials lesen und dorthin schreiben — Daten über einen RaaS-Bericht importieren und Buchungsjournale buchen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workday-financials/index.md
---

Workflow-Schritte, die über Ihre [Workday-Financials-Verbindung](/de/guides/connections/workday-financials/) aus Workday Financials lesen und dorthin schreiben. Der Importschritt ruft einen vom Kunden bereitgestellten Report-as-a-Service-(RaaS-)Bericht ab; der Buchungsschritt bucht Buchungsjournale über die gemeinsame ERP-Schreibpipeline von PlaidCloud.

## Schritte

- [Import Workday Entity](/de/reference/workflow-steps/workday-financials/import-workday-entity/) — ruft einen RaaS-Bericht ab, mit Berichtsparameter-Filtern.
- [Workday Financials: Post Journal Entry](/de/reference/workflow-steps/workday-financials/workday-post/) — bucht Buchungsjournale über `Submit_Accounting_Journal`, mit einer gebuchten Stornobuchung für Korrekturen.

## Verwandte Themen

- [Workday-Financials-Konnektor](/de/reference/connectors/rest/workday-financials/)
- [Mit Workday Financials verbinden](/de/guides/connections/workday-financials/)
- [ERP-Buchungsverlauf prüfen](/de/guides/connections/erp-post-history/)
