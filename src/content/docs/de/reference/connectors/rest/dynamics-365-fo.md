---
title: Dynamics-365-Finance-&-Operations-REST-Konnektor
description: Richten Sie in PlaidCloud eine Verbindung zu Dynamics 365 Finance & Operations ein, um OData-/DMF-Entitäten zu importieren und Journalbuchungen asynchron zu buchen.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/dynamics-365-fo.md
---

## API-Dokumentation

Die [OData-v4-Endpunkte](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/odata) und das [Data Management Framework](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-management-import-export) von D365 F&O dokumentieren die Endpunkte und den Massenextraktionspfad, die dieser Konnektor verwendet.

## So funktioniert die Authentifizierung

Die Verbindung authentifiziert sich als Anwendung über die **Client-Credentials** von Entra ID (Azure AD): Client-ID und Client-Secret einer App-Registrierung werden gegen ein Zugriffstoken getauscht, dessen Geltungsbereich die Ressource der Umgebung ist. Es gibt keine interaktive Anmeldung.

## Konfiguration

| Feld | Typ | Beschreibung |
|---|---|---|
| Name | Text | Anzeigename für diese Verbindung. |
| Umgebungs-URL | Text | Die URL Ihrer D365-F&O-Umgebung, z. B. `https://yourorg.operations.dynamics.com`. |
| Client-ID | Text | Die Anwendungs-ID (Client-ID) der Entra-App-Registrierung. |
| Client-Secret | Text | Das Client-Secret der App-Registrierung. Wird verschlüsselt gespeichert. |
| Mandanten-ID | Text | Ihre Azure-AD-Mandanten-ID. |
| Ressource/Geltungsbereich | Text | Der angeforderte OAuth2-Geltungsbereich, in der Regel die Umgebungs-URL plus `/.default`. |

## Zum Import verfügbare Entitäten

Der Schritt **Import D365 F&O Entity** deckt sechs Entitäten ab: `main_accounts`, `currencies`, `customers`, `vendors`, `released_products`, `ledger_journal_headers`. Jeder Abruf läuft entweder im Synchronmodus `odata` (ein direkter Aufruf, für routinemäßige Abrufe) oder im Massenmodus `dmf` (ein asynchroner Exportjob des Data Management Framework, für große Extrakte) und unterstützt serverseitige Filter pro Entität, darunter Datums-, Konto- und Dimensionsbereiche. Die vollständige Feldreferenz finden Sie unter [Import D365 F&O Entity](/de/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/).

## Journalbuchungen buchen

Der Schritt **D365 F&O: Post Journal Entry** bucht Hauptbuch-Journalbuchungen über die gemeinsame ERP-Schreibpipeline von PlaidCloud: Er übergibt sie an die asynchrone benutzerdefinierte Journalbuchungsaktion von D365 F&O, fragt den Status ab, bis ein Endzustand erreicht ist, und bestätigt die Buchung, bevor sie als gebucht gemeldet wird. Eine Korrektur bucht eine neue Stornobuchung mit vertauschtem Soll und Haben, anstatt die ursprüngliche Buchung zu ändern. Die Feldreferenz finden Sie unter [D365 F&O: Post Journal Entry](/de/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/), die vollständige Anleitung zum Buchen unter [Mit Dynamics 365 Finance & Operations verbinden](/de/guides/connections/dynamics-365-fo/).

## Bekannte Einschränkungen

| Einschränkung | Bedeutung |
|---|---|
| Der DMF-Synchronmodus hat eine Extraktionslatenz | Ein Abruf im Modus `dmf` wartet auf einen asynchronen Exportjob und ist deutlich langsamer als ein `odata`-Abruf derselben Größe. |
| Die Dimensionsfilterung hängt von der Struktur ab | Eine Finanzdimension, die nicht Teil Ihrer Kontenstruktur ist, lässt sich nicht serverseitig filtern. Grenzen Sie sie in Ihrem Workflow nach dem Abruf ein. |

## Verwandte Themen

- [Mit Dynamics 365 Finance & Operations verbinden (Anleitung)](/de/guides/connections/dynamics-365-fo/) – Schritt für Schritt: Verbindung erstellen, testen, eine Entität importieren und ein Journal buchen.
- [Import D365 F&O Entity](/de/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/)
- [D365 F&O: Post Journal Entry](/de/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/)
- [ERP-Buchungsverlauf prüfen](/de/guides/connections/erp-post-history/)
