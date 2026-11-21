---
title: Data Foundation Coverage Matrix
description: Welchen Datensatz des Common Finance Model jedes System, mit dem Data Foundation sich verbindet, direkt liefert und welchen Sie als Datei hinzufügen.
sidebar:
  label: Data Foundation Coverage
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/data-foundation-coverage-matrix.md
---

Data Foundation liest jedes ERP-System und jede Instanz, die Sie verbinden, direkt in ein Common Finance Model ein. Dateien füllen alles auf, was ein System nicht enthält, sodass sich jeder der folgenden Datensätze auch als Datei bereitstellen lässt.

## Legende

| Markierung | Bedeutung |
| --- | --- |
| **Vollständig** | Data Foundation liest den Datensatz direkt aus dem System. |
| **Vollständig¹** | Wird direkt gelesen, wenn das System ihn enthält. Ein System ohne die Daten unterbricht das Laden nicht. Eine Verbindung ohne Zugriff darauf lässt diesen Datensatz leer oder lässt nur diesen Datensatz fehlschlagen, und der Rest wird geladen. |
| **Datei** | Das System liefert diesen Datensatz nicht. Fügen Sie ihn als Datei hinzu. |

## SAP, Oracle und Dynamics 365

| Datensatz | SAP S/4HANA | SAP ECC | SAP S/4HANA Cloud | Oracle E-Business Suite | Oracle Fusion | Dynamics 365 Finance and Operations |
| --- | --- | --- | --- | --- | --- | --- |
| Entitäten | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Geschäftskalender | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Kontenplan | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Abteilungen | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Profitcenter | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Datei | Vollständig¹ |
| Standorte | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ |
| Projekte | Datei | Datei | Datei | Datei | Datei | Datei |
| Vertriebsmitarbeiter | Datei | Datei | Datei | Datei | Datei | Datei |
| Produkte | Vollständig | Vollständig | Vollständig | Vollständig¹ | Vollständig¹ | Vollständig |
| Kunden | Vollständig | Vollständig | Vollständig | Vollständig¹ | Vollständig¹ | Vollständig |
| Lieferanten | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ |
| Hauptbuch | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Saldenliste | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Monatsendsaldo | Datei | Vollständig¹ | Datei | Vollständig¹ | Vollständig¹ | Datei |
| Banksalden | Datei | Vollständig¹ | Datei | Vollständig¹ | Vollständig¹ | Vollständig¹ |
| Verkaufspositionen | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ |
| Pipeline | Datei | Datei | Datei | Datei | Datei | Datei |
| Lieferantenrechnungspositionen | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ |
| Bestellungen | Vollständig¹ | Vollständig¹ | Datei | Vollständig¹ | Vollständig¹ | Datei |
| Offene Posten | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ |
| Zahlungen | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ |
| Lagerbestände | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ |
| Standardkosten | Vollständig¹ | Vollständig¹ | Datei | Vollständig¹ | Vollständig¹ | Datei |
| Anlagevermögen | Vollständig¹ | Vollständig¹ | Datei | Vollständig¹ | Vollständig¹ | Datei |
| Anlagenbewegungen | Vollständig¹ | Vollständig¹ | Datei | Vollständig¹ | Vollständig¹ | Datei |
| Budget | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ |
| Verteilungstreiber | Vollständig¹ | Vollständig¹ | Datei | Datei | Datei | Datei |
| Wechselkurse | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Segmentwerte | Datei | Datei | Datei | Datei | Datei | Datei |
| CO-PA nach Bewertung | Vollständig¹ | Vollständig¹ | Datei | Datei | Datei | Datei |

## Mid-Market- und Cloud-Finanzsysteme

