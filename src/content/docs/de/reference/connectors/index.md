---
title: Daten- und Dienstkonnektoren
description: Verbinden Sie PlaidCloud mit externen Datenquellen und Diensten wie Datenbanken, ERP-Systemen, REST-APIs, Cloud-Speichern und Git-Repositories.
sidebar:
  label: Konnektoren
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/index.md
---

PlaidCloud verbindet sich über speziell entwickelte Konnektoren mit externen Datenquellen und Diensten. Jeder Konnektor übernimmt Authentifizierung, Protokoll und Datenformat einer Anbieterfamilie.

## Kategorien

### Datenbanken und Data Lakes

Relationale Datenbanken, Cloud-Warehouses, Abfrage-Engines und Lakehouse-Formate.

- [Datenbanken](/de/reference/connectors/databases/) – PostgreSQL, MySQL, SQL Server, Oracle, Snowflake, Redshift, BigQuery, Databricks, MongoDB, Kafka und über 15 weitere
- [Offene Tabellen](/de/reference/connectors/open-tables/) – offene Tabellenformate Apache Iceberg, Delta Lake, Hudi und Hive

### Cloud- und SaaS-Dienste

- [REST](/de/reference/connectors/rest/) – Salesforce, NetSuite, Workday, QuickBooks, Stripe, Dynamics und mehr
- [ERP-Systeme](/de/reference/connectors/erp/) – SAP ECC / S/4HANA, Oracle EBS/Fusion, Infor, JD Edwards
- [Cloud-Dienste](/de/reference/connectors/cloud-services/) – Datendienste von Drittanbietern
- [Google](/de/reference/connectors/google/) – BigQuery, Google Sheets
- [Zusammenarbeit](/de/reference/connectors/collaboration/) – Slack, Microsoft Teams, Tableau
- [Singer-Quellen](/de/reference/connectors/singer-sources/) – über 130 Singer-Tap-Quellen: Stripe, GitHub, HubSpot, Datenbanken und mehr

### Entwicklung und Quellcodeverwaltung

- [Git-Anbieter](/de/reference/connectors/git/) – PlaidCloud Git (verwaltet, integriert) sowie GitHub, GitLab, Bitbucket, Azure Repos, CodeCommit

## Verwandte Themen

- [Leitfaden zu Verbindungen](/de/guides/connections/) – aufgabenorientierte Anleitung zum Erstellen und Verwalten von Verbindungen
- [Referenz der Workflow-Schritte](/de/reference/workflow-steps/) – was Sie mit einer Verbindung tun können, sobald sie konfiguriert ist
