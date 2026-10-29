---
title: Business-Central-REST-Konnektor
description: Richten Sie in PlaidCloud mit Azure-AD-Client-Credentials eine Verbindung zu Microsoft Dynamics 365 Business Central ein, um OData-Entitäten zu importieren und Sachkonten-Journalzeilen zu buchen.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/business-central.md
---

## API-Dokumentation

Die [Standard-OData-v2.0-API](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/) von Business Central dokumentiert die Entitäten sowie die Optionen `$filter`/`$orderby`, die dieser Konnektor verwendet.

## So funktioniert die Authentifizierung

Die Verbindung authentifiziert sich als Anwendung über die **Client-Credentials (S2S)** von Entra ID (Azure AD): Client-ID und Client-Secret einer App-Registrierung werden gegen ein Zugriffstoken unter `https://login.microsoftonline.com/<tenant id>/oauth2/v2.0/token` getauscht, mit dem Geltungsbereich `https://api.businesscentral.dynamics.com/.default`. Es gibt keine interaktive Anmeldung. Die App-Registrierung benötigt API-Berechtigungen für Business Central (`API.ReadWrite.All` oder einen engeren Geltungsbereich, den Ihr Administrator ausstellt).

Jede Anfrage bezieht sich auf eine **Umgebung** (z. B. `Production` oder eine Sandbox-Umgebung) und ein **Unternehmen** darin. Beides wird in der Verbindung festgelegt und nicht pro Anfrage gewählt.

## Konfiguration

| Feld | Typ | Beschreibung |
|---|---|---|
| Name | Text | Anzeigename für diese Verbindung. |
| Client-ID | Text | Die Anwendungs-ID (Client-ID) der Entra-App-Registrierung. |
| Client-Secret | Text | Das Client-Secret der App-Registrierung. Wird verschlüsselt gespeichert. |
| Mandanten-ID | Text | Ihre Azure-AD-Mandanten-ID. |
| Umgebung | Text | Der Name der Business-Central-Umgebung, z. B. `Production`. |
| Unternehmen | Text | Die Business-Central-Unternehmens-ID, aus der diese Verbindung liest und in die sie bucht. |

## Zum Import verfügbare Entitäten

Der Schritt **Import Business Central Entity** deckt sechs Entitäten ab: `accounts`, `generalLedgerEntries`, `customers`, `vendors`, `items`, `journals`. Jeder Abruf unterstützt serverseitige Filter pro Entität. Die vollständige Feldreferenz finden Sie unter [Import Business Central Entity](/de/reference/workflow-steps/business-central/import-business-central-entity/).

`generalLedgerEntries` ist schreibgeschützt und enthält nur gebuchte Einträge. Es ist die Entität, die Sie für eine Saldenliste oder Hauptbuchdetails abrufen, da sie nie eine Zeile enthält, die noch in einem ungebuchten Journalstapel liegt.

## Sachkonten-Journalzeilen buchen

Der Schritt **Business Central Post** legt Zeilen in einem **bestehenden** Journalstapel an und bucht diesen Stapel über die gemeinsame ERP-Schreibpipeline von PlaidCloud. Vor dem Buchen prüft er, dass der Stapel nur die Zeilen dieser Anfrage enthält, und bestätigt die Buchung anhand von `generalLedgerEntries` (nicht anhand des Journalstapels selbst). Die Feldreferenz finden Sie unter [Business Central: Post General Journal Lines](/de/reference/workflow-steps/business-central/business-central-post/), die vollständige Anleitung zum Buchen unter [Mit Business Central verbinden](/de/guides/connections/business-central/).

## Bekannte Einschränkungen

| Einschränkung | Bedeutung |
|---|---|
| Ein Belegtyp zum Schreiben | Unterstützt wird nur das Buchen von Sachkonten-Journalzeilen. Der Ablauf mit Entwurfsbelegen (Verkaufs- und Einkaufsrechnungen, Entwurf → Gebucht) wird nicht unterstützt, da die Buchungsaktion für diesen Ablauf in der veröffentlichten Dokumentation von Microsoft nicht eindeutig festgelegt ist. |
| Buchen nur in einen bestehenden Stapel | Dieser Konnektor legt in Business Central nie einen Journalstapel an – erstellen Sie ihn zuvor dort. |
| Gleichzeitiges Buchen in denselben Stapel | Der Idempotenzschutz bezieht sich auf die Belegnummer, nicht auf den Journalstapel. Wenn zwei verschiedene Belegnummern gleichzeitig in denselben Stapel buchen, ist keine serielle Verarbeitung garantiert. |

## Verwandte Themen

- [Mit Business Central verbinden (Anleitung)](/de/guides/connections/business-central/) – Schritt für Schritt: Verbindung erstellen, testen, eine Entität importieren und ein Journal buchen.
- [Import Business Central Entity](/de/reference/workflow-steps/business-central/import-business-central-entity/)
- [Business Central: Post General Journal Lines](/de/reference/workflow-steps/business-central/business-central-post/)
- [ERP-Buchungsverlauf prüfen](/de/guides/connections/erp-post-history/)