| Datensatz | Business Central | Sage 100 | Sage Intacct | QuickBooks Online | Xero | Workday | NetSuite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Entitäten | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Geschäftskalender | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Kontenplan | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Abteilungen | Vollständig | Vollständig¹ | Vollständig | Datei | Vollständig¹ | Vollständig | Vollständig |
| Profitcenter | Vollständig¹ | Datei | Vollständig¹ | Vollständig¹ | Vollständig¹ | Datei | Vollständig¹ |
| Standorte | Vollständig¹ | Datei | Vollständig¹ | Vollständig¹ | Vollständig¹ | Datei | Vollständig¹ |
| Projekte | Datei | Datei | Vollständig¹ | Datei | Datei | Datei | Datei |
| Vertriebsmitarbeiter | Datei | Datei | Datei | Datei | Datei | Datei | Vollständig¹ |
| Produkte | Vollständig | Datei | Vollständig | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig |
| Kunden | Vollständig | Datei | Vollständig | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig |
| Lieferanten | Vollständig¹ | Datei | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ |
| Hauptbuch | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Saldenliste | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Monatsendsaldo | Vollständig¹ | Datei | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Datei |
| Banksalden | Vollständig¹ | Datei | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ |
| Verkaufspositionen | Vollständig¹ | Datei | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig |
| Pipeline | Datei | Datei | Datei | Datei | Datei | Datei | Datei |
| Lieferantenrechnungspositionen | Vollständig¹ | Datei | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ |
| Offene Posten | Vollständig¹ | Datei | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ |
| Zahlungen | Vollständig¹ | Datei | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ |
| Bestellungen | Datei | Datei | Datei | Datei | Datei | Datei | Datei |
| Lagerbestände | Vollständig¹ | Datei | Datei | Vollständig¹ | Datei | Datei | Vollständig¹ |
| Standardkosten | Datei | Datei | Datei | Datei | Datei | Datei | Datei |
| Anlagevermögen | Datei | Datei | Datei | Datei | Datei | Datei | Datei |
| Anlagenbewegungen | Datei | Datei | Datei | Datei | Datei | Datei | Datei |
| Budget | Vollständig¹ | Datei | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ |
| Verteilungstreiber | Vollständig¹ | Datei | Vollständig¹ | Datei | Datei | Vollständig¹ | Vollständig |
| Wechselkurse | Vollständig | Datei | Vollständig | Vollständig¹ | Datei | Vollständig | Vollständig¹ |
| Segmentwerte | Datei | Datei | Datei | Datei | Datei | Vollständig¹ | Vollständig¹ |
| CO-PA nach Bewertung | Datei | Datei | Datei | Datei | Datei | Datei | Datei |

## CRM-, Konsolidierungs- und Planungsquellen

| Datensatz | Salesforce | OneStream | Anaplan |
| --- | --- | --- | --- |
| Entitäten | Datei | Datei | Datei |
| Geschäftskalender | Vollständig¹ | Datei | Datei |
| Kontenplan | Datei | Datei | Datei |
| Abteilungen | Datei | Datei | Datei |
| Profit-Center | Datei | Datei | Datei |
| Projekte | Vollständig¹ | Datei | Datei |
| Vertriebsmitarbeiter | Vollständig¹ | Datei | Datei |
| Produkte | Vollständig¹ | Datei | Datei |
| Kunden | Vollständig¹ | Datei | Datei |
| Hauptbuch | Datei | Datei | Datei |
| Saldenliste | Datei | Datei | Datei |
| Verkaufspositionen | Datei | Datei | Datei |
| Pipeline | Vollständig¹ | Datei | Datei |
| Kundenaufträge | Vollständig¹ | Datei | Datei |
| Lagerbestände | Datei | Datei | Datei |
| Budget | Datei | Vollständig | Vollständig |
| Verteilungstreiber | Datei | Vollständig¹ | Vollständig¹ |
| Wechselkurse | Datei | Datei | Datei |
| Segmentwerte | Datei | Datei | Datei |
| CO-PA nach Bewertung | Datei | Datei | Datei |

## Hinweise zu den Systemen

