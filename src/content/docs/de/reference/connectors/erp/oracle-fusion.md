---
title: Oracle-Fusion-Connector
description: Richten Sie in PlaidCloud mit OAuth2-Anmeldedaten eine Oracle-Fusion-Cloud-Verbindung ein, um Hauptbuchsalden und Journalstapel über OData/BIP zu importieren und Journale über FBDI zu buchen.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/oracle-fusion.md
---

## API-Dokumentation

Die Referenzen zur [REST-API (OData)](https://docs.oracle.com/en/cloud/saas/financials/) sowie zu [BI Publisher (BIP) und File-Based Data Import (FBDI)](https://docs.oracle.com/en/cloud/saas/applications-common/) von Oracle Fusion Cloud dokumentieren die Endpunkte und den Bulk-Extract-/Ladepfad, die dieser Connector verwendet.

## So funktioniert die Authentifizierung

Die Verbindung authentifiziert sich mit OAuth2-Client-Anmeldedaten (oder den Basic-Auth-API-Anmeldedaten, die Ihre Fusion-Cloud-Sicherheitseinrichtung für Integrationsbenutzer ausstellt) gegenüber einem dedizierten API-Benutzer. Die Rolle des API-Benutzers steuert sowohl, welche Hauptbuch-Entitäten er lesen kann, als auch, über welche FBDI-/GL-Interface-Funktionen er buchen kann.

## Konfiguration

| Feld | Typ | Beschreibung |
|---|---|---|
| Name | Text | Anzeigename dieser Verbindung. |
| Instance URL | Text | Die URL Ihrer Fusion-Cloud-Instanz, z. B. `https://yourorg.fa.us2.oraclecloud.com`. |
| Client-ID | Text | Die OAuth2-Client-ID des API-Benutzers (bei Basic Auth der Benutzername). |
| Client-Secret | Text | Das OAuth2-Client-Secret des API-Benutzers (bei Basic Auth das Passwort). Wird verschlüsselt gespeichert. |

## Zum Import verfügbare Entitäten

Zwei Importschritte decken unterschiedliche Abrufgrößen ab, beide für `gl_balances` und `journal_batches`:

- **Import Fusion Entity** (Schritt) — ein direkter OData-/BIP-Aufruf für einen routinemäßigen, begrenzten Abruf.
- **Import Fusion Bulk Extract** (Schritt) — ein asynchroner FBDI-/BIP-Exportjob für einen umfangreichen Extrakt.

Beide unterstützen Bereichsfilter (`ge`/`le`) für Datums-, Buchungsperioden- und numerische Saldo-/Betragsfelder sowie Gleichheitsfilter für diskrete Felder wie Hauptbuch oder Währung. Die vollständige Feldreferenz finden Sie unter [Import Fusion Entity](/de/reference/workflow-steps/oracle-fusion/import-fusion-entity/) (Schritt) und [Import Fusion Bulk Extract](/de/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/) (Schritt).

## Journalbuchungen buchen

Der Schritt **Oracle Fusion: Post Journal Entry** bucht Hauptbuch-Journalstapel über die gemeinsame ERP-Schreibpipeline von PlaidCloud: Er schreibt den Stapel als FBDI-Datei in die Staging-Tabelle GL_INTERFACE von Oracle, startet den ESS-Job Journal Import Launcher und fragt ihn ab, bis er einen Endzustand erreicht, und bestätigt das Ergebnis, bevor ein Stapel als gebucht gemeldet wird. Eine Korrektur bucht eine neue Stornobuchung mit vertauschtem Soll und Haben, statt das Original zu bearbeiten. Die Feldreferenz finden Sie unter [Oracle Fusion: Post Journal Entry](/de/reference/workflow-steps/oracle-fusion/oracle-fusion-post/) (Schritt), die vollständige Anleitung zum Buchen unter [Verbindung zu Oracle Fusion herstellen](/de/guides/connections/oracle-fusion/).

## Bekannte Einschränkungen

| Einschränkung | Bedeutung |
|---|---|
| ESS-Job-Latenz | Der Journal Import Launcher läuft als geplanter Job, nicht als synchroner Aufruf; eine Buchungsausführung dauert daher deutlich länger als ein direkter API-Schreibvorgang. |
| Bulk-Extract-Latenz | `import_fusion_bulk_extract` wartet auf einen FBDI-/BIP-Exportjob; verwenden Sie ihn nur für Abrufe, die für den direkten Pfad von `import_fusion_entity` zu groß sind. |
## Verwandte Themen

- [Verbindung zu Oracle Fusion herstellen (Anleitung)](/de/guides/connections/oracle-fusion/) — Schritt für Schritt: Verbindung erstellen, testen, eine Entität importieren und ein Journal buchen.
- [Import Fusion Entity](/de/reference/workflow-steps/oracle-fusion/import-fusion-entity/) (Schritt)
- [Import Fusion Bulk Extract](/de/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/) (Schritt)
- [Oracle Fusion: Post Journal Entry](/de/reference/workflow-steps/oracle-fusion/oracle-fusion-post/) (Schritt)
- [ERP-Buchungsverlauf prüfen](/de/guides/connections/erp-post-history/)
