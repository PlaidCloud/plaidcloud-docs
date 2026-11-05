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
| **Vollständig¹** | Wird direkt gelesen, wenn das System ihn enthält. Ein System ohne die Daten oder eine Verbindung ohne Zugriff darauf unterbricht das Laden nicht. |
| **Datei** | Das System liefert diesen Datensatz nicht. Fügen Sie ihn als Datei hinzu. |

## SAP, Oracle und Dynamics 365

| Datensatz | SAP S/4HANA | SAP ECC | SAP S/4HANA Cloud | Oracle E-Business Suite | Oracle Fusion | Dynamics 365 Finance and Operations |
| --- | --- | --- | --- | --- | --- | --- |
| Entitäten | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Geschäftskalender | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Kontenplan | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Abteilungen | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Profit-Center | Vollständig¹ | Vollständig¹ | Datei | Datei | Datei | Datei |
| Produkte | Vollständig | Vollständig | Vollständig | Vollständig¹ | Vollständig¹ | Vollständig |
| Kunden | Vollständig | Vollständig | Vollständig | Vollständig¹ | Vollständig¹ | Vollständig |
| Hauptbuch | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Saldenliste | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Verkaufspositionen | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ |
| Pipeline | Datei | Datei | Datei | Datei | Datei | Datei |
| Lagerbestände | Vollständig¹ | Vollständig¹ | Vollständig¹ | Datei | Datei | Vollständig¹ |
| Budget | Vollständig¹ | Vollständig¹ | Vollständig¹ | Datei | Datei | Vollständig¹ |
| Verteilungstreiber | Vollständig¹ | Vollständig¹ | Datei | Datei | Datei | Datei |
| Wechselkurse | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Segmentwerte | Datei | Datei | Datei | Datei | Datei | Datei |
| CO-PA nach Bewertung | Datei | Datei | Datei | Datei | Datei | Datei |

## Mid-Market- und Cloud-Finanzsysteme

| Datensatz | Business Central | Sage Intacct | QuickBooks Online | Xero | Workday | NetSuite |
| --- | --- | --- | --- | --- | --- | --- |
| Entitäten | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Geschäftskalender | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Kontenplan | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Abteilungen | Vollständig | Vollständig | Vollständig¹ | Vollständig | Vollständig | Vollständig |
| Profit-Center | Datei | Datei | Datei | Datei | Datei | Datei |
| Produkte | Vollständig | Vollständig | Vollständig¹ | Vollständig | Vollständig¹ | Vollständig |
| Kunden | Vollständig | Vollständig | Vollständig¹ | Vollständig | Vollständig¹ | Vollständig |
| Hauptbuch | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Saldenliste | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig | Vollständig |
| Verkaufspositionen | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig |
| Pipeline | Datei | Datei | Datei | Datei | Datei | Datei |
| Lagerbestände | Datei | Datei | Vollständig¹ | Datei | Datei | Vollständig¹ |
| Budget | Vollständig¹ | Vollständig¹ | Vollständig¹ | Vollständig¹ | Datei | Vollständig¹ |
| Verteilungstreiber | Vollständig¹ | Vollständig¹ | Datei | Datei | Vollständig¹ | Vollständig |
| Wechselkurse | Vollständig | Vollständig | Vollständig¹ | Datei | Vollständig | Vollständig¹ |
| Segmentwerte | Datei | Datei | Datei | Datei | Vollständig¹ | Vollständig |
| CO-PA nach Bewertung | Datei | Datei | Datei | Datei | Datei | Datei |

## CRM-, Konsolidierungs- und Planungsquellen

| Datensatz | Salesforce | OneStream | Anaplan |
| --- | --- | --- | --- |
| Entitäten | Datei | Datei | Datei |
| Geschäftskalender | Datei | Datei | Datei |
| Kontenplan | Datei | Datei | Datei |
| Abteilungen | Datei | Datei | Datei |
| Profit-Center | Datei | Datei | Datei |
| Produkte | Vollständig¹ | Datei | Datei |
| Kunden | Vollständig¹ | Datei | Datei |
| Hauptbuch | Datei | Datei | Datei |
| Saldenliste | Datei | Datei | Datei |
| Verkaufspositionen | Datei | Datei | Datei |
| Pipeline | Vollständig¹ | Datei | Datei |
| Lagerbestände | Datei | Datei | Datei |
| Budget | Datei | Vollständig | Vollständig |
| Verteilungstreiber | Datei | Datei | Datei |
| Wechselkurse | Datei | Datei | Datei |
| Segmentwerte | Datei | Datei | Datei |
| CO-PA nach Bewertung | Datei | Datei | Datei |

## Hinweise zu den Systemen

- **Salesforce** ist eine CRM-Quelle. Sie liefert Kunden, Produkte und die Vertriebspipeline, nie das Hauptbuch.
- **OneStream** ist eine Ergebnisquelle. Sie liefert nur den Budget-Datensatz und bringt Ihre konsolidierten Ergebnisse ein, damit Data Foundation die Konzern-GuV damit abstimmen kann.
- **Anaplan** ist eine Planquelle. Sie liefert nur den Budget-Datensatz, aus einem Budget-, Forecast- oder Konsolidierungsplan.
- **SAP S/4HANA und SAP ECC** lesen dieselben Stammdaten. ECC liest sein Hauptbuch aus den Positionen der Finanzbuchhaltung und des Controllings und seine Summen aus den Summentabellen des Hauptbuchs. Profit-Center werden gelesen, wenn das System sie enthält. Verkaufspositionen sind Fakturabelege, nicht CO-PA.
- **CO-PA nach Bewertung** wird aus keinem System direkt gelesen. Fügen Sie es als Datei hinzu.
- **Workday** hat keinen direkten Journal- oder Saldendienst. Data Foundation stellt Ihnen die zu erstellenden Berichte bereit und liest sie. Segmentwerte (Worktags), Kunden, Produkte, Verkaufspositionen und Headcount-Treiber stammen aus optionalen Berichten. Budgets bleiben Dateien.
- **Xero** liefert keine Wechselkurse. Fügen Sie sie als Datei hinzu, wenn Ihre Entitäten mehr als eine Währung verwenden.
- **QuickBooks Online** liest Abteilungen, Kunden, Produkte, Wechselkurse, Budgets, Lagerbestände und Verkaufspositionen, wenn die Unternehmensdatei sie enthält.
- **NetSuite** liest benutzerdefinierte Segmente als Segmentwerte. Wechselkurse und Lagerbestände werden gelesen, wenn das Konto sie anbietet, und Budgets, wenn das Konto NetSuite Budgets verwendet und die Rolle sie lesen kann.

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
  - [Sage Intacct](/de/guides/connections/sage-intacct-access-for-data-foundation/)
  - [QuickBooks Online](/de/guides/connections/quickbooks-access-for-data-foundation/)
  - [Xero](/de/guides/connections/xero-access-for-data-foundation/)
  - [Workday](/de/guides/connections/workday-access-for-data-foundation/)
  - [OneStream](/de/guides/connections/onestream-for-data-foundation/)
  - [Anaplan](/de/guides/connections/anaplan/#anaplan-als-quelle-für-data-foundation)
