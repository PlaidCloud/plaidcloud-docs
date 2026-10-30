---
title: Schritte für IBM TM1 / Planning Analytics
description: Workflow-Schritte, die über Ihre TM1-Verbindung von einem IBM-TM1-/Planning-Analytics-Server lesen — Cube-Daten per gespeicherter Ansicht oder MDX sowie Dimensionshierarchien — direkt aus der Cloud oder über einen lokalen PlaidLink-Agent.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/index.md
---

Workflow-Schritte, die über Ihre [TM1-Verbindung](/de/guides/connections/tm1/) von IBM **TM1 / Planning Analytics** lesen: Cube-Daten per gespeicherter Ansicht oder MDX mit optionalem Betrachtungspunkt-Ausschnitt sowie Dimensionshierarchien, die in eine PlaidCloud-Dimension geladen werden. Sie erreichen TM1 direkt aus der Cloud oder, bei einem Server, der nur aus Ihrem eigenen Netzwerk erreichbar ist, über einen lokalen PlaidLink-Agent.

## Schritte

- [TM1: Cube abfragen](/de/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — liest einen Cube per gespeicherter Ansicht oder MDX, mit Betrachtungspunkt-Ausschnitt und einer Vorschau vor dem Speichern. Direkt aus der Cloud.
- [TM1: Cube abfragen (Agent)](/de/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) — das lokale Gegenstück zu TM1: Cube abfragen, über einen installierten PlaidLink-Agent ausgeführt.
- [TM1: Dimension lesen](/de/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — lädt eine TM1-Hierarchie in eine PlaidCloud-Dimension. Direkt aus der Cloud.

## Verwandte Themen

- [Mit TM1 verbinden (Leitfaden)](/de/guides/connections/tm1/)
- [TM1-Connector](/de/reference/connectors/rest/tm1/)
