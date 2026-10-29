---
title: Workday-Financials-Connector
description: Richten Sie in PlaidCloud eine Workday-Financials-Verbindung mit einem Integrationssystembenutzer ein, um Daten über einen RaaS-Bericht zu importieren und Journalbuchungen über SOAP zu buchen.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/workday-financials.md
---

## API-Dokumentation

Die [SOAP-Webservices](https://community.workday.com/sites/default/files/file-hosting/productionapi/) und [Report-as-a-Service (RaaS)](https://doc.workday.com/) von Workday dokumentieren die Schnittstellen, die dieser Connector verwendet.

## So funktioniert die Authentifizierung

Die Verbindung authentifiziert sich mit einem **Integrationssystembenutzer (Integration System User, ISU)** – einem Workday-Benutzertyp für die Integration zwischen Systemen, der durch eine Integrationssystem-Sicherheitsgruppe abgesichert ist und genau die Zugriffsrechte erhält, die dieser Connector benötigt (Berichtszugriff zum Lesen, den Geschäftsprozess „Submit Accounting Journal“ zum Buchen). Anfragen enthalten Benutzername und Passwort des ISU; es gibt keine interaktive Anmeldung.

## Konfiguration

| Feld | Typ | Beschreibung |
|---|---|---|
| Name | Text | Anzeigename dieser Verbindung. |
| Tenant-Host | Text | Ihr Workday-Host, z. B. `wd5-impl.workday.com`. |
| Tenant-Name | Text | Der Name Ihres Workday-Tenants. |
| ISU-Benutzername | Text | Der Benutzername des Integrationssystembenutzers. |
| ISU-Passwort | Text | Das Passwort des Integrationssystembenutzers. Wird verschlüsselt gespeichert. |

## Daten importieren

Workday Financials hat keinen festen Satz vorgefertigter Entitäten. Stattdessen ruft der Schritt **Import Workday Entity** einen **Report-as-a-Service-Bericht (RaaS)** auf, den Sie in Workday erstellen und mit Webservice-Zugriff veröffentlichen – seine URL geben Sie selbst an. Der Schritt unterstützt Filter auf `company`, `ledger`, `period`, `accounting_date` (Bereich), `ledger_account` (Bereich) und `cost_center`, die jeweils als Berichtsparameter durchgereicht werden. Ein Filter funktioniert also nur, wenn Ihr Bericht eine passende Eingabeaufforderung definiert. Die vollständige Feldreferenz finden Sie unter [Import Workday Entity](/de/reference/workflow-steps/workday-financials/import-workday-entity/).

## Journalbuchungen buchen

Der Schritt **Workday Financials: Post Journal Entry** bucht Buchhaltungsjournale über die gemeinsame ERP-Schreibpipeline von PlaidCloud. Er verwendet die SOAP-Operation `Submit_Accounting_Journal` von Workday und fragt den Status des Geschäftsprozesses der Buchung ab, bis ein Endzustand erreicht ist, bevor sie als gebucht gemeldet wird. Eine Korrektur bucht eine neue Stornobuchung mit vertauschtem Soll und Haben, anstatt die ursprüngliche Buchung zu ändern. Die Feldreferenz finden Sie unter [Workday Financials: Post Journal Entry](/de/reference/workflow-steps/workday-financials/workday-post/), die vollständige Anleitung zum Buchen unter [Mit Workday Financials verbinden](/de/guides/connections/workday-financials/).

## Bekannte Einschränkungen

| Einschränkung | Bedeutung |
|---|---|
| Die Form des Imports hängt von Ihrem RaaS-Bericht ab | PlaidCloud hat keine vorgefertigten Entitäten für Workday Financials – die Felder, Eingabeaufforderungen und die Zugriffssteuerung des Berichts liegen vollständig in Workday. Eine Änderung des Berichts dort kann die Form Ihres Imports verändern, ohne dass sich auf der PlaidCloud-Seite etwas ändert. |
| Die Genehmigung im Geschäftsprozess erhöht die Latenz | Ein Journal, das in Ihrem Geschäftsprozess „Submit Accounting Journal“ über einen Genehmigungsschritt läuft, bleibt `pending`, bis es in Workday genehmigt wird; die Abfrage des Endzustands wartet darauf. |

## Verwandte Themen

- [Mit Workday Financials verbinden (Anleitung)](/de/guides/connections/workday-financials/) – Schritt für Schritt: Verbindung erstellen, testen, einen Bericht importieren und ein Journal buchen.
- [Import Workday Entity](/de/reference/workflow-steps/workday-financials/import-workday-entity/)
- [Workday Financials: Post Journal Entry](/de/reference/workflow-steps/workday-financials/workday-post/)
- [ERP-Buchungsverlauf prüfen](/de/guides/connections/erp-post-history/)
- [Workday-REST-Connector](/de/reference/connectors/rest/workday/) – der separate, generische Workday-Connector für HR- und Gehaltsabrechnungsdaten über REST.