- **Kundenaufträge, Verträge, passive Rechnungsabgrenzung und Lagerbewegungen** werden aus keinem System gelesen, außer den Aufträgen aus Salesforce. Fügen Sie sie als Dateien hinzu.
- **Salesforce** ist eine CRM-Quelle. Sie liefert Kunden, Produkte, die Vertriebspipeline, Vertriebsmitarbeiter (Benutzer), Kampagnen als Projekte, ihre Geschäftsmonate und Aufträge, nie das Hauptbuch. Aufträge setzen voraus, dass Orders in Salesforce aktiviert ist. Wenn Salesforce das Lesen der Aufträge verweigert, schlagen nur die Auftragsmonate fehl, und sie behalten, was zuletzt geladen wurde.
- **OneStream** ist eine Ergebnisquelle. Sie liefert den Budget-Datensatz, bringt Ihre konsolidierten Ergebnisse ein, damit Data Foundation die Konzern-GuV damit abstimmen kann, und ein Budget- oder Forecast-Szenario als Plan. Ein optionaler zweiter Adapter liefert geplanten Headcount und geplante Mengen als Verteilungstreiber.
- **Anaplan** ist eine Planquelle. Sie liefert den Budget-Datensatz aus einem Budget-, Forecast- oder Konsolidierungsplan und Verteilungstreiber aus einem optionalen zweiten Export.
- **SAP S/4HANA und SAP ECC** lesen dieselben Stammdaten, Lieferanten, Lieferantenrechnungen, Bestellungen, offenen Posten, Zahlungen, das Anlagenverzeichnis und die Standardkosten. ECC liest sein Hauptbuch aus den Positionen der Finanzbuchhaltung und des Controllings und seine Summen und seinen Monatsendsaldo aus der Summentabelle des Hauptbuchs. Profitcenter und Werke (Standorte) werden gelesen, wenn das System sie enthält. Verkaufspositionen sind Fakturabelege. CO-PA nach Bewertung wird aus der Einzelpostentabelle des Ergebnisbereichs gelesen, die Sie angeben; ist keine angegeben, fügen Sie es als Datei hinzu.
- **Oracle E-Business Suite** liest Standorte und Profitcenter jeweils aus dem Segment des Kontenplans, das Sie dafür angeben.
- **Oracle Fusion** liest jeden optionalen Datensatz aus einem eigenen BI-Publisher-Bericht. Ein Bericht für Kunden, Produkte, Standorte oder Lieferanten, den Sie nicht bereitstellen, lässt diesen Datensatz mit einer Warnung leer; der Datensatz jedes anderen Berichts schlägt fehl und behält, was zuletzt geladen wurde; alles andere wird geladen.
- **Workday** hat keinen direkten Journal- oder Saldendienst. Data Foundation stellt Ihnen die zu erstellenden Berichte bereit und liest sie. Segmentwerte (Worktags), Kunden, Produkte, Lieferanten, Verkaufspositionen, Nebenbücher, Banksalden, Budgets und Treiber stammen aus optionalen Berichten und der Monatsendsaldo aus dem Endsaldo des Berichts der Anfangssalden.
- **Sage 100** wird über einen PlaidLink-Agent gelesen, ein Unternehmen pro Verbindung. Es führt seine Bücher in einer Währung, liefert daher keine Wechselkurse, und Data Foundation liest seine Produkte, Kunden und Verkaufspositionen nicht. Abteilungen werden aus dem Abteilungssegment des Kontos gelesen, wenn die Kontomaske eines hat.
- **Xero** liefert keine Wechselkurse. Fügen Sie sie als Datei hinzu, wenn Ihre Entitäten mehr als eine Währung verwenden. Abteilungen, Standorte und Profitcenter sind die Optionen der Tracking-Kategorien mit den genauen Namen Department, Site und Profit centre. Xero erlaubt zwei Tracking-Kategorien, sodass eine Organisation höchstens zwei der drei hat.
- **QuickBooks Online** hat keine Abteilungen: Seine Standorte (Locations) werden als Standorte und seine Klassen als Profitcenter gelesen. Kunden, Produkte, Lieferanten, Wechselkurse, Budgets, Lagerbestände, Verkäufe und Einkäufe werden gelesen, wenn das Unternehmen sie enthält, Lagerbestände nur, wenn das Unternehmen den Bestand verfolgt.
- **NetSuite** liest benutzerdefinierte Segmente als Segmentwerte, Klassen als Profitcenter und Standorte (Locations) als Standorte. Wechselkurse und Lagerbestände werden gelesen, wenn das Konto sie anbietet, und Budgets, wenn das Konto NetSuite Budgets verwendet und die Rolle sie lesen kann.

## Monatsendsaldo

Data Foundation liest den Schlusssaldo, den jedes System selbst zu jedem Monatsende ausweist (siehe [Sind die Zahlen vertrauenswürdig?](/de/guides/projects/data-foundation-proof/)), aus:

| System | Monatsendsaldo gelesen aus |
| --- | --- |
| SAP ECC | Der Summentabelle des Hauptbuchs (`FAGLFLEXT` oder beim klassischen Hauptbuch `GLT0`) |
| Oracle E-Business Suite | `GL_BALANCES`, das jede Periode enthalten muss |
| Oracle Fusion | Dem Bericht PlaidCloudBalances, der jede Periode abdeckt |
| Business Central | Der Saldenliste zu jedem Monatsende |
| Sage Intacct | Den Kontosalden (dem Endsaldo jedes Monats) |
| QuickBooks Online | Dem Bericht Saldenliste zu jedem Monatsende |
| Xero | Dem Bericht Saldenliste zu jedem Monatsende |
| Workday | Dem Endsaldo des Berichts Beginning Balances |

