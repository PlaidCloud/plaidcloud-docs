---
title: Verbindungen
description: PlaidCloud-Verbindungen einrichten und verwalten – gespeicherte Konfigurationen, über die Workflows externe Datenbanken, Cloud-Speicher, ERPs und REST-APIs erreichen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/connections/index.md
---

Eine **Verbindung** ist eine gespeicherte Konfiguration, über die PlaidCloud ein externes System erreicht – eine Datenbank, ein Cloud-Speicherkonto, ein ERP oder eine REST-API. Workflow-Schritte, die aus diesem System lesen oder dorthin schreiben müssen, verweisen auf die Verbindung, sodass Zugangsdaten und Endpunktdetails an einer Stelle liegen.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 210" role="img" aria-label="Viele Workflow-Schritte verweisen auf eine gespeicherte Verbindung, die Zugangsdaten und Endpunkt an einer einzigen Stelle hält und das externe System erreicht – eine Datenbank, Cloud-Speicher, ein ERP oder eine REST-API." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="cn-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">Workflow-Schritte</text>
  <rect x="16" y="40" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="61" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Import-Schritt</text>
  <rect x="16" y="88" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="109" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Export-Schritt</text>
  <rect x="16" y="136" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="157" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Lookup-Schritt</text>
  <path d="M136 57 C190 57 210 96 248 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 105 L248 108" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 153 C190 153 210 118 248 114" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="250" y="76" width="180" height="66" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="340" y="104" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Verbindung</text>
  <text x="340" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">Zugangsdaten + Endpunkt, einmalig</text>
  <path d="M430 109 L512 109" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="514" y="80" width="150" height="58" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="589" y="104" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">externes System</text>
  <text x="589" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">DB · Speicher · ERP · REST</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Konfigurieren Sie die Verbindung einmal; jeder Schritt, der das externe System liest oder beschreibt, verweist darauf, sodass Zugangsdaten und Endpunktdetails nicht über mehrere Schritte dupliziert werden.</figcaption>
</figure>

## Anleitungen

