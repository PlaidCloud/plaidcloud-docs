---
title: Connecteurs de données et de services
description: Connectez PlaidCloud à des sources de données et services externes, dont bases de données, ERP, API REST, stockage cloud et dépôts Git.
sidebar:
  label: Connecteurs
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/index.md
---

PlaidCloud se connecte à des sources de données et à des services externes grâce à des connecteurs dédiés. Chaque connecteur gère les spécificités d'authentification, de protocole et de format de données d'une famille de fournisseurs.

## Catégories

### Bases de données et lacs de données

Bases de données relationnelles, entrepôts cloud, moteurs de requêtes et formats Lakehouse.

- [Bases de données](/fr/reference/connectors/databases/) — PostgreSQL, MySQL, SQL Server, Oracle, Snowflake, Redshift, BigQuery, Databricks, MongoDB, Kafka et plus de 15 autres
- [Tables ouvertes](/fr/reference/connectors/open-tables/) — formats de tables ouvertes Apache Iceberg, Delta Lake, Hudi et Hive

### Services cloud et SaaS

- [REST](/fr/reference/connectors/rest/) — Salesforce, NetSuite, Workday, QuickBooks, Stripe, Dynamics, etc.
- [Systèmes ERP](/fr/reference/connectors/erp/) — SAP ECC / S/4HANA, Oracle EBS/Fusion, Infor, JD Edwards
- [Services cloud](/fr/reference/connectors/cloud-services/) — services de données tiers
- [Google](/fr/reference/connectors/google/) — BigQuery, Google Sheets
- [Collaboration](/fr/reference/connectors/collaboration/) — Slack, Microsoft Teams, Tableau
- [Sources Singer](/fr/reference/connectors/singer-sources/) — plus de 130 sources Singer-tap{NN}: Stripe, GitHub, HubSpot, bases de données, etc.

### Développement et gestion de code source

- [Fournisseurs Git](/fr/reference/connectors/git/) — PlaidCloud Git (géré, intégré), ainsi que GitHub, GitLab, Bitbucket, Azure Repos et CodeCommit

## Voir aussi

- [Guide des connexions](/fr/guides/connections/) — procédure pas à pas pour créer et gérer des connexions
- [Référence des étapes de workflow](/fr/reference/workflow-steps/) — que faire d'une connexion une fois configurée
