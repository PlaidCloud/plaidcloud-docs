---
title: Oracle-Fusion-Schritte
description: Workflow-Schritte, die über Ihre Oracle-Fusion-Verbindung aus Oracle Fusion Cloud lesen und dorthin schreiben – Hauptbuchsalden und Journalstapel über OData/BIP oder FBDI-Massenextrakt importieren sowie Journalbuchungen buchen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-fusion/index.md
---

Workflow-Schritte, die über Ihre [Oracle-Fusion-Verbindung](/de/guides/connections/oracle-fusion/) aus Oracle Fusion Cloud lesen und dorthin schreiben. Zwei Importschritte decken unterschiedliche Abrufgrößen ab – ein direkter OData/BIP-Aufruf für routinemäßige Abrufe und ein asynchroner FBDI/BIP-Massenextrakt für große Abrufe; der Buchungsschritt bucht Journalstapel über die gemeinsame ERP-Schreibpipeline von PlaidCloud.

## Schritte

- [Import Fusion Entity](/de/reference/workflow-steps/oracle-fusion/import-fusion-entity/) – Hauptbuchsalden und Journalstapel, mit serverseitigen Filtern für Datum, Periode und numerische Bereiche.
- [Import Fusion Bulk Extract](/de/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/) – dieselben Entitäten über einen asynchronen FBDI/BIP-Exportjob für große Abrufe.
- [Oracle Fusion: Post Journal Entry](/de/reference/workflow-steps/oracle-fusion/oracle-fusion-post/) – bucht Hauptbuch-Journalstapel über die FBDI-GL-Schnittstelle, mit einer gebuchten Stornobuchung für Korrekturen.

## Verwandte Themen

- [Oracle-Fusion-Konnektor](/de/reference/connectors/erp/oracle-fusion/)
- [Mit Oracle Fusion verbinden](/de/guides/connections/oracle-fusion/)
- [ERP-Buchungsverlauf prüfen](/de/guides/connections/erp-post-history/)