- [Verbindung erstellen und verwalten](/de/guides/connections/create-connection/) – eine Verbindung erstellen, bearbeiten, testen und den Zugriff darauf steuern sowie sie pro Umgebung konfigurieren.
- [Eigenes Warehouse verwenden](/de/guides/connections/external-lakehouse/) – Ihr eigenes Snowflake- oder Databricks-Warehouse selbst verbinden, sich mit Ihrer eigenen Identität anmelden, mehrere Warehouses verwalten und sehen, was jede Ausführung kostet.
- [PlaidCloud-Git-Verbindung](/de/guides/connections/plaidcloud-git/) – eine Verbindung zum eigenen verwalteten Git-Server Ihres Workspace ohne Server-URL oder Zugangsdaten herstellen und Panel-App-Builds daraus automatisieren.
- [Verbindung klonen](/de/guides/connections/clone-connection/) – eine bestehende Verbindung für eine neue Umgebung oder einen neuen Tenant duplizieren.
- [Data Foundation: Das Common Finance Model](/de/guides/projects/data-foundation/) – das Common Finance Model führt ERP-Daten aus mehreren ERP-Systemen und -Instanzen in einem Modell zusammen, mit einem Kontenplan, einem Satz Entitäten und einer Berichtswährung, die Berichte, Kennzahlen und KI-Assistenten alle lesen.
- [Singer-Quellen](/de/guides/connections/singer-sources/) – mit Singer-Taps Quellen wie Stripe, GitHub, Slack und BigQuery verbinden und deren Daten in Projekttabellen importieren.
- [Mit NetSuite verbinden](/de/guides/connections/netsuite/) – eine NetSuite-Verbindung einrichten und Finanz- und Betriebsdaten mit SuiteQL abrufen.
- [NetSuite-Zugriff für Data Foundation](/de/guides/connections/netsuite-access-for-data-foundation/) – was Ihr NetSuite-Administrator einrichtet, damit Data Foundation NetSuite direkt lesen kann, und was Sie zurücksenden.
- [NetSuite-Finanzdaten importieren](/de/guides/connections/import-netsuite-financials/) – Salden, Hauptbuchdetails und Stammdaten mit den vorgefertigten NetSuite-Importschritten abrufen, ohne SuiteQL zu schreiben.
- [Eine NetSuite-Journalbuchung buchen](/de/guides/connections/post-netsuite-journal-entries/) – Kopf- und Zeilentabellen zuordnen, eine Vorschau anzeigen und Journalbuchungen in NetSuite buchen.
- [Mit Acumatica verbinden](/de/guides/connections/acumatica/) – eine Acumatica-Verbindung einrichten, Entitäten importieren und Journaltransaktionen, Rechnungen, Eingangsrechnungen und Zahlungen buchen.
- [Mit Business Central verbinden](/de/guides/connections/business-central/) – eine Business-Central-Verbindung mit Azure AD einrichten, OData-Entitäten importieren und Sachkonten-Buchungszeilen buchen.
- [Mit Dynamics 365 Finance & Operations verbinden](/de/guides/connections/dynamics-365-fo/) – eine D365-F&O-Verbindung mit Azure AD einrichten, OData-/DMF-Entitäten importieren und Journalbuchungen buchen.
- [Mit Oracle Fusion verbinden](/de/guides/connections/oracle-fusion/) – eine Oracle-Fusion-Verbindung einrichten, Hauptbuchsalden und Journalstapel importieren und Journale über FBDI buchen.
- [Mit Workday Financials verbinden](/de/guides/connections/workday-financials/) – eine Workday-Financials-Verbindung mit einem Integrationssystembenutzer einrichten, einen RaaS-Bericht importieren und Journalbuchungen buchen.
- [Mit SAP S/4HANA Cloud verbinden](/de/guides/connections/s4hana-cloud/) – eine direkte S/4HANA-Cloud-Verbindung mit OAuth2 einrichten, Saldenliste und Journalbuchungspositionen importieren und Journalbuchungen über SOAP buchen.
- [Ad-hoc-Extrakte aus SAP ECC / S/4HANA](/de/guides/connections/sap-adhoc-extract/) – SAP nach Tabelle, Transaktionscode oder gespeicherter SAP Query durchsuchen, den Extrakt in der Vorschau anzeigen und planen und ihn über einen PlaidLink-Agent in eine Tabelle laden.
- [Mit Sage Intacct verbinden](/de/guides/connections/sage-intacct/) – eine Sage-Intacct-Verbindung einrichten und Finanz- und Buchhaltungsdaten abrufen.
- [Mit Xero verbinden](/de/guides/connections/xero/) – eine Xero-Organisation mit einem Klick autorisieren, Entitäten der Accounting API importieren und manuelle Journale, Rechnungen, Eingangsrechnungen, Zahlungen und Gutschriften buchen.
- [Mit Salesforce verbinden](/de/guides/connections/salesforce/) – eine Salesforce External Client App und einen Run-As-Benutzer einrichten und dann CRM-Objekte in Projekttabellen extrahieren.
- [Aus HFM / FCCS extrahieren (Ad-hoc)](/de/guides/connections/hfm-fccs/) – eine Verbindung zu Oracle FCCS herstellen und einen Datenausschnitt per Point-of-View-Auswahl selbst abrufen, ohne Ticket an das HFM-Team.
- [Mit TM1 verbinden](/de/guides/connections/tm1/) – eine Verbindung zu einem IBM TM1 / Planning Analytics-Server herstellen und Cube-Daten per Ansicht oder MDX lesen, nach Periode aufgeteilt.
- [Mit Anaplan verbinden](/de/guides/connections/anaplan/) – eine Verbindung zu Anaplan herstellen und eine gespeicherte Ansicht lesen, eine bereits vorhandene Exportaktion ausführen oder Listen in eine PlaidCloud-Dimension laden. Nur lesend.
- [OneStream für Data Foundation](/de/guides/connections/onestream-for-data-foundation/) – was Ihr OneStream-Administrator einrichtet, damit Data Foundation konsolidierte Ergebnisse über einen Datenadapter lesen kann.
- [Mit QuickBooks verbinden](/de/guides/connections/quickbooks/) – Voraussetzungen und aktuelle Einschränkungen für QuickBooks Online.
- [Das Buchungsregister prüfen](/de/guides/connections/posting-register/) – eine Konsole auf Tenant-Ebene, mit der Finanz- und Rechnungswesen ERP-Buchungen über alle Projekte und Verbindungen prüfen, die sie sehen können.

## Verwandte Themen

- [Connector-Referenz](/de/reference/connectors/) – der vollständige Katalog der unterstützten Systeme und der Felder, die jedes benötigt.
