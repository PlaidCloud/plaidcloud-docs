---
title: Apache Spark
description: Configurez une connexion à une base de données Apache Spark dans PlaidCloud pour exécuter des requêtes distribuées et intégrer des données volumineuses aux workflows.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/spark.md
---

**Apache Spark** est le moteur de calcul distribué couramment utilisé pour l'ETL sur de grands jeux de données. Utilisez ce connecteur pour lire et écrire des données via des points de terminaison Spark SQL (généralement Spark Thrift Server). Pour Spark géré par Databricks, privilégiez le connecteur [Azure Databricks](../azure-databricks/).

## Documentation officielle
[La documentation d'Apache Spark](https://spark.apache.org/documentation.html).

Le [projet Apache](https://spark.apache.org/).

## Configuration

Ce connecteur utilise un flux d'authentification propre à l'éditeur et se configure directement depuis l'écran **Connexions** de votre espace de travail. Les champs de configuration affichés dépendent des identifiants que l'administrateur de votre tenant a provisionnés pour l'intégration.

Consultez la [documentation de Spark](https://spark.apache.org/docs/latest/) pour connaître les dernières précisions sur la configuration.

Si vous avez besoin d'aide pour configurer ce connecteur pour votre tenant, contactez votre équipe commerciale : les identifiants propres au connecteur, les URL d'environnement et tout provisionnement préalable requis doivent généralement être coordonnés avec le support PlaidCloud.
