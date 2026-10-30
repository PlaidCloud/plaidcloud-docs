---
title: SAP-S/4HANA-Cloud-REST-Konnektor
description: Richten Sie in PlaidCloud eine Verbindung zu SAP S/4HANA Cloud Public Edition ein, um Saldenlisten- und Journalbuchungspositionsdaten über OData zu importieren und Journalbuchungen über SOAP zu buchen.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/s4hana-cloud.md
---

## API-Dokumentation

Die [Trial Balance API (`API_OPLACCTGDOCITEMCUBE_SRV`)](https://api.sap.com/) und die [Journal Entry Item - Basic API (`API_JOURNALENTRYITEMBASIC_SRV`)](https://api.sap.com/) von SAP S/4HANA Cloud im SAP API Business Hub dokumentieren die OData-Endpunkte, die dieser Konnektor verwendet, sowie den SOAP-Dienst für das Massenanlegen von Journalbuchungen, der über eine Communication Arrangement bereitgestellt wird.

## So funktioniert die Authentifizierung

Die Verbindung authentifiziert sich als Anwendung über **OAuth2 Client Credentials**: Client-ID und Client-Secret einer Communication Arrangement werden am OAuth2-Token-Endpunkt des Mandanten gegen ein Zugriffstoken getauscht. Es gibt keine interaktive Anmeldung.

## Konfiguration

| Feld | Typ | Beschreibung |
|---|---|---|
| Name | Text | Anzeigename für diese Verbindung. |
| Host | Text | Der Host Ihres S/4HANA-Cloud-Mandanten, z. B. `https://yourorg.s4hana.ondemand.com`. |
| Token-URL | Text | Der OAuth2-Token-Endpunkt der Communication Arrangement. |
| Client-ID | Text | Die OAuth2-Client-ID der Communication Arrangement. |
| Client-Secret | Text | Das OAuth2-Client-Secret der Communication Arrangement. Wird verschlüsselt gespeichert. |

## Zum Import verfügbare Entitäten

Der Schritt **Import S/4HANA Entity** deckt zwei Entitäten ab: `trial_balance` (aggregierte Hauptbuchkontensalden zum Periodenende, über `API_OPLACCTGDOCITEMCUBE_SRV`) und `journal_entry_items` (gebuchte Journalbuchungspositionen, über `API_JOURNALENTRYITEMBASIC_SRV`). Beide unterstützen serverseitige Filter auf `CompanyCode`, `GLAccount`, `CostCenter`, `ProfitCenter`, `FiscalYear`, `FiscalPeriod` und `Ledger`, wobei `PostingDate`, `FiscalYear` und `FiscalPeriod` Bereichsgrenzen mit `ge`/`le` akzeptieren. Die vollständige Feldreferenz finden Sie unter [Import S/4HANA Entity](/de/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/).

## Journalbuchungen buchen

Der Schritt **S/4HANA: Post Journal Entry** bucht Hauptbuch-Journalbuchungen über die gemeinsame ERP-Schreibpipeline von PlaidCloud: Er übergibt sie über den SOAP-Dienst `JournalEntryBulkCreateRequest_In` von S/4HANA Cloud, wartet auf die Bestätigung `JournalEntryBulkCreateConfirmation_Out` und bestätigt die Buchung, bevor sie als gebucht gemeldet wird. Eine Korrektur bucht eine neue Stornobuchung mit vertauschtem Soll und Haben, anstatt die ursprüngliche Buchung zu ändern. Die Feldreferenz finden Sie unter [S/4HANA: Post Journal Entry](/de/reference/workflow-steps/s4hana-cloud/s4hana-post/), die vollständige Anleitung zum Buchen unter [Mit SAP S/4HANA Cloud verbinden](/de/guides/connections/s4hana-cloud/).

## Bekannte Einschränkungen

| Einschränkung | Bedeutung |
|---|---|
| Bestätigungslatenz | Der SOAP-Dienst zum Massenanlegen verarbeitet Anfragen asynchron und ist deutlich langsamer als ein synchroner OData-Schreibvorgang gleicher Größe. |
| Filterbare Felder hängen von Ihrem Communication Scenario ab | Ein Kostenobjekt oder eine Dimension, die Ihr Communication Scenario nicht bereitstellt, lässt sich nicht serverseitig filtern. Grenzen Sie sie in Ihrem Workflow nach dem Abruf ein. |

## Verwandte Themen

- [Mit SAP S/4HANA Cloud verbinden (Anleitung)](/de/guides/connections/s4hana-cloud/) – Schritt für Schritt: Verbindung erstellen, testen, eine Entität importieren und ein Journal buchen.
- [Import S/4HANA Entity](/de/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/)
- [S/4HANA: Post Journal Entry](/de/reference/workflow-steps/s4hana-cloud/s4hana-post/)
- [ERP-Buchungsverlauf prüfen](/de/guides/connections/erp-post-history/)
- [SAP-ECC-/S/4HANA-Konnektor](/de/reference/connectors/erp/sap-s4/) – der separate RFC-/agentenbasierte Konnektor für S/4HANA On-Premises oder in der Private Cloud.
