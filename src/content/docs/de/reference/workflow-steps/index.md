---
title: Workflow-Schritte
description: Jeder Workflow-Schritttyp in PlaidCloud – Import, Export, Transformationen, Umlagen, Dimensionen, Dokumente, Benachrichtigungen und mehr.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/index.md
---

Workflow-Schritte sind die Bausteine der Automatisierung in PlaidCloud. Jeder Schritt führt einen Vorgang aus (eine CSV importieren, zwei Tabellen verknüpfen, eine Benachrichtigung senden), und Schritte werden zu Workflows zusammengesetzt, die nacheinander, parallel, bedingt oder in Schleifen ausgeführt werden.

## Kategorien

### Datenbewegung

- [Import](/de/reference/workflow-steps/import/) – Daten aus CSV, Excel, Parquet, JSON, ORC, Delta Lake, SQL, BigQuery, MongoDB, Kafka, SPSS, Singer-Quellen und mehr einlesen
- [Export](/de/reference/workflow-steps/export/) – Daten nach CSV, XML, SQL, Excel, Google Sheets, Parquet, ORC, MongoDB, Kafka, Tabellenarchiv und mehr ausgeben

### Tabellentransformationen

- [Tabellen](/de/reference/workflow-steps/tables/) – Joins, Unions, Filter, Lookups, Pivots, Melts, gezielte Updates, Zeilenzugriff-Berechtigungen aus einer Quelltabelle, Wiederherstellung zu einem Zeitpunkt
- [Allgemeine Operationen](/de/reference/workflow-steps/common/) – gemeinsame Muster für Datenzuordnung und Filterung

### Geodaten

- [Geodaten](/de/reference/workflow-steps/spatial/) – räumliche Dateien importieren und exportieren, Puffer bilden, abgleichen, messen, neu projizieren und Geometrie aufbauen; vollständige Abdeckung der räumlichen Alteryx-Tools

### Modellierung

- [Umlage](/de/reference/workflow-steps/allocation/) – treiberbasierte Verteilung, geteilte Umlagen, regelbasiertes Tagging
- [Dimensionen](/de/reference/workflow-steps/dimensions/) – Hierarchien laden, sortieren, leeren, exportieren und verwalten
- [Optimierung](/de/reference/workflow-steps/optimization/) – lineare und gemischt-ganzzahlige Solver-Schritte
- [Maschinelles Lernen](/de/reference/workflow-steps/machine-learning/) – Modelle trainieren, einschließlich XGBoost und KNIME-Lernern, und Tabellen damit bewerten

### Dokumente und Dateien

- [Dokument](/de/reference/workflow-steps/document/) – Dateioperationen, Verzeichnislisten, Verschlüsselung, PDF-Bearbeitung, Bildverarbeitung, Kodierungskonvertierung, Aktualisierung von Excel-Zellen
- [Text und Dokumente](/de/reference/workflow-steps/text-documents/) – PDF-Textextraktion, Bild-OCR, Blob lesen und schreiben, Stimmungsanalyse, Themenmodellierung, Wortwolken

### Kommunikation

- [Benachrichtigungen](/de/reference/workflow-steps/notifications/) – E-Mail, Slack, Teams, SMS, Webhook, Twitter, Protokoll
- [Berichte](/de/reference/workflow-steps/reports/) – einzelne oder gebündelte PDF-Berichte aus RML-Vorlagen rendern

### Workflow-Steuerung

- [Workflow-Steuerung](/de/reference/workflow-steps/workflow-control/) – Variablen, Schleifen, Unter-Workflows, Makros, Fehlerbehandlung, Zeilenanzahl-Prüfung
- [Allgemein](/de/reference/workflow-steps/general/) – LLM-Schritt, Pass, Warten, benutzerdefinierte Transformation, Remote-Python ausführen, Alteryx-Executor
- [Gepackte Makros](/de/reference/workflow-steps/macros/) – Entsprechungen zu gepackten Alteryx-Makros: Create Samples, DateTime Now, Heat Map, Pie Wedge Trade Area

### Unternehmensintegrationen

- [Agent](/de/reference/workflow-steps/agent/) – Vorgänge des PlaidLink-Agenten für lokale Ressourcen
- [NetSuite](/de/reference/workflow-steps/netsuite/) – Salden, Hauptbuchdetails, Stammdaten oder Ihre eigene [SuiteQL-Abfrage](/de/reference/workflow-steps/netsuite/import-suiteql-query/) importieren; Journalbuchungen nach NetSuite buchen
- [Acumatica](/de/reference/workflow-steps/acumatica/) – Stamm- und Bewegungsentitäten importieren; Journaltransaktionen, Rechnungen, Eingangsrechnungen und Zahlungen buchen
- [Business Central](/de/reference/workflow-steps/business-central/) – OData-Entitäten importieren; Hauptbuch-Journalzeilen buchen
- [Xero](/de/reference/workflow-steps/xero/) – Entitäten der Accounting API importieren; manuelle Journale, Rechnungen, Eingangsrechnungen, Zahlungen und Gutschriften buchen
- [Dynamics 365 F&O](/de/reference/workflow-steps/dynamics-365-fo/) – OData-/DMF-Entitäten importieren; Journalbuchungen buchen
- [Oracle Fusion](/de/reference/workflow-steps/oracle-fusion/) – Hauptbuchsalden und Journalstapel importieren; Journalbuchungen über FBDI buchen
- [Oracle EPM (HFM / FCCS)](/de/reference/workflow-steps/oracle-epm/) – einen Ad-hoc-Datenausschnitt aus Oracle FCCS per Self-Service mit einer Betrachtungspunkt-Auswahl abrufen; optional geplantes wiederkehrendes Laden
- [Oracle Essbase](/de/reference/workflow-steps/essbase/) – eine Live-MDX-Abfrage gegen einen Cube ausführen oder eine Dimensionsgliederung als PlaidCloud-Dimension laden; cloud-direkt
- [IBM TM1 / Planning Analytics](/de/reference/workflow-steps/ibm-planning-analytics/) – einen Cube über eine gespeicherte Ansicht oder MDX lesen, oder eine Dimensionshierarchie; cloud-direkt oder über einen lokalen Agenten
- [Anaplan](/de/reference/workflow-steps/anaplan/) – eine gespeicherte Ansicht lesen, eine bereits vorhandene Exportaktion ausführen oder eine oder mehrere Listen in eine PlaidCloud-Dimension laden; cloud-direkt, nur lesend
- [Workday Financials](/de/reference/workflow-steps/workday-financials/) – einen RaaS-Bericht importieren; Buchhaltungsjournale buchen
- [Salesforce](/de/reference/workflow-steps/salesforce/) – jedes Standard- oder benutzerdefinierte CRM-Objekt über Bulk API 2.0 in eine Projekttabelle extrahieren, wobei Objekt und Feldliste aus der Org gelesen werden
- [Sage Intacct](/de/reference/workflow-steps/sage-intacct/) – Salden, Eingangsrechnungen, Ad-hoc-Abfragen und Hauptbuch-/Dimensionsobjekte importieren; Journalbuchungen buchen
- [SAP S/4HANA Cloud](/de/reference/workflow-steps/s4hana-cloud/) – Saldenliste und Journalbuchungspositionen über OData importieren; Journalbuchungen über SOAP buchen
- [SAP](/de/reference/workflow-steps/sap/) – RFC-Aufrufe für SAP ECC / S/4HANA
- [SAP-PCM](/de/reference/workflow-steps/sap-pcm/) – Modellsteuerung für SAP Profitability and Cost Management
