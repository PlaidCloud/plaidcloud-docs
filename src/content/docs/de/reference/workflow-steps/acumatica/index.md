---
title: Acumatica-Schritte
description: Workflow-Schritte, die über Ihre Acumatica-Verbindung aus Acumatica lesen und dorthin schreiben — vertragsbasierte REST-Entitäten importieren sowie Journalbuchungen, Rechnungen und Zahlungen buchen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/acumatica/index.md
---

Workflow-Schritte, die über Ihre [Acumatica-Verbindung](/de/guides/connections/acumatica/) aus Acumatica lesen und dorthin schreiben. Der Import-Schritt holt die vertragsbasierten REST-Entitäten von Acumatica, ohne dass OData geschrieben werden muss; der Buchungsschritt bucht Journalbuchungen, Ausgangsrechnungen, Eingangsrechnungen und Zahlungen über die gemeinsame ERP-Schreibpipeline von PlaidCloud.

## Schritte

- [Import Acumatica Entity](/de/reference/workflow-steps/acumatica/import-acumatica-entity/) — Stamm- und Bewegungsdaten-Entitäten, mit serverseitigen Filtern.
- [Acumatica: Post Documents](/de/reference/workflow-steps/acumatica/acumatica-post/) — Journalbuchungen, Ausgangsrechnungen, Eingangsrechnungen und Zahlungen buchen.

## Verwandte Themen

- [Acumatica-REST-Konnektor](/de/reference/connectors/rest/acumatica/)
- [Mit Acumatica verbinden](/de/guides/connections/acumatica/)
- [ERP-Buchungsverlauf prüfen](/de/guides/connections/erp-post-history/)
