---
title: Konektory danych i usług
description: Połącz PlaidCloud z zewnętrznymi źródłami danych i usługami, w tym bazami danych, systemami ERP, interfejsami REST API, magazynami w chmurze i repozytoriami Git.
sidebar:
  label: Konektory
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/index.md
---

PlaidCloud łączy się z zewnętrznymi źródłami danych i usługami za pomocą wyspecjalizowanych konektorów. Każdy konektor obsługuje uwierzytelnianie, protokół i specyfikę danych jednej rodziny dostawców.

## Kategorie

### Bazy danych i jeziora danych

Relacyjne bazy danych, hurtownie w chmurze, silniki zapytań i formaty lakehouse.

- [Bazy danych](/pl/reference/connectors/databases/) — PostgreSQL, MySQL, SQL Server, Oracle, Snowflake, Redshift, BigQuery, Databricks, MongoDB, Kafka i ponad 15 innych
- [Otwarte tabele](/pl/reference/connectors/open-tables/) — otwarte formaty tabel Apache Iceberg, Delta Lake, Hudi i Hive

### Usługi chmurowe i SaaS

- [REST](/pl/reference/connectors/rest/) — Salesforce, NetSuite, Workday, QuickBooks, Stripe, Dynamics i inne
- [Systemy ERP](/pl/reference/connectors/erp/) — SAP ECC / S/4HANA, Oracle EBS/Fusion, Infor, JD Edwards
- [Usługi w chmurze](/pl/reference/connectors/cloud-services/) — zewnętrzne usługi danych
- [Google](/pl/reference/connectors/google/) — BigQuery, Arkusze Google
- [Współpraca](/pl/reference/connectors/collaboration/) — Slack, Microsoft Teams, Tableau
- [Źródła Singer](/pl/reference/connectors/singer-sources/) — ponad 130 źródeł Singer-tap: Stripe, GitHub, HubSpot, bazy danych i inne

### Programowanie i kontrola wersji

- [Dostawcy Git](/pl/reference/connectors/git/) — PlaidCloud Git (zarządzany, wbudowany), a także GitHub, GitLab, Bitbucket, Azure Repos i CodeCommit

## Powiązane

- [Przewodnik po połączeniach](/pl/guides/connections/) — przewodnik zadaniowy dotyczący tworzenia połączeń i zarządzania nimi
- [Dokumentacja kroków przepływu pracy](/pl/reference/workflow-steps/) — co zrobić z połączeniem po jego skonfigurowaniu
