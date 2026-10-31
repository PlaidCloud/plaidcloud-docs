---
title: Verbindungen
description: Richten Sie PlaidCloud-Verbindungen ein und verwalten Sie sie – gespeicherte Konfigurationen, mit denen Workflows externe Datenbanken, Cloud-Speicher, ERPs und REST-APIs erreichen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/connections/index.md
---

Eine **Verbindung** ist eine gespeicherte Konfiguration, mit der PlaidCloud ein externes System erreicht – eine Datenbank, ein Cloud-Speicherkonto, ein ERP oder eine REST-API. Workflow-Schritte, die aus diesem System lesen oder darin schreiben müssen, verweisen auf die Verbindung, sodass Anmeldedaten und Endpunktdetails an einem Ort liegen.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 210" role="img" aria-label="Viele Workflow-Schritte verweisen auf eine gespeicherte Verbindung, die Anmeldedaten und Endpunkt an einem Ort enthält und das externe System erreicht – eine Datenbank, Cloud-Speicher, ein ERP oder eine REST-API." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="cn-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">Workflow-Schritte</text>
  <rect x="16" y="40" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="61" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Importschritt</text>
  <rect x="16" y="88" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="109" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Exportschritt</text>
  <rect x="16" y="136" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="157" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Lookup-Schritt</text>
  <path d="M136 57 C190 57 210 96 248 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 105 L248 108" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 153 C190 153 210 118 248 114" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="250" y="76" width="180" height="66" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="340" y="104" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Verbindung</text>
  <text x="340" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">Anmeldedaten + Endpunkt, einmalig</text>
  <path d="M430 109 L512 109" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="514" y="80" width="150" height="58" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="589" y="104" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">externes System</text>
  <text x="589" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">DB · Speicher · ERP · REST</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Konfigurieren Sie die Verbindung einmal; jeder Schritt, der das externe System liest oder darin schreibt, verweist auf sie, sodass Anmeldedaten und Endpunktdetails nicht in jedem Schritt doppelt vorliegen.</figcaption>
</figure>

## Leitfäden

