---
title: Dynamics 365 F&O-Schritte
description: Workflow-Schritte, die über Ihre D365-F&O-Verbindung aus Dynamics 365 Finance & Operations lesen und dorthin schreiben – OData-/DMF-Entitäten importieren und Journalbuchungen buchen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dynamics-365-fo/index.md
---

Workflow-Schritte, die über Ihre [D365-F&O-Verbindung](/de/guides/connections/dynamics-365-fo/) aus Dynamics 365 Finance & Operations (D365 F&O) lesen und dorthin schreiben. Der Importschritt lädt OData-Entitäten oder DMF-Bulk-Extrakte, ohne dass OData geschrieben werden muss; der Buchungsschritt bucht Hauptbuch-Journalbuchungen über die gemeinsame ERP-Schreibpipeline von PlaidCloud.

## Schritte

- [Import D365 F&O Entity](/de/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/) – Stammdaten und Journalköpfe, im OData- oder DMF-Bulk-Modus, mit serverseitigen Filtern.
- [D365 F&O: Post Journal Entry](/de/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/) – bucht Hauptbuch-Journalbuchungen, mit einer gebuchten Stornobuchung für Korrekturen.

## Verwandte Themen

- [Dynamics 365 F&O REST Connector](/de/reference/connectors/rest/dynamics-365-fo/)
- [Mit Dynamics 365 Finance & Operations verbinden](/de/guides/connections/dynamics-365-fo/)
- [ERP-Buchungsverlauf prüfen](/de/guides/connections/erp-post-history/)
