---
title: Acumatica-REST-Konnektor
description: Richten Sie in PlaidCloud eine Verbindung zur vertragsbasierten Acumatica-REST-API ein, um Stamm- und Bewegungsdaten zu importieren und Journalbuchungen, Rechnungen, Eingangsrechnungen und Zahlungen zu buchen.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/acumatica.md
---

## API-Dokumentation

Die [vertragsbasierte REST-API](https://help.acumatica.com/Help?ScreenId=ShowWiki&pageid=e0dea52d-0339-4f34-a6c0-9615ce6a25c2) von Acumatica dokumentiert die Endpunkte und Abfrageoptionen, die dieser Konnektor verwendet.

## So funktioniert die Authentifizierung

Die Verbindung ist **sitzungsbasiert**: PlaidCloud meldet sich pro abgegrenzter Arbeitseinheit einmal an (`POST <instance>/entity/auth/login` mit Ihrem Benutzernamen, Passwort, Unternehmen und optional der Niederlassung) und verwendet das daraus resultierende Sitzungs-Cookie für jeden Aufruf in dieser Einheit. Danach meldet es sich wieder ab. Dies ist weder ein Bearer-Token- noch ein OAuth-Ablauf. Sitzungen werden auf das Limit gleichzeitiger Sitzungen Ihrer Acumatica-Lizenz angerechnet, das bei Test- und Instanzen niedrigerer Stufen auf nur 2 begrenzt sein kann. Vermeiden Sie daher, viele Acumatica-Schritte parallel über eine Verbindung auszuführen.

## Konfiguration

| Feld | Typ | Beschreibung |
|---|---|---|
| Name | Text | Anzeigename für diese Verbindung. |
| Basis-URL der Instanz | Text | Die URL Ihrer Acumatica-Instanz, z. B. `https://yourcompany.acumatica.com`. |
| Endpunktname | Text | Der Name des Vertragsendpunkts. `Default`, sofern kein benutzerdefinierter Endpunkt veröffentlicht wurde. |
| Endpunktversion | Text | Optional, z. B. `25.200.001`. Lassen Sie das Feld leer, um die neueste veröffentlichte Version des Endpunkts zu verwenden. |
| Unternehmen / Mandant | Text | Die genaue Acumatica-Unternehmens-ID, bei der sich diese Verbindung anmeldet. |
| Niederlassung | Text | Optional. Lassen Sie das Feld leer, um die Standardniederlassung des anmeldenden Benutzers zu verwenden. |
| Benutzername | Text | Der Login des PlaidCloud-API-Benutzers. |
| Passwort | Text | Das Passwort des PlaidCloud-API-Benutzers. Wird verschlüsselt gespeichert. |

## Zum Import verfügbare Entitäten

Der Schritt **Import Acumatica Entity** deckt 18 vertragsbasierte Entitäten ab:

**Stamm- und Referenzdaten** – `account`, `subaccount`, `ledger`, `financial_period`, `branch`, `currency`, `currency_rate`, `customer`, `vendor`, `stock_item`, `warehouse`, `employee`, `tax_category`, `project`

**Bewegungsdaten** – `sales_invoice`, `bill`, `sales_order`, `shipment`

Jeder Abruf unterstützt einen Schalter `Active Only`, einen Stichtag `Updated After` und serverseitige Filter pro Entität. Die vollständige Feldreferenz finden Sie unter [Import Acumatica Entity](/de/reference/workflow-steps/acumatica/import-acumatica-entity/).

## Belege buchen

Der Schritt **Acumatica Post** bucht die Belege **JournalTransaction**, **SalesInvoice**, **Bill** und **Payment** über die gemeinsame ERP-Schreibpipeline von PlaidCloud: Er legt sie im Status „Hold“ an, gibt sie frei (eine asynchrone Aktion) und bestätigt die Freigabe, bevor ein Beleg als gebucht gemeldet wird. Die Feldreferenz finden Sie unter [Acumatica: Post Documents](/de/reference/workflow-steps/acumatica/acumatica-post/), die vollständige Anleitung zum Buchen unter [Mit Acumatica verbinden](/de/guides/connections/acumatica/).

## Bekannte Einschränkungen

| Einschränkung | Bedeutung |
|---|---|
| Lesezugriffe, die von Generic Inquiries abhängen, werden nicht abgedeckt | Saldenliste, Hauptbuch-Buchungsdetails, Lagerbestand, Budgets und Intercompany-Daten liegen hinter Acumatica Generic Inquiries und nicht in den oben genannten 18 vertragsbasierten Entitäten. Erstellen Sie die Generic Inquiry in Acumatica und rufen Sie sie über eine [generische REST-Verbindung](/de/reference/connectors/rest/generic-rest/) ab. |
| Kein nativer Idempotenzschlüssel beim Schreiben | Die PUT-basierte Schreib-API von Acumatica hat kein Idempotenzfeld. Der eigene Ledger-Claim von PlaidCloud ist der einzige Schutz vor einer doppelten Buchung. |
| Stornierung erfolgt manuell | Für keinen Belegtyp ist eine Void- oder Storno-Aktion dokumentiert. Ein gebuchter Beleg kann nicht aus PlaidCloud heraus storniert werden – korrigieren Sie ihn direkt in Acumatica. |
| Kein Korrelationsfeld für Zahlungen | Acumatica stellt kein dokumentiertes Feld bereit, um eine Zahlung nach einem uneindeutigen Ergebnis der PlaidCloud-Anfrage zuzuordnen. Eine Zahlung mit unklarem Status wird zur manuellen Klärung in Quarantäne gestellt. |
| Filterung von Positionen erfolgt nicht serverseitig | Filter im Stil von `$filter` erreichen Entitäts- und Kopffelder, nicht aber die Positionsdimensionen eines Belegs (zum Beispiel eine Kostenstelle auf Positionsebene). Grenzen Sie die Positionen in Ihrem Workflow nach dem Abruf ein. |

## Verwandte Themen

- [Mit Acumatica verbinden (Anleitung)](/de/guides/connections/acumatica/) – Schritt für Schritt: Verbindung erstellen, testen, eine Entität importieren und einen Stapel buchen.
- [Import Acumatica Entity](/de/reference/workflow-steps/acumatica/import-acumatica-entity/)
- [Acumatica: Post Documents](/de/reference/workflow-steps/acumatica/acumatica-post/)
- [ERP-Buchungsverlauf prüfen](/de/guides/connections/erp-post-history/)