- [Verbindung erstellen und verwalten](/de/guides/connections/create-connection/) – eine Verbindung erstellen, bearbeiten, testen und den Zugriff darauf steuern sowie sie pro Umgebung konfigurieren.
- [Eigenes Warehouse verwenden](/de/guides/connections/external-lakehouse/) – verbinden Sie Ihr eigenes Snowflake- oder Databricks-Warehouse selbst, melden Sie sich mit Ihrer eigenen Identität an, verwalten Sie mehrere Warehouses und sehen Sie, was jede Ausführung kostet.
- [PlaidCloud-Git-Verbindung](/de/guides/connections/plaidcloud-git/) – verbinden Sie sich ohne Server-URL oder Anmeldedaten mit dem eigenen verwalteten Git-Server Ihres Workspace und automatisieren Sie damit Panel-App-Builds.
- [Verbindung klonen](/de/guides/connections/clone-connection/) – duplizieren Sie eine bestehende Verbindung für eine neue Umgebung oder einen neuen Mandanten.
- [Data Foundation: Das Common Finance Model](/de/guides/projects/data-foundation/) – das Common Finance Model führt ERP-Daten aus mehreren ERP-Systemen und -Instanzen in einem Modell zusammen, mit einem Kontenplan, einem Satz von Entitäten und einer Berichtswährung, die Berichte, Kennzahlen und KI-Assistenten alle lesen.
- [Singer-Quellen](/de/guides/connections/singer-sources/) – verbinden Sie sich mit Quellen wie Stripe, GitHub, Slack und BigQuery über Singer-Taps und importieren Sie deren Daten in Projekttabellen.
- [Mit NetSuite verbinden](/de/guides/connections/netsuite/) – richten Sie eine NetSuite-Verbindung ein und rufen Sie Finanz- und Betriebsdaten mit SuiteQL ab.
- [NetSuite-Zugriff für Data Foundation](/de/guides/connections/netsuite-access-for-data-foundation/) – was Ihr NetSuite-Administrator einrichtet, damit Data Foundation NetSuite direkt lesen kann, und was Sie zurücksenden.
- [NetSuite-Finanzdaten importieren](/de/guides/connections/import-netsuite-financials/) – rufen Sie Salden, Hauptbuchdetails und Stammdaten mit den vorgefertigten NetSuite-Importschritten ab, ohne SuiteQL zu schreiben.
- [Eine NetSuite-Journalbuchung buchen](/de/guides/connections/post-netsuite-journal-entries/) – ordnen Sie Kopf- und Positionstabellen zu, zeigen Sie eine Vorschau an und buchen Sie Journalbuchungen in NetSuite.
- [Mit Acumatica verbinden](/de/guides/connections/acumatica/) – richten Sie eine Acumatica-Verbindung ein, importieren Sie Entitäten und buchen Sie Journaltransaktionen, Rechnungen, Eingangsrechnungen und Zahlungen.
- [Mit Business Central verbinden](/de/guides/connections/business-central/) – richten Sie eine Business-Central-Verbindung mit Azure AD ein, importieren Sie OData-Entitäten und buchen Sie Sachkonten-Journalzeilen.
- [Mit Dynamics 365 Finance & Operations verbinden](/de/guides/connections/dynamics-365-fo/) – richten Sie eine D365-F&O-Verbindung mit Azure AD ein, importieren Sie OData-/DMF-Entitäten und buchen Sie Journalbuchungen.
- [Mit Oracle Fusion verbinden](/de/guides/connections/oracle-fusion/) – richten Sie eine Oracle-Fusion-Verbindung ein, importieren Sie Hauptbuchsalden und Journalstapel und buchen Sie Journale über FBDI.
- [Mit Workday Financials verbinden](/de/guides/connections/workday-financials/) – richten Sie eine Workday-Financials-Verbindung mit einem Integrationssystembenutzer ein, importieren Sie einen RaaS-Bericht und buchen Sie Journalbuchungen.
- [Mit SAP S/4HANA Cloud verbinden](/de/guides/connections/s4hana-cloud/) – richten Sie eine direkte S/4HANA-Cloud-Verbindung mit OAuth2 ein, importieren Sie Saldenlisten- und Journalbuchungspositionen und buchen Sie Journalbuchungen über SOAP.
- [Ad-hoc-Extrakte aus SAP ECC / S/4HANA](/de/guides/connections/sap-adhoc-extract/) – durchsuchen Sie SAP nach Tabelle, Transaktionscode oder gespeicherter SAP Query, zeigen Sie den Extrakt in der Vorschau an, planen Sie ihn und laden Sie ihn über einen PlaidLink-Agent in eine Tabelle.
- [Mit Sage Intacct verbinden](/de/guides/connections/sage-intacct/) – richten Sie eine Sage-Intacct-Verbindung ein und rufen Sie Finanz- und Buchhaltungsdaten ab.
- [Mit Xero verbinden](/de/guides/connections/xero/) – autorisieren Sie eine Xero-Organisation mit einem Klick, importieren Sie Entitäten der Accounting API und buchen Sie manuelle Journale, Rechnungen, Eingangsrechnungen, Zahlungen und Gutschriften.
- [Mit Salesforce verbinden](/de/guides/connections/salesforce/) – richten Sie eine Salesforce External Client App und einen Run-As-Benutzer ein und extrahieren Sie dann CRM-Objekte in Projekttabellen.
- [Aus HFM / FCCS extrahieren (Ad-hoc)](/de/guides/connections/hfm-fccs/) – verbinden Sie sich mit Oracle FCCS und holen Sie sich einen Datenausschnitt selbst per Betrachtungspunkt-Auswahl, ohne Ticket an das HFM-Team.
- [Mit TM1 verbinden](/de/guides/connections/tm1/) – verbinden Sie sich mit einem IBM TM1 / Planning Analytics-Server und lesen Sie Cube-Daten per Ansicht oder MDX, nach Periode aufgeteilt.
- [Mit Anaplan verbinden](/de/guides/connections/anaplan/) – verbinden Sie sich mit Anaplan und lesen Sie eine gespeicherte Ansicht, führen Sie eine vorhandene Export-Aktion aus oder laden Sie Listen in eine PlaidCloud-Dimension. Nur lesend.
- [Mit QuickBooks verbinden](/de/guides/connections/quickbooks/) – Voraussetzungen und aktuelle Einschränkungen für QuickBooks Online.
- [Das Buchungsregister prüfen](/de/guides/connections/posting-register/) – eine mandantenweite Konsole für Finanz- und Rechnungswesen, um ERP-Buchungen über alle Projekte und Verbindungen zu prüfen, die sie sehen können.

## Verwandte Themen

- [Connector-Referenz](/de/reference/connectors/) – der vollständige Katalog der unterstützten Systeme und der Felder, die jedes benötigt.
