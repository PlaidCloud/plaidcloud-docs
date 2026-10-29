---
title: Xero-REST-Connector
description: Richten Sie in PlaidCloud eine Xero-Verbindung mit einer OAuth-Freigabe per Klick ein, importieren Sie Entitäten der Accounting API und buchen Sie manuelle Journale, Rechnungen, Eingangsrechnungen, Zahlungen und Gutschriften.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/xero.md
---

## API-Dokumentation

Die [Accounting-API-Referenz](https://developer.xero.com/documentation/api/accounting/overview) von Xero dokumentiert die Entitäten, die `where=`-Filter und die Create-Payloads, die dieser Connector verwendet.

## So funktioniert die Authentifizierung

Die Verbindung authentifiziert sich mit der **OAuth 2.0**-Freigabe von Xero. PlaidCloud registriert die OAuth-App selbst, sodass Sie keine Client-ID und kein Client-Secret beschaffen oder eingeben müssen – Sie klicken auf **Mit Xero verbinden**, melden sich bei Xero an und bestätigen die Freigabe. PlaidCloud speichert die resultierenden Tokens an der Verbindung und aktualisiert sie für Sie; dabei wird jedes rotierte Refresh-Token gespeichert, damit eine lange inaktive Verbindung weiter funktioniert.

Eine Freigabe deckt jede Xero-Organisation ab, für die Sie sie bestätigen. Die Verbindung zielt auf genau eine davon: Die Auswahl **Organisation** listet die Organisationen auf, die die Freigabe zurückgegeben hat, und jede Anfrage enthält die Tenant-ID dieser Organisation. Um in einer zweiten Organisation zu lesen oder zu buchen, erstellen Sie eine zweite Xero-Verbindung und wählen dort diese Organisation aus.

Die Demo Company von Xero ist eine Eigenschaft der Organisation, keine Verbindungseinstellung – eine Demo-Organisation erscheint wie jede andere in der Liste **Organisation**, eine Sandbox-Verbindung ist also eine Verbindung, die auf sie verweist.

## Konfiguration

| Feld | Typ | Beschreibung |
|---|---|---|
| Name | Text | Anzeigename dieser Verbindung. |
| Mit Xero verbinden | Schaltfläche | Startet die Anmeldung und den Zustimmungsablauf bei Xero. |
| Verbindungsstatus | Status | Zeigt `Not connected`, bis die Freigabe abgeschlossen ist, und meldet danach, wie viele Organisationen sie abdeckt. |
| Organisation | Auswahl | Die Xero-Organisation, in der diese Verbindung liest und bucht. Wird aus der Freigabe befüllt. |

## Ratenbegrenzungen

Xero begrenzt jede Organisation auf 60 Aufrufe pro Minute und 5.000 Aufrufe pro Tag, bei maximal 5 gleichzeitigen Aufrufen. PlaidCloud steuert die Begrenzungen pro Minute und für die Gleichzeitigkeit pro Verbindung, sodass die Drosselung einer Organisation die Aufrufe einer anderen Verbindung nie blockiert, und beachtet bei einer gedrosselten Antwort den `Retry-After` von Xero. Das Tageslimit müssen Sie selbst verwalten – planen Sie umfangreiche Abrufe per Zeitplan, statt viele gleichzeitig auszuführen.

## Entitäten, die sich importieren lassen

Der Schritt **Xero: Entität importieren** deckt elf Entitäten der Accounting API ab: `accounts`, `contacts`, `invoices`, `credit_notes`, `payments`, `manual_journals`, `bank_transactions`, `items`, `tracking_categories`, `tax_rates` und `currencies`. Jeder Abruf akzeptiert optional eine Statuseinschränkung, einen Datumsbereich und einen Stichtag für geänderte Datensätze. Die vollständige Feldreferenz finden Sie unter [Xero: Entität importieren](/de/reference/workflow-steps/xero/import-xero-entity/).

## Belege buchen

Der Schritt **Xero: Beleg buchen** bucht manuelle Journale, Rechnungen, Eingangsrechnungen, Zahlungen und Gutschriften über die gemeinsame ERP-Schreibpipeline von PlaidCloud, aus einer Kopftabelle und einer Positionstabelle. Die Feldreferenz finden Sie unter [Xero: Beleg buchen](/de/reference/workflow-steps/xero/xero-post/), die vollständige Anleitung zum Buchen unter [Mit Xero verbinden](/de/guides/connections/xero/).

## Bekannte Einschränkungen

| Einschränkung | Bedeutung |
|---|---|
| Manuelle Journale und Zahlungen lassen sich nach einem unklaren Ergebnis nicht nachschlagen | Rechnungen, Eingangsrechnungen und Gutschriften tragen eine Belegnummer, die PlaidCloud vergibt und über die sie sich zurückabfragen lassen. Die Beschreibung eines manuellen Journals und die Referenz einer Zahlung sind nicht abfragbar; ein Schreibvorgang mit ungewissem Ausgang wird daher unter Quarantäne gestellt, damit Sie ihn in Xero klären, statt zu raten. |
| Die Stornierung deckt nur manuelle Journale und Rechnungen ab | Ein manuelles Journal wird als Journal mit vertauschtem Soll und Haben storniert; eine Rechnung wird durch eine spiegelnde Gutschrift storniert. Für Eingangsrechnungen, Zahlungen und Gutschriften gibt es keinen dokumentierten Rückgängig-Payload, daher lehnt PlaidCloud eine Stornierung ab, statt einen zu erfinden. |
| Filter sind feste Felder, keine Abfragesprache | Die Abfrage-API von Xero bietet pro Entität eine Statuseinschränkung und einen Datumsbereich, keine offene Filtersprache – daher bietet der Importschritt diese Felder an statt einer Tabelle aus Feld, Operator und Wert. |
| Eine Organisation pro Verbindung | Jede Anfrage enthält eine Tenant-ID. Eine zweite Organisation erfordert eine zweite Verbindung. |

## Verwandte Themen

- [Mit Xero verbinden (Anleitung)](/de/guides/connections/xero/) – Schritt für Schritt: Verbindung erstellen, testen, eine Entität importieren und einen Beleg buchen.
- [Xero: Entität importieren](/de/reference/workflow-steps/xero/import-xero-entity/)
- [Xero: Beleg buchen](/de/reference/workflow-steps/xero/xero-post/)
- [ERP-Buchungsverlauf prüfen](/de/guides/connections/erp-post-history/)