SAP S/4HANA, SAP S/4HANA Cloud, Dynamics 365 Finance and Operations, NetSuite und Sage 100 weisen keinen separaten Saldo aus, den Data Foundation liest. Sie laden und funktionieren wie gewohnt. Wenn Business Central seine Saldenliste zu einem Monatsende verweigert, schlägt der Saldo dieses Monats fehl und behält, was zuletzt geladen wurde.

## Journaldetails

Neben den Beträgen enthält jede Hauptbuchposition die Art des Journals, sein Belegdatum, wer es wann erfasst hat, wer es genehmigt hat, das Journal, das es storniert, und seine Steuer, sofern das System sie enthält. Der Geschäftskalender enthält den Status jeder Periode.

| System | Journalart | Belegdatum | Erfasst von und wann | Genehmiger | Stornierung | Steuer | Periodenstatus |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SAP S/4HANA | Ja | Ja | Ja | Nein | Nein | Code | Ja |
| SAP ECC | Ja | Ja | Ja | Nein | Ja | Code und Betrag | Ja |
| SAP S/4HANA Cloud | Ja | Ja | Ja | Nein | Ja | Nein | Nein |
| Oracle E-Business Suite | Ja | Ja | Ja | Ja | Ja | Nein | Ja |
| Oracle Fusion | Ja | Ja | Ja | Ja | Ja | Nein | Ja |
| Dynamics 365 Finance and Operations | Ja | Ja | Ja | Nein | Nein | Nein | Ja |
| Business Central | Ja | Ja | Ja | Nein | Ja | Nein | Ja |
| Sage 100 | Nein | Nein | Nein | Nein | Nein | Nein | Abgeschlossen, sobald die Periode endet |
| Sage Intacct | Ja | Ja | Ja | Ja | Ja | Nein | Ja |
| QuickBooks Online | Ja | Ja | Ja | Nein | Nein | Nein | Das Datum für den Abschluss der Bücher |
| Xero | Ja | Ja | Nur wann | Nein | Nein | Nein | Das Sperrdatum |
| Workday | Ja | Ja | Ja | Ja | Ja | Code und Betrag | Ja |
| NetSuite | Ja | Ja | Ja | Nein | Nein | Nein | Ja |

SAP S/4HANA Cloud liest, wer ein Journal erfasst hat und was es storniert, aus dem Journal-Entry-Service, Sage Intacct aus Journalstapeln und Oracle E-Business Suite den Genehmiger aus `GL_JE_BATCHES`. Eine Verbindung, die sie nicht lesen kann, lässt diese Spalten leer.

## Verwandte Themen

- [Data Foundation](/de/guides/projects/data-foundation/)
- [Erste Schritte mit Data Foundation](/de/guides/projects/data-foundation-getting-started/)
- [Dateien für Daten außerhalb Ihres ERP hinzufügen](/de/guides/projects/data-foundation/#dateien-für-daten-außerhalb-ihres-erp-hinzufügen)
- Anleitungen zum Verbindungszugriff:
  - [NetSuite](/de/guides/connections/netsuite-access-for-data-foundation/)
  - [Salesforce](/de/guides/connections/salesforce-access-for-data-foundation/)
  - [SAP S/4HANA](/de/guides/connections/sap-s4hana-access-for-data-foundation/)
  - [SAP ECC](/de/guides/connections/sap-ecc-access-for-data-foundation/)
  - [SAP S/4HANA Cloud](/de/guides/connections/s4hana-cloud-access-for-data-foundation/)
  - [Oracle E-Business Suite](/de/guides/connections/oracle-ebs-access-for-data-foundation/)
  - [Oracle Fusion](/de/guides/connections/oracle-fusion-access-for-data-foundation/)
  - [Dynamics 365 Finance and Operations](/de/guides/connections/dynamics-365-fo-access-for-data-foundation/)
  - [Business Central](/de/guides/connections/business-central-access-for-data-foundation/)
  - [Sage 100](/de/guides/connections/sage-100/)
  - [Sage Intacct](/de/guides/connections/sage-intacct-access-for-data-foundation/)
  - [QuickBooks Online](/de/guides/connections/quickbooks-access-for-data-foundation/)
  - [Xero](/de/guides/connections/xero-access-for-data-foundation/)
  - [Workday](/de/guides/connections/workday-access-for-data-foundation/)
  - [OneStream](/de/guides/connections/onestream-for-data-foundation/)
  - [Anaplan](/de/guides/connections/anaplan/#anaplan-als-quelle-für-data-foundation)
