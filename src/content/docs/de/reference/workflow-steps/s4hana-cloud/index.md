---
title: SAP-S/4HANA-Cloud-Schritte
description: Workflow-Schritte, die über Ihre S/4HANA-Cloud-Verbindung aus SAP S/4HANA Cloud Public Edition lesen und dorthin schreiben – Saldenliste und Journalbuchungspositionen importieren sowie Journalbuchungen buchen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/s4hana-cloud/index.md
---

Workflow-Schritte, die über Ihre [S/4HANA-Cloud-Verbindung](/de/guides/connections/s4hana-cloud/) aus SAP S/4HANA Cloud Public Edition lesen und dorthin schreiben. Der Importschritt ruft Saldenlisten- oder Journalbuchungspositionsdaten ab, ohne dass Sie OData schreiben müssen; der Buchungsschritt bucht Journalbuchungen über die gemeinsame ERP-Schreibpipeline von PlaidCloud.

## Schritte

- [Import S/4HANA Entity](/de/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/) – Saldenlisten- und Journalbuchungspositionsdaten, mit serverseitigen Filtern.
- [S/4HANA: Post Journal Entry](/de/reference/workflow-steps/s4hana-cloud/s4hana-post/) – bucht Journalbuchungen über SOAP, mit einer gebuchten Stornobuchung für Korrekturen.

## Verwandte Themen

- [SAP S/4HANA Cloud REST Connector](/de/reference/connectors/rest/s4hana-cloud/)
- [Mit SAP S/4HANA Cloud verbinden](/de/guides/connections/s4hana-cloud/)
- [ERP-Buchungsverlauf prüfen](/de/guides/connections/erp-post-history/)
